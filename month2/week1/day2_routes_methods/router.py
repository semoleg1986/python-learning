from typing import List

from data import products
from fastapi import APIRouter, HTTPException, status
from models import Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={"404": {"description": "product not found"}},
)


@router.get("/products/", response_model=List[Product], description="Returns products")
def get_products():
    return products


@router.get(
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


@router.post("/products/", response_model=Product, description="Create product")
def create_product(product: Product):
    products.append(product)
    return product


@router.put(
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


@router.delete(
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
