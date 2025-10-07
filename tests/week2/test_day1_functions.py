import pytest

from week2.day1_functions import calc_avg, print_info, sum_all


@pytest.mark.parametrize(
    "inp, expected",
    [
        ((1, 2, 3, 4), 10),
        ((3.0, 2, 5.0), 10.0),
        ((-1, -2, -3), -6),
    ],
)  # type: ignore[misc]
def test_sum_all(inp: tuple[float, ...], expected: float) -> None:
    assert sum_all(*inp) == expected


@pytest.mark.parametrize(
    "inp",
    [({"name": "", "age": 38}), ({"city": "Tokyo", "country": "Japan"}), ({})],
)
def test_print_info(inp: dict[str, object], capsys) -> None:
    print_info(**inp)
    captured = capsys.readouterr()

    for key, value in inp.items():
        assert f"{key} = {value}" in captured.out


@pytest.mark.parametrize(
    "inp, expected",
    [
        ((1, 2, 3, 4), 2.5),
        ((3.0, 2, 5.0), 3.3333333333333335),
        ((-1, -2, -3), -2.0),
    ],
)
def test_calc_avg_valid(inp: tuple[float, ...], expected: float) -> None:
    assert calc_avg(*inp) == expected


@pytest.mark.parametrize(
    "inp, exception",
    [
        ((), ValueError),
        ((1, "2", 3), ValueError),
    ],
)
def test_calc_avg_invalid(inp: tuple, exception: type[Exception]) -> None:
    with pytest.raises(exception):
        calc_avg(*inp)
