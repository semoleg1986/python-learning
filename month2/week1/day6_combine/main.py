from fastapi import FastAPI

from month2.week1.day6_combine.infrastructure.config.settings import settings
from month2.week1.day6_combine.interface.api.router import api_router

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


app.include_router(api_router)
