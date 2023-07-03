#!/usr/bin/python3
"""Defines the BaseGeometry class with an area method."""


class BaseGeometry:
    """BaseGeometry class serves as a base class for other geometry classes.
    """
    def area(self):
        """Area method for calculating the area of a shape.

        Raises:
            Exception: if area is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")
