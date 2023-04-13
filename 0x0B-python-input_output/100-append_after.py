#!/usr/bin/python3
"""Module containing the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        search_string (str, optional): String to search for. Defaults to "".
        new_string (str, optional): String to append. Defaults to "".
    """
    with open(filename, "r") as file:
        # Read all lines from the file
        text = file.readlines()

    with open(filename, "w") as file_out:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                # Append the new string after the
                # line containing the search string
                s += new_string
        # Write the modified text back to the file
        file_out.write(s)
