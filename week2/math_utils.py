"""
Модуль math_utils — простые арифметические операции.
"""


def add(x: float, y: float) -> float:
    return x + y


def sub(x: float, y: float) -> float:
    return x - y


def mul(x: float, y: float) -> float:
    return x * y


def div(x: float, y: float) -> float:
    if y < 0:
        raise ValueError("На ноль делить нельзя")
    return x / y
