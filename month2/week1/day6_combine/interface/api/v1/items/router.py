from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from month2.week1.day6_combine.dependencies import items_service
from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotChangedError,
    ItemNotFoundError,
    ItemValidationError,
)
from month2.week1.day6_combine.interface.api.v1.items.request import (
    RequestCreateItem,
    RequestUpdateItem,
)
from month2.week1.day6_combine.interface.api.v1.items.response import (
    ResponseCreateItem,
    ResponseItem,
)

items_router = APIRouter(prefix="/items", tags=["items"])


@items_router.get(
    "/",
    response_model=List[ResponseItem],
    summary="Список всех товаров",
    description="Возвращает полный список товаров в хранилище.",
)
def get_items():
    """
    Получить список товаров.

    Возвращает список товаров с параметрами пагинации.

    # :param page: Номер страницы (начиная с 1)
    # :type page: int
    # :param per_page: Количество товаров на одной странице (1–100)
    # :type per_page: int
    :return: Объект с данными о товарах и метаинформацией пагинации
    :rtype: List[ResponseItem]
    """
    return [item for item in items_service.list_item()]


@items_router.get(
    "/{item_id}",
    response_model=ResponseItem,
    summary="Получить товар по ID",
    description="Возвращает объект товара по UUID.",
    responses={404: {"description": "Item with given ID not found"}},
)
def get_item(item_id: UUID) -> ResponseItem:
    """
    Получить товар по его UUID.

    :param item_id: Уникальный идентификатор товара
    :type item_id: UUID
    :raises HTTPException 404: Если товар не найден
    :return: Информация о товаре
    :rtype: ResponseItem
    """
    try:
        item = items_service.get_item(item_id)
        return ResponseItem.model_validate(item)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@items_router.post(
    "/",
    response_model=ResponseCreateItem,
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый товар",
    description="Создаёт новый товар с уникальным названием и ценой.",
    responses={
        400: {"description": "Товар с таким именем уже существует"},
        422: {"description": "Ошибка валидации данных"},
    },
)
def create_item(req: RequestCreateItem) -> ResponseCreateItem:
    """
    Создать новый товар.

    :param req: Данные для создания нового товара
    :type req: RequestCreateItem
    :raises HTTPException 400: Если товар с таким именем уже существует
    :return: Статус операции и ID созданного товара
    :rtype: ResponseCreateItem
    """
    try:
        item = items_service.create_item(req)
        return ResponseCreateItem(id=item.id)
    except ItemAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@items_router.put(
    "/{item_id}",
    response_model=ResponseItem,
    summary="Обновить товар по ID",
    description="Обновляет название и/или цену товара по ID.",
)
def update_item(item_id: UUID, req: RequestUpdateItem) -> ResponseItem:
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
    :rtype: ResponseItem
    """
    try:
        item = items_service.update_item(item_id, req)
        return ResponseItem.model_validate(item)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ItemValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail=str(e)
        )
    except ItemNotChangedError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ItemAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@items_router.delete(
    "/{item_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить товар",
    description="Удаляет товар по ID. Возбуждает 404, если товар не найден.",
    responses={404: {"description": "Item not found"}},
)
def delete_item(item_id: UUID):
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
