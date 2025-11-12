from typing import List
from uuid import UUID, uuid4

from month2.week1.day3_validation.domain.entities.item_model import ItemModel

from ...infrastructure.repositories.item_memory import ItemRepositoryMemory
from ..commands.create_item import CreateItemCommand


class ItemService:
    def __init__(self, repo: ItemRepositoryMemory):
        self.repo = repo

    def list_item(self) -> List[ItemModel]:
        return self.repo.list_all()

    def get_item(self, item_id: UUID) -> ItemModel:
        item = self.repo.get(item_id)
        if not item:
            raise ValueError("Item not found")
        return item

    def create_item(self, item: CreateItemCommand) -> ItemModel:
        new_id = uuid4()
        new_item = ItemModel(id=new_id, name=item.name, price=item.price)
        return self.repo.save(new_item)

    def update_item(self, item_id: UUID, item: ItemModel) -> ItemModel:
        existing = self.repo.get(item_id)
        if not existing:
            raise ValueError("Item not found")
        updated = ItemModel(
            id=item_id,
            name=item.name if item.name is not None else existing.name,
            price=item.price if item.price is not None else existing.price,
        )
        return self.repo.save(updated)

    def delete_item(self, item_id: UUID) -> None:
        if not self.repo.exists(item_id):
            raise ValueError("Item not found")
        self.repo.delete(item_id)
