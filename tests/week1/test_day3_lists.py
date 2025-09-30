import pytest

from week1.day3_lists import find_max_min, flatten, unique


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 2, 2, 3, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([3, 4, 1, 1, 5, 2, 5, 6, 2], [3, 4, 1, 5, 2, 6]),
    ],
)  # type: ignore[misc]
def test_unique(inp: list[int], expected: list[int]) -> None:
    assert unique(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([[1, 2], [3, 4], [5]], [1, 2, 3, 4, 5]),
        ([[1], [3, 4], [5], [1]], [1, 3, 4, 5, 1]),
    ],
)  # type: ignore[misc]
def test_flatten(inp: list[list[int]], expected: list[int]) -> None:
    assert flatten(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 2, 2, 3, 4, 15, 5, -6], (15, -6)),
        ([5, 1, 2, 6, 9, -1], (9, -1)),
        ([1], (1, 1)),
    ],
)  # type: ignore[misc]
def test_find_max_min(inp: list[int], expected: tuple[int, int]) -> None:
    assert find_max_min(inp) == expected


def test_find_max_min_empty() -> None:
    with pytest.raises(ValueError, match="Пустой список"):
        find_max_min([])
