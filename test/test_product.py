import pytest

@pytest.fixture
def access_token(client):
    # Login para obtener token JWT
    response = client.post("/login", json={
        "username": "cris",
        "password": "seguro123"
    })
    assert response.status_code == 200
    return response.get_json()["access_token"]

def test_get_products(client, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = client.get("/products", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_product(client, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = client.post("/products", json={
        "name": "ProductoTest",
        "price": 123.45
    }, headers=headers)

    assert response.status_code in (201, 400)
    json_data = response.get_json()
    assert "msg" in json_data
