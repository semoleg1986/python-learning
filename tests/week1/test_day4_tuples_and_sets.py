import pytest

from week1.day4_tuples_and_sets import common_elements, most_frequent, remove_duplicates


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 2, 2, 3, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([3, 4, 1, 1, 5, 2, 5, 6, 2], [3, 4, 1, 5, 2, 6]),
    ],
)  # type: ignore[misc]
def test_remove_duplicates(inp: list[int], expected: list[int]) -> None:
    assert remove_duplicates(inp) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3, 4], [3, 4, 5, 6], [3, 4]),
        ([1, 1, 2, 2], [2, 2, 3], [2]),
        ([], [1, 2, 3], []),
        ([1, 2, 3], [], []),
        ([1, 2, 3], [4, 5, 6], []),
        ([7, 8, 9], [9, 8, 7], [8, 9, 7]),
    ],
)  # type: ignore[misc]
def test_common_elements(a: list[int], b: list[int], expected: list[int]) -> None:
    result = common_elements(a, b)
    assert set(result) == set(expected)


@pytest.mark.parametrize(
    "lst, expected",
    [
        (["a", "b", "a", "c", "b", "a"], "a"),
        (["x", "y", "y", "z", "z", "z"], "z"),
        (["one"], "one"),
    ],
)  # type: ignore[misc]
def test_most_frequent(lst: list[str], expected: str) -> None:
    assert most_frequent(lst) == expected


def test_most_frequent_empty() -> None:
    with pytest.raises(ValueError):
        most_frequent([])
