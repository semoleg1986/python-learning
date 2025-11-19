from typing import List
from uuid import UUID, uuid4

from month2.week1.day6_combine.application.commands.item.create_item import (
    CreateItemCommand,
)
from month2.week1.day6_combine.application.commands.item.update_item import (
    UpdateItemCommand,
)
from month2.week1.day6_combine.domain.entities.item_model import ItemModel
from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from month2.week1.day6_combine.infrastructure.repositories.item_rep import (
    ItemRepositoryMemory,
)


class ItemService:
    """
    Сервис Item
    """

    def __init__(self, repo: ItemRepositoryMemory = None) -> None:
        self.repo = repo or ItemRepositoryMemory()

    def list_item(self) -> List[ItemModel]:
        return self.repo.get_all()

    def get_item(self, item_id: UUID) -> ItemModel:
        item = self.repo.get(item_id)
        if not item:
            raise ItemNotFoundError(f"item with id={item_id} not found")
        return item

    def create_item(self, cmd: CreateItemCommand) -> ItemModel:
        if self.repo.exists_by_name(cmd.name):
            raise ItemAlreadyExistsError(f"Item with name={cmd.name} already exists")

        new_item = ItemModel(id=uuid4(), name=cmd.name, price=cmd.price)
        return self.repo.add(new_item)

    def update_item(self, item_id: UUID, cmd: UpdateItemCommand) -> ItemModel:
        existing = self.repo.get(item_id)
        existing = self.repo.get(item_id)
        if not existing:
            raise ItemNotFoundError(f"Item with id={item_id} not found")
        if cmd.name and self.repo.exists_by_name(cmd.name, exclude_id=item_id):
            raise ItemAlreadyExistsError(f"Item with name='{cmd.name}' already exists")

        existing.update(cmd.name, cmd.price)
        return self.repo.update(existing)

    def delete_item(self, item_id: UUID) -> None:
        self.repo.delete(item_id)
