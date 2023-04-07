#!/usr/bin/python3
"""This module defines a function for printing a name."""


def say_my_name(first_name, last_name=""):
    """Prints the name of the user based on input parameters.

    Args:
        first_name (str): The user's first name.
        last_name (str, optional): The user's last name. Defaults to "".

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.
    """
    # Check if `first_name` is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Check if `last_name` is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Print the user's name
    print("My name is {} {}".format(first_name, last_name))
