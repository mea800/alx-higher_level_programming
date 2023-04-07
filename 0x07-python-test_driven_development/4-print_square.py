#!/usr/bin/python3
"""
This module defines a function for printing a square of '#' characters.
"""


def print_square(size):
    """
    Prints a square of '#' characters with a side length equal to `size`.

    Args:
        size (int): The length of one side of the square.

    Raises:
        TypeError: If `size` is not an integer or if
        it is a float and less than 0.
        ValueError: If `size` is less than 0.
    """
    message = "size must be an integer"

    if not isinstance(size, int):
        raise TypeError(message)

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError(message)

    for i in range(size):
        print("#" * size)
