#!/usr/bin/python3
"""Defines a rebel class MyInt that inherits from int.
MyInt rebels against the default behavior of equality and inequality operators.
"""


class MyInt(int):
    """A rebel class that flips the equality and inequality operators.

    Args:
        int (int): An integer value.
    """
    def __init__(self, value):
        """Creates a new instance of MyInt class.

        Args:
            value (int): An integer value.
        """
        self.__value = value

    def __eq__(self, other):
        """Overrides the equality operator to return the opposite result.

        Args:
            other (int): An integer value.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return self.__value != other

    def __ne__(self, other):
        """Overrides the inequality operator to return the opposite result.

        Args:
            other (int): An integer value.

        Returns:
            bool: True if equal, False otherwise.
        """
        return self.__value == other
