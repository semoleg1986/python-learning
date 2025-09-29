import pytest

from week1.day1_numbers import digit_sum, factorial, factorial2, is_even


def test_is_even() -> None:
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-4) is True
    assert is_even(-5) is False


def test_digit_sum() -> None:
    assert digit_sum(123) == 6
    assert digit_sum(0) == 0
    assert digit_sum(9999) == 36
    assert digit_sum(1001) == 2
    assert digit_sum(abs(-123)) == 6


def test_factorial_iterative() -> None:
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040


def test_factorial_recursive() -> None:
    assert factorial2(0) == 1
    assert factorial2(1) == 1
    assert factorial2(5) == 120
    assert factorial2(7) == 5040


@pytest.mark.parametrize("n", [0, 1, 5, 7, 10])  # type: ignore[misc]
def test_factorial_and_factorial2_equivalence(n: int) -> None:
    assert factorial(n) == factorial2(n)
