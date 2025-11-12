from math import ceil
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from month2.week1.day3_validation.dependencies import items_service
from month2.week1.day3_validation.interface.api.schemas.meta import PaginationMeta
from month2.week1.day3_validation.interface.api.v1.items.request import (
    RequestCreateItem,
    RequestUpdateItem,
)
from month2.week1.day3_validation.interface.api.v1.items.response import (
    ItemListResponse,
    ResponseCreatedItem,
    ResponseItem,
)

items_router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Items not found"}},
)


@items_router.get("/", response_model=ItemListResponse)
def get_items(
    page: int = Query(1, ge=1, description="Номер страницы"),
    per_page: int = Query(
        10, ge=1, le=100, description="Количество продуктов в страницу"
    ),
) -> ItemListResponse:
    """
    Возвращает список всех товаров.

        :param page: Номер текущей страницы (по умолчанию 1).
    :param per_page: Количество записей на странице (по умолчанию 10).
    :return: ItemListResponse с ключом "data", содержащим список объектов ResponseItem.
    :rtype: ItemListResponse
    """
    all_items = items_service.list_item()
    total_items = len(all_items)
    total_pages = ceil(total_items / per_page) if total_items > 0 else 1

    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = all_items[start:end]

    pagination_meta = PaginationMeta(
        total_records=total_items,
        page=page,
        per_page=per_page,
        pages=total_pages,
        has_next=page < total_pages,
        has_prev=page > 1,
    )
    return ItemListResponse(
        data=paginated_data,
        pagination=pagination_meta,
    )


@items_router.get("/{item_id}", response_model=ResponseItem)
def get_item(item_id: UUID) -> ResponseItem:
    """
    Возврат товара по UUID.

    :param item_id: UUID существующего товара.
    :raises HTTPException: Если товар с указанным UUID не найден.
    :return: Объект ResponseItem.
    """
    try:
        existing_item = items_service.get_item(item_id)
        return ResponseItem.model_validate(existing_item)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


@items_router.post(
    "/", response_model=ResponseCreatedItem, status_code=status.HTTP_201_CREATED
)
def create_item(item: RequestCreateItem) -> ResponseCreatedItem:
    """
    Создаёт новый товар с автоматически сгенерированным UUID.

    :param item: Данные нового товара.
    :type item: RequestCreateItem
    :return: Словарь с ключом "id" и UUID созданного товара.
    :rtype: ResponseCreatedItem
    """
    new_item = items_service.create_item(item)
    return ResponseCreatedItem(id=new_item.id)


@items_router.put("/{item_id}", response_model=ResponseItem)
def update_item(item_id: UUID, item: RequestUpdateItem) -> ResponseItem:
    """
    Обновляет существующий товар по UUID.

    :param item_id: UUID существующего товара.
    :type item_id: UUID
    :param item: Данные для обновления товара.
    :type item: RequestUpdateItem.
    :raises HTTPException: Если товар с указанным UUID не найден.
    :return: Обновлённый объект ResponseItem.
    :rtype: ResponseItem
    """
    try:
        return ResponseItem.model_validate(items_service.update_item(item_id, item))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


@items_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: UUID) -> None:
    """
    Удаляет существующий товар по UUID.

    :param item_id: UUID удаляемого товара.
    :type item_id: UUID
    :raises HTTPException: Если товар с указанным UUID не найден.
    """
    try:
        items_service.delete_item(item_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
