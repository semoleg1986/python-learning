import pytest

from week1.day2_strings import count_vowels, is_palindrome, reverse_string


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Hello", "olleH"),
        ("Hello World", "dlroW olleH"),
        ("012", "210"),
    ],
)  # type: ignore[misc]
def test_reverse_string(inp: str, expected: str) -> None:
    assert reverse_string(inp) == expected


def test_reverse_string_negative() -> None:
    assert reverse_string("Hello") != "olleh"


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("A man", False),
    ],
)  # type: ignore[misc]
def test_is_palindrome(inp: str, expected: bool) -> None:
    assert is_palindrome(inp) is expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Hello World", 3),
        ("Python", 1),
        ("AEIOU", 5),
        ("bcdfg", 0),
    ],
)  # type: ignore[misc]
def test_count_vowels(inp: str, expected: int) -> None:
    assert count_vowels(inp) == expected
