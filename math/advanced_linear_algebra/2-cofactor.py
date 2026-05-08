#!/usr/bin/env python3
"""Module to calculate the cofactor matrix of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix"""
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 1
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for j in range(n):
        sub = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * determinant(sub)
    return det


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix"""
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a list of lists")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    if len(matrix) == 0 or len(matrix[0]) == 0 or \
       any(len(row) != len(matrix) for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    n = len(matrix)
    if n == 1:
        return [[1]]

    cofactor_matrix = []
    for i in range(n):
        row_cofactors = []
        for j in range(n):
            # Create sub-matrix for the minor
            sub_matrix = [row[:j] + row[j+1:] for k, row in enumerate(matrix)
                          if k != i]
            # Cofactor = (-1)^(i+j) * minor
            minor_val = determinant(sub_matrix)
            row_cofactors.append(((-1) ** (i + j)) * minor_val)
        cofactor_matrix.append(row_cofactors)

    return cofactor_matrix
