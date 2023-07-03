#!/usr/bin/python3
"""This module defines a function to check if
an object is an instance of a class or its subclass."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a class or its subclass.

    Args:
        obj (a_class): Object to check type.
        a_class (type): Type of class to check.

    Returns:
        bool: True if obj is an instance of a_class
    or its subclass, False otherwise.
    """
    # Use isinstance() to check if obj is an instance
    # of a_class or its subclass
    return isinstance(obj, a_class)
