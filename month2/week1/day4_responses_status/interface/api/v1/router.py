from fastapi import APIRouter

from month2.week1.day4_responses_status.interface.api.v1.items.router import (
    items_router,
)

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(items_router)
