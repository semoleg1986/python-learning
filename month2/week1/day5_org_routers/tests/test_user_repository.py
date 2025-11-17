from uuid import uuid4

import pytest

from month2.week1.day5_org_routers.domain.entities.user_model import UserModel
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
def user():
    return UserModel(
        email="test@example.com",
        password="Password1",
    )


def test_add_user_success(repo, user):
    saved = repo.add(user)
    assert saved.id == user.id
    assert repo.get(user.id) == user


def test_add_user_duplicate_id(repo, user):
    repo.add(user)
    with pytest.raises(UserAlreadyExistsError):
        repo.add(user)


def test_add_user_duplicate_email(repo):
    user1 = UserModel(email="same@example.com", password="Password1")
    user2 = UserModel(email="same@example.com", password="Password2")

    repo.add(user1)
    with pytest.raises(UserAlreadyExistsError):
        repo.add(user2)


def test_get_user_success(repo, user):
    repo.add(user)
    found = repo.get(user.id)
    assert found == user


def test_get_user_not_exists(repo):
    random_id = uuid4()
    assert repo.get(random_id) is None


def test_get_all_users(repo):
    u1 = UserModel(email="u1@example.com", password="Password1")
    u2 = UserModel(email="u2@example.com", password="Password1")
    repo.add(u1)
    repo.add(u2)

    all_users = repo.get_all()
    assert len(all_users) == 2
    assert u1 in all_users
    assert u2 in all_users


def test_update_user_success(repo, user):
    repo.add(user)

    updated_user = UserModel(id=user.id, email="new@example.com", password="Password1")
    result = repo.update(updated_user)

    assert result.email == "new@example.com"
    assert repo.get(user.id).email == "new@example.com"


def test_update_user_not_found(repo, user):
    with pytest.raises(UserNotFoundError):
        repo.update(user)


def test_update_user_duplicate_email(repo):
    user1 = UserModel(email="test1@example.com", password="Password1")
    user2 = UserModel(email="test2@example.com", password="Password1")

    repo.add(user1)
    repo.add(user2)

    updated = UserModel(id=user2.id, email="test1@example.com", password="PasswordX1")

    with pytest.raises(UserAlreadyExistsError):
        repo.update(updated)


def test_delete_user_success(repo, user):
    repo.add(user)
    repo.delete(user.id)
    assert repo.get(user.id) is None


def test_exists(repo, user):
    repo.add(user)
    assert repo.exists(user.id)
    assert not repo.exists(uuid4())


def test_exists_by_email(repo, user):
    repo.add(user)
    assert repo.exists_by_email("test@example.com")
    assert not repo.exists_by_email("unknown@example.com")
