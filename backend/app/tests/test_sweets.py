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
def test_search_sweets(client):
    headers = auth_header(client)

    client.post(
        "/api/sweets",
        headers=headers,
        json={
            "name": "Rasgulla",
            "category": "Indian",
            "price": 15.0,
            "quantity": 30
        }
    )

    res = client.get(
        "/api/sweets/search?name=ras",
        headers=headers
    )

    assert res.status_code == 200
    assert len(res.json()) == 1
    assert res.json()[0]["name"] == "Rasgulla"
def test_update_sweet(client):
    headers = auth_header(client)

    create = client.post(
        "/api/sweets",
        headers=headers,
        json={
            "name": "Barfi",
            "category": "Indian",
            "price": 25.0,
            "quantity": 40
        }
    )

    sweet_id = create.json()["id"]

    update = client.put(
        f"/api/sweets/{sweet_id}",
        headers=headers,
        json={"price": 30.0}
    )

    assert update.status_code == 200
    assert update.json()["price"] == 30.0
