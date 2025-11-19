from decimal import Decimal
from uuid import UUID, uuid4

from month2.week1.day6_combine.domain.exceptions.item_exceptions import (
    ItemNotChangedError,
    ItemValidationError,
)


class ItemModel:
    MIN_NAME_LEN = 3
    MAX_NAME_LEN = 30

    def __init__(
        self, name: str, price: float | Decimal, id: UUID | None = None
    ) -> None:
        self.id: UUID = id or uuid4()
        self.name = self._validate_name(name)
        self.price = self._validate_price(price)

    @staticmethod
    def _validate_name(name: str) -> str:
        clean_name = name.strip()
        if not ItemModel.MIN_NAME_LEN <= len(clean_name) <= ItemModel.MAX_NAME_LEN:
            raise ItemValidationError(
                f"Название({ItemModel.MIN_NAME_LEN}-{ItemModel.MAX_NAME_LEN})"
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
