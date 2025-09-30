"""
Day 3 — Lists practice
Задачи на базовые операции со списками.
"""


def unique(lst: list[int]) -> list[int]:
    """
    Удаляет дубликаты из списка целых чисел.

    :param lst: Список целых чисел, в котором могут быть дубликаты.
    :type lst: list[int]
    :return lst: Новый список без повторяющихся элементов.
    :rtype: list[int]
    """
    result = []
    duplicate = set()
    for i in lst:
        if i not in duplicate:
            duplicate.add(i)
            result.append(i)
    return result


def flatten(lst: list[list[int]]) -> list[int]:
    """
    Преобразует список списков целых чисел в плоский список.

    result = []
    for i in lst:
        for j in i:
            result.append(j)
    return result

    :param lst: Список списков целых чисел.
    :type lst: list[list[int]]
    :return: Одномерный список целых чисел.
    :rtype: list[int]
    """
    return [j for i in lst for j in i]


def find_max_min(lst: list[int]) -> tuple[int, int]:
    """
    Находит максимальный и минимальный элемент в списке целых чисел

    if not lst:
        raise ValueError("Пустой список")
    return max(lst), min(lst)

    :param lst: Список целых чисел
    :type lst: list[int]
    :return: Кортеж из двух элементов (max, min)
    :rtype: tuple[int, int]
    """
    if not lst:
        raise ValueError("Пустой список")

    min_val = max_val = lst[0]

    for num in lst[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return max_val, min_val


if __name__ == "__main__":
    print(unique([1, 2, 2, 3, 4, 5, 5, 6]))
    print(unique([3, 4, 1, 1, 5, 2, 5, 6, 2]))
    print(flatten([[1, 2], [3, 4], [5]]))
    print(flatten([[1], [3, 4], [5], [1]]))
    print(find_max_min([3, 4, 1, 1, 5, 2, 5, 6, -2]))
