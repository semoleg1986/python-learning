from decimal import Decimal

from pydantic import BaseModel, Field


class CreateItemCommand(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Название товара от 3 до 50 символов",
    )
    price: Decimal = Field(
        ...,
        gt=0,
        max_digits=10,
        decimal_places=2,
        description="Цена товара, больше 0, максимум 2 знака после запятой",
    )
