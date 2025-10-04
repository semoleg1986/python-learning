import pytest

from ..analyzer import Analyser


@pytest.mark.parametrize(
    "text, count, uniq, top",
    [
        ("apple banana apple", 3, 2, ["apple", "banana"]),
        ("one two three", 3, 3, ["one", "two", "three"]),
        ("", 0, 0, []),
        ("python Python PYTHON", 3, 1, ["python"]),
    ],
)  # type: ignore[misc]
def test_analyzer(text: str, count: int, uniq: int, top: list[str]) -> None:
    a = Analyser(text)
    assert a.count_words() == count
    assert a.count_uniq_words() == uniq
    assert a.top_freq_words(3) == top
