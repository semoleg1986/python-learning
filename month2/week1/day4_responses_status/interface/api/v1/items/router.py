from math import ceil
from uuid import UUID

from fastapi import APIRouter, HTTPException, Path, Query, status

from month2.week1.day4_responses_status.dependencies import items_service
from month2.week1.day4_responses_status.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotChangedError,
    ItemNotFoundError,
)
from month2.week1.day4_responses_status.interface.api.schemas.meta import PaginationMeta
from month2.week1.day4_responses_status.interface.api.v1.items.request import (
    RequestCreateItem,
    RequestUpdateItem,
)
from month2.week1.day4_responses_status.interface.api.v1.items.response import (
    InfoResponse,
    ItemListResponse,
    ResponseCreateItem,
    ResponseItem,
)

items_router = APIRouter(
    prefix="/items",
    tags=["items"],  # Swagger group
)


@items_router.get(
    "/",
    response_model=ItemListResponse,
    summary="Список всех товаров",
    description="Возвращает полный список товаров в хранилище.",
)
def get_items(
    page: int = Query(1, ge=1, description="Номер страницы"),
    per_page: int = Query(
        10, ge=1, le=100, description="Количество продуктов в страницу"
    ),
) -> ItemListResponse:
    """
    Получить список товаров.

    Возвращает список товаров с параметрами пагинации.

    :param page: Номер страницы (начиная с 1)
    :type page: int
    :param per_page: Количество товаров на одной странице (1–100)
    :type per_page: int
    :return: Объект с данными о товарах и метаинформацией пагинации
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


@items_router.get(
    "/{item_id}",
    response_model=InfoResponse,
    summary="Получить товар по ID",
    description="Возвращает объект товара по UUID.",
    responses={404: {"description": "Item with given ID not found"}},
)
def get_item(
    item_id: UUID = Path(
        ...,
        description="UUID товара для получения",  # описание для Swagger
        example="f47ac10b-58cc-4372-a567-0e02b2c3d479",  # пример UUID
    )
) -> InfoResponse:
    """
    Получить товар по его UUID.

    :param item_id: Уникальный идентификатор товара
    :type item_id: UUID
    :raises HTTPException 404: Если товар не найден
    :return: Информация о товаре
    :rtype: InfoResponse
    """
    try:
        item = items_service.get_item(item_id)
        return InfoResponse(
            status="success",
            message="Item fetched successful",
            data=ResponseItem.model_validate(item),
        )
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")


@items_router.post(
    "/",
    response_model=InfoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый товар",
    description="Создаёт новый товар с уникальным названием и ценой.",
    responses={
        400: {"description": "Товар с таким именем уже существует"},
        422: {"description": "Ошибка валидации данных"},
    },
)
def create_item(req: RequestCreateItem) -> InfoResponse:
    """
    Создать новый товар.

    :param req: Данные для создания нового товара
    :type req: RequestCreateItem
    :raises HTTPException 400: Если товар с таким именем уже существует
    :return: Статус операции и ID созданного товара
    :rtype: InfoResponse
    """
    try:
        item = items_service.create_item(req)
        return InfoResponse(
            status="success",
            message="Item created",
            data=ResponseCreateItem(id=item.id),
        )
    except ItemAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@items_router.put(
    "/{item_id}",
    response_model=InfoResponse,
    summary="Обновить товар",
    description="Обновляет название и/или цену товара по ID.",
    responses={
        404: {"description": "Item not found"},
        409: {"description": "Item with this name already exists"},
        422: {"description": "Ошибка валидации входных данных"},
    },
)
def update_item(item_id: UUID, req: RequestUpdateItem) -> InfoResponse:
    """
    Обновить существующий товар по UUID.

    :param item_id: Уникальный идентификатор товара
    :type item_id: UUID
    :param req: Новые данные товара (имя и/или цена)
    :type req: RequestUpdateItem
    :raises HTTPException 404: Если товар не найден
    :raises HTTPException 409: Если имя товара уже используется
    :raises HTTPException 400: Если данные не изменились
    :return: Обновлённая информация о товаре
    :rtype: InfoResponse
    """
    try:
        item = items_service.update_item(item_id, req)
        return InfoResponse(
            status="success",
            message="Item updated",
            data=ResponseItem.model_validate(item),
        )
    except ItemNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ItemAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
    except ItemNotChangedError as e:
        raise HTTPException(status_code=400, detail=str(e))


@items_router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить товар",
    description="Удаляет товар по ID. Возбуждает 404, если товар не найден.",
    responses={404: {"description": "Item not found"}},
)
def delete_item(
    item_id: UUID = Path(
        ...,
        description="UUID товара для удаления",
        example="f47ac10b-58cc-4372-a567-0e02b2c3d479",
    )
):
    """
    Удалить товар по его UUID.

    :param item_id: Уникальный идентификатор товара
    :type item_id: UUID
    :raises HTTPException 404: Если товар не найден
    :return: Пустой ответ с кодом 204 при успешном удалении
    :rtype: None
    """
    try:
        items_service.delete_item(item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
