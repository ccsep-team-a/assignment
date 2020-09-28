# fixtures setup in ./conftest.py
# Security Tests
def test_dom_xss_search_using_innertext(client):
    """ Page must  use the innertext function rather than innerhtml. """
    
    rv = client.get("/search")
    assert not b"document.getElementById('searchQuery').innerHTML" in rv.data
    assert b"document.getElementById('searchQuery').innerText" in rv.data

def test_dom_xss_product_encode_hash_num(client):
    """ page must encode the num vaiable attained from hash, removing html tags. """
    rv = client.get("/product")
    assert b"num = encodeURI(num);" in rv.data

def test_dom_xss_product_encode_param_store(client):
    """ page must encode the store parameter, removing html tags. """
    rv = client.get("/product")
    assert b"store = encodeURI(store);" in rv.data
