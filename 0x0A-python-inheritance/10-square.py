#!/usr/bin/python3
"""Square Class Definition

This module defines a Square class that inherits from Rectangle class
defined in the '9-rectangle.py' module.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that represents a square shape.

    Attributes:
        size (int): size of one side of the square.
    """

    def __init__(self, size):
        """Square class constructor.

        Args:
            size (int): size of one side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
