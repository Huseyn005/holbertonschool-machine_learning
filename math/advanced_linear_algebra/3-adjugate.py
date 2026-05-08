#!/usr/bin/env python3
"""Module to calculate the adjugate matrix of a matrix"""


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


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix"""
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

    # Step 1: Calculate the cofactor matrix
    # Note: We build the transpose (adjugate) directly
    adj = []
    for i in range(n):
        adj_row = []
        for j in range(n):
            # To get adjugate, we calculate cofactor of (j, i) for element (i, j)
            # This is the same as calculating cofactors then transposing.
            sub_matrix = [row[:i] + row[i+1:] for k, row in enumerate(matrix)
                          if k != j]
            minor_val = determinant(sub_matrix)
            adj_row.append(((-1) ** (i + j)) * minor_val)
        adj.append(adj_row)

    return adj
