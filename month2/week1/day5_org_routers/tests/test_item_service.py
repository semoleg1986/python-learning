import unittest
from uuid import uuid4

from month2.week1.day5_org_routers.application.commands.item.create_item import (
    CreateItemCommand,
)
from month2.week1.day5_org_routers.application.commands.item.update_item import (
    UpdateItemCommand,
)
from month2.week1.day5_org_routers.application.services.item_service import ItemService
from month2.week1.day5_org_routers.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from month2.week1.day5_org_routers.infrastructure.repositories.item_memory import (
    ItemRepositoryMemory,
)


class TestItemService(unittest.TestCase):
    def setUp(self):
        self.repo = ItemRepositoryMemory()  # новый репозиторий перед каждым тестом
        self.service = ItemService(self.repo)

    def test_create_item_success(self):
        cmd = CreateItemCommand(name="Test", price=10.0)
        item = self.service.create_item(cmd)

        self.assertEqual(item.name, "Test")
        self.assertEqual(item.price, 10.0)
        self.assertTrue(self.repo.exist(item.id))

    def test_create_item_duplicate_name(self):
        self.service.create_item(CreateItemCommand(name="Test", price=10.0))

        with self.assertRaises(ItemAlreadyExistsError):
            self.service.create_item(CreateItemCommand(name="Test", price=15.0))

    def test_get_item_success(self):
        item = self.service.create_item(CreateItemCommand(name="Item", price=5))
        fetched = self.service.get_item(item.id)
        self.assertEqual(fetched.id, item.id)

    def test_get_item_not_found(self):
        with self.assertRaises(ItemNotFoundError):
            self.service.get_item(uuid4())

    def test_update_item_success(self):
        item = self.service.create_item(CreateItemCommand(name="Old", price=10))

        cmd = UpdateItemCommand(name="New", price=20)
        updated = self.service.update_item(item.id, cmd)

        self.assertEqual(updated.name, "New")
        self.assertEqual(updated.price, 20)

    def test_update_item_not_found(self):
        with self.assertRaises(ItemNotFoundError):
            self.service.update_item(uuid4(), UpdateItemCommand(name="Xau", price=1))

    def test_update_item_duplicate_name(self):
        self.service.create_item(CreateItemCommand(name="Abc", price=10))
        b = self.service.create_item(CreateItemCommand(name="Bcd", price=20))

        with self.assertRaises(ItemAlreadyExistsError):
            self.service.update_item(b.id, UpdateItemCommand(name="Abc", price=99))

    def test_delete_item_success(self):
        item = self.service.create_item(CreateItemCommand(name="XXX", price=1))
        self.service.delete_item(item.id)

        with self.assertRaises(ItemNotFoundError):
            self.service.get_item(item.id)

    def test_delete_item_not_found(self):
        with self.assertRaises(ItemNotFoundError):
            self.service.delete_item(uuid4())


if __name__ == "__main__":
    unittest.main()
