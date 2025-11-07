from typing import List
from uuid import UUID, uuid4

from data import products
from fastapi import APIRouter, HTTPException, status
from models import BaseProduct, CreateProduct, ResponseCreateProduct, ResponseProduct

router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={404: {"description": "Product not found"}},
)


@router.get("/products/", response_model=List[ResponseProduct])
def get_products():
    """
    Возвращает список всех продуктов.

    :return: Список объектов `Product`.
    :rtype: List[ResponseProduct]
    """
    return products


@router.get("/products/{product_id}", response_model=ResponseProduct)
def get_product(product_id: UUID):
    """
    Возвращает продукт по идентификатору (UUID).

    :param product_id: UUID продукта.
    :type product_id: UUID
    :raises HTTPException: Если продукт не найден.
    :return: Объект `Product`.
    :rtype: ResponseProduct
    """
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.post("/products/", response_model=ResponseCreateProduct)
def create_product(product: CreateProduct):
    """
    Создаёт новый продукт и добавляет его в список.

    UUID генерируется автоматически.

    :param product: Объект продукта без ID.
    :type product: CreateProduct
    :return: UUID cозданного объекта.
    :rtype: ResponseCreateProduct
    """
    new_product = ResponseProduct(id=uuid4(), name=product.name, price=product.price)
    products.append(new_product)
    return new_product.id


@router.put("/products/{product_id}", response_model=ResponseProduct)
def update_product(product_id: UUID, product: BaseProduct):
    """
    Обновляет данные существующего продукта по UUID.

    :param product_id: UUID продукта.
    :type product_id: UUID
    :param product: Обновлённые данные продукта.
    :type product: BaseProduct
    :raises HTTPException: Если продукт не найден.
    :return: Обновлённый объект `Product`.
    :rtype: ResponseProduct
    """
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            updated_product = ResponseProduct(
                id=product_id, name=product.name, price=product.price
            )
            products[i] = updated_product
            return updated_product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(product_id: UUID):
    """Удаляет продукт по UUID."""
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            del products[i]
            return
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )
