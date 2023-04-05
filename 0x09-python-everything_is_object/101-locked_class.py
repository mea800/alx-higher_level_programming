#!/usr/bin/python3
"""Defines the class Locked_Class"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if  new instance attribute is called :
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked_Class."""

        self.first_name = "first_name"
    