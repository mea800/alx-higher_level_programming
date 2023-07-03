#!/usr/bin/python3
"""Rectangle Class Definition.

Defines a Rectangle class that inherits from
BaseGeometry and has width and height attributes.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Rectangle Class Constructor.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
