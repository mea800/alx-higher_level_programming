#!/usr/bin/python3
"""This module defines a function to add two integers or floats.

This module defines the function `add_integer`,
which takes two arguments, `a` and `b`,
and returns their sum as an integer.
If `b` is not provided, it defaults to 98.
The function performs type checking to ensure
that `a` and `b` are integers or floats.
If they are not, a `TypeError` is raised.

Example:
    The following code snippet adds two integers:
        >>> add_integer(2, 3)
        5

    The following code snippet adds an integer and a float:
        >>> add_integer(2, 3.0)
        5

    The following code snippet adds two floats:
        >>> add_integer(2.0, 3.0)
        5

Attributes:
    add_integer: function that adds two integers or floats.
"""


def add_integer(a, b=98):
    """Add two integer or float values.

    Args:
        a (int or float): First value
        b (int or float, optional): Second value. Defaults to 98.

    Raises:
        TypeError: If a and b are not integers or floats.

    Returns:
        int: Sum of a and b.
    """
    # Check that a and b are integers or floats
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer or float")

    # Convert floats to integers before adding
    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return a + b
