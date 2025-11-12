from pydantic import BaseModel, EmailStr, Field


class UpdateUserCommand(BaseModel):
    email: EmailStr | None = Field(None, description="Новый email пользователя")
    password: str | None = Field(None, description="Новый пароль")
