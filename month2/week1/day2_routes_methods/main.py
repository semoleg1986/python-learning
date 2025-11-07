from fastapi import FastAPI
from router import router as product_router

app = FastAPI(
    title="Routes and Methods API",
    description="Simple get, post, put, delete service",
    version="1.0.0",
)

app.include_router(product_router)
