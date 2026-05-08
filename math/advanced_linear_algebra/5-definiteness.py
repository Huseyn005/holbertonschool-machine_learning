#!/usr/bin/env python3
"""Module to calculate the determinant of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix"""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1

    if any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a square matrix")

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for j in range(n):
        # Create the sub-matrix (minor)
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        # Calculate cofactor and add to total determinant
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)

    return det
