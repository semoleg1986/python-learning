from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from month2.week1.day3_validation.application.services.item_service import ItemService
from month2.week1.day3_validation.infrastructure.repositories.item_memory import (
    ItemRepositoryMemory,
)
from month2.week1.day3_validation.interface.api.v1.items.request import (
    RequestCreateItem,
    RequestUpdateItem,
)
from month2.week1.day3_validation.interface.api.v1.items.response import (
    PaginatedResponse,
    ResponseCreatedItem,
    ResponseItem,
)

repo = ItemRepositoryMemory()
service = ItemService(repo)

items_router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Items not found"}},
)


@items_router.get("/", response_model=PaginatedResponse)
def get_items() -> PaginatedResponse:
    """
    Возвращает список всех товаров.

    :return: PaginatedResponse с ключом "data", содержащим список объектов ItemModel.
    :rtype: PaginatedResponse
    """
    all_items = service.list_item()
    return PaginatedResponse(data=all_items)


@items_router.get("/{item_id}", response_model=ResponseItem)
def get_item(item_id: UUID) -> ResponseItem:
    """
    Возврат товара по UUID.

    :param item_id: UUID существующего товара.
    :raises HTTPException: Если товар с указанным UUID не найден.
    :return: Объект ResponseItem.
    """
    try:
        existing_item = service.get_item(item_id)
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
    new_item = service.create_item(item)
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
        return ResponseItem.model_validate(service.update_item(item_id, item))
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
        service.delete_item(item_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )


user_routers = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Users not found"}},
)
