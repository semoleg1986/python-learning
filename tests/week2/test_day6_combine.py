import pytest

from week2.day6_combine import Stats, count_letters_in_file, sort_and_filter


@pytest.mark.parametrize(
    "inp, mean_expected, median_expected, variance_expected",
    [
        ([1, 2, 3, 4, 5], 3, 3, 2.5),
        ([1, 1, 1, 1], 1, 1, 0),
        ([1.5, 2.5, 3.5], 2.5, 2.5, 1.0),
    ],
)
def test_stats(
    inp: list[float],
    mean_expected: float,
    median_expected: float,
    variance_expected: float,
) -> None:
    s = Stats(inp)
    assert s.mean() == mean_expected
    assert s.median() == median_expected
    assert s.variance() == variance_expected


def test_stats_empty_raises():
    with pytest.raises(ValueError):
        Stats([])


def test_stats_non_numeric_raises():
    with pytest.raises(ValueError):
        Stats([1, "a", 3])


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([3, -1, 0, 2, -5], [2, 3]),
        ([0, 0, 0], []),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_sort_and_filter_basic(lst: list[int], expected: list[int]):
    assert sort_and_filter(lst) == expected


def test_sort_and_filter_empty():
    with pytest.raises(ValueError):
        sort_and_filter([])


def test_sort_and_filter_non_numeric():
    with pytest.raises(ValueError):
        sort_and_filter([1, 2, "a"])


@pytest.fixture
def tmp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Привет world 123! Привет_123")
    return file


def test_count_letters_in_file_letters_and_digits(tmp_file):
    result = count_letters_in_file(str(tmp_file))
    assert result["п"] == 2
    assert result["р"] == 2
    assert result["и"] == 2
    assert result["в"] == 2
    assert result["е"] == 2
    assert result["т"] == 2
    assert result["w"] == 1
    assert result["o"] == 1
    assert result["r"] == 1
    assert result["l"] == 1
    assert result["d"] == 1
    assert result["1"] == 2
    assert result["2"] == 2
    assert result["3"] == 2
