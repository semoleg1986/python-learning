from pydantic import BaseModel, Field


class PaginationMeta(BaseModel):
    total_records: int = Field(..., description="Общее количество записей")
    page: int = Field(..., description="Номер текущей страницы")
    per_page: int = Field(..., description="Количество записей на странице")
    pages: int = Field(..., description="Всего страниц")
    has_next: bool = Field(..., description="Есть ли следующая страница")
    has_prev: bool = Field(..., description="Есть ли предыдущая страница")
