#!/usr/bin/python3
"""MyList - a custom list class that inherits from the built-in list class."""


class MyList(list):
    """Custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        # Create a copy of the list
        list_copy = self[:]
        # Sort the copied list in ascending order
        list_copy.sort()
        # Print the sorted list
        print(list_copy)
