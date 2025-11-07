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
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.post("/products/", response_model=Product, description="Create product")
def create_product(product: Product):
    new_id = max((p.id for p in products), default=0) + 1
    product.id = new_id
    products.append(product)
    return product


@router.put(
    "/products/{product_id}",
    response_model=Product,
    description="Update product by index",
)
def update_product(product_id: int, product: Product):
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            updated_product = Product(
                id=product_id, name=product.name, price=product.price
            )
            products[i] = updated_product
            return updated_product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )


@router.delete(
    "/products/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete product by index",
)
def remove_product(product_id: int):
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            del products[i]
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )
