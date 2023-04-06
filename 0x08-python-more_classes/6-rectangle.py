#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """
    Class that defines properties of a rectangle (from 5-rectangle.py).

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """

    number_of_instances = 0
    """ tracks the number of instances of the
    Rectangle class that have been created """

    def __init__(self, width=0, height=0):
        """Initializes a new instance of the Rectangle class.

        Args:
            width (int, optional): Width of the rectangle. Defaults to 0.
            height (int, optional): Height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # Remove last newline character
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of the Rectangle class."""
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances
