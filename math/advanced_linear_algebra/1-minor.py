#!/usr/bin/env python3
"""Module to calculate the minor matrix of a matrix"""
determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Calculates the minor matrix of a matrix"""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if empty or not square
    if len(matrix[0]) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    
    # Handle the 1x1 case: the project output for [[5]] is [[1]]
    if n == 1:
        return [[1]]

    minor_matrix = []
    for i in range(n):
        row_minors = []
        for j in range(n):
            # Create sub-matrix by removing row i and column j
            sub_matrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix)
                          if k != i]
            # Calculate the determinant of the sub-matrix
            row_minors.append(determinant(sub_matrix))
        minor_matrix.append(row_minors)

    return minor_matrix
