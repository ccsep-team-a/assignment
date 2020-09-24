# Guide: https://flask.palletsprojects.com/en/1.1.x/testing/
# https://stackoverflow.com/questions/17375340/testing-code-that-requires-a-flask-app-or-request-context
import os
import tempfile
import flask
import pytest
from app import create_app


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

# Functionality Tests
def test_errorhandlers(client):
    """Error handling is not a feature."""
    rv = client.get('/foobar')
    assert b'404' in rv.data

def test_route_index(client):
    """Root should return the page index with expected title."""
    rv = client.get('/')

    assert b'SHOPII' in rv.data

def test_route_about(client):
    """should return data"""

    rv = client.get('/about')
    assert b'123' in rv.data

def test_route_search(client, app_fixture):
    """should return data"""
    
    rv = client.get('/search')
    assert b'Search' in rv.data  

    with app_fixture.test_client() as c:
        rv = c.get('/search?q=1')
        assert flask.request.args['q'] == '1'

def test_route_product(client, app_fixture):
    """should return data"""

    rv = client.get('/product')
    assert b'' in rv.data

    with app_fixture.test_client() as c:
        rv = c.get('/product?product=1')
        assert flask.request.args['product'] == "1"