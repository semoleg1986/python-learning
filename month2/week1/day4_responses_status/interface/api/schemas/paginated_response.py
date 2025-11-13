from typing import Generic, TypeVar

from pydantic import Field
from pydantic.generics import GenericModel

from month2.week1.day4_responses_status.interface.api.schemas.meta import PaginationMeta

T = TypeVar("T")


class PaginatedResponse(GenericModel, Generic[T]):
    """Обёртка для пагинированного ответа с универсальным типом данных."""

    data: list[T] = Field(..., description="Список объектов")
    pagination: PaginationMeta = Field(..., description="Метаданные пагинации")
