"""
Day 6 — Combine tasks practice
Комбинированные задачи на строки и коллекции.
"""


def count_of_words(s: str) -> int:
    """
    Подсчитывает количество слов в строке.

    Слова разделяются пробелами. Знаки препинания не учитываются.

    :param s: Входная строка.
    :type s: str
    :return: Количество слов в строке.
    :rtype: int
    """
    return len(s.split())


def freq_chars(s: str) -> dict[str, int]:
    """
    Подсчитывает частоту встречаемости символов в строке.

    :param s: Входная строка.
    :type s: str
    :return: Словарь, где ключ — символ, значение — количество его вхождений.
    :rtype: dict[str, int]
    """
    result: dict[str, int] = {}

    for ch in s.lower():
        result[ch] = result.get(ch, 0) + 1

    return result


def remove_duplicates_words(s: str) -> str:
    """
    Удаляет повторяющиеся слова из строки, сохраняя порядок появления.

    :param s: Исходная строка.
    :type s: str
    :return: Новая строка без повторяющихся слов.
    :rtype: str
    """
    uniq = set()
    result = []
    for word in s.split():
        if word not in uniq:
            uniq.add(word)
            result.append(word)
    return " ".join(result)


def top3_words(s: str) -> list[str]:
    """
    Находит три самых часто встречающихся слова в строке.

    :param s: Входная строка.
    :type s: str
    :return: Список из трёх слов с наибольшей частотой появления.
    :rtype: list[str]
    """
    words = s.lower().split()
    counter: dict[str, int] = {}
    order: dict[str, int] = {}

    for i, word in enumerate(words):
        counter[word] = counter.get(word, 0) + 1
        if word not in order:
            order[word] = i

    top3 = sorted(counter, key=lambda w: (-counter[w], order[w]))
    return top3[:3]


def reverse_words(s: str) -> str:
    """
    Разворачивает порядок слов в строке, сохраняя символы внутри слова.

    :param s: Исходное предложение.
    :type s: str
    :return: Строка с перевёрнутым порядком слов.
    :rtype: str
    """
    return " ".join(reversed(s.split()))


if __name__ == "__main__":
    print(count_of_words("Hello world from Python"))
    print(freq_chars("helLo"))
    print(remove_duplicates_words("hello world hello python"))
    print(top3_words("apple banana apple orange banana apple"))
    print(top3_words("one two three two two three three"))
    print(reverse_words("Python is fun"))
