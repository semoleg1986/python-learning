from uuid import UUID

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_product():
    """Тест создания продукта"""
    response = client.post(
        "/product/products/", json={"name": "Test Product", "price": 1999.99}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert UUID(data["id"])


def test_get_products():
    """Тест получения всех продуктов"""
    response = client.get("/product/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_product_by_id():
    """Тест получения продукта по UUID"""
    create_response = client.post(
        "/product/products/", json={"name": "ItemX", "price": 500}
    )
    assert create_response.status_code == 201
    product_data = create_response.json()
    product_uuid = product_data["id"]

    response = client.get(f"/product/products/{product_uuid}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_uuid
    assert data["name"] == "ItemX"
    assert data["price"] == 500


def test_update_product():
    """Тест обновления продукта"""
    create_response = client.post(
        "/product/products/", json={"name": "OldName", "price": 100}
    )
    product_id = create_response.json()["id"]

    response = client.put(
        f"/product/products/{product_id}", json={"name": "NewName", "price": 200}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["name"] == "NewName"
    assert data["price"] == 200


def test_delete_product():
    """Тест удаления продукта"""
    create_response = client.post(
        "/product/products/", json={"name": "DeleteMe", "price": 999}
    )
    product_id = create_response.json()["id"]

    delete_response = client.delete(f"/product/products/{product_id}")
    assert delete_response.status_code == 204

    get_response = client.get(f"/product/products/{product_id}")
    assert get_response.status_code == 404
