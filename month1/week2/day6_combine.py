"""
Day 6 — Combined tasks
Комбинированные задачи на функции, классы и модули.
"""
import re
import statistics
from typing import Dict, Sequence


class Stats:
    """
    Класс для вычисления базовых статистических показателей набора чисел.


    • Среднее арифметическое (`mean`)
    • Медиану (`median`)
    • Дисперсию (`variance`)

    :param data: Последовательность чисел (list, tuple и т. д.)
    :type data: Sequence[float]

    :raises ValueError: Если список пустой или содержит нечисловые значения.
    """

    def __init__(self, data: Sequence[float]) -> None:
        if not data:
            raise ValueError("Список не может быть пустым.")
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Все элементы должны быть числами.")
        self.data = list(map(float, data))

    def mean(self) -> float:
        """Возвращает среднее арифметическое."""
        return statistics.mean(self.data)

    def median(self) -> float:
        """Возвращает медиану."""
        return statistics.median(self.data)

    def variance(self) -> float:
        """Возвращает дисперсию."""
        return statistics.variance(self.data)

    def __str__(self) -> str:
        """Возвращает строковое представление статистики."""
        return f"Stats({self.mean():.2f}, {self.median():.2f}, {self.variance():.2f})"


def sort_and_filter(lst: list[int]) -> list[int]:
    """
    Сортирует список чисел по возрастанию, исключая отрицательные значения.

    :param lst: Список целых чисел.
    :type lst: list[int]
    :return: Новый отсортированный список, содержащий только положительные числа.
    :rtype: list[int]
    :raises ValueError: Если список пустой или содержит нечисловые значения.
    """

    if not lst:
        raise ValueError("Список не может быть пустым.")
    if not all(isinstance(i, (int, float)) for i in lst):
        raise ValueError("Все элементы списка должны быть числами.")

    return sorted([i for i in lst if i > 0])


def count_letters_in_file(path: str) -> Dict[str, int]:
    """
    Считывает текст из файла и возвращает частоту букв и цифр.

    :param path: Путь к файлу для анализа.
    :type path: str
    :return: Словарь, где ключ — символ, значение — количество вхождений.
    :rtype: dict[str, int]
    :raises FileNotFoundError: Если файл не найден по указанному пути.
    :raises UnicodeDecodeError: Если файл невозможно прочитать с кодировкой UTF-8.
    """
    uniq_symbol: dict[str, int] = {}

    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
        cleaned_text = re.sub(r"[^a-zа-я0-9]", "", text, flags=re.IGNORECASE)

    for char in cleaned_text:
        uniq_symbol[char] = uniq_symbol.get(char, 0) + 1

    return uniq_symbol


if __name__ == "__main__":
    stats = Stats([1, 2, 3, 4, 5, 6])
    print(stats)
    print(sort_and_filter([-9, 5, 2, 5, 2, 7, 11, 1, -11]))
    print(count_letters_in_file("week2/test.txt"))
