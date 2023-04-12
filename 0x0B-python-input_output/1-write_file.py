#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """Write string to text file and return character count.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text string to write to file. Defaults to "".

    Returns:
        int: Number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        # Write text to file and return character count
        return f.write(text)
