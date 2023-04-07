#!/usr/bin/python3
"""
This script defines a function that multiplies
two matrices using the NumPy module.
"""

import numpy as np


def matrix_multiply(m_a, m_b):
    """
    This function takes two matrices as arguments and returns their product.
    """
    # Perform matrix multiplication using NumPy's matmul function
    return np.matmul(m_a, m_b)
