import pytest

from week3.day2_custom_exceptions import (
    InvalidAgeError,
    NegativeValueError,
    check_age,
    validate_positive_number,
)


@pytest.mark.parametrize(
    "value, should_raise",
    [
        (10, False),
        (0, False),
        (-5, True),
        (-100, True),
    ],
)
def test_validate_positive_number(value, should_raise):
    if should_raise:
        with pytest.raises(NegativeValueError):
            validate_positive_number(value)
    else:
        validate_positive_number(value)


@pytest.mark.parametrize(
    "age, should_raise",
    [
        (25, False),
        (0, False),
        (120, False),
        (-1, True),
        (150, True),
    ],
)
def test_check_age(age, should_raise):
    if should_raise:
        with pytest.raises(InvalidAgeError):
            check_age(age)
    else:
        result = check_age(age)
        assert f"Возраст {age} корректен" in result
