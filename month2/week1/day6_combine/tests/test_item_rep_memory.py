from uuid import uuid4

import pytest

from month2.week1.day6_combine.domain.entities.item_model import ItemModel
from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from month2.week1.day6_combine.infrastructure.repositories.item_rep import (
    ItemRepositoryMemory,
)


class TestItemRepositoryMemory:
    def setup_method(self):
        self.repo = ItemRepositoryMemory()

    def test_add_item_success(self):
        item = ItemModel(id=uuid4(), name="Test", price=100)
        result = self.repo.add(item)

        assert result == item
        assert len(self.repo.get_all()) == 1

    def test_add_item_duplicate_id(self):
        item = ItemModel(id=uuid4(), name="Test", price=100)
        self.repo.add(item)

        with pytest.raises(ItemAlreadyExistsError):
            self.repo.add(item)  # id тот же

    def test_add_item_duplicate_name(self):
        item1 = ItemModel(id=uuid4(), name="AAA", price=10)
        item2 = ItemModel(id=uuid4(), name="AAA", price=20)

        self.repo.add(item1)
        with pytest.raises(ItemAlreadyExistsError):
            self.repo.add(item2)

    def test_get_item_success(self):
        item = ItemModel(id=uuid4(), name="Item", price=100)
        self.repo.add(item)

        found = self.repo.get(item.id)
        assert found == item

    def test_get_item_not_found(self):
        assert self.repo.get(uuid4()) is None

    def test_update_item_success(self):
        item = ItemModel(id=uuid4(), name="Item", price=100)
        self.repo.add(item)

        updated = ItemModel(id=item.id, name="NewName", price=200)
        result = self.repo.update(updated)

        assert result.name == "NewName"
        assert result.price == 200

    def test_update_item_not_found(self):
        item = ItemModel(id=uuid4(), name="Item", price=100)
        with pytest.raises(ItemNotFoundError):
            self.repo.update(item)

    def test_update_item_duplicate_name(self):
        item1 = ItemModel(id=uuid4(), name="Item1", price=10)
        item2 = ItemModel(id=uuid4(), name="Item2", price=20)

        self.repo.add(item1)
        self.repo.add(item2)

        updated = ItemModel(id=item1.id, name="Item2", price=10)

        with pytest.raises(ItemAlreadyExistsError):
            self.repo.update(updated)

    def test_delete_item_success(self):
        item = ItemModel(id=uuid4(), name="Item", price=100)
        self.repo.add(item)

        self.repo.delete(item.id)

        assert len(self.repo.get_all()) == 0
        assert self.repo.get(item.id) is None

    def test_delete_item_not_found(self):
        with pytest.raises(ItemNotFoundError):
            self.repo.delete(uuid4())
