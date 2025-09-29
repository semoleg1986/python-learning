"""
Day 2 — Strings practice
Задачи на базовые операции со строками.
"""
import re


def reverse_string(s: str) -> str:
    return "".join(reversed(list(s)))


def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r"[^\w]", "", s).lower()
    return cleaned == cleaned[::-1]


def count_vowels(s: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in s.lower():
        if i in vowels:
            count += 1
    return count


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string("hello world!"))
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(count_vowels("Hello World"))  # 3 (e, o, o)
    print(count_vowels("Python"))  # 1 (o)
    print(count_vowels("AEIOU"))  # 5
    print(count_vowels("bcdfg"))
