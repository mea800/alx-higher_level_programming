#!/usr/bin/python3
"""Function for checking inheritance"""


def inherits_from(obj, a_class):
    """Check if object is instance of a subclass of specified class.

    Args:
        obj (a_class): Object to check type.
        a_class (type): Type/class to check against.

    Returns:
        bool: True if object is an instance of a subclass
    of specified class, False otherwise.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
