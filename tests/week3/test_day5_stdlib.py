import re

import pytest

from week3.day5_stdlib import combine_lists, count_elements, current_time, multiply_all


def test_current_date_format() -> None:
    """Проверяет формат возвращаемого времени."""
    result = current_time()
    assert re.match(r"^\d{2}:\d{2}:\d{2}$", result)


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        ([10, 20, 30], ["a", "b", "c"], [(10, "a"), (20, "b"), (30, "c")]),
        ([10, 20, 30], [2], [(10, 2), (20, None), (30, None)]),
    ],
)
def test_combine_lists(lst1: list, lst2: list, expected: list[tuple]) -> None:
    assert combine_lists(lst1, lst2) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        (["a", "b", "c", "a"], {"a": 2, "b": 1, "c": 1}),
    ],
)
def test_count_elements(lst: list, expected: dict[str, int]) -> None:
    assert count_elements(lst) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4], 24),
        ([5, 5], 25),
        ([7], 7),
        ([], 1),
    ],
)
def test_multiply_all(lst: list[int], expected: int) -> None:
    assert multiply_all(lst) == expected
