"""
Unit tests for the calculator library
"""

import math
import calculator


# class RandomName:
class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_division(self):
        assert 2 == calculator.divide(4, 2)

    '''
    def test_lobAbs(self):
        assert 3 == calculator.logAbs(math.exp(3))

    def test_lobAbsNegative(self):
        assert 3 == calculator.logAbs(-math.exp(3))
    '''
