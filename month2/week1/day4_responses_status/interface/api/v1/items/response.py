from uuid import UUID

from pydantic import BaseModel, Field


class ResponseCreateItem(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор товара")


class ResponseItem(ResponseCreateItem):
    name: str = Field(..., description="Название товара")
    price: float = Field(..., description="Цена товара")

    model_config = {"from_attributes": True}
