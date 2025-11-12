from math import ceil
from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from month2.week1.day3_validation.dependencies import user_service
from month2.week1.day3_validation.interface.api.schemas.meta import PaginationMeta
from month2.week1.day3_validation.interface.api.v1.users.request import (
    RequestCreateUser,
    RequestUpdateUser,
)
from month2.week1.day3_validation.interface.api.v1.users.response import (
    ResponseUser,
    UserListResponse,
)

users_router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Users not found"}},
)


@users_router.get("/", response_model=UserListResponse)
def get_users(
    page: int = Query(1, ge=1, description="Номер страницы"),
    per_page: int = Query(
        10, ge=1, le=100, description="Количество продуктов в страницу"
    ),
) -> UserListResponse:
    """
    Возвращает список всех пользователь.

    :return: UserListResponse с ключом "data", содержащим список объектов ResponseUser.
    :rtype: UserListResponse
    """
    all_users = user_service.list_users()
    total_users = len(all_users)
    total_pages = ceil(total_users / per_page) if total_users > 0 else 1

    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = all_users[start:end]

    pagination_meta = PaginationMeta(
        total_records=total_users,
        page=page,
        per_page=per_page,
        pages=total_pages,
        has_next=page < total_pages,
        has_prev=page > 1,
    )
    return UserListResponse(
        data=paginated_data,
        pagination=pagination_meta,
    )


@users_router.get("/{user_id}", response_model=ResponseUser)
def get_user(user_id: UUID) -> ResponseUser:
    """
    Возврат пользователя по UUID.

    :param user_id: UUID существующего пользователя.
    :raises HTTPException: Если пользователь с указанным UUID не найден.
    :return: Объект ResponseUser.
    """
    try:
        user = user_service.get_user(user_id)
        return ResponseUser.model_validate(user)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@users_router.post(
    "/", response_model=ResponseUser, status_code=status.HTTP_201_CREATED
)
def create_user(user: RequestCreateUser) -> ResponseUser:
    """
    Создаёт нового пользователя с автоматически сгенерированным UUID.

    :param user: Данные нового товара.
    :type user: RequestCreateUser
    :return: Словарь с ключом "id" и UUID созданного пользователя.
    :rtype: ResponseUser
    """
    new_user = user_service.create_user(user)
    return ResponseUser(id=new_user.id, email=new_user.email)


@users_router.put("/{user_id}", response_model=ResponseUser)
def update_user(user_id: UUID, user: RequestUpdateUser) -> ResponseUser:
    """
    Обновляет существующего пользователя по UUID.

    :param user_id: UUID существующего пользователя.
    :type user_id: UUID
    :param user: Данные для обновления пользователя.
    :type user: RequestUpdateItem.
    :raises HTTPException: Если пользователь с указанным UUID не найден.
    :return: Обновлённый объект ResponseUser.
    :rtype: ResponseUser
    """
    try:
        return ResponseUser.model_validate(user_service.update_user(user_id, user))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@users_router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_item(user_id: UUID) -> None:
    """
    Удаляет существующего пользователя по UUID.

    :param user_id: UUID удаляемого пользователя.
    :type user_id: UUID
    :raises HTTPException: Если пользователь с указанным UUID не найден.
    """
    try:
        user_service.delete_user(user_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
