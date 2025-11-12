from typing import Dict, List, Optional
from uuid import UUID

from month2.week1.day3_validation.domain.entities.item_model import ItemModel


class ItemRepositoryMemory:
    """Хранилище для Item"""

    def __init__(self) -> None:
        self._storage: Dict[UUID, ItemModel] = {}

    def save(self, item: ItemModel) -> ItemModel:
        self._storage[item.id] = item
        return item

    def get(self, item_id: UUID) -> Optional[ItemModel]:
        return self._storage.get(item_id)

    def list_all(self) -> List[ItemModel]:
        return list(self._storage.values())

    def delete(self, item_id: UUID) -> bool:
        return self._storage.pop(item_id, None) is not None

    def exists(self, item_id: UUID) -> bool:
        return item_id in self._storage
