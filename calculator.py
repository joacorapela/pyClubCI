"""
Calculator library containing basic math operations.
"""
import math

def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def divide(numerator, denominator):
    return numerator / denominator

def logAbs(x):
    if x<0:
        x *= -1
    return math.log(x)
