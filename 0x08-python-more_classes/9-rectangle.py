#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """
    Represents a Rectangle object.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method for the width attribute.

        Args:
            value (int): The value to set as the width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for the height attribute.

        Args:
            value (int): The value to set as the height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
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

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with equal width and height.

        Args:
            cls: The class object.
            size (int, optional): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)

    def __str__(self):
        """Returns a string representation of the rectangle.

        Returns:
            str: A string representation of the rectangle.
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """Returns a string representation of a rectangle.
        Returns:
            str: a rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes the instance of a class
        """
        type(self).number_of_instances -= 1
        print("{:s}".format("Bye rectangle..."))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes the area of two rectangles and compares them.
        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.
        Returns:
            Rectangle: the rectangle with the biggest area else rect_1 if
            areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
