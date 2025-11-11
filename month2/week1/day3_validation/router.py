from uuid import UUID, uuid4

from api.items.request import RequestCreateItem, RequestUpdateItem
from api.items.response import PaginatedResponse, ResponseCreatedItem, ResponseItem
from fastapi import APIRouter, HTTPException, status
from item_repository_memory import ItemRepositoryMemory
from models import ItemModel

repo_items = ItemRepositoryMemory()

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
    all_items = repo_items.list_all()
    return PaginatedResponse(data=all_items)


@items_router.get("/{item_id}", response_model=ResponseItem)
def get_item(item_id: UUID) -> ResponseItem:
    """
    Возврат товара по UUID.

    :param item_id: UUID существующего товара.
    :raises HTTPException: Если товар с указанным UUID не найден.
    :return: Объект ResponseItem.
    """
    existing_item = repo_items.get(item_id)
    if not existing_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return ResponseItem.model_validate(existing_item)


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
    new_id = uuid4()
    new_item = ItemModel(id=new_id, name=item.name, price=item.price)
    repo_items.save(new_item)
    return ResponseCreatedItem(id=new_id)


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
    existing_item = repo_items.get(item_id)
    if not existing_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    updated_item = ItemModel(
        id=item_id,
        name=item.name if item.name is not None else existing_item.name,
        price=item.price if item.price is not None else existing_item.price,
    )
    repo_items.save(updated_item)
    return ResponseItem.model_validate(updated_item)


@items_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(item_id: UUID) -> None:
    """
    Удаляет существующий товар по UUID.

    :param item_id: UUID удаляемого товара.
    :type item_id: UUID
    :raises HTTPException: Если товар с указанным UUID не найден.
    """
    existing_item = repo_items.get(item_id)
    if not existing_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    repo_items.delete(item_id)
    return None


user_routers = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Users not found"}},
)
