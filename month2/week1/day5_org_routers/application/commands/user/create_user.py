from pydantic import BaseModel, EmailStr, Field


class CreateUserCommand(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: str = Field(..., description="Хэшированный пароль пользователя")
