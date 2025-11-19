from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field

from month2.week1.day6_combine.interface.api.schemas.paginated_response import (
    PaginatedResponse,
)


class ResponseCreateItem(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор товара")


class ResponseItem(ResponseCreateItem):
    name: str = Field(..., description="Название товара")
    price: float = Field(..., description="Цена товара")

    model_config = {"from_attributes": True}


class InfoResponse(BaseModel):
    status: str = Field(..., description="Статус операции, например success/fail")
    message: str = Field(..., description="Описание результата")
    data: Any = Field(None, description="Результат операции")


ItemListResponse = PaginatedResponse[ResponseItem]
