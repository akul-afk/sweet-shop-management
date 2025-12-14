def auth_header(client, email="sweetadmin@example.com", password="test"):
    client.post(
        "/api/auth/register",
        json={"email": email, "password": password}
    )
    login = client.post(
        "/api/auth/login",
        json={"email": email, "password": password}
    )
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_sweet_requires_auth(client):
    res = client.post("/api/sweets", json={})
    assert res.status_code == 401


def test_create_and_list_sweets(client):
    headers = auth_header(client)

    create = client.post(
        "/api/sweets",
        headers=headers,
        json={
            "name": "Gulab Jamun",
            "category": "Indian",
            "price": 20.0,
            "quantity": 50
        }
    )
    assert create.status_code == 201

    list_res = client.get("/api/sweets", headers=headers)
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1
    assert list_res.json()[0]["name"] == "Gulab Jamun"
