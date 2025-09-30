import pytest

from leetcode.strings.reverse_vowels_of_a_string_345 import reverse_vowels


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("IceCreAm", "AceCreIm"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
        ("", ""),
        ("bcdfg", "bcdfg"),
        ("uoiea", "aeiou"),
    ],
)  # type: ignore[misc]
def test_reverse_vowels(inp: str, expected: str) -> None:
    assert reverse_vowels(inp) == expected
