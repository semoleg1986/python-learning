"""
Day 1 — Numbers practice
Задачи на базовые операции с числами.
"""


def is_even(n: int) -> bool:
    return n % 2 == 0


def digit_sum(s: int) -> int:
    return sum(int(i) for i in str(s))


def factorial(n: int) -> int:
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def factorial2(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial2(n - 1)
