"""
calculator/basic.py
===================

A MODULE is just a single .py file that holds reusable code.
This module contains the simplest calculator operations.

Every function here:
  - takes two numbers as inputs (parameters)
  - returns one number as the output
"""


def add(a, b):
    """Return the sum of a and b."""
    # The + operator adds the two inputs and return sends the result back.
    return a + b


def subtract(a, b):
    """Return the result of subtracting b from a."""
    # Order matters: a - b is not the same as b - a.
    return a - b
