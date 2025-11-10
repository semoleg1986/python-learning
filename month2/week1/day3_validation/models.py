from uuid import UUID, uuid4

from pydantic import BaseModel, EmailStr, Field, condecimal, constr

password_regex = r"^(?=.*[A-Za-z])(?=.*\d).+$"


class ItemModel(BaseModel):
    id: UUID = Field(
        default_factory=uuid4, description="Уникальный идентификатор товара"
    )
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Название товара от 3 до 50 символов",
    )
    price: condecimal(gt=0, decimal_places=2) = Field(
        ..., description="Цена товара, больше 0, максимум 2 знака после запятой"
    )


class UserModel(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: constr(min_length=8, regex=password_regex) = Field(
        ...,
        description="Пароль 8 символов, включая хотя бы одну букву и одну цифру",
    )
