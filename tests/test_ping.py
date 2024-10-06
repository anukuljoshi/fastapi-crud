from fastapi import status
from fastapi.testclient import TestClient


def test_ping(test_app: TestClient):
    """function to test ping endpoint"""
    response = test_app.get("/ping")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"ping": "pong!"}
