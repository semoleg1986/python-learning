from pathlib import Path

import pytest

from week3.day4_pathlib import create_folder, file_info, list_files

# ---------- list_files ----------


def test_list_files_returns_only_files(tmp_path: Path) -> None:
    """Функция должна возвращать только файлы в директории."""
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.log"
    folder = tmp_path / "nested"
    file1.write_text("hello")
    file2.write_text("world")
    folder.mkdir()

    files = list_files(tmp_path)

    assert str(file1) in files
    assert str(file2) in files
    assert not any("nested" in f for f in files)


def test_list_files_raises_if_not_exists(tmp_path: Path) -> None:
    """Если директории не существует, выбрасывается FileNotFoundError."""
    fake_dir = tmp_path / "unknown"
    with pytest.raises(FileNotFoundError):
        list_files(fake_dir)


def test_list_files_raises_if_not_directory(tmp_path: Path) -> None:
    """Если путь не является директорией, выбрасывается NotADirectoryError."""
    file = tmp_path / "file.txt"
    file.write_text("data")
    with pytest.raises(NotADirectoryError):
        list_files(file)


# ---------- create_folder ----------


def test_create_folder_creates_directory(tmp_path: Path) -> None:
    """Создание новой директории проходит успешно."""
    folder = tmp_path / "new_folder"
    create_folder(folder)
    assert folder.exists()
    assert folder.is_dir()


def test_create_folder_raises_if_exists(tmp_path: Path) -> None:
    """Если директория уже существует, выбрасывается FileExistsError."""
    existing = tmp_path / "exists"
    existing.mkdir()
    with pytest.raises(FileExistsError):
        create_folder(existing)


# ---------- file_info ----------


def test_file_info_returns_correct_data(tmp_path: Path) -> None:
    """Проверка корректности данных о файле."""
    f = tmp_path / "example.txt"
    f.write_text("hello world")
    info = file_info(f)

    assert info["name"] == "example"
    assert info["suffix"] == ".txt"
    assert "bytes" in info["size"]


def test_file_info_raises_if_not_found(tmp_path: Path) -> None:
    """Если файл не найден, выбрасывается FileNotFoundError."""
    missing = tmp_path / "nofile.txt"
    with pytest.raises(FileNotFoundError):
        file_info(missing)


def test_file_info_raises_if_directory(tmp_path: Path) -> None:
    """Если путь указывает на директорию, выбрасывается IsADirectoryError."""
    folder = tmp_path / "dir"
    folder.mkdir()
    with pytest.raises(IsADirectoryError):
        file_info(folder)
