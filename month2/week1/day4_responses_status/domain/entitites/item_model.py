from decimal import Decimal
from uuid import UUID, uuid4

from month2.week1.day4_responses_status.domain.exceptions.item_exceptions import (
    ItemNotChangedError,
    ItemValidationError,
)


class Item:
    """
    Домашняя модель товара (Domain Entity)
    """

    MIN_NAME_LENGTH = 3
    MAX_NAME_LENGTH = 50

    def __init__(
        self, name: str, price: float | Decimal, id: UUID | None = None
    ) -> None:
        self.id: UUID = id or uuid4()
        self.name = self._validate_name(name)
        self.price = self._validate_price(price)

    @staticmethod
    def _validate_name(name: str) -> str:
        clean_name = name.strip()
        if not (Item.MIN_NAME_LENGTH <= len(clean_name) <= Item.MAX_NAME_LENGTH):
            raise ItemValidationError(
                f"Название({Item.MIN_NAME_LENGTH}-{Item.MAX_NAME_LENGTH})"
            )
        return clean_name

    @staticmethod
    def _validate_price(price: float | Decimal) -> Decimal:
        if price is None or price <= 0:
            raise ItemValidationError("Цена товара должна быть больше 0")
        return Decimal(price).quantize(Decimal("0.01"))

    def update(self, name: str | None = None, price: float | Decimal = None):
        """
        Обновление полей Item.
        """
        updated = False

        if name is not None:
            clean_name = self._validate_name(name)
            if clean_name != self.name:
                self.name = clean_name
                updated = True

        if price is not None:
            clean_price = self._validate_price(price)
            if clean_price != self.price:
                self.price = clean_price
                updated = True

        if not updated:
            raise ItemNotChangedError("При обновлении не изменилось ни одно поле")

        return self
