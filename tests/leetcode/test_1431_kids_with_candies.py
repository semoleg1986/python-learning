import pytest

from leetcode.lists.kids_with_candies_1431 import kids_with_candies


@pytest.mark.parametrize(
    "candies, extra, expected",
    [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
        ([0], 0, [True]),
    ],
)  # type: ignore[misc]
def test_kids_with_candies(
    candies: list[int], extra: int, expected: list[bool]
) -> None:
    assert kids_with_candies(candies, extra) == expected
