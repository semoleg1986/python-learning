import pytest

from leetcode.strings.reverse_string_2_541 import reverse_string


@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("abc", 5, "cba"),
        ("a", 2, "a"),
        ("abcdef", 10, "fedcba"),
        ("abcd", 4, "dcba"),
        ("abcdef", 4, "dcbaef"),
        ("abcdefg", 3, "cbadefg"),
        ("abcdefg", 2, "bacdfeg"),
        ("abcdefghij", 2, "bacdfeghji"),
        ("abcdefghijkl", 3, "cbadefihgjkl"),
        ("abcdef", 1, "abcdef"),
        ("", 3, ""),
    ],
)  # type: ignore[misc]
def test_reverse_string(s: str, k: int, expected: str) -> None:
    assert reverse_string(s, k) == expected
