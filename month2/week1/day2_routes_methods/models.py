from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(default="Apple AirMax Pro")
    price: float = Field(default=60000, gt=0)
