from fastapi import Depends, FastAPI

from month2.week1.day4_responses_status.infrastructure.config.settings import (
    Settings,
    settings,
)
from month2.week1.day4_responses_status.interface.api.v1.router import api_v1_router

tags_metadata = [
    {"name": "info", "description": "Эндпоинты для информации о приложении"},
    {
        "name": "items",
        "description": "Эндпоинты для работы с товарами.",
    },
]

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_tags=tags_metadata,
)


@app.get(
    "/info",
    tags=["info"],
    summary="Информация о приложении",
    description="Возвращает имя приложения и его версию.",
    response_model=dict,
    responses={200: {"description": "Информация успешно получена"}},
)
def info(cfg: Settings = Depends(lambda: settings)):
    """
    Эндпоинт возвращает базовую информацию о приложении.
    """
    return {"app_name": cfg.APP_NAME, "version": cfg.VERSION}


app.include_router(api_v1_router)
