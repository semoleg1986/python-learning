"""
Day 4 — Tuples and sets practice
Задачи на базовые операции с кортежами и множество.
"""


def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Удаляет дубликаты из списка целых чисел с использованием множества.

    :param lst: Список целых чисел, в котором могут встречаться повторяющиеся элементы.
    :type lst: list[int]
    :return: Новый список, содержащий только уникальные элементы.
    :rtype: list[int]
    """
    duplicate = set()
    result = []
    for i in lst:
        if i not in duplicate:
            duplicate.add(i)
            result.append(i)
    return result


def common_elements(a: list[int], b: list[int]) -> list[int]:
    """
    Находит общие элементы двух списков целых чисел.

    :param a: Первый список целых чисел.
    :type a: list[int]
    :param b: Второй список целых чисел.
    :type b: list[int]
    :return: Список элементов, которые встречаются в обоих списках.
    :rtype: list[int]
    """
    return list(set(a) & set(b))


def most_frequent(lst: list[str]) -> str:
    """
    Определяет наиболее часто встречающийся элемент в списке строк.

    :param lst: Список строк.
    :type lst: list[str]
    :return: Элемент, который встречается в списке чаще всего.
    :rtype: str
    :raises ValueError: Если список пустой.
    """
    if not lst:
        raise ValueError("Пустой список")

    return max(set(lst), key=lst.count)


if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    print(most_frequent(["a", "b", "c", "d", "b", "c", "e", "c"]))
