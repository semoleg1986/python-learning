import pytest

from week3.day1_exceptions import access_list_element, divide, safe_int


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (7, -1, -7),
    ],
)
def test_divide_valid(a, b, expected):
    assert divide(a, b) == expected


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("42", 42),
        ("-10", -10),
        ("0", 0),
        ("abc", 0),  # некорректный ввод
        ("3.14", 0),  # некорректный ввод
    ],
)
def test_safe_int(value, expected):
    assert safe_int(value) == expected


@pytest.mark.parametrize(
    "lst, index, expected",
    [
        ([10, 20, 30], 0, 10),
        ([10, 20, 30], 2, 30),
        ([10, 20, 30], 5, None),
        ([10, 20, 30], -1, 30),
    ],
)
def test_access_list_element_valid(lst, index, expected):
    assert access_list_element(lst, index) == expected


def test_access_list_element_invalid_type():
    lst = [1, 2, 3]
    assert access_list_element(lst, "1") is None
