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
def test_protected_route_requires_auth(client):
    response = client.get("/api/auth/me")
    assert response.status_code == 401
def test_protected_route_with_token(client):
    client.post(
        "/api/auth/register",
        json={"email": "me@example.com", "password": "test"}
    )

    login = client.post(
        "/api/auth/login",
        json={"email": "me@example.com", "password": "test"}
    )

    token = login.json()["access_token"]

    response = client.get(
        "/api/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["email"] == "me@example.com"
