def reverse_vowels(s: str) -> str:  # O(2n) -> O(n) Два прохода
    """
    :type s: str
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
