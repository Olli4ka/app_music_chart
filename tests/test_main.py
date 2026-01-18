import threading
import time
import http.client
import pytest

from main import run


HOST = "localhost"
PORT = 8080


@pytest.fixture(scope="module")
def server():
    thread = threading.Thread(target=run, daemon=True)
    thread.start()

    time.sleep(1)

    yield


def make_request(path):
    conn = http.client.HTTPConnection(HOST, PORT)
    conn.request("GET", path)
    response = conn.getresponse()
    body = response.read()
    conn.close()
    return response.status, body


def test_index_page(server):
    status, body = make_request("/")
    assert status == 200
    assert len(body) > 0


def test_search_page(server):
    status, body = make_request("/search")
    assert status == 200
    assert len(body) > 0


def test_error_page_for_unknown_path(server):
    status, body = make_request("/unknown-page")
    assert status == 200 or status == 404
    assert len(body) > 0


def test_static_css(server):
    status, body = make_request("/static/css/styles.css")
    assert status == 200
    assert len(body) > 0


def test_static_js(server):
    status, body = make_request("/static/js/script.js")
    assert status == 200
    assert len(body) > 0
