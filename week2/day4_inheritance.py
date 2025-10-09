"""
Day 4 — Inheritance and polymorphism
Тема: Инкапсуляция, наследование, полиморфизм.
"""

import math
from abc import ABC, abstractmethod
from typing import Protocol


class Animal:
    """
    Базовый класс животного.
    Содержит общий метод speak(), который может быть переопределён в дочерних классах.
    """

    def speak(self) -> str:
        """
        Возвращает базовое звуковое сообщение.
        :return: Строка с общим звуком животного.
        :rtype: str
        """
        return "Животное издаёт звук"


class Dog(Animal):
    """
    Класс, представляющий собаку.
    Наследует от Animal и переопределяет метод speak().
    """

    def speak(self) -> str:
        """
        Переопределяет метод родителя.
        Возвращает объединённый результат родительского и собственного поведения.
        :return: Строка с сообщением от родителя и собаки.
        :rtype: str
        """
        parent_sound = super().speak()
        return f"{parent_sound} А собака говорит: гав-гав!"


class Cat(Animal):
    """
    Класс, представляющий кошку.
    Наследует от Animal и переопределяет метод speak().
    """

    def speak(self) -> str:
        """
        Переопределяет метод родителя.
        Возвращает объединённый результат родительского и собственного поведения.
        :return: Строка с сообщением от родителя и кошки.
        :rtype: str
        """
        parent_sound = super().speak()
        return f"{parent_sound} А кошка говорит: мяу-мяу!"


class TransactionError(Exception):
    """Исключение для ошибок транзакций."""

    pass


class AccountProtocol(Protocol):
    """Протокол банковского счёта."""

    @property
    def balance(self) -> float:
        ...

    def deposit(self, amount: float) -> None:
        ...

    def withdraw(self, amount: float) -> None:
        ...

    def account_type(self) -> str:
        ...


class Account(ABC):
    """Базовый класс банковского счёта."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        """
        Инициализирует счёт.

        :param owner: Имя владельца.
        :type owner: str
        :param balance: Начальный баланс.
        :type balance: float
        """
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self) -> float:
        """
        Возвращает текущий баланс (readonly).
        :return: Баланс на счете.
        :rtype: float
        """
        return round(self._balance, 2)

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Зашищенный сеттер
        :param value:
        :type value: float
        """
        if value < 0:
            raise TransactionError("Баланс не может быть отрицательным.")
        self._balance = float(value)

    def deposit(self, amount: float) -> None:
        """
        Пополняет баланс
        :param amount: сумма пополнения
        :type amount: float
        """
        if amount < 0:
            raise TransactionError("Сумма пополнения должна быть положительной.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Обналичвание средств
        :param amount: сумма снятия
        :type amount: float
        """
        if amount <= 0:
            raise TransactionError("Сумма снятия должна быть положительной.")
        if amount > self._balance:
            raise TransactionError("Недостаточно средств.")
        self._balance -= amount

    @abstractmethod
    def account_type(self) -> str:
        """Возвращает тип счёта."""
        pass

    def __str__(self) -> str:
        return f"{self.account_type()} {self.owner}: баланс {self.balance:.2f}"


class SavingsAccount(Account):
    """
    Сберегательный счёт с процентной ставкой.
    """

    def __init__(
        self, owner: str, balance: float = 0.0, interest_rate: float = 0.01
    ) -> None:
        """
        Инициализирует сберегательный счёт.

        :param owner: Имя владельца.
        :type owner: str
        :param balance: Начальный баланс.
        :type balance: float
        :param interest_rate: Процентная ставка (например, 0.01 = 1%).
        :type interest_rate: float
        """
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    @property
    def interest_rate(self) -> float:
        """Возвращает текущую процентную ставку."""
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value: float) -> None:
        """Устанавливает процентную ставку, проверяя, что она не отрицательная."""
        if value < 0:
            raise TransactionError("Процентная ставка не может быть отрицательной.")
        self._interest_rate = float(value)

    def add_interest(self) -> float:
        """
        Начисляет проценты на баланс.
        :return: Сумму начисления.
        :rtype: float
        """
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        return interest

    def account_type(self) -> str:
        return "Сберегательный счёт"

    def __str__(self) -> str:
        return super().__str__() + f", ставка {self.interest_rate * 100:.1f}%"


class CreditAccount(Account):
    """
    Кредитный счёт с лимитом.
    """

    def __init__(
        self, owner: str, balance: float = 0.0, credit_limit: float = 10000.0
    ) -> None:
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise TransactionError("Сумма снятия должна быть положительной.")
        if self._balance - amount < -self.credit_limit:
            raise TransactionError("Превышен кредитный лимит.")
        self._balance -= amount

    def account_type(self) -> str:
        return "Кредитный счёт"

    def __str__(self) -> str:
        return super().__str__() + f", лимит {self.credit_limit:.2f}"


class Shape(ABC):
    """Базовый класс фигуры"""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass


class Rectangle(Shape):
    """Класс прямоугольника."""

    def __init__(self, length: float, height: float) -> None:
        self.length = length
        self.height = height

    def area(self) -> float:
        """
        Возвращает площадь прямоугольника.
        :return: площадь прямоугольника
        :rtype: float
        """
        return self.height * self.length

    def __str__(self) -> str:
        return f"Rectangle({self.length}×{self.height}) → area={self.area():.2f}"


class Circle(Shape):
    """Класс окружности."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """
        Возвращает площадь круга.
        :return: площадь круга
        :rtype: float
        """
        return self.radius**2 * math.pi

    def __str__(self) -> str:
        return f"Circle(r={self.radius}) → area={self.area():.2f}"
