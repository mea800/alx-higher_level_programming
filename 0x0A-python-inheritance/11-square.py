#!/usr/bin/python3
"""Square class based on Rectangle class.

Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle.

    Args:
        Rectangle (Rectangle): Rectangle class for inheritance.
    """

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): Size of one side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """String representation of the Square.

        Returns:
            str: String representation of the square.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2
