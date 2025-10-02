import pytest

from leetcode.strings.reverse_words_in_a_string3_557 import reverse_word


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("Mr Ding", "rM gniD"),
    ],
)  # type: ignore[misc]
def test_reverse_vowels(inp: str, expected: str) -> None:
    assert reverse_word(inp) == expected
