import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    """setup for tests

    Yields:
    ------
        instance of the fastapi app
    """
    client = TestClient(app)
    yield client
