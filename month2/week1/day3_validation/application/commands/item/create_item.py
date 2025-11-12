from pydantic import BaseModel, Field, condecimal


class CreateItemCommand(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Название товара от 3 до 50 символов",
    )
    price: condecimal(gt=0, decimal_places=2) = Field(
        ...,
        description="Цена товара, больше 0, максимум 2 знака после запятой",
    )
