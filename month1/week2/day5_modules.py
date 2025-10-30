"""
Day 5 — Modules and import
Тема: Создание и импорт модулей.
"""
import datetime
import math
import random


def random_sqrt() -> float:
    """Возвращает квадратный корень случайного числа от 1 до 100.

    :return: Квадратный корень случайного числа.
    :rtype: float
    """
    return math.sqrt(random.randint(1, 100))


def current_date() -> str:
    """Возвращает текущую дату в формате YYYY-MM-DD.

    :return: Строка с текущей датой.
    :rtype: str
    """
    return datetime.datetime.now().strftime("%Y-%m-%d")


def from_math_utils() -> None:
    """
    Импортирует функции add, sub, mul, div из модуля math_utils и использует их.
    """
    from math_utils import add, div, mul, sub

    numbers = list(range(0, 100))
    x, y = random.sample(numbers, 2)
    print(f"x = {x}, y = {y}, x + y = {add(x, y)}")
    print(f"x = {x}, y = {y}, x - y = {sub(x, y)}")
    print(f"x = {x}, y = {y}, x * y = {mul(x, y)}")
    print(f"x = {x}, y = {y}, x / y = {div(x, y)}")


if __name__ == "__main__":
    print(f"Случайный корень: {random_sqrt()}")
    print(f"Сегодня: {current_date()}")
    print("\nРабота с модулем math_utils:")
    from_math_utils()
