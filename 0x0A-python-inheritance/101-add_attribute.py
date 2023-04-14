#!/usr/bin/python3
"""add_attribute function to add a new attribute to an object if possible"""


def add_attribute(object, attr_name, value):
    """Add a new attribute to an object if possible.

    Args:
        object (object): The object to which the attribute will be added.
        attr_name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    # Check if object has __dict__ attribute
    if not hasattr(object, "__dict__"):
        raise TypeError("Cannot add new attribute to object")
    # Set the attribute with given name and value
    setattr(object, attr_name, value)
