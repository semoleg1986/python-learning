from typing import Dict, List, Optional
from uuid import UUID

from month2.week1.day4_responses_status.domain.entitites.item_model import Item
from month2.week1.day4_responses_status.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
)


class ItemRepositoryMemory:
    """Хранилище для Item"""

    def __init__(self) -> None:
        self._storage: Dict[UUID, Item] = {}

    def list(self) -> List[Item]:
        return list(self._storage.values())

    def get(self, item_id: UUID) -> Optional[Item]:
        return self._storage.get(item_id)

    def save(self, item: Item) -> Item:
        if self.exist(item.id):
            raise ItemAlreadyExistsError(f"Item with id={item.id} already exists")
        self._storage[item.id] = item
        return item

    def delete(self, item_id: UUID) -> bool:
        return self._storage.pop(item_id, None) is not None

    def exist(self, item_id: UUID) -> bool:
        return item_id in self._storage

    def exist_by_name(self, name: str) -> bool:
        return any(item.name == name for item in self._storage.values())
