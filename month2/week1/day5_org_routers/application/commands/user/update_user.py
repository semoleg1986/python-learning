from pydantic import BaseModel, EmailStr, Field


class UpdateUserCommand(BaseModel):
    email: EmailStr | None = Field(None, description="Новая почта пользователя")
    password: str | None = Field(None, description="Новый пароль пользователя")
