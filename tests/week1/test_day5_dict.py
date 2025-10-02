import pytest

from week1.day5_dict import char_frequency, invert_dict, merge_dicts


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("aaa", {"a": 3}),
        ("", {}),
        ("AaA", {"a": 3}),
        ("abc abc", {"a": 2, "b": 2, "c": 2, " ": 1}),
    ],
)  # type: ignore[misc]
def test_char_frequency(inp: str, expected: dict[str, int]) -> None:
    assert char_frequency(inp) == expected


@pytest.mark.parametrize(
    "d1, d2, expected",
    [
        ({"a": 1, "b": 2}, {"c": 3}, {"a": 1, "b": 2, "c": 3}),
        ({"a": 1, "b": 2}, {"b": 99}, {"a": 1, "b": 99}),
        ({}, {"x": 10}, {"x": 10}),
        ({"x": 5}, {}, {"x": 5}),
        ({}, {}, {}),
    ],
)  # type: ignore[misc]
def test_merge_dicts(
    d1: dict[str, int], d2: dict[str, int], expected: dict[str, int]
) -> None:
    assert merge_dicts(d1, d2) == expected


@pytest.mark.parametrize(
    "d, expected",
    [
        ({"a": "x", "b": "y", "c": "x"}, {"x": ["a", "c"], "y": ["b"]}),
        (
            {"one": "1", "two": "2", "three": "3"},
            {"1": ["one"], "2": ["two"], "3": ["three"]},
        ),
        ({}, {}),
        ({"a": "z", "b": "z", "c": "z"}, {"z": ["a", "b", "c"]}),
    ],
)  # type: ignore[misc]
def test_invert_dict(d: dict[str, str], expected: dict[str, list[str]]) -> None:
    assert invert_dict(d) == expected
