"""
Day 3 — File handling
Тема: Работа с файлами (open, read, write, with).
"""

from __future__ import annotations

from pathlib import Path


def read_file(path: str | Path) -> str:
    """
    Читает содержимое текстового файла.

    :param path: Путь к файлу.
    :type path: str | Path
    :raises FileNotFoundError: Если файл не найден.
    :raises IOError: При ошибке чтения.
    :return: Содержимое файла.
    :rtype: str

    :example:
        >>> read_file("example.txt")
        'Hello, world!'
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {path}")
    except IOError as e:
        raise IOError(f"Ошибка чтения файла {path}: {e}")


def write_file(path: str | Path, text: str) -> None:
    """
    Перезаписывает файл указанным текстом.

    :param path: Путь к файлу.
    :type path: str | Path
    :param text: Текст для записи.
    :type text: str
    :raises IOError: При ошибках записи (например, нет прав доступа).
    :return: None
    :rtype: None
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except IOError as e:
        raise IOError(f"Ошибка записи файла {path}: {e}")


def append_line(path: str | Path, line: str) -> None:
    """
    Добавляет строку в конец файла, автоматически вставляя перенос строки.

    :param path: Путь к файлу.
    :type path: str | Path
    :param line: Строка для добавления.
    :type line: str
    :raises IOError: Если невозможно открыть или записать файл.
    :return: None
    :rtype: None
    """
    try:
        path = Path(path)
        with open(path, "a", encoding="utf-8") as f:
            if path.exists() and path.stat().st_size > 0:
                f.write("\n")
            f.write(line)
    except IOError as e:
        raise IOError(f"Ошибка при добавлении строки: {e}")
