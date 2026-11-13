from contextlib import contextmanager
from types import SimpleNamespace
from unittest.mock import Mock, patch
import pytest
from ragger.backend.interface import RaisePolicy
from ragger.error import ExceptionRAPDU
from ragger.navigator import Navigator
from ragger_bitcoin.ragger_bitcoin import RaggerClient

class Transport:
    def __init__(self):
        self.raise_policy = RaisePolicy.RAISE_CUSTOM
        self.whitelisted_status = [0x9000, 0xE000]
        self.round = 0
        self.last_async_response = None
    @contextmanager
    def exchange_async_raw(self, raw):
        self.round += 1
        yield False
        self.last_async_response = SimpleNamespace(status=0x9000, data=b'signed')

class Screens:
    def __init__(self, transport, status=0xE000):
        self.transport, self.status, self.seen = transport, status, []
    def navigate_until_text(self, *args, **kwargs):
        text = args[2]
        if self.transport.round == 1 and text == 'second':
            from ragger.backend.speculos import SpeculosBackend
            from speculos.client import ApduException
            backend=SpeculosBackend.__new__(SpeculosBackend)
            backend.raise_policy=self.transport.raise_policy
            backend.whitelisted_status=self.transport.whitelisted_status
            backend._last_async_response=None
            response=Mock();response.receive.side_effect=ApduException(self.status,b'proof request')
            backend._pending_async_response=response
            backend.apdu_logger=Mock();backend.logger=Mock()
            with patch('ragger.backend.speculos.has_data_available',return_value=True):
                backend._check_async_error()
            raise RuntimeError('protocol response ignored; guest timeout')
        self.seen.append(text)

def client_and_instructions():
    t = Transport()
    c = RaggerClient.__new__(RaggerClient)
    c.transport_client = t
    c.builder = SimpleNamespace(continue_interrupted=lambda x: dict(cla=0xf8, ins=1, p1=0, p2=0, data=x))
    instructions = SimpleNamespace(data={'text':[['first','second']], 'instruction_until_text':[[1,1]], 'instruction_on_text':[[2,2]], 'save_screenshot':[[False,False]]})
    return c, t, instructions

def test_late_protocol_response_resumes_unfinished_review():
    c,t,i = client_and_instructions(); nav=Screens(t); interpreter=Mock()
    interpreter.execute.return_value=b'proof'
    result=c._make_request_with_navigation(nav,dict(cla=0xe1,ins=4,p1=0,p2=0,data=b''),interpreter,'case',i)
    assert result==(0x9000,b'signed')
    assert nav.seen==['first','second']
    interpreter.execute.assert_called_once_with(b'proof request')
    assert t.raise_policy==RaisePolicy.RAISE_CUSTOM
    assert t.whitelisted_status==[0x9000,0xE000]

def test_navigation_errors_propagate_and_policy_restores():
    c,t,i=client_and_instructions(); nav=Screens(t,0x6985)
    with pytest.raises(ExceptionRAPDU) as ex:
        c._make_request_with_navigation(nav,dict(cla=0xe1,ins=4,p1=0,p2=0,data=b''),None,'case',i)
    assert ex.value.status==0x6985
    assert t.raise_policy==RaisePolicy.RAISE_CUSTOM

@pytest.mark.parametrize('method', ['navigate_and_compare','navigate_until_text_and_compare'])
def test_ticker_restored_when_navigation_unwinds(method):
    nav=Navigator.__new__(Navigator); backend=Mock(); nav._backend=backend
    nav._run_instruction=Mock(side_effect=ExceptionRAPDU(0xE000,b'proof'))
    if method=='navigate_and_compare':
        args=(None,None,[])
    else:
        args=(1,[2],'Approve')
    with pytest.raises(ExceptionRAPDU):
        getattr(nav,method)(*args)
    backend.pause_ticker.assert_called_once_with()
    backend.resume_ticker.assert_called_once_with()

def test_success_without_review_is_still_rejected():
    c,t,i=client_and_instructions()
    @contextmanager
    def already_done(raw):
        t.last_async_response=SimpleNamespace(status=0x9000,data=b'not reviewed')
        yield True
    t.exchange_async_raw=already_done
    with pytest.raises(RuntimeError,match='expected UI interactions'):
        c._make_request_with_navigation(Screens(t),dict(cla=0xe1,ins=4,p1=0,p2=0,data=b''),None,'case',i)
    assert t.raise_policy==RaisePolicy.RAISE_CUSTOM

def test_real_backend_late_response_unwinds_before_next_tick(monkeypatch):
    from ragger.backend.speculos import SpeculosBackend
    import ragger.backend.speculos as module
    from speculos.client import ApduException
    backend=SpeculosBackend.__new__(SpeculosBackend)
    backend.raise_policy=RaisePolicy.RAISE_ALL_BUT_0x9000
    backend._last_async_response=None
    response=Mock();response.receive.side_effect=ApduException(0xE000,b'proof')
    backend._pending_async_response=response
    backend.apdu_logger=Mock();backend.logger=Mock()
    monkeypatch.setattr(module,'has_data_available',lambda response,timeout:True)
    with pytest.raises(ExceptionRAPDU) as ex:
        backend._check_async_error()
    assert ex.value.status==0xE000 and ex.value.data==b'proof'
    response.receive.assert_called_once_with()
