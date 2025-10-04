import re
from typing import List


class Analyser:
    """
    Анализатор текста.

    Подсчитывает:
      • количество слов;
      • количество уникальных слов;
      • топ-5 самых частых слов.


    :param text: Исходный текст для анализа.
    :type text: str
    """

    def __init__(self, text: str) -> None:
        """
        Инициализация анализатора.

        :param text: Входной текст.
        :type text: str
        :return: None
        :rtype: None
        """
        self.text: List[str] = re.findall(r"\w+", text.lower())

    def count_words(self) -> int:
        """
        Возвращает общее количество слов в тексте.

        :return: Общее количество слов (токенов).
        :rtype: int
        """
        return len(self.text)

    def count_uniq_words(self) -> int:
        """
        Возвращает количество уникальных слов в тексте.

        :return: Количество различных слов.
        :rtype: int
        """
        return len(set(self.text))

    def top_freq_words(self, n: int = 5) -> list[str]:
        """
        Возвращает список из n самых часто встречающихся слов.

        :param n: Количество слов в результате (по умолчанию 5).
        :type n: int
        :return: Список из n наиболее частых слов.
        :rtype: list[str]
        """
        words = self.text
        counter: dict[str, int] = {}
        order: dict[str, int] = {}

        for idx, word in enumerate(words):
            counter[word] = counter.get(word, 0) + 1
            if word not in order:
                order[word] = idx

        top5 = sorted(counter, key=lambda word: (-counter[word], order[word]))

        return top5[:n]
