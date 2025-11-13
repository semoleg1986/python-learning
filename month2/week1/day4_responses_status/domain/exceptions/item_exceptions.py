class ItemAlreadyExistsError(Exception):
    """Выбрасывается, если товар с таким именем уже существует."""

    pass


class ItemNotFoundError(Exception):
    """Выбрасывается, если товар не найден."""

    pass
