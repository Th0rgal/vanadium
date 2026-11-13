from unittest.mock import Mock,patch
from inspect import signature
import pytest
from ragger.backend.speculos import SpeculosBackend
from ragger.backend.interface import RaisePolicy
from ragger.error import ExceptionRAPDU
from speculos.client import ApduException

def backend(status):
    b=SpeculosBackend.__new__(SpeculosBackend)
    b._pending_async_response=Mock();b._pending_async_response.receive.side_effect=ApduException(status,b'proof')
    b._last_async_response=None;b.raise_policy=RaisePolicy.RAISE_ALL_BUT_0x9000
    b.apdu_logger=Mock();b.logger=Mock()
    return b

def test_loading_screen_observable_before_interruption_but_before_any_next_tick():
    b=backend(0xE000)
    kwargs={'defer_interruption':True} if 'defer_interruption' in signature(b._check_async_error).parameters else {}
    with patch('ragger.backend.speculos.has_data_available',return_value=True):
        b._check_async_error(**kwargs)
        assert b._last_async_response.status==0xE000
        # The loading screenshot is compared between the changed-screen return and next wait.
        with pytest.raises(ExceptionRAPDU) as ex:b._check_async_error()
    assert ex.value.status==0xE000 and ex.value.data==b'proof'
    b._pending_async_response.receive.assert_called_once_with()

def test_unrelated_error_never_deferred_on_changed_screen():
    b=backend(0x6985)
    kwargs={'defer_interruption':True} if 'defer_interruption' in signature(b._check_async_error).parameters else {}
    with patch('ragger.backend.speculos.has_data_available',return_value=True),pytest.raises(ExceptionRAPDU) as ex:
        b._check_async_error(**kwargs)
    assert ex.value.status==0x6985

def test_pending_loading_flushes_before_comparison_then_unwinds_before_next_tick():
    from io import BytesIO
    b=backend(0xE000);b._last_screenshot=BytesIO(b'old');b._client=Mock()
    visible=[b'old'];b._client.get_screenshot.side_effect=lambda:visible[0]
    b.send_tick=Mock(side_effect=lambda:visible.__setitem__(0,b'loading'))
    equal=lambda a,z:a.getvalue()==z.getvalue()
    with patch('ragger.backend.speculos.has_data_available',return_value=True),patch('ragger.backend.speculos.screenshot_equal',side_effect=equal):
        b.wait_for_screen_change()
        assert b._last_screenshot.getvalue()==b'loading'
        assert b.send_tick.call_count==1
        with pytest.raises(ExceptionRAPDU) as ex:b.wait_for_screen_change()
        assert ex.value.status==0xE000
        assert b.send_tick.call_count==1

def test_pending_response_without_changed_screen_is_bounded_below_guest50_ticks():
    from io import BytesIO
    b=backend(0xE000);b._last_screenshot=BytesIO(b'old');b._client=Mock()
    b._client.get_screenshot.return_value=b'old';b.send_tick=Mock()
    with patch('ragger.backend.speculos.has_data_available',return_value=True),patch('ragger.backend.speculos.screenshot_equal',return_value=True),pytest.raises(ExceptionRAPDU) as ex:
        b.wait_for_screen_change()
    assert ex.value.status==0xE000
    assert b.send_tick.call_count<=11
