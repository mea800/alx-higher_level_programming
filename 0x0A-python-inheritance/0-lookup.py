#!/usr/bin/python3
"""Defines a function lookup()"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object

    Args:
        obj (object): The object to inspect

    Returns:
        list: A list of available attributes and methods of the object
    """
    return dir(obj)
