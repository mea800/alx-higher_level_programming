#!/usr/bin/python3
"""This script defines a function to print
a text with 2 new lines after each occurrence of ., ? and :

The function is called text_indentation.
"""


def text_indentation(text):
    """Prints a given text with 2 new lines after ., ? and : characters

    Args:
        text (str): The text to be examined

    Raises:
        TypeError: If text is not a string
    """
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text at each delimiter and join
    # them back with the delimiter and 2 new lines
    for delimiter in ".:?":
        text = (delimiter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimiter)])

    # Print the resulting text with no newline at the end
    print(text, end="")
