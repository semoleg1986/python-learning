from pathlib import Path

import pytest

from week3.day3_files import append_line, read_file, write_file


def test_write_and_read_file(tmp_path: Path):
    file_path = tmp_path / "test.txt"
    text = "Hello, world!"

    write_file(file_path, text)
    content = read_file(file_path)

    assert content == text


def test_append_line(tmp_path: Path):
    file_path = tmp_path / "append.txt"
    write_file(file_path, "Line1")
    append_line(file_path, "Line2")

    content = read_file(file_path).splitlines()
    assert content == ["Line1", "Line2"]


def test_read_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        read_file("no_such_file.txt")


def test_write_file_io_error(monkeypatch, tmp_path: Path):
    file_path = tmp_path / "test.txt"

    def mock_open(*args, **kwargs):
        raise IOError("Permission denied")

    monkeypatch.setattr("builtins.open", mock_open)

    with pytest.raises(IOError):
        write_file(file_path, "data")
