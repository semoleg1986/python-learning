from pydantic import BaseModel, Field, condecimal, constr


class RequestCreateItem(BaseModel):
    name: constr(strip_whitespace=True, min_length=3, max_length=50) = Field(
        ...,
        description="Название товара",
        json_schema_extra={"example": "Apple AirMax Pro"},
    )
    price: condecimal(gt=0, decimal_places=2) = Field(
        ...,
        description="Цена товара, больше 0",
        json_schema_extra={"example": 50000},
    )


class RequestUpdateItem(BaseModel):
    name: constr(strip_whitespace=True, min_length=3, max_length=50) | None = Field(
        None,
        description="Название товара",
        json_schema_extra={"example": "Apple AirMax Pro"},
    )
    price: condecimal(gt=0, decimal_places=2) | None = Field(
        None,
        description="Цена товара, больше 0",
        json_schema_extra={"example": 50000},
    )
