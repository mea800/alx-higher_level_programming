#!/usr/bin/python3
"""
This is the "add_integer" module.
It defines a function called "add_integer",
which takes two numbers and returns their sum.
"""


def add_integer(a, b):
    """Return the sum of two numbers."""
    # Check that both a and b are integers or floats.
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer or float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer or float")
    # Convert a and b to integers if they are floats.
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    # Return the sum of a and b.
    return a + b
