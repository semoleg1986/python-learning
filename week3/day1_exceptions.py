"""
Day 1 — Exceptions
Тема: Основы обработки исключений (try / except / finally / raise).
"""

from typing import Optional, SupportsIndex


def divide(a: float, b: float) -> float:
    """
    Делит два числа с обработкой деления на ноль.

    :param a: Делимое.
    :param b: Делитель.
    :return: Результат деления.
    :raises ZeroDivisionError: Если b равно нулю.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Ошибка:", e)
        raise
    except Exception as e:
        print("Неожиданная ошибка:", e)
        raise


def safe_int(value: str) -> int:
    """
    Преобразует строку в целое число, обрабатывая исключения.

    :param value: Строка для преобразования.
    :return: Целое число или 0, если ввод некорректен.
    """
    try:
        return int(value)
    except ValueError:
        print(f"Ошибка: '{value}' не является числом.")
        return 0


def access_list_element(lst: list[int], index: SupportsIndex) -> Optional[int]:
    """
    Возвращает элемент списка по индексу с обработкой IndexError.

    :param lst: Список чисел.
    :param index: Индекс элемента.
    :return: Элемент списка или -1, если индекс выходит за границы.
    """

    try:
        return lst[index]
    except IndexError:
        print(f"Ошибка: индекс {index} выходит за границы списка.")
        return None
    except TypeError:
        print(
            f"Ошибка: индекс должен быть целым числом, получено {type(index).__name__}."
        )
        return None


if __name__ == "__main__":
    numbers = [10, 20, 30]

    print(divide(4, 2))
    # print(divide(2, 0))

    print(safe_int("1"))
    print(safe_int("a"))

    print(access_list_element(numbers, 1))
    print(access_list_element(numbers, 10))
    print(access_list_element(numbers, "2"))
