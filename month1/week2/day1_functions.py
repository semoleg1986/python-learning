"""
Day 8 — Functions and arguments
Тема: Определение функций, *args, **kwargs.
"""
from datetime import datetime
from typing import Any


def sum_all(*args: int) -> int:
    """
    Возвращает сумму всех переданных чисел.

    :param args: Набор чисел.
    :type args: int
    :return: Сумма чисел.
    :rtype: int
    """
    if not all(isinstance(i, (int, float)) for i in args):
        raise ValueError("Все аргументы должны быть числами")
    return sum(args)


def print_info(**kwargs: Any) -> None:
    """
    Выводит пары ключ–значение из kwargs.

    :param kwargs: Именованные аргументы.
    :type kwargs: str
    :return: None
    """
    for k, v in kwargs.items():
        print(f"{k} = {v}")


def calc_avg(*args: float) -> float:
    """
    Вычисляет среднее арифметическое всех переданных чисел.

    :param args: Набор чисел.
    :type args: float
    :return: Среднее значение.
    :rtype: float
    """
    if not args:
        raise ValueError("Нужно передать хотя бы одно число")

    if not all(isinstance(i, (int, float)) for i in args):
        raise ValueError("Все аргументы должны быть числами")

    return sum(args) / len(args)


if __name__ == "__main__":
    print(sum_all())
    print(sum_all(1, 2, 3, 4, 5))
    print_info(name="Print info", time=datetime.now(), lang="python")
