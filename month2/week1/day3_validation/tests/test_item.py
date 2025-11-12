from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError

from month2.week1.day3_validation.application.commands.item.create_item import (
    CreateItemCommand,
)
from month2.week1.day3_validation.application.services.item_service import ItemService
from month2.week1.day3_validation.domain.entities.item_model import ItemModel
from month2.week1.day3_validation.infrastructure.repositories.item_memory import (
    ItemRepositoryMemory,
)


def test_item_model_valid():
    item = ItemModel(id=uuid4(), name="Test Item", price=10.50)
    assert isinstance(item.id, UUID)
    assert item.name == "Test Item"
    assert item.price == 10.50


def test_item_model_invalid_price():
    # Цена <= 0
    with pytest.raises(ValidationError):
        ItemModel(id=uuid4(), name="Invalid Item", price=-5)

    # Пустое имя
    with pytest.raises(ValidationError):
        ItemModel(id=uuid4(), name="", price=10)


def test_item_repository_crud():
    repo = ItemRepositoryMemory()
    item = ItemModel(id=uuid4(), name="Repo Item", price=20)

    # Create / Save
    saved_item = repo.save(item)
    assert saved_item.id == item.id

    # Get
    fetched_item = repo.get(item.id)
    assert fetched_item.id == item.id

    # List all
    items = repo.list_all()
    assert len(items) == 1
    assert items[0].id == item.id

    # Exists
    assert repo.exists(item.id)

    # Delete
    assert repo.delete(item.id)
    assert not repo.exists(item.id)


def test_item_service_crud():
    repo = ItemRepositoryMemory()
    service = ItemService(repo)

    # Create item via service
    cmd = CreateItemCommand(name="Service Item", price=15.0)
    item = service.create_item(cmd)
    assert item.name == "Service Item"

    # Get item
    fetched = service.get_item(item.id)
    assert fetched.id == item.id

    # Update item
    updated_item_model = ItemModel(id=item.id, name="Updated Name", price=20.0)
    updated = service.update_item(item.id, updated_item_model)
    assert updated.name == "Updated Name"
    assert updated.price == 20.0
