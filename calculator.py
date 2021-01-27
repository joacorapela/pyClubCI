"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_factor, second_factor):
    return first_factor * second_factor


def divide(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError()
    return numerator / denominator
