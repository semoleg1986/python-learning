from uuid import UUID

from fastapi import APIRouter, HTTPException, Path, status

from month2.week1.day4_responses_status.dependencies import items_service
from month2.week1.day4_responses_status.domain.exceptions.item_exceptions import (
    ItemAlreadyExistsError,
    ItemNotFoundError,
)
from month2.week1.day4_responses_status.interface.api.v1.items.request import (
    RequestCreateItem,
    RequestUpdateItem,
)
from month2.week1.day4_responses_status.interface.api.v1.items.response import (
    ResponseCreateItem,
    ResponseItem,
)

items_router = APIRouter(
    prefix="/items",
    tags=["items"],  # Swagger group
)


@items_router.get(
    "/",
    response_model=list[ResponseItem],
    summary="Список всех товаров",
    description="Возвращает полный список товаров в хранилище.",
)
def get_items():
    items = items_service.list_item()
    return [ResponseItem.model_validate(item) for item in items]


@items_router.get(
    "/{item_id}",
    response_model=ResponseItem,
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
):
    try:
        item = items_service.get_item(item_id)
        return ResponseItem.model_validate(item)
    except ItemNotFoundError:
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")


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
def create_item(req: RequestCreateItem):
    try:
        item = items_service.create_item(req)
        return ResponseCreateItem(id=item.id)
    except ItemAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@items_router.put(
    "/{item_id}",
    response_model=ResponseItem,
    summary="Обновить товар",
    description="Обновляет название и/или цену товара по ID.",
    responses={
        404: {"description": "Item not found"},
        409: {"description": "Item with this name already exists"},
        422: {"description": "Ошибка валидации входных данных"},
    },
)
def update_item(item_id: UUID, req: RequestUpdateItem):
    try:
        item = items_service.update_item(item_id, req)
        return ResponseItem.model_validate(item)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except ItemAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


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
    try:
        items_service.delete_item(item_id)
    except ItemNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
