from typing import List


def product_exc_self(lst: List[int]) -> List[int]:
    """
    Вычисляет список, в котором каждый элемент
    равен произведению всех элементов исходного списка,
    кроме элемента с этим индексом.

    Ограничения:
        - Нельзя использовать оператор деления.
        - Решение должно иметь сложность O(n).
    O(n)

    :param lst: Список целых чисел.
    :type lst: List[int]
    :return: Новый список
    :rtype: List[int]
    """
    n = len(lst)
    result = n * [0]

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= lst[i]

    surfix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= surfix
        surfix *= lst[i]

    return result


if __name__ == "__main__":
    print(product_exc_self([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(product_exc_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
