from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Example API",
    description="Simple get service with typed responses",
    version="1.0.0",
)


class RootResponse(BaseModel):
    message: str


class ItemResponse(BaseModel):
    item_id: int


@app.get("/", response_model=RootResponse, description="Returns a welcome message")
def read_root():
    return RootResponse(message="Hello, World!")


@app.get(
    "/item/{item_id}",
    response_model=ItemResponse,
    description="Returns item information by ID",
)
def read_item(item_id: int):
    return ItemResponse(item_id=item_id)
