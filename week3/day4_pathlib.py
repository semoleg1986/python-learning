"""
Day 4 — Pathlib
Тема: Работа с путями, каталогами и проверкой файлов.
"""

from __future__ import annotations

from pathlib import Path


def list_files(directory: str | Path) -> list[str]:
    """
    Возвращает список всех файлов в указанной директории.

    :param directory: Путь к директории.
    :type directory: str
    :return: Список имён файлов (только файлов, без папок).
    :rtype: list[str]
    :raises FileNotFoundError: Если директория не найдена.
    :raises NotADirectoryError: Если путь не является директорией.
    """
    folder = Path(directory)

    if not folder.exists():
        raise FileNotFoundError(f"Директория '{directory}' не найдена.")
    if not folder.is_dir():
        raise NotADirectoryError(f"'{directory}' не является директорией.")
    return [str(file) for file in folder.iterdir() if file.is_file()]


def create_folder(path: str | Path) -> None:
    """
    Создаёт директорию по указанному пути, если её не существует.

    :param path: Путь к создаваемой директории (строка или Path).
    :type path: str | Path
    :raises FileExistsError: Если директория уже существует.
    :raises OSError: При ошибке создания директории (например, нет прав).
    :return: None
    """
    new_folder = Path(path)

    if new_folder.exists():
        raise FileExistsError(f"Директория '{path}' уже существует.")
    new_folder.mkdir(parents=True, exist_ok=False)


def file_info(path: str | Path) -> dict[str, str]:
    """
    Возвращает информацию о файле (имя, размер, расширение).

    :param path: Путь к файлу.
    :type path: str | Path
    :return: Словарь с информацией о файле.
    :rtype: dict[str, str]
    :raises FileNotFoundError: Если файл не найден.
    :raises IsADirectoryError: Если путь указывает на директорию, а не на файл.
    """
    file = Path(path)

    if not file.exists():
        raise FileNotFoundError(f"Файл '{file}' не найден.")
    if not file.is_file():
        raise IsADirectoryError(f"'{file}' — это директория, а не файл.")

    result: dict[str, str] = {
        "name": file.stem,
        "size": f"{file.stat().st_size} bytes",
        "suffix": file.suffix or "—",
    }

    return result


if __name__ == "__main__":
    try:
        files = list_files("week3")
        print("Файлы:", files)
    except FileNotFoundError as e:
        print("Ошибка:", e)
    except NotADirectoryError as e:
        print("Ошибка:", e)

    try:
        create_folder("week3/test/2025")
        print("Папка успешно создана ✅")
    except FileExistsError as e:
        print("Ошибка:", e)
    except OSError as e:
        print("Ошибка при создании:", e)

    try:
        info = file_info("README.md")
        print(info)
    except (FileNotFoundError, IsADirectoryError) as e:
        print("Ошибка:", e)
