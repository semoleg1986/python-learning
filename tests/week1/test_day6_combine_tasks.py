import pytest

from week1.day6_combine import (
    count_of_words,
    freq_chars,
    remove_duplicates_words,
    reverse_words,
    top3_words,
)


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Hello world from Python", 4),
        ("One two three", 3),
        ("  spaced   words  ", 2),
        ("", 0),
    ],
)  # type: ignore[misc]
def test_count_of_words(inp: str, expected: int) -> None:
    assert count_of_words(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("hello", {"h": 1, "e": 1, "l": 2, "o": 1}),
        ("abc abc", {"a": 2, "b": 2, "c": 2, " ": 1}),
        ("", {}),
    ],
)  # type: ignore[misc]
def test_freq_chars(inp: str, expected: dict[str, int]) -> None:
    assert freq_chars(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("this is is a test test string", "this is a test string"),
        ("one two two three one", "one two three"),
        ("", ""),
    ],
)  # type: ignore[misc]
def test_remove_duplicates_words(inp: str, expected: str) -> None:
    assert remove_duplicates_words(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("apple banana apple orange banana apple", ["apple", "banana", "orange"]),
        ("one two three two two three three", ["three", "two", "one"]),
        ("a b c", ["a", "b", "c"]),
        ("", []),
    ],
)  # type: ignore[misc]
def test_top3_words(inp: str, expected: list[str]) -> None:
    assert set(top3_words(inp)) == set(expected)


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("Hello world from Python", "Python from world Hello"),
        ("a b c d", "d c b a"),
        ("Привет мир", "мир Привет"),
        ("", ""),
    ],
)  # type: ignore[misc]
def test_reverse_words(inp: str, expected: str) -> None:
    assert reverse_words(inp) == expected
