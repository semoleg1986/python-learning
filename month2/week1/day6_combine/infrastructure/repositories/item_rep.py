from typing import Dict, List, Optional
from uuid import UUID

from month2.week1.day6_combine.domain.entities.item_model import ItemModel
from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)


class ItemRepositoryMemory:
    """Хранилище для Item"""

    def __init__(self) -> None:
        self._storage: Dict[UUID, ItemModel] = {}

    def get_all(
        self, name: str = None, min_price: float = None, max_price=None
    ) -> List[ItemModel]:
        result = list(self._storage.values())

        if name:
            result = [i for i in result if name.lower() in i.name.lower()]

        if min_price is not None:
            result = [i for i in result if float(i.price) >= min_price]

        if max_price is not None:
            result = [i for i in result if float(i.price) <= max_price]

        return result

    def get(self, item_id: UUID) -> Optional[ItemModel]:
        return self._storage.get(item_id)

    def add(self, new_item: ItemModel) -> ItemModel:
        if self.exists(new_item.id):
            raise ItemAlreadyExistsError(f"Item with id={new_item.id} already exists")
        if self.exists_by_name(new_item.name):
            raise ItemAlreadyExistsError(
                f"Item with name={new_item.name} already exists"
            )
        self._storage[new_item.id] = new_item
        return new_item

    def update(self, item: ItemModel) -> ItemModel:
        if not self.exists(item.id):
            raise ItemNotFoundError(f"Item with id={item.id} not found")

        if self.exists_by_name(item.name, item.id):
            raise ItemAlreadyExistsError(f"Item with name={item.name} already exists")

        self._storage[item.id] = item
        return item

    def delete(self, item_id: UUID) -> None:
        if not self.exists(item_id):
            raise ItemNotFoundError(f"Item with id={item_id} not found")
        del self._storage[item_id]

    def exists(self, item_id: UUID) -> bool:
        return item_id in self._storage

    def exists_by_name(self, name: str, exclude_id: Optional[UUID] = None) -> bool:
        return any(
            item.name == name and item.id != exclude_id
            for item in self._storage.values()
        )
