def reverse_string(s: str, k: int) -> str:
    """
    Обрабатывает строку по правилам "обратного разворота блоков".

    :param s: Входная строка.
    :type s: str
    :param k: Длина блока для разворота.
    :type k: int
    :return: Преобразованная строка.
    :rtype: str
    """
    result = []
    for i in range(0, len(s), 2 * k):
        block = s[i : i + 2 * k]
        result.append(block[:k][::-1] + block[k:])
    return "".join(result)


if __name__ == "__main__":
    print(reverse_string("abcdefg", 2))
    print(reverse_string("abcd", 2))
    print(reverse_string("abcd", 4))
