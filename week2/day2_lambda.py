"""
Day 2 — Lambda, map, filter, reduce
Тема: Анонимные функции и функции высшего порядка.
"""
from functools import reduce


def squares(lst: list[int]) -> list[int]:
    """
    Возвращает новый список квадратов элементов.

    :param lst: Список целых чисел.
    :type lst: list[int]
    :return: Список квадратов.
    :rtype: list[int]
    """
    return list(map(lambda x: x * x, lst))


def filter_even(lst: list[int]) -> list[int]:
    """
    Возвращает только чётные элементы списка.

    :param lst: Список целых чисел.
    :type lst: list[int]
    :return: Отфильтрованный список.
    :rtype: list[int]
    """
    return list(filter(lambda x: (x % 2 == 0), lst))


def product(lst: list[int]) -> int:
    """
    Возвращает произведение всех элементов списка.

    :param lst: Список целых чисел.
    :type lst: list[int]
    :return: Произведение элементов.
    :rtype: int
    :raises ValueError: Если список пустой.
    """
    if not lst:
        raise ValueError("Список не должен быть пустым")
    return reduce(lambda x, y: x * y, lst)


if __name__ == "__main__":
    print(squares([1, 2, 3, 4]))  # [1, 4, 9, 16]
    print(filter_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(product([1, 2, 3, 4]))
