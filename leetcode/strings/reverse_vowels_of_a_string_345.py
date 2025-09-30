def reverse_vowels(s: str) -> str:
    """
    Возвращает строку, в которой гласные расположены в обратном порядке.

    Функция выполняет два прохода по строке:
        1. Собирает все гласные в стек(stack).
        2. Формирует новую строку, заменяя гласные в обратном порядке(result).

    Сложность: O(2n) → O(n)

    :param s: Исходная строка.
    :type s: str
    :return: Строка с обратным порядком гласных.
    :rtype: str
    """
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    result = ""
    stack = []
    for ch in s:
        if ch in vowels:
            stack.append(ch)
    for ch in s:
        if ch in vowels:
            result += stack.pop()
        else:
            result += ch
    return result


if __name__ == "__main__":
    print(reverse_vowels("IceCreAm") == "AceCreIm")
    print(reverse_vowels("leetcode") == "leotcede")
