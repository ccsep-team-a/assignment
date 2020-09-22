# Guide: https://flask.palletsprojects.com/en/1.1.x/testing/
import os
import tempfile

import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()

    with app.test_client() as client:
        # with app.app_context():
            # flasker.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_index_exists(client):
    """Root should return index page text stub."""

    rv = client.get('/')
    assert b'Index Page' in rv.data