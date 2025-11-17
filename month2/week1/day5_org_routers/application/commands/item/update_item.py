from decimal import Decimal

from pydantic import BaseModel, Field


class UpdateItemCommand(BaseModel):
    name: str | None = Field(
        None,
        min_length=3,
        max_length=50,
        description="Новое название товара (опционально)",
    )
    price: Decimal | None = Field(
        None,
        gt=0,
        max_digits=10,
        decimal_places=2,
        description="Новая цена товара (опционально)",
    )

    model_config = {
        "validate_assignment": True,
        "extra": "forbid",
    }
