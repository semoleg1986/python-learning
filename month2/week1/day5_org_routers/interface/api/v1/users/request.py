from pydantic import BaseModel, EmailStr, Field, field_validator


class RequestCreateUser(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Электронная почта пользователя",
        json_schema_extra={"example": "test@example.com"},
    )
    password: str = Field(
        ...,
        min_length=8,
        description="Пароль минимум 8 символов, должен содержать буквы и цифры",
        json_schema_extra={"example": "Passw0rd123"},
    )

    @field_validator("password")
    def validate_password(cls, v: str) -> str:
        if not any(c.isdigit() for c in v):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not any(c.isalpha() for c in v):
            raise ValueError("Пароль должен содержать хотя бы одну букву")
        return v


class RequestUpdateUser(BaseModel):
    email: EmailStr | None = Field(
        None,
        description="Новый email пользователя",
        json_schema_extra={"example": "updated@example.com"},
    )
    password: str | None = Field(
        None,
        min_length=8,
        description="Новый пароль (минимум 8 символов, буквы и цифры)",
        json_schema_extra={"example": "NewPass2025"},
    )

    @field_validator("password")
    def validate_password(cls, v: str | None) -> str | None:
        if v is None:
            return v
        if not any(c.isdigit() for c in v):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not any(c.isalpha() for c in v):
            raise ValueError("Пароль должен содержать хотя бы одну букву")
        return v
