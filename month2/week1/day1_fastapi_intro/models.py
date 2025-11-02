from pydantic import BaseModel


class RootResponse(BaseModel):
    message: str


class ItemResponse(BaseModel):
    item_id: int
