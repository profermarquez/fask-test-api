import pytest

def test_register_user(client):
    response = client.post("/register", json={
        "username": "cris",
        "password": "seguro123"
    })
    assert response.status_code in (201, 400)  # puede fallar si el usuario ya existe

def test_login_user(client):
    response = client.post("/login", json={
        "username": "cris",
        "password": "seguro123"
    })
    json_data = response.get_json()
    assert response.status_code == 200
    assert "access_token" in json_data
