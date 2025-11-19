from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from month2.week1.day6_combine.interface.api.schemas.meta import PaginationMeta

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    """Обёртка для пагинированного ответа с универсальным типом данных."""

    data: list[T] = Field(..., description="Список объектов")
    pagination: PaginationMeta = Field(..., description="Метаданные пагинации")

    model_config = {"arbitrary_types_allowed": True}
