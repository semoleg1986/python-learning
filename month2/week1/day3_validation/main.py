from config import Settings, settings
from fastapi import Depends, FastAPI
from router import items_router

app = FastAPI(
    title=settings.APP_NAME, version=settings.VERSION, description=settings.DESCRIPTION
)


@app.get("/info")
def info(cfg: Settings = Depends(lambda: settings)):
    return {"app_name": cfg.APP_NAME, "version": cfg.VERSION}


app.include_router(items_router)
