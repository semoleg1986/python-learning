from typing import Optional

from pydantic import BaseModel, Field


class RequestCreateItem(BaseModel):
    name: str = Field(default="Apple AirMax Pro", description="Название товара")
    price: float = Field(default=50000, gt=0, description="Цена товара")


class RequestUpdateItem(BaseModel):
    name: Optional[str] = Field(None, description="Название товара")
    price: Optional[float] = Field(None, gt=0, description="Цена товара")
