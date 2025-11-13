from typing import Dict, Optional
from uuid import UUID

from month2.week1.day5_org_routers.domain.entities.item_model import ItemModel
from month2.week1.day5_org_routers.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)


class ItemRepositoryMemory:
    """Хранилище для Item"""

    def __init__(self) -> None:
        self._storage = Dict[UUID, ItemModel] = {}

    def get_all(self):
        return list(self._storage.values())

    def get(self, item_id: UUID) -> Optional[ItemModel]:
        return self._storage.get(item_id)

    def add(self, item: ItemModel) -> ItemModel:
        if self.exist(item.id):
            raise ItemAlreadyExistsError(f"Item with id={item.id} already exists")
        if self.exist_by_name(item.name):
            raise ItemAlreadyExistsError(f"Item with name={item.name} already exists")
        self._storage[item.id] = item
        return item

    def update(self, item: ItemModel) -> ItemModel:
        if not self.exist(item.id):
            raise ItemNotFoundError(f"Item with id={item.id} not found")

        if self.exist_by_name(item.name, exclude_id=item.id):
            raise ItemAlreadyExistsError(f"Item with name='{item.name}' already exists")

        self._storage[item.id] = item
        return item

    def delete(self, item_id: UUID) -> None:
        if not self.exist(item_id):
            raise ItemNotFoundError(f"item with id={item_id} not found")
        del self._storage[item_id]

    def exist(self, item_id: UUID) -> bool:
        return item_id in self._storage

    def exist_by_name(self, name: str, exclude_id: Optional[UUID] = None) -> bool:
        return any(
            item.name == name and item.id != exclude_id
            for item in self._storage.values()
        )
