#!/usr/bin/python3
"""This module contains a function for
converting an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Converts an object to its JSON representation as a string.

    Args:
        my_obj (type): The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    # Serialize object to JSON
    return json.dumps(my_obj)
