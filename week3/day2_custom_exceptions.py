"""
Day 2 — Custom exceptions
Тема: Пользовательские исключения и их обработка.
"""


class NegativeValueError(Exception):
    """Ошибка, возникающая при отрицательном значении."""

    def __str__(self):
        return "Значение не может быть отрицательным!"


class InvalidAgeError(Exception):
    """Ошибка, возникающая при некорректном возрасте."""

    pass


def validate_positive_number(value: int) -> None:
    """
    Проверяет, что число положительное.

    :param value: Проверяемое число.
    :raises NegativeValueError: Если число отрицательное.
    """
    if value < 0:
        raise NegativeValueError()


def check_age(age: int) -> str:
    """
    Проверяет возраст и выбрасывает исключения при ошибках.

    :param age: Возраст.
    :return: Сообщение о корректности возраста.
    :raises InvalidAgeError: Если возраст < 0 или > 120.
    """
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Возраст {age} некорректен!")
    return f"Возраст {age} корректен."
