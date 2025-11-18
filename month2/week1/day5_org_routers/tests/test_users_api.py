from uuid import uuid4

from fastapi.testclient import TestClient

from month2.week1.day5_org_routers.main import app

client = TestClient(app)


def test_create_user_success():
    body = {"email": "test@example.com", "password": "pass1234S"}

    r = client.post("/api/v1/users/", json=body)

    assert r.status_code == 201
    assert "id" in r.json()


def test_create_user_duplicate_email():
    body = {"email": "dup@example.com", "password": "pass1234S"}

    client.post("/api/v1/users/", json=body)
    r = client.post("/api/v1/users/", json=body)

    assert r.status_code == 400


def test_get_user_success():
    body = {"email": "find@example.com", "password": "pass1234S"}
    created = client.post("/api/v1/users/", json=body).json()
    user_id = created["id"]

    r = client.get(f"/api/v1/users/{user_id}")

    assert r.status_code == 200
    assert r.json()["email"] == "find@example.com"


def test_get_user_not_found():
    r = client.get(f"/api/v1/users/{uuid4()}")

    assert r.status_code == 404
    assert "not found" in r.json()["detail"].lower()


def test_update_user_success():
    body = {"email": "upd@example.com", "password": "pass1234S"}
    created = client.post("/api/v1/users/", json=body).json()
    user_id = created["id"]

    update_body = {"email": "updated@example.com"}

    r = client.put(f"/api/v1/users/{user_id}", json=update_body)

    assert r.status_code == 200
    assert r.json()["email"] == "updated@example.com"


def test_update_user_no_changes():
    body = {"email": "same@example.com", "password": "pass1234S"}
    created = client.post("/api/v1/users/", json=body).json()
    user_id = created["id"]

    r = client.put(f"/api/v1/users/{user_id}", json=body)

    assert r.status_code == 400
    assert "изменений не было" in r.json()["detail"].lower()


def test_delete_user_success():
    body = {"email": "del@example.com", "password": "pass1234S"}
    created = client.post("/api/v1/users/", json=body).json()
    user_id = created["id"]

    r = client.delete(f"/api/v1/users/{user_id}")

    assert r.status_code == 204


def test_delete_user_not_found():
    r = client.delete(f"/api/v1/users/{uuid4()}")

    assert r.status_code == 404
    assert "not found" in r.json()["detail"].lower()
