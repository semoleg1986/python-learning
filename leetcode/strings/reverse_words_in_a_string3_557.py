def reverse_word(s: str) -> str:
    """
    Разворачивает символы в каждом слове строки, сохраняя порядок слов и пробелы.

    :param s: Входная строка, содержащая слова, разделённые пробелами.
    :type s: str
    :return: Строка, где символы каждого слова идут в обратном порядке,
             но порядок слов и пробелов остаётся неизменным.
    :rtype: str
    """
    return " ".join([i[::-1] for i in s.split()])


if __name__ == "__main__":
    print(reverse_word("Let's take LeetCode contest"))
