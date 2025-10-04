def gcd_of_strings(str1: str, str2: str) -> str:
    """
    Находит наибольший общий делитель (НОД) двух строк.

    Две строки имеют общий делитель, если обе могут быть составлены
    путём многократного повторения одной и той же подстроки.
    Функция возвращает самую длинную такую подстроку, или пустую строку,
    если общего делителя не существует.

    :param str1: Первая строка.
    :type str1: str
    :param str2: Вторая строка.
    :type str2: str
    :return: Наибольшая общая подстрока, из которой могут быть составлены обе строки.
    :rtype: str
    :example:
        >>> gcd_of_strings("ABCABC", "ABC")
        'ABC'
        >>> gcd_of_strings("ABABAB", "ABAB")
        'AB'
        >>> gcd_of_strings("LEET", "CODE")
        ''
    """
    if str1 + str2 != str2 + str1:
        return ""

    len1, len2 = len(str1), len(str2)

    while len2:
        len1, len2 = len2, len1 % len2

    return str1[:len1]


if __name__ == "__main__":
    print(gcd_of_strings("ABABAB", "ABAB"))
    print(gcd_of_strings("ABCABC", "ABC"))
    print(gcd_of_strings("LEET", "CODE"))
