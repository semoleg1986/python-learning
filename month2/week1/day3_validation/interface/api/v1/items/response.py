from uuid import UUID

from pydantic import BaseModel, Field

from month2.week1.day3_validation.interface.api.schemas.paginated_response import (
    PaginatedResponse,
)


class ResponseCreatedItem(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор товара")


class ResponseItem(BaseModel):
    id: UUID = Field(..., description="Уникальный идентификатор товара")
    name: str = Field(..., description="Название товара")
    price: float = Field(..., description="Цена товара")

    model_config = {"from_attributes": True}


ItemListResponse = PaginatedResponse[ResponseItem]
