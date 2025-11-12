from typing import Dict, List, Optional
from uuid import UUID

from month2.week1.day3_validation.domain.entities.user_model import UserModel


class UserRepositoryMemory:
    """Хранилище для User"""

    def __init__(self) -> None:
        self._storage: Dict[UUID, UserModel] = {}

    def save(self, user: UserModel) -> UserModel:
        self._storage[user.id] = user
        return user

    def get(self, user_id: UUID) -> Optional[UserModel]:
        return self._storage.get(user_id)

    def list_all(self) -> List[UserModel]:
        return list(self._storage.values())

    def delete(self, user_id: UUID) -> bool:
        return self._storage.pop(user_id, None) is not None

    def exists(self, user_id: UUID) -> bool:
        return user_id in self._storage
