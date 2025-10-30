"""
Day 5 — Standard library
Тема: datetime, collections, itertools, functools.
"""

from collections import Counter
from datetime import datetime
from functools import reduce
from itertools import zip_longest


def current_time() -> str:
    """Возвращает текущее время в формате HH:MM:SS."""
    return datetime.now().strftime("%H:%M:%S")


def combine_lists(a: list[int], b: list[int]) -> list[tuple[int, int]]:
    """Возвращает пары элементов из двух списков с помощью itertools.zip_longest()."""
    return list(zip_longest(a, b, fillvalue=None))


def count_elements(lst: list[str]) -> dict[str, int]:
    """Возвращает частоту элементов списка с помощью collections.Counter."""
    return dict(Counter(lst))


def multiply_all(lst: list[int]) -> int:
    """Возвращает произведение всех элементов списка с помощью functools.reduce."""
    return reduce(lambda x, y: x * y, lst, 1)


if __name__ == "__main__":
    print(current_time())
    print(count_elements(["a", "b", "c", "a"]))
