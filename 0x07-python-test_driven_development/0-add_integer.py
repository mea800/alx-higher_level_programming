#!/usr/bin/python3
"""
This is the "add_integer" module.
It defines a function called "add_integer",
which takes two numbers and returns their sum.
"""


def add_integer(a, b):
    """Return the addition of two numbers."""
    # Check that both a and b are integers or floats.
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    # Convert a and b to integers if they are floats.
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    # Return the sum of a and b.
    return a + b
