import pytest

from week2.day2_lambda import filter_even, product, squares


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 2, 3, 4], [1, 4, 9, 16]),
        ([0, -1, -2], [0, 1, 4]),
        ([], []),
    ],
)
def test_squares(inp, expected):
    assert squares(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 2, 3, 4, 5, 6], [2, 4, 6]),
        ([0, -2, -3, -4], [0, -2, -4]),
        ([1, 3, 5], []),
    ],
)  # type: ignore[misc]
def test_filter_even(inp, expected):
    assert filter_even(inp) == expected


@pytest.mark.parametrize(
    "inp, expected",
    [
        ([1, 2, 3, 4], 24),
        ([5, 5, 5], 125),
        ([2], 2),
    ],
)  # type: ignore[misc]
def test_product(inp, expected):
    assert product(inp) == expected


@pytest.mark.parametrize(
    "inp",
    [
        ([]),
    ],
)  # type: ignore[misc]
def test_product_empty(inp):
    with pytest.raises(ValueError):
        product(inp)
