import re
import sys
import types
from datetime import datetime

from week2.day5_modules import current_date, from_math_utils, random_sqrt


def test_random_sqrt():
    result = random_sqrt()
    assert isinstance(result, float)
    assert 1 <= result <= 10  # sqrt(1..100) всегда в этом диапазоне


def test_current_date_format():
    """Проверяет формат возвращаемой даты."""
    result = current_date()
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", result)
    today = datetime.now().strftime("%Y-%m-%d")
    assert result == today


def test_from_math_utils(monkeypatch, capsys):
    """Тестирует импорт и вывод функции from_math_utils с подменой math_utils."""
    mock_math_utils = types.SimpleNamespace(
        add=lambda x, y: x + y,
        sub=lambda x, y: x - y,
        mul=lambda x, y: x * y,
        div=lambda x, y: x / y,
    )

    sys.modules["math_utils"] = mock_math_utils

    from_math_utils()

    captured = capsys.readouterr().out
    assert "x +" in captured
    assert "x -" in captured
    assert "x *" in captured
    assert "x /" in captured
