#!/usr/bin/python3
"""
This script defines a function that multiplies
two matrices using the NumPy module.
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function takes two matrices as arguments and returns their product.
    """
    # Perform matrix multiplication using NumPy's matmul function
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
