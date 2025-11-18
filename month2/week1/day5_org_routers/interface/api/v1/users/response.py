from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class ResponseCreateUser(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор пользователя")


class ResponseUser(ResponseCreateUser):
    email: EmailStr = Field(..., description="Электронная почта пользователя")

    model_config = {"from_attributes": True}
