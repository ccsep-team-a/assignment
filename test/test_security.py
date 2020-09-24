# Guide: https://flask.palletsprojects.com/en/1.1.x/testing/
import os
import tempfile
import flask
import pytest

from app import create_app

# Untested TEST DATA

# <img src="javascript:alert(1)">
# <iframe src="data:text/html,<img src=1 onerror=alert(document.
# <body onafterprint=alert(1)>
# <svg><animate onend=alert(1) attributeName=x dur=1s>
# <audio src/onerror=alert(1)>
# {{constructor.constructor('alert(1)')()}}

# Test if rv has js enabled

# good.com/?URL="alert(1);//
#  <script>window.location=""alert(1);//"</script>

# good.com/?URL="alert(document.cookie);//
# <script>window.location=""alert(document.cookie);//"</script>

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()

    with app.test_client() as client:
        # with app.app_context():
        #     app.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

@pytest.fixture
def app_fixture():
    app = create_app({"TESTING": True})
    _, app.config['DATABASE'] = tempfile.mkstemp()
    return app



# Security Tests
def test_dom_xss_search(client,app_fixture):
    """ Payloads represent tampered URLs clicked by victems """
    
    rv = client.get("/search?q=1#1' onerror='alert(1);//")
    assert not b"onerror='alert(1);//" in rv.data

    with app_fixture.test_request_context("/search?q=1#1' onerror='alert(1);//") as request_context:
        assert flask.request.path == "/search"
        assert flask.request.args['q'] == '1'
        
    rv = client.get("/search?q=<img src="" onerror=alert(1)>")
    assert not b"onerror='alert(1);//" in rv.data

    with app_fixture.test_request_context("/search?q=<img src="" onerror=alert(1)>") as request_context:
        assert flask.request.path == "/search"
        assert flask.request.args['q'] != "<img src="" onerror=alert(1)>"

def test_dom_xss_product(app_fixture):
    """ Payloads represent tampered URLs clicked by victems """

    with app_fixture.test_request_context("/product?product=1#1' onerror='alert(1);//") as request_context:
        assert flask.request.path == "/product"
        assert flask.request.args['product'] == '1'
        # assert flask.request.
        # "product?product=1#1' onerror='alert(1);//"

    with app_fixture.test_request_context("/product?product=<img src="" onerror=alert(1)>") as request_context:
        assert flask.request.path == "/product"
        assert flask.request.args['product'] != "<img src="" onerror=alert(1)>"