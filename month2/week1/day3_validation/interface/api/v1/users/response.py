from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from month2.week1.day3_validation.interface.api.schemas.paginated_response import (
    PaginatedResponse,
)


class ResponseUser(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор пользователя")
    email: EmailStr = Field(..., description="Электронная почта пользователя")

    model_config = {"from_attributes": True}


UserListResponse = PaginatedResponse[ResponseUser]
