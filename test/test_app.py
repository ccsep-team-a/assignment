# fixtures setup in ./conftest.py
import flask


# Functionality Tests
def test_errorhandlers(client):
    """Error handling is not a feature."""
    rv = client.get('/foobar')
    assert b'Page doesn\'t exist' in rv.data

def test_route_index(client):
    """Root should return the page index with expected title."""
    rv = client.get('/')
    assert b'SHOPII' in rv.data

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