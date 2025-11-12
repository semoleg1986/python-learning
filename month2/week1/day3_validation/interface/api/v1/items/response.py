from uuid import UUID

from pydantic import BaseModel, Field


class ResponseCreatedItem(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор товара")


class ResponseItem(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор товара")
    name: str = Field(..., description="Название товара")
    price: float = Field(..., description="Цена товара")

    model_config = {"from_attributes": True}


class PaginatedResponse(BaseModel):
    """Обёртка для пагинированного ответа."""

    data: list[ResponseItem] = Field(..., description="Список Item")
