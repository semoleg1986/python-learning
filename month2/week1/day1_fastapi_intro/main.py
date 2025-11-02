from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    data = {"message": "Hello, World!"}
    return JSONResponse(content=data, status_code=200)


@app.get("/{item_id}")
def read_id(item_id: int):
    data = {"id": item_id}
    return JSONResponse(content=data, status_code=200)
