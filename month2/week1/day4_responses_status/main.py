from fastapi import Depends, FastAPI

from month2.week1.day4_responses_status.infrastructure.config.settings import (
    Settings,
    settings,
)
from month2.week1.day4_responses_status.interface.api.v1.router import api_v1_router

app = FastAPI(
    title=settings.APP_NAME, version=settings.VERSION, description=settings.DESCRIPTION
)


@app.get("/info")
def info(cfg: Settings = Depends(lambda: settings)):
    return {"app_name": cfg.APP_NAME, "version": cfg.VERSION}


app.include_router(api_v1_router)
