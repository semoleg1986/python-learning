from fastapi import APIRouter

from month2.week1.day6_combine.interface.api.v1.info.router import info_router
from month2.week1.day6_combine.interface.api.v1.items.router import items_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(items_router)
v1_router.include_router(info_router)
