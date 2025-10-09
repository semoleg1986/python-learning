import pytest

from week2.day4_inheritance import SavingsAccount, TransactionError


def test_deposit_and_withdraw():
    sa = SavingsAccount("Sam", 1000)
    sa.deposit(500)
    sa.withdraw(200)
    assert sa.balance == 1300


def test_withdraw_too_much():
    sa = SavingsAccount("Sam", 100)
    with pytest.raises(TransactionError):
        sa.withdraw(200)


def test_interest_addition():
    sa = SavingsAccount("Sam", 1000, 0.05)
    interest = sa.add_interest()
    assert interest == 50
    assert round(sa.balance, 2) == 1050.00
