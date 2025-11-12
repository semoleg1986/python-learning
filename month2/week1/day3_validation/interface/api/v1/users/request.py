from pydantic import BaseModel, EmailStr, Field, constr, field_validator


class RequestCreateUser(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: constr(min_length=8) = Field(..., description="Пароль минимум 8 символов")

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


class RequestUpdateUser(BaseModel):
    email: EmailStr | None = Field(None, description="Новый email пользователя")
    password: str | None = Field(None, description="Новый пароль")

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
