#!/usr/bin/python3
"""Module containing the append_write function"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns the number
    of characters added.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string of text
        to write to the file. Defaults to "".

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        # Write the text to the file and return
        # the number of characters written
        return f.write(text)
