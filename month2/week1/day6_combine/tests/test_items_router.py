from unittest.mock import MagicMock
from uuid import uuid4

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from month2.week1.day6_combine.domain.entities.item_model import ItemModel
from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotChangedError,
    ItemNotFoundError,
    ItemValidationError,
)
from month2.week1.day6_combine.interface.api.v1.items.router import items_router

# ------------------------------------------------------------------------------
# FIXTURES
# ------------------------------------------------------------------------------


@pytest.fixture
def client():
    """Создаём отдельное FastAPI-приложение для роутов items."""
    app = FastAPI()
    app.include_router(items_router)
    return TestClient(app)


@pytest.fixture(autouse=True)
def mock_items_service(monkeypatch):
    """
    Автоматически подменяем items_service мок-объектом.
    Все тесты используют его.
    """
    mock = MagicMock()
    monkeypatch.setattr(
        "month2.week1.day6_combine.interface.api.v1.items.router.items_service",
        mock,
    )
    return mock


# ------------------------------------------------------------------------------
# GET /items
# ------------------------------------------------------------------------------


def test_get_items(client, mock_items_service):
    item1 = ItemModel(id=uuid4(), name="Item1", price=100)
    item2 = ItemModel(id=uuid4(), name="Item2", price=200)

    mock_items_service.list_item.return_value = [item1, item2]

    resp = client.get("/items/")

    assert resp.status_code == 200
    assert len(resp.json()) == 2
    assert resp.json()[0]["name"] == "Item1"


# ------------------------------------------------------------------------------
# GET /items/{id}
# ------------------------------------------------------------------------------


def test_get_item_success(client, mock_items_service):
    item = ItemModel(id=uuid4(), name="Test", price=10)
    mock_items_service.get_item.return_value = item

    resp = client.get(f"/items/{item.id}")

    assert resp.status_code == 200
    assert resp.json()["name"] == "Test"


def test_get_item_not_found(client, mock_items_service):
    mock_items_service.get_item.side_effect = ItemNotFoundError("not found")

    resp = client.get(f"/items/{uuid4()}")

    assert resp.status_code == 404


# ------------------------------------------------------------------------------
# POST /items
# ------------------------------------------------------------------------------


def test_create_item_success(client, mock_items_service):
    new_id = uuid4()
    mock_items_service.create_item.return_value = ItemModel(
        id=new_id, name="Abc", price=10
    )

    resp = client.post("/items/", json={"name": "Abc", "price": 10})

    assert resp.status_code == 201
    assert resp.json()["id"] == str(new_id)


def test_create_item_exists(client, mock_items_service):
    mock_items_service.create_item.side_effect = ItemAlreadyExistsError("exists")

    resp = client.post("/items/", json={"name": "Abc", "price": 10})

    assert resp.status_code == 400


# ------------------------------------------------------------------------------
# PUT /items/{id}
# ------------------------------------------------------------------------------


def test_update_item_success(client, mock_items_service):
    item_id = uuid4()
    updated = ItemModel(id=item_id, name="Updated", price=50)

    mock_items_service.update_item.return_value = updated

    resp = client.put(
        f"/items/{item_id}",
        json={"name": "Updated", "price": 50},
    )

    assert resp.status_code == 200
    assert resp.json()["name"] == "Updated"


def test_update_item_not_found(client, mock_items_service):
    mock_items_service.update_item.side_effect = ItemNotFoundError("not found")

    resp = client.put(
        f"/items/{uuid4()}",
        json={"name": "Abc", "price": 10},
    )

    assert resp.status_code == 404


def test_update_item_conflict(client, mock_items_service):
    mock_items_service.update_item.side_effect = ItemAlreadyExistsError("dup")

    resp = client.put(
        f"/items/{uuid4()}",
        json={"name": "Abc", "price": 10},
    )

    assert resp.status_code == 409


def test_update_item_not_changed(client, mock_items_service):
    mock_items_service.update_item.side_effect = ItemNotChangedError("not changed")

    resp = client.put(
        f"/items/{uuid4()}",
        json={"name": "Abc", "price": 10},
    )

    assert resp.status_code == 400


def test_update_item_validation_error(client, mock_items_service):
    mock_items_service.update_item.side_effect = ItemValidationError("invalid")

    resp = client.put(
        f"/items/{uuid4()}",
        json={"name": "Abc", "price": 10},
    )

    assert resp.status_code == 422


# ------------------------------------------------------------------------------
# DELETE /items/{id}
# ------------------------------------------------------------------------------


def test_delete_item_success(client, mock_items_service):
    resp = client.delete(f"/items/{uuid4()}")
    assert resp.status_code == 204


def test_delete_item_not_found(client, mock_items_service):
    mock_items_service.delete_item.side_effect = ItemNotFoundError("not found")

    resp = client.delete(f"/items/{uuid4()}")

    assert resp.status_code == 404


def test_get_items_filter_by_name(client, mock_items_service):
    """Фильтрация по частичному совпадению имени."""
    item1 = ItemModel(id=uuid4(), name="Apple Watch", price=300)
    item2 = ItemModel(id=uuid4(), name="Apple MacBook", price=1500)

    mock_items_service.list_item.return_value = [item1, item2]

    resp = client.get("/items/?name=Apple")

    assert resp.status_code == 200
    assert len(resp.json()) == 2
    mock_items_service.list_item.assert_called_once_with(
        name="Apple", min_price=None, max_price=None
    )


def test_get_items_filter_by_min_price(client, mock_items_service):
    """Фильтрация по минимальной цене."""
    item = ItemModel(id=uuid4(), name="iPhone", price=1000)

    mock_items_service.list_item.return_value = [item]

    resp = client.get("/items/?min_price=900")

    assert resp.status_code == 200
    assert len(resp.json()) == 1
    mock_items_service.list_item.assert_called_once_with(
        name=None, min_price=900.0, max_price=None
    )


def test_get_items_filter_by_max_price(client, mock_items_service):
    """Фильтрация по максимальной цене."""
    item = ItemModel(id=uuid4(), name="Keyboard", price=50)

    mock_items_service.list_item.return_value = [item]

    resp = client.get("/items/?max_price=100")

    assert resp.status_code == 200
    assert len(resp.json()) == 1
    mock_items_service.list_item.assert_called_once_with(
        name=None, min_price=None, max_price=100.0
    )


def test_get_items_filter_by_name_and_price(client, mock_items_service):
    """Фильтрация по имени + диапазону цен."""
    item = ItemModel(id=uuid4(), name="Monitor Pro", price=300)

    mock_items_service.list_item.return_value = [item]

    resp = client.get("/items/?name=Pro&min_price=200&max_price=400")

    assert resp.status_code == 200
    assert len(resp.json()) == 1

    mock_items_service.list_item.assert_called_once_with(
        name="Pro", min_price=200.0, max_price=400.0
    )


def test_get_items_no_results(client, mock_items_service):
    """Если ничего не найдено — возвращаем пустой массив."""
    mock_items_service.list_item.return_value = []

    resp = client.get("/items/?name=XYZ&min_price=999")

    assert resp.status_code == 200
    assert resp.json() == []

    mock_items_service.list_item.assert_called_once_with(
        name="XYZ", min_price=999.0, max_price=None
    )
