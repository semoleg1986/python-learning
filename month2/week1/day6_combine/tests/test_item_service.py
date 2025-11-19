from uuid import uuid4

import pytest

from month2.week1.day6_combine.application.commands.item.create_item import (
    CreateItemCommand,
)
from month2.week1.day6_combine.application.commands.item.update_item import (
    UpdateItemCommand,
)
from month2.week1.day6_combine.application.services.item_service import ItemService
from month2.week1.day6_combine.domain.entities.item_model import ItemModel
from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from month2.week1.day6_combine.infrastructure.repositories.item_rep import (
    ItemRepositoryMemory,
)


@pytest.fixture
def repo():
    return ItemRepositoryMemory()


@pytest.fixture
def service(repo):
    return ItemService(repo)


def test_create_and_get_item(service: ItemService):
    cmd = CreateItemCommand(name="Test Item", price=100)
    item = service.create_item(cmd)

    assert isinstance(item, ItemModel)
    assert item.name == "Test Item"
    assert item.price == 100

    fetched = service.get_item(item.id)
    assert fetched.id == item.id
    assert fetched.name == item.name


def test_create_duplicate_name_raises(service: ItemService):
    cmd = CreateItemCommand(name="Test Item", price=100)
    service.create_item(cmd)

    with pytest.raises(ItemAlreadyExistsError):
        service.create_item(cmd)


def test_get_item_not_found(service: ItemService):
    with pytest.raises(ItemNotFoundError):
        service.get_item(uuid4())


def test_update_item(service: ItemService):
    create_cmd = CreateItemCommand(name="Item1", price=50)
    item = service.create_item(create_cmd)

    update_cmd = UpdateItemCommand(name="Item1 Updated", price=75)
    updated = service.update_item(item.id, update_cmd)

    assert updated.name == "Item1 Updated"
    assert updated.price == 75


def test_update_item_duplicate_name_raises(service: ItemService):
    service.create_item(CreateItemCommand(name="Item1", price=10))
    item2 = service.create_item(CreateItemCommand(name="Item2", price=20))

    update_cmd = UpdateItemCommand(name="Item1", price=30)
    with pytest.raises(ItemAlreadyExistsError):
        service.update_item(item2.id, update_cmd)


def test_delete_item(service: ItemService):
    item = service.create_item(CreateItemCommand(name="ToDelete", price=10))
    service.delete_item(item.id)

    with pytest.raises(ItemNotFoundError):
        service.get_item(item.id)
