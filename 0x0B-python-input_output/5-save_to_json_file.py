#!/usr/bin/python3
"""Module with save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using JSON representation.

    Args:
        my_obj (type): Object to be written to text file.
        filename (str): File name.

    Returns:
        type: JSON representation.
    """

    # Serialize object to JSON
    json_object = json.dumps(my_obj)

    # Write serialized JSON object to file
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json_object)
        # Close the file automatically with 'with' statement
        f.close()
