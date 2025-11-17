from typing import Dict, List, Optional
from uuid import UUID

from month2.week1.day5_org_routers.domain.entities.user_model import UserModel
from month2.week1.day5_org_routers.domain.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)


class UserRepositoryMemory:
    """Хранилище для User"""

    def __init__(self) -> None:
        self._storage: Dict[UUID, UserModel] = {}

    def get_all(self) -> List[UserModel]:
        return list(self._storage.values())

    def get(self, user_id: UUID) -> Optional[UserModel]:
        return self._storage.get(user_id)

    def add(self, new_user: UserModel) -> UserModel:
        if self.exists(new_user.id):
            raise UserAlreadyExistsError(f"User with id={new_user.id} already exists")

        if self.exists_by_email(new_user.email):
            raise UserAlreadyExistsError(
                f"User with email={new_user.email} already exists"
            )

        self._storage[new_user.id] = new_user
        return new_user

    def update(self, user: UserModel) -> UserModel:
        if not self.exists(user.id):
            raise UserNotFoundError(f"User with id={user.id} not found")

        if self.exists_by_email(user.email, exclude_id=user.id):
            raise UserAlreadyExistsError(
                f"User with email='{user.email}' already exists"
            )

        self._storage[user.id] = user
        return user

    def delete(self, user_id: UUID) -> None:
        if not self.exists(user_id):
            raise UserNotFoundError(f"User with id={user_id} not found")
        del self._storage[user_id]

    def exists(self, user_id: UUID) -> bool:
        return user_id in self._storage

    def exists_by_email(self, email: str, exclude_id: Optional[UUID] = None) -> bool:
        return any(
            user.email == email and user.id != exclude_id
            for user in self._storage.values()
        )
