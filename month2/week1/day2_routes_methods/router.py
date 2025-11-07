from typing import Dict
from uuid import UUID, uuid4

from data import products
from fastapi import APIRouter, HTTPException, status
from models import BaseProduct, CreateProduct, ResponseCreateProduct, ResponseProduct

router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={404: {"description": "Product not found"}},
)


@router.get("/products/", response_model=Dict[UUID, ResponseProduct])
def get_products():
    """
    Возвращает список всех продуктов.

    :return: Список объектов `Product`.
    :rtype: Dict[UUID, ResponseProduct]
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
    product = products.get(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.post(
    "/products/",
    response_model=ResponseCreateProduct,
    status_code=status.HTTP_201_CREATED,
)
def create_product(product: CreateProduct):
    """
    Создаёт новый продукт и добавляет его в список.

    UUID генерируется автоматически.

    :param product: Объект продукта без ID.
    :type product: CreateProduct
    :return: UUID cозданного объекта.
    :rtype: ResponseCreateProduct
    """
    new_id = uuid4()
    new_product = ResponseProduct(id=new_id, name=product.name, price=product.price)
    products[new_id] = new_product
    return ResponseCreateProduct(id=new_id)


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
    if product_id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    updated_product = ResponseProduct(id=product_id, **product.model_dump())
    products[product_id] = updated_product
    return updated_product


@router.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product(product_id: UUID):
    """Удаляет продукт по UUID."""
    if product_id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    del products[product_id]
