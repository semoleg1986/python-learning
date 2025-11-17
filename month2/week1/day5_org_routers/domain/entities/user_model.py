import re
from uuid import UUID, uuid4

from month2.week1.day5_org_routers.domain.exceptions.user_exceptions import (
    UserNotChangedError,
    UserValidationError,
)


class UserModel:
    """
    Домашняя модель пользователя (Domain Entity)
    """

    MIN_PASSWORD_LEN = 8

    def __init__(self, email: str, password: str, id: UUID | None = None) -> None:
        self.id = id or uuid4()
        self.email = self._validate_email(email)
        self.password = self._validate_password(password)

    @staticmethod
    def _validate_email(email: str) -> str:
        email = email.strip()
        if "@" not in email or "." not in email:
            raise UserValidationError("Incorrect email")
        return email

    @classmethod
    def _validate_password(cls, password: str) -> str:
        if len(password) < cls.MIN_PASSWORD_LEN:
            raise UserValidationError("Пароль должен быть минимум 8 символов")

        if not re.search(r"[A-Z]", password):
            raise UserValidationError("Пароль должен содержать заглавную букву")

        if not re.search(r"[a-z]", password):
            raise UserValidationError("Пароль должен содержать строчную букву")

        if not re.search(r"\d", password):
            raise UserValidationError("Пароль должен содержать цифру")

        return password

    def update(self, email: str | None = None, password: str | None = None):
        updated = False

        if email is not None:
            new_email = self._validate_email(email)
            if new_email != self.email:
                self.email = new_email
                updated = True

        if password is not None:
            new_password = self._validate_password(password)
            if new_password != self.password:
                self.password = new_password
                updated = True

        if not updated:
            raise UserNotChangedError("Изменений не было")
