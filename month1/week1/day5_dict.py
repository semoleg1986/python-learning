"""
Day 5 — Dict practice
Задачи на базовые операции со словарем.
"""


def char_frequency(s: str) -> dict[str, int]:
    """
    Подсчитывает частоту каждого символа в строке.

    :param s: Входная строка.
    :type s: str
    :return: Словарь, где ключ — символ, значение — количество его вхождений.
    :rtype: dict[str, int]
    """
    result: dict[str, int] = {}
    for i in s.lower():
        result[i] = result.get(i, 0) + 1
    return result


def merge_dicts(d1: dict[str, int], d2: dict[str, int]) -> dict[str, int]:
    """
    Объединяет два словаря в один.

    Если ключи совпадают, значения из второго словаря заменяют значения первого.

    d1 | d2

    :param d1: Первый словарь.
    :type d1: dict
    :param d2: Второй словарь.
    :type d2: dict
    :return: Новый словарь, содержащий объединённые пары ключ–значение.
    :rtype: dict
    """
    result = d1.copy()
    result.update(d2)
    return result


def invert_dict(d: dict[str, str]) -> dict[str, list[str]]:
    """
    Инвертирует словарь: ключи становятся значениями, а значения ключами.

    Если несколько ключей имеют одинаковое значение, они группируются в список.

    :param d: Исходный словарь, где значения — строки.
    :type d: dict[str, str]
    :return: Новый словарь, где ключи — это исходные значения,
             а значения — списки исходных ключей.
    :rtype: dict[str, list[str]]
    """
    result: dict[str, list[str]] = {}
    for k, v in d.items():
        if v in result:
            result[v].append(k)
        else:
            result[v] = [k]
    return result


if __name__ == "__main__":
    print(char_frequency("HelLo"))
    print(invert_dict({"a": "all", "b": "back", "c": "cell", "d": "all"}))
