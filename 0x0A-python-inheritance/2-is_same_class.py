#!/usr/bin/python3
"""Defines a function is_same_class() to check if an
object is an instance of a specific class"""


def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class and
    return True if they match, False otherwise.

    Args:
        obj (a_class): Object to check the type.
        a_class (type): Type of object to compare.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
