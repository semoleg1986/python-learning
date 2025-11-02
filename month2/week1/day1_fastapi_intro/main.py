from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/{item_id}")
def read_id(item_id: int):
    return {"item_id": item_id}
