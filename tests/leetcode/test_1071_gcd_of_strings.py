import pytest

from leetcode.strings.greatest_common_divisor_of_strings_1071 import gcd_of_strings


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ABABAB", "ABAB", "AB"),
        ("ABCABC", "ABC", "ABC"),
        ("LEET", "CODE", ""),
    ],
)  # type: ignore[misc]
def test_merge_alt(s1: str, s2: str, expected: str) -> None:
    assert gcd_of_strings(s1, s2) == expected
