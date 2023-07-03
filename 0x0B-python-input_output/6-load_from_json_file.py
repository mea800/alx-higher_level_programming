#!/usr/bin/python3
"""Module containing a function to load data from a JSON file."""
import json


def load_from_json_file(filename):
    """Load data from a JSON file and return as an object.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        object: Loaded data as an object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
