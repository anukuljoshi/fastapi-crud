from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping():
    """function to test ping endpoint"""
    response = client.get("/ping")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"ping": "pong!"}
