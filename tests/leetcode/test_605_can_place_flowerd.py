import pytest

from leetcode.lists.can_place_flowers_605 import (
    can_place_flowers,  # измени путь под свой модуль
)


@pytest.mark.parametrize(
    "flowerbed, n, expected",
    [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 0, 1, 0, 0], 2, True),
        ([1, 0, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 0, 0, 1], 2, True),
        ([1, 0, 0, 0, 0, 0, 1], 3, False),
        ([0], 1, True),
        ([1], 1, False),
        ([0, 0, 0, 0, 0], 2, True),
        ([0, 0, 0, 0, 0], 3, True),
        ([1, 0, 0, 0, 1, 0, 0], 1, True),
        ([0, 0, 0, 0], 2, True),
        ([0, 0, 0, 0], 3, False),
    ],
)
def test_can_place_flowers(flowerbed: list[int], n: int, expected: bool) -> None:
    assert can_place_flowers(flowerbed, n) == expected
