from typing import List

from data import products
from fastapi import APIRouter, HTTPException, status
from models import Product

router = APIRouter(
    prefix="/product",
    tags=["product"],
    responses={404: {"description": "Product not found"}},
)


@router.get(
    "/products/", response_model=List[Product], description="Returns all products."
)
def get_products():
    """
    Возвращает список всех продуктов.

    :return: Список объектов `Product`.
    :rtype: List[Product]
    """
    return products


@router.get(
    "/products/{product_id}",
    response_model=Product,
    description="Returns a product by its ID.",
)
def get_product(product_id: int):
    """
    Возвращает продукт по идентификатору.

    :param product_id: Идентификатор продукта.
    :type product_id: int
    :raises HTTPException: Если продукт с таким ID не найден.
    :return: Объект `Product`.
    :rtype: Product
    """
    product = next((p for p in products if p.id == product_id), None)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.post("/products/", response_model=Product, description="Creates a new product.")
def create_product(product: Product):
    """
    Создаёт новый продукт и добавляет его в список.

    ID генерируется автоматически (max(id) + 1).

    :param product: Объект продукта для добавления.
    :type product: Product
    :return: Созданный объект `Product` с новым ID.
    :rtype: Product
    """
    new_id = max((p.id for p in products), default=0) + 1
    product.id = new_id
    products.append(product)
    return product


@router.put(
    "/products/{product_id}",
    response_model=Product,
    description="Updates an existing product by ID.",
)
def update_product(product_id: int, product: Product):
    """
    Обновляет данные существующего продукта по ID.

    :param product_id: Идентификатор продукта для обновления.
    :type product_id: int
    :param product: Обновлённые данные продукта.
    :type product: Product
    :raises HTTPException: Если продукт с таким ID не найден.
    :return: Обновлённый объект `Product`.
    :rtype: Product
    """
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
    description="Deletes a product by ID.",
)
def remove_product(product_id: int):
    """
    Удаляет продукт по идентификатору.

    :param product_id: Идентификатор продукта для удаления.
    :type product_id: int
    :raises HTTPException: Если продукт с таким ID не найден.
    :return: None
    """
    for i, existing_product in enumerate(products):
        if existing_product.id == product_id:
            del products[i]
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
    )
