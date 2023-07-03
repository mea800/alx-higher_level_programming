#!/usr/bin/python3
"""Module containing a function for reading file contents."""


def read_file(filename=""):
    """Reads and prints contents of a file.

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()  # Read file contents
        print(read_data, end='')  # Print file contents to stdout
