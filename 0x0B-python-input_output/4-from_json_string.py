#!/usr/bin/python3
"""JSON String to Python Object Converter"""

import json


def from_json_string(my_str):
    """Converts a JSON string to a Python object.

    Args:
        my_str (str): JSON string to be converted.

    Returns:
        obj: Python object.
    """
    # Call json.loads() to parse JSON string and convert to Python object
    return json.loads(my_str)
