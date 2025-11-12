from uuid import UUID

import pytest
from pydantic import ValidationError

from month2.week1.day3_validation.domain.entities.user_model import UserModel
from month2.week1.day3_validation.interface.api.v1.users.request import (
    RequestCreateUser,
)


def test_user_model_valid():
    user = UserModel(email="test@example.com", password="StrongP@ss1")
    assert isinstance(user.id, UUID)
    assert user.email == "test@example.com"
    assert user.password == "StrongP@ss1"


def test_user_model_invalid_password():
    # Пароль без заглавной буквы
    with pytest.raises(ValidationError) as exc_info:
        UserModel(email="test@example.com", password="weakp@ss1")
    assert "Пароль должен содержать хотя бы одну заглавную букву" in str(exc_info.value)

    # Пароль без цифры
    with pytest.raises(ValidationError) as exc_info:
        UserModel(email="test@example.com", password="WeakPass@")
    assert "Пароль должен содержать хотя бы одну цифру" in str(exc_info.value)

    # Пароль без спецсимвола
    with pytest.raises(ValidationError) as exc_info:
        UserModel(email="test@example.com", password="WeakPass1")
    assert "Пароль должен содержать хотя бы один специальный символ" in str(
        exc_info.value
    )


def test_request_create_user_validation():
    # Валидный DTO
    dto = RequestCreateUser(email="dto@example.com", password="DtoP@ss1")
    assert dto.email == "dto@example.com"
    assert dto.password == "DtoP@ss1"

    # Некорректный email
    with pytest.raises(ValidationError):
        RequestCreateUser(email="not-an-email", password="DtoP@ss1")
