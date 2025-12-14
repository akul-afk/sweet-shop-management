from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_can_register():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "testuser@example.com",
            "password": "strongpassword"
        }
    )
    assert response.status_code == 201
