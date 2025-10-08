import math

import pytest

from week2.day3_classes import Book, Circle, Person


@pytest.mark.parametrize(
    "name, age, expected",
    [
        ("John", 38, "Hi, John!"),
        ("Sarah", 22, "Hi, Sarah!"),
    ],
)
def test_person_greet(name: str, age: int, expected: str) -> None:
    person = Person(name, age)
    assert person.greet() == expected
    assert person.name == name
    assert person.age == age


@pytest.mark.parametrize(
    "radius, expected_area, expected_perimeter",
    [
        (1, math.pi, 2 * math.pi),
        (2, 4 * math.pi, 4 * math.pi),
        (0.5, 0.25 * math.pi, math.pi),
    ],
)
def test_circle_area_and_perimeter(
    radius: float, expected_area: float, expected_perimeter: float
) -> None:
    circle = Circle(radius)
    assert math.isclose(circle.area(), expected_area, rel_tol=1e-9)
    assert math.isclose(circle.perimeter(), expected_perimeter, rel_tol=1e-9)


@pytest.mark.parametrize(
    "title, author, expected",
    [
        ("1984", "George Orwell", "1984 - George Orwell"),
        ("Мастер и Маргарита", "М. Булгаков", "Мастер и Маргарита - М. Булгаков"),
    ],
)
def test_book_info(title: str, author: str, expected: str) -> None:
    book = Book(title, author)
    assert book.info() == expected
    assert book.title == title
    assert book.author == author
