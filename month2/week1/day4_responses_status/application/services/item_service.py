from typing import List
from uuid import UUID, uuid4

from month2.week1.day4_responses_status.application.commands.item.create_item import (
    CreateItemCommand,
)
from month2.week1.day4_responses_status.application.commands.item.update_item import (
    UpdateItemCommand,
)
from month2.week1.day4_responses_status.domain.entitites.item_model import Item
from month2.week1.day4_responses_status.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from month2.week1.day4_responses_status.infrastructure.repositories.item_memory import (
    ItemRepositoryMemory,
)


class ItemService:
    """
    Сервис Item

    Проверка бизнес-правил (уникальность имени, допустимая цена и т.д.)
    должна быть в сервисе, не в репозитории.
    """

    def __init__(self, repo: ItemRepositoryMemory = None):
        self.repo = repo or ItemRepositoryMemory()

    def list_item(self) -> List[Item]:
        return self.repo.get_all()

    def get_item(self, item_id: UUID) -> Item:
        item = self.repo.get(item_id)
        if not item:
            raise ItemNotFoundError(f"Item with id={item_id} not found")
        return item

    def create_item(self, cmd: CreateItemCommand) -> Item:
        if self.repo.exist_by_name(cmd.name):
            raise ItemAlreadyExistsError(f"Item with name='{cmd.name}' already exists")

        new_item = Item(id=uuid4(), name=cmd.name, price=cmd.price)
        return self.repo.add(new_item)

    def update_item(self, item_id: UUID, cmd: UpdateItemCommand) -> Item:
        existing = self.repo.get(item_id)
        if not existing:
            raise ItemNotFoundError(f"Item with id={item_id} not found")

        if cmd.name and self.repo.exist_by_name(cmd.name, exclude_id=item_id):
            raise ItemAlreadyExistsError(f"Item with name='{cmd.name}' already exists")

        existing.update(name=cmd.name, price=cmd.price)

        return self.repo.update(existing)

    def delete_item(self, item_id: UUID) -> None:
        self.repo.delete(item_id)
