"""
Day 1 — Numbers practice
Задачи на базовые операции с числами.
"""


def is_even(n: int) -> bool:
    """
    Проверяет, является ли число чётным.

    :param n: Целое число.
    :type n: int
    :return: True, если число чётное, иначе False.
    :rtype: bool
    """
    return n % 2 == 0


def digit_sum(s: int) -> int:
    """
    Вычисляет сумму цифр целого числа.

    :param s: Целое число
    :type s: int
    :return: Сумма цифр числа.
    :rtype: int
    """
    return sum(int(i) for i in str(s))


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n (n!).

    Реализовано через цикл.

    :param n: Целое неотрицательное число.
    :type n: int
    :return: Факториал числа n.
    :rtype: int
    """
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def factorial2(n: int) -> int:
    """
    Вычисляет факториал числа n (n!).

    Реализовано через рекурсивный вызов функции.

    :param n: Целое неотрицательное число.
    :type n: int
    :return: Факториал числа n.
    :rtype: int
    """
    if n == 0:
        return 1
    return n * factorial2(n - 1)
