from typing import List
from uuid import UUID, uuid4

from month2.week1.day3_validation.application.commands.user.create_user import (
    CreateUserCommand,
)
from month2.week1.day3_validation.domain.entities.user_model import UserModel

from ...infrastructure.repositories.user_memory import UserRepositoryMemory
from ..commands.user.update_user import UpdateUserCommand


class UserService:
    def __init__(self, repo: UserRepositoryMemory):
        self.repo = repo

    def list_users(self) -> List[UserModel]:
        return self.repo.list_all()

    def get_user(self, user_id: UUID) -> UserModel:
        user = self.repo.get(user_id)
        if not user:
            raise ValueError("User not found")
        return user

    def create_user(self, cmd: CreateUserCommand) -> UserModel:
        new_user = UserModel(id=uuid4(), email=cmd.email, password=cmd.password)
        return self.repo.save(new_user)

    def update_user(self, user_id: UUID, cmd: UpdateUserCommand) -> UserModel:
        existing = self.repo.get(user_id)
        if not existing:
            raise ValueError("User not found")

        updated_user = UserModel(
            id=user_id,
            email=cmd.email if cmd.email is not None else existing.email,
            password=cmd.password if cmd.password is not None else existing.password,
        )
        return self.repo.save(updated_user)

    def delete_user(self, user_id: UUID) -> None:
        if not self.repo.exists(user_id):
            raise ValueError("User not found")
        self.repo.delete(user_id)
