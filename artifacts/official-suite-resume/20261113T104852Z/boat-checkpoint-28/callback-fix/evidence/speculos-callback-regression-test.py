from flask import Flask
from flask_restful import Api
import pytest
from speculos.api.apdu import APDU, pending_replies


class RespondingSeph:
    def __init__(self):
        self.apdu_callbacks = []
        self.callback_counts = []
        self.fail = False

    def get_tick_count(self):
        return 0

    def to_app(self, data):
        self.callback_counts.append(len(self.apdu_callbacks))
        if self.fail:
            raise RuntimeError("transport failed")
        for callback in list(self.apdu_callbacks):
            callback(b"\x90\x00")


def client_for(seph):
    app = Flask(__name__)
    app.testing = True
    Api(app).add_resource(APDU, "/apdu", resource_class_kwargs={"seph": seph})
    return app.test_client()


def test_completed_requests_release_callbacks_and_keep_other_observers():
    seph = RespondingSeph()
    observed = []
    observer = observed.append
    seph.apdu_callbacks.append(observer)
    client = client_for(seph)
    for _ in range(50):
        response = client.post("/apdu", json={"data": "e0ff000000"})
        assert response.get_json() == {"data": "9000"}
        response.close()
    assert seph.apdu_callbacks == [observer]
    assert seph.callback_counts == [2] * 50
    assert observed == [b"\x90\x00"] * 50
    assert pending_replies.wait_idle(0)


def test_invalid_requests_do_not_register_callbacks():
    seph = RespondingSeph()
    client = client_for(seph)
    for _ in range(10):
        response = client.post("/apdu", json={"nodata": ""})
        assert response.status_code == 400
        response.close()
    assert seph.apdu_callbacks == []


def test_transport_failure_releases_callback():
    seph = RespondingSeph()
    seph.fail = True
    response = client_for(seph).post("/apdu", json={"data": "e0ff000000"}, buffered=False)
    try:
        with pytest.raises(RuntimeError, match="transport failed"):
            response.get_data()
    finally:
        response.close()
    assert seph.apdu_callbacks == []
    assert pending_replies.wait_idle(0)
