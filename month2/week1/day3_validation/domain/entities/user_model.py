from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: str = Field(..., description="Хэшированный пароль пользователя")
