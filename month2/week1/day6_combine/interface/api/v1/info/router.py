from fastapi import APIRouter, Depends

from month2.week1.day6_combine.infrastructure.config.settings import Settings, settings
from month2.week1.day6_combine.interface.api.v1.info.response import ResponseInfo

info_router = APIRouter(
    prefix="/info",
    tags=["info"],
)


@info_router.get(
    "/info",
    tags=["info"],
    summary="Информация о приложении",
    description="Возвращает имя приложения и его версию.",
    response_model=ResponseInfo,
    responses={200: {"description": "Информация успешно получена"}},
)
def info(cfg: Settings = Depends(lambda: settings)) -> ResponseInfo:
    """
    Эндпоинт возвращает базовую информацию о приложении.
    """
    return ResponseInfo(app_name=cfg.APP_NAME, version=cfg.VERSION)
