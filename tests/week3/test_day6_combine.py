import json
from pathlib import Path

import pytest

from week3.day6_combine import count_lines_with_word, read_json, safe_write


def test_read_json_valid(tmp_path: Path):
    file_path = tmp_path / "data.json"
    data = {"name": "Unknown", "age": 23}

    file_path.write_text(json.dumps(data), encoding="utf-8")
    result = read_json(file_path)

    assert result == data


def test_read_json_invalid(tmp_path: Path):
    file_path = tmp_path / "invalid.json"

    file_path.write_text("Not a JSON!", encoding="utf-8")

    with pytest.raises(ValueError):
        read_json(file_path)


@pytest.mark.parametrize(
    "content, word, expected",
    [
        ("Error: file missing\nWarning: low memory\nError: retry\n", "error", 2),
        ("Hello world\nHello again\nHELLO", "hello", 3),
        ("No matches here\nCompletely different text", "missing", 0),
    ],
)
def test_count_lines_with_word(
    tmp_path: Path, content: str, word: str, expected: int
) -> None:
    file_path = tmp_path / "test.txt"
    file_path.write_text(content, encoding="utf-8")

    result = count_lines_with_word(file_path, word)
    assert result == expected


def test_count_lines_with_word_file_not_found(tmp_path: Path) -> None:
    """Проверяет выброс FileNotFoundError, если файл отсутствует."""
    missing_file = tmp_path / "missing.txt"
    with pytest.raises(FileNotFoundError):
        count_lines_with_word(missing_file, "error")


def test_safe_write_creates_file(tmp_path: Path) -> None:
    """Проверяет создание нового файла и запись текста."""
    file_path = tmp_path / "output.txt"
    text = "Hello, world!"

    safe_write(file_path, text)

    assert file_path.exists()
    assert file_path.read_text(encoding="utf-8") == text


def test_safe_write_appends_with_newline(tmp_path: Path) -> None:
    """Проверяет, что при повторной записи добавляется новая строка."""
    file_path = tmp_path / "append.txt"
    file_path.write_text("First line", encoding="utf-8")

    safe_write(file_path, "Second line")

    content = file_path.read_text(encoding="utf-8").splitlines()
    assert content == ["First line", "Second line"]


def test_safe_write_error(monkeypatch, tmp_path: Path) -> None:
    """Проверяет, что выбрасывается OSError при ошибке записи."""
    file_path = tmp_path / "fail.txt"

    def fake_open(*args, **kwargs):
        raise OSError("Permission denied")

    monkeypatch.setattr(Path, "open", fake_open)

    with pytest.raises(OSError, match="Ошибка при записи"):
        safe_write(file_path, "text")
