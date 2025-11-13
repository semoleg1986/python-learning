from pydantic import BaseModel, Field


class RequestCreateItem(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Название товара",
        example="Apple AirMax Pro",
    )
    price: float = Field(..., gt=0, description="Цена товара, больше 0", example=50000)


class RequestUpdateItem(BaseModel):
    name: str | None = Field(
        None,
        min_length=3,
        max_length=50,
        description="Название товара",
        example="Apple AirMax Pro",
    )
    price: float | None = Field(
        None, gt=0, description="Цена товара, больше 0", example=50000
    )
