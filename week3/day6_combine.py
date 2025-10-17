"""
Day 6 — Combined tasks
Тема: Комбинирование исключений, файлов и стандартных модулей.
"""

from __future__ import annotations

import json
from pathlib import Path


def read_json(path: str | Path) -> dict:
    """
    Считывает JSON-файл с обработкой ошибок.

    :param path: Путь к JSON-файлу.
    :type path: str
    :return: Словарь данных.
    :rtype: dict
    :raises FileNotFoundError: Если файл не найден.
    :raises ValueError: Если файл содержит некорректный JSON.
    """
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"Файл '{file}' не найден.")

    try:
        with file.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Файл '{file}' содержит некорректный JSON: {e.msg}")
    except OSError as e:
        raise OSError(f"Ошибка при чтении файла '{file}': {e}")


def count_lines_with_word(path: str | Path, word: str) -> int:
    """
    Считает количество строк, содержащих заданное слово (без учёта регистра).

    :param path: Путь к файлу.
    :type path: str
    :param word: Ключевое слово для поиска.
    :type word: str
    :return: Количество строк, содержащих указанное слово.
    :rtype: int
    :raises FileNotFoundError: Если файл не найден.
    :raises OSError: Если произошла ошибка при чтении файла.
    """
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"Файл '{file}' не найден.")

    try:
        with file.open("r", encoding="utf-8") as f:
            return sum(1 for line in f if word.lower() in line.lower())
    except OSError as e:
        raise OSError(f"Ошибка при чтении файла '{file}': {e}")


def safe_write(path: str | Path, data: str) -> None:
    """
    Безопасно записывает данные в файл.

    Если файл существует и не пуст, добавляет перевод строки перед записью.

    :param path: Путь к файлу.
    :type path: str
    :param data: Текст для записи.
    :type data: str
    :raises OSError: Если произошла ошибка при записи файла.
    """
    file = Path(path)

    try:
        new_line = file.exists() and file.stat().st_size > 0

        with file.open("a", encoding="utf-8") as f:
            if new_line:
                f.write("\n")
            f.write(data)
    except OSError as e:
        raise OSError(f"Ошибка при записи в файл '{file}': {e}")


if __name__ == "__main__":
    try:
        count = count_lines_with_word("test.txt", "вasdads")
        print(count)
    except FileNotFoundError as e:
        print("Ошибка:", e)
    except OSError as e:
        print("Ошибка:", e)
