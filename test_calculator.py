"""
Unit tests for the calculator library
"""

import pytest
import calculator


def test_addition():
    assert 4 == calculator.add(2, 2)


def test_subtraction():
    assert 2 == calculator.subtract(4, 2)


def test_multiplication():
    assert 8 == calculator.multiply(4, 2)


def test_division():
    assert 2 == calculator.divide(4, 2)


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(4, 0)
