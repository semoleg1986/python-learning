from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class BaseProduct(BaseModel):
    """
    Базовая модель продукта.
    """

    name: str = Field(default="Apple AirMax Pro", description="Название продукта")
    price: float = Field(default=60000, gt=0, description="Цена продукта (в рублях)")


class CreateProduct(BaseProduct):
    """
    Модель для создания нового продукта.
    UUID генерируется автоматически на сервере.
    """

    pass


class ResponseProduct(BaseProduct):
    """
    Модель ответа API с информацией о продукте.
    Содержит уникальный идентификатор UUID.
    """

    id: UUID = Field(
        default_factory=uuid4, description="Уникальный идентификатор продукта"
    )


class ResponseCreateProduct(BaseModel):
    """
    Модель ответа API созданного продукта.
    Содержит уникальный идентификатор UUID.
    """

    id: UUID = Field(
        default_factory=uuid4, description="Уникальный идентификатор продукта"
    )


class PaginationMeta(BaseModel):
    """Метаданные пагинации."""

    total_records: int = Field(..., description="Общее количество записей")
    page: int = Field(..., description="Номер текущей страницы")
    per_page: int = Field(..., description="Количество записей на странице")
    pages: int = Field(..., description="Всего страниц")
    has_next: bool = Field(..., description="Есть ли следующая страница")
    has_prev: bool = Field(..., description="Есть ли предыдущая страница")


class PaginatedResponse(BaseModel):
    """Обёртка для пагинированного ответа."""

    data: List[ResponseProduct] = Field(..., description="Список продуктов")
    pagination: PaginationMeta = Field(..., description="Метаданные пагинации")
