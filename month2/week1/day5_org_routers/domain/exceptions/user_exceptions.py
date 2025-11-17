class UserError(Exception):
    """Базовое исключение для User в Domain."""

    pass


class UserValidationError(UserError):
    """Ошибка при нарушении правил создания или обновления User."""

    pass


class UserAlreadyExistsError(UserError):
    """Выбрасывается, если пользователь с таким именем уже существует."""

    pass


class UserNotFoundError(UserError):
    """Выбрасывается, если пользователь не найден."""

    pass


class UserNotChangedError(UserError):
    """Выбрасывается, если не было изменено ни одно поле"""

    pass
