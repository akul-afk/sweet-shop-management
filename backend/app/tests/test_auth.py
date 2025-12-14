from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_can_register(client):
    response = client.post(
        "/api/auth/register",
        json={
            "email": "testuser@example.com",
            "password": "test"
        }
    )
    assert response.status_code == 201
    assert response.json()["email"] == "testuser@example.com"
