#!/usr/bin/env python3
"""
Module for calculating the determinant of a matrix
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix
    """
    # Validation: Input must be a list of lists
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Handle the 0x0 matrix case [[]]
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    # Validation: Must be a square matrix
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            raise ValueError("matrix must be a square matrix")

    # Base Case: 1x1 matrix
    if n == 1:
        return matrix[0][0]

    # Base Case: 2x2 matrix
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # Recursive Step: Laplace Expansion
    det = 0
    for j in range(n):
        # Create the sub-matrix (minor)
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Calculate cofactor and add to total determinant
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det
