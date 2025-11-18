from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Path, status

from month2.week1.day5_org_routers.dependencies import users_service
from month2.week1.day5_org_routers.domain.exceptions.user_exceptions import (
    UserAlreadyExistsError,
    UserNotChangedError,
    UserNotFoundError,
    UserValidationError,
)
from month2.week1.day5_org_routers.interface.api.v1.users.request import (
    RequestCreateUser,
    RequestUpdateUser,
)
from month2.week1.day5_org_routers.interface.api.v1.users.response import (
    ResponseCreateUser,
    ResponseUser,
)

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get(
    "/",
    response_model=List[ResponseUser],
    summary="Список всех пользователей",
    description="Возвращает полный список пользователей в хранилище.",
)
def get_users() -> List[ResponseUser]:
    """
    Получить список пользователей.

    Возвращает список пользователей.

    :return: Объект с данными о пользователей
    :rtype: List[ResponseUser]
    """
    return [user for user in users_service.list_user()]


@users_router.get(
    "/{user_id}",
    response_model=ResponseUser,
    summary="Получить пользователя по ID",
    description="Возвращает пользователя по UUID.",
    responses={404: {"description": "User with given ID not found"}},
)
def get_user(user_id: UUID = Path) -> ResponseUser:
    """
    Получить пользователя по его UUID.

    :param user_id: Уникальный идентификатор пользователя
    :type user_id: UUID
    :raises HTTPException 404: Если пользователь не найден
    :return: Информация о пользователя
    :rtype: ResponseUser
    """
    try:
        user = users_service.get_user(user_id)
        return ResponseUser.model_validate(user)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@users_router.post(
    "/",
    response_model=ResponseCreateUser,
    status_code=status.HTTP_201_CREATED,
    summary="Создать нового пользователя",
    description="Создаёт нового пользователя с уникальным email.",
    responses={
        400: {"description": "Пользователь с таким email уже существует"},
        422: {"description": "Ошибка валидации данных"},
    },
)
def create_user(req: RequestCreateUser) -> ResponseCreateUser:
    """
    Создать нового пользователя.

    Обрабатывает запрос на создание пользователя. Проверяет уникальность email,
    корректность данных, создаёт команду и передаёт её в сервис.

    :param req: Данные нового пользователя (email и пароль).
    :type req: RequestCreateUser

    :raises HTTPException 400: Если пользователь с таким email уже существует.
    :raises HTTPException 422: Если данные не проходят валидацию.

    :return: Идентификатор созданного пользователя.
    :rtype: ResponseCreateUser
    :status 201: Успешное создание пользователя.
    :status 400: Нарушение бизнес-правил (email уже существует).
    :status 422: Ошибка валидации входных данных.
    """
    try:
        new_user = users_service.create_user(req)
        return ResponseCreateUser(id=new_user.id)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except UserValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )


@users_router.put(
    "/{user_id}",
    response_model=ResponseUser,
    summary="Обновить данные пользователя по ID",
    description="Обновляет email и/или пароль пользователя по ID.",
)
def update_user(user_id: UUID, req: RequestUpdateUser) -> ResponseUser:
    """
    Обновить существующего пользователя по UUID.

    :param user_id: Уникальный идентификатор пользователя
    :type user_id: UUID
    :param req: Новые данные пользователя (email и/или пароль)
    :type req: RequestUpdateUser
    :raises HTTPException 404: Если пользователь не найден
    :raises HTTPException 409: Если email пользователя уже используется
    :raises HTTPException 400: Если данные не изменились
    :return: Обновлённая информация о пользователе
    :rtype: ResponseUser
    """
    try:
        user = users_service.update_user(user_id, req)
        return ResponseUser.model_validate(user)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    except UserValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(e)
        )
    except UserNotChangedError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))


@users_router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить пользователя",
    description="Удаляет пользователя по ID.",
    responses={404: {"description": "User not found"}},
)
def delete_user(user_id: UUID) -> None:
    """
    Удалить пользователя по его UUID.

    :param user_id: Уникальный идентификатор пользователя
    :type user_id: UUID
    :raises HTTPException 404: Если пользователь не найден
    :return: Пустой ответ с кодом 204 при успешном удалении
    :rtype: None
    """
    try:
        users_service.delete_user(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
