from uuid import uuid4

import pytest

from month2.week1.day5_org_routers.application.services.user_service import (
    CreateUserCommand,
    UpdateUserCommand,
    UserService,
)
from month2.week1.day5_org_routers.domain.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from month2.week1.day5_org_routers.infrastructure.repositories.user_memory import (
    UserRepositoryMemory,
)


@pytest.fixture
def repo():
    return UserRepositoryMemory()


@pytest.fixture
def service(repo):
    return UserService(repo)


@pytest.fixture
def user_cmd():
    return CreateUserCommand(email="test@example.com", password="Password1")


def test_create_user_success(service, user_cmd):
    user = service.create_user(user_cmd)
    assert user.id is not None
    assert user.email == user_cmd.email


def test_create_user_duplicate_email(service, user_cmd):
    service.create_user(user_cmd)
    with pytest.raises(UserAlreadyExistsError):
        service.create_user(user_cmd)


def test_get_user_success(service, user_cmd):
    user = service.create_user(user_cmd)
    found = service.get_user(user.id)
    assert found.id == user.id


def test_get_user_not_found(service):
    with pytest.raises(UserNotFoundError):
        service.get_user(uuid4())


def test_list_user(service, user_cmd):
    user = service.create_user(user_cmd)
    users = service.list_user()
    assert len(users) == 1
    assert users[0].id == user.id


def test_update_user_success(service, user_cmd):
    user = service.create_user(user_cmd)
    update_cmd = UpdateUserCommand(email="new@example.com", password="NewPass1")
    updated = service.update_user(user.id, update_cmd)
    assert updated.email == "new@example.com"
    assert updated.password == "NewPass1"


def test_update_user_not_found(service):
    update_cmd = UpdateUserCommand(email="new@example.com")
    with pytest.raises(UserNotFoundError):
        service.update_user(uuid4(), update_cmd)


def test_update_user_duplicate_email(service, user_cmd):
    user1 = service.create_user(user_cmd)
    user2 = service.create_user(
        CreateUserCommand(email="other@example.com", password="Password1")
    )
    update_cmd = UpdateUserCommand(email=user1.email)
    with pytest.raises(UserAlreadyExistsError):
        service.update_user(user2.id, update_cmd)


def test_delete_user_success(service, user_cmd):
    user = service.create_user(user_cmd)
    service.delete_user(user.id)
    assert service.list_user() == []


def test_delete_user_not_found(service):
    with pytest.raises(UserNotFoundError):
        service.delete_user(uuid4())
