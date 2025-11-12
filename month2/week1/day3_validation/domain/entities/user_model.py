from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: str = Field(
        ...,
        description="Пароль минимум 8 с, с заглавной, строчной, цифрой и спецсимволом",
    )

    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("Пароль должен быть минимум 8 символов")
        if not any(c.isupper() for c in value):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву")
        if not any(c.islower() for c in value):
            raise ValueError("Пароль должен содержать хотя бы одну маленькую букву")
        if not any(c.isdigit() for c in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not any(c in '!@#$%^&*(),.?":{}|<>' for c in value):
            raise ValueError("Пароль должен содержать хотя бы один специальный символ")
        return value
