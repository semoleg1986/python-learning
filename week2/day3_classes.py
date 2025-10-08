"""
Day 3 — Classes and objects
Тема: Создание классов, __init__, методы, атрибуты.
"""
import math


class Person:
    """
    Класс, описывающий человека.
    """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def greet(self) -> str:
        """
        Возвращает приветственное сообщение.
        """
        return f"Hi, {self.name}!"


class Circle:
    """
    Класс окружности.
    """

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга."""
        return self.radius**2 * math.pi

    def perimeter(self) -> float:
        """Вычисляет длину окружности."""
        return 2 * math.pi * self.radius


class Book:
    """
    Класс книги.
    """

    def __init__(self, title: str, author: str) -> None:
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        """
        self.title = title
        self.author = author

    def info(self) -> str:
        """
        Возвращает строку с названием и автором.

        :return: Информация о книге.
        """
        return f"{self.title} - {self.author}"

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта книги.

        :return: Описание книги.
        """
        return f"Книга '{self.title}' автора {self.author}"


class Car:
    """
    Класс автомобиля.
    """

    def __init__(self, brand: str, year: int) -> None:
        """
        Инициализация автомобиля.

        :param brand: Марка автомобиля.
        :param year: Год выпуска.
        """
        self.brand = brand
        self.year = year

    def start(self) -> str:
        """
        Симулирует запуск автомобиля.

        :return: Сообщение о запуске.
        """
        return f"Машина {self.brand} заведена"

    def __str__(self) -> str:
        return f"{self.brand} ({self.year})"


class Rectangle:
    """
    Класс прямоугольника.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Инициализация прямоугольника.

        :param width: Ширина.
        :param height: Высота.
        """
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        :return: Площадь.
        """
        return self.width * self.height

    def __str__(self) -> str:
        """
        Строковое представление прямоугольника.

        :return: Описание прямоугольника.
        """
        return f"Прямоугольник {self.width}x{self.height}"
