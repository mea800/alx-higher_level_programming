#!/usr/bin/python3
"""Defines the BaseGeometry class as a base
class for geometrical calculations."""


class BaseGeometry:
    """BaseGeometry class for geometrical calculations."""
    def area(self):
        """Calculates the area of a shape.

        Raises:
            Exception: If area is not implemented in the subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is an integer and greater than 0.

        Args:
            name (str): Name of the object.
            value (int): Value of the property.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
