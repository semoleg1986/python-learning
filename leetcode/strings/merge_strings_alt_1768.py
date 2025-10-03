def merge_alt(s1: str, s2: str) -> str:
    """
    Объединяет две строки, чередуя символы из каждой.

    Символы берутся поочерёдно, начиная с первой строки.
    Если одна из строк длиннее, оставшиеся символы добавляются в конец результата.

    :param s1: Первая строка.
    :type s1: str
    :param s2: Вторая строка.
    :type s2: str
    :return: Новая строка, составленная из символов двух строк в чередующемся порядке.
    :rtype: str
    """
    result = []
    l_s1, l_s2 = len(s1), len(s2)
    k = min(l_s1, l_s2)

    for i in range(k):
        result.append(s1[i])
        result.append(s2[i])

    result.extend(s1[k:] or s2[k:])
    return "".join(result)


if __name__ == "__main__":
    print(merge_alt("abc", "defg"))
    print(merge_alt("ab", "defg"))
    print(merge_alt("abcd", "ef"))
