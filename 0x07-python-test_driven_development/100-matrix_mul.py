#!/usr/bin/python3
"""This module defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (matrix): first matrix
        m_b (matrix): second matrix

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists, or if
        an element of those list of lists is not an integer or a float
        ValueError: If m_a or m_b is empty, or if they cannot be multiplied
        TypeError: If m_a or m_b is not a rectangle (all rows should be
        of the same size)

    Returns:
        matrix: the product of the two matrices
    """

    # Check that m_a and m_b are lists of lists containing only numbers
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        string = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError("{} must be a list".format(string))
    for element in m_a:
        if not isinstance(element, list):
            raise TypeError("m_a must be a list of lists")
        for item in element:
            if not isinstance(item, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for element in m_b:
        if not isinstance(element, list):
            raise TypeError("m_b must be a list of lists")
        for item in element:
            if not isinstance(item, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Check that m_a and m_b are not empty and are rectangles
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")
    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])
    for element in m_a:
        if len(element) != len_m_a:
            raise TypeError("each row of m_a must be of the same size")
    for element in m_b:
        if len(element) != len_m_b:
            raise TypeError("each row of m_b must be of the same size")

    # Check that m_a and m_b can be multiplied
    if len_m_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply m_a and m_b and return the product
    result = [[0 for a in m_b[0]] for x in m_a]
    for i in range(len(m_a)):
        for n in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][n] += m_a[i][k] * m_b[k][n]
    return result
