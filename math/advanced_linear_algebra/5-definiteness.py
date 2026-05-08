#!/usr/bin/env python3
"""Module to calculate the definiteness of a matrix"""
import numpy as np


def definiteness(matrix):
    """Calculates the definiteness of a matrix"""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1] or \
       not np.allclose(matrix, matrix.T):
        return None

    try:
        eigenvalues = np.linalg.eigvals(matrix)
    except np.linalg.LinAlgError:
        return None

    pos = np.all(eigenvalues > 0)
    pos_semi = np.all(eigenvalues >= 0)
    neg = np.all(eigenvalues < 0)
    neg_semi = np.all(eigenvalues <= 0)

    if pos:
        return "Positive definite"
    if neg:
        return "Negative definite"
    if pos_semi:
        return "Positive semi-definite"
    if neg_semi:
        return "Negative semi-definite"

    return "Indefinite"
