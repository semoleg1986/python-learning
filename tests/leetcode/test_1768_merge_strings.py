import pytest

from leetcode.strings.merge_strings_alt_1768 import merge_alt


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),
        ("hello", "", "hello"),
        ("a", "z", "az"),
    ],
)  # type: ignore[misc]
def test_merge_alt(s1: str, s2: str, expected: str) -> None:
    assert merge_alt(s1, s2) == expected
