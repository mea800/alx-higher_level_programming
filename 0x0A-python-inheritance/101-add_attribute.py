#!/usr/bin/python3
"""add_attribute function to add a new attribute to an object if possible"""


def add_attribute(object, attr_name, value):
    """Add a new attribute to an object if possible.

    Args:
        object (__main__.MyClass): name of the object.
        attr_name ('str): name of the attribute.
        value (str): value of the attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.
    """
    # Check if object has __dict__ attribute
    # print("object type ---> {}".format(type(object)))
    # print("attr_name type ---> {}".format(type(attr_name)))
    # print("value type ---> {}".format(type(value)))
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    # Set the attribute with given name and value
    setattr(object, attr_name, value)
