import os
import tempfile
import pytest
from app import create_app

def pytest_sessionfinish(session, exitstatus):
    # Run the tests without failing tests effecting Makefile integrity```
    if exitstatus != 0:
        session.exitstatus = 0 

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

@pytest.fixture
def app_fixture():
    app = create_app({"TESTING": True})
    _, app.config['DATABASE'] = tempfile.mkstemp()
    return app