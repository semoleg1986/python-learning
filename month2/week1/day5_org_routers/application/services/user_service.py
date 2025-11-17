from typing import List, Optional
from uuid import UUID, uuid4

from month2.week1.day5_org_routers.application.commands.user.create_user import (
    CreateUserCommand,
)
from month2.week1.day5_org_routers.application.commands.user.update_user import (
    UpdateUserCommand,
)
from month2.week1.day5_org_routers.domain.entities.user_model import UserModel
from month2.week1.day5_org_routers.domain.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from month2.week1.day5_org_routers.infrastructure.repositories.user_memory import (
    UserRepositoryMemory,
)


class UserService:
    """
    Сервис User
    """

    def __init__(self, repo: UserRepositoryMemory = None) -> None:
        self.repo = repo or UserRepositoryMemory()

    def list_user(self) -> List[UserModel]:
        return self.repo.get_all()

    def get_user(self, user_id: UUID) -> Optional[UserModel]:
        user = self.repo.get(user_id)
        if not user:
            raise UserNotFoundError(f"User with id={user_id} not found")
        return user

    def create_user(self, cmd: CreateUserCommand) -> UserModel:
        if self.repo.exists_by_email(cmd.email):
            raise UserAlreadyExistsError(f"User with email={cmd.email} already exists")
        new_user = UserModel(id=uuid4(), email=cmd.email, password=cmd.password)
        return self.repo.add(new_user)

    def update_user(self, user_id: UUID, cmd: UpdateUserCommand) -> UserModel:
        existing = self.repo.get(user_id)
        if not existing:
            raise UserNotFoundError(f"User with id={user_id} not found")
        if cmd.email and self.repo.exists_by_email(cmd.email, exclude_id=user_id):
            raise UserAlreadyExistsError(
                f"User with email='{cmd.email}' already exists"
            )

        existing.update(cmd.email, cmd.password)
        return self.repo.update(existing)

    def delete_user(self, user_id: UUID) -> None:
        self.repo.delete(user_id)
