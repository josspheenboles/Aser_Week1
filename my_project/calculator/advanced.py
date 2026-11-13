"""
calculator/advanced.py
======================

Another module in the same package. It uses Python's built-in math
module, which shows that modules can import other modules.

A PACKAGE is a folder of modules, and this file is one of its modules.
"""

# Import the standard-library math module so we can use math.sqrt later.
# The name "math" is not a file we wrote; it ships with Python.
import math


def power(base, exponent):
    """Return base raised to the power of exponent."""
    # ** is Python's exponent operator: 2 ** 3 is 8.
    return base**exponent


def square_root(number):
    """Return the square root of a number.

    Raises:
        ValueError: if number is negative, because real square roots
            of negative numbers are not defined.
    """
    # Validate the input before doing the math.
    if number < 0:
        raise ValueError("Cannot take the square root of a negative number.")

    # math.sqrt does the actual calculation for us.
    return math.sqrt(number)
