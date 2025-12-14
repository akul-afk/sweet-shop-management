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
def test_user_can_login(client):
    # First register the user
    client.post(
        "/api/auth/register",
        json={
            "email": "loginuser@example.com",
            "password": "test"
        }
    )

    # Then login
    response = client.post(
        "/api/auth/login",
        json={
            "email": "loginuser@example.com",
            "password": "test"
        }
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
