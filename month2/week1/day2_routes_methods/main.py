from typing import List

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Routes and Methods API",
    description="Simple get, post, put, delete service",
    version="1.0.0",
)


class Product(BaseModel):
    name: str = Field(default="Apple AirMax Pro")
    price: float = Field(default=60000, gt=0)


products: List[Product] = []


@app.get("/products/", response_model=List[Product], description="Returns products")
def get_products():
    return products


@app.get(
    "/products/{product_id}",
    response_model=Product,
    description="Returns product by index",
)
def get_product(product_id: int):
    if product_id < 0 or product_id >= len(products):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    product = products[product_id]
    return product


@app.post("/products/", response_model=Product, description="Create product")
def create_product(product: Product):
    products.append(product)
    return product


@app.put(
    "/products/{product_id}",
    response_model=Product,
    description="Update product by index",
)
def update_product(product_id: int, product: Product):
    if product_id < 0 or product_id >= len(products):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    products[product_id] = product
    return product


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete product by index",
)
def remove_product(product_id: int):
    if product_id < 0 or product_id >= len(products):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    del products[product_id]
    pass
