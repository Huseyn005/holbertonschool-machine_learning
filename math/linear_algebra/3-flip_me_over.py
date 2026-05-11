#!/usr/bin/env python3
"""Function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix"""
    return [[matrix[row][col] for row in range(len(matrix))]
            for col in range(len(matrix[0]))]
