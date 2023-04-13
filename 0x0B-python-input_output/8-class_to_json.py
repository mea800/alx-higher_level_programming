#!/usr/bin/python3
"""Module containing the class_to_json function"""


def class_to_json(obj):
    """Converts an object to a dictionary
    representation for JSON serialization.

    Args:
        obj (MyClass): The object to be serialized.

    Returns:
        dict: A dictionary containing simple data
    structures suitable for JSON serialization.
    """
    # Print the type of the object for debugging
    # print("type of obj --> {}".format(type(obj)))

    # Retrieve the attributes and their
    # values from the object's __dict__ attribute
    return obj.__dict__
