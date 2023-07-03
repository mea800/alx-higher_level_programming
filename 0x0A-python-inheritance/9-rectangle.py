#!/usr/bin/python3
"""Rectangle class based on BaseGeometry class.

Attributes:
    __width (int): width of the rectangle.
    __height (int): height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
