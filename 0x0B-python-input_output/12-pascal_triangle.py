#!/usr/bin/python3
"""Module containing the function pascal_triangle"""


def pascal_triangle(n):
    """Generates and returns Pascal's Triangle as a list of lists of integers.

    Args:
        n (int): Number of rows to generate.

    Returns:
        list: List of lists of integers representing Pascal's Triangle.
    """
    if n <= 0:
        return []  # Return an empty list for n <= 0
    if n == 1:
        return [[1]]  # Return the first row of Pascal's Triangle for n = 1

    pascal = [[1]]  # Initialize Pascal's Triangle with the first row
    for i in range(n - 1):
        # Generate subsequent rows by summing pairs of consecutive elements
        pascal.append([x + y for x, y in zip(
                    pascal[-1] + [0], [0] + pascal[-1])])
    return pascal  # Return Pascal's Triangle with n rows
