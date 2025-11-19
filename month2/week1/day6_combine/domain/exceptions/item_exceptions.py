class ItemError(Exception):
    "Базовае исключение для Item в Domain"

    pass


class ItemValidationError(ItemError):
    """Ошибка при нарушении правил создания или обновления Item."""

    pass


class ItemAlreadyExistsError(ItemError):
    """Выбрасывается, если товар с таким именем уже существует."""

    pass


class ItemNotFoundError(ItemError):
    """Выбрасывается, если товар не найден."""

    pass


class ItemNotChangedError(ItemError):
    """Выбрасывается, если не было изменено ни одно поле"""

    pass
