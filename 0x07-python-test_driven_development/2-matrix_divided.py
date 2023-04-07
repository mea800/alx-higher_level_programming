#!/usr/bin/python3
"""Defines a function for dividing all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): Value to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix isn't of the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If a row in the matrix is not a list.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        matrix: A result of the division.
    """
    row_size = None
    error_msg = "Invalid input: matrix must be a \
        list of lists containing integers/floats."

    # Check if the input matrix is valid
    if not matrix or not isinstance(matrix, list):
        raise TypeError(error_msg)

    for i in matrix:
        # Check if each row of the matrix is a\
        # list containing only integers or floats
        if not i or not isinstance(i, list):
            raise TypeError(error_msg)

        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(error_msg)

        # Check if each row of the matrix has the same size
        if row_size is None:
            row_size = len(i)
        elif row_size != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    # Check if the divisor is a number and not equal to zero
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("Invalid input: div must be a number")

    if div == 0:
        raise ZeroDivisionError("Invalid input: division by zero")

    # Perform the division and return the result
    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return new_matrix
