#!/usr/bin/env python3
"""Calculates a correlation matrix"""
import numpy as np


def correlation(C):
    """Calculates a correlation matrix from a covariance matrix"""
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")
    if len(C.shape) != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")
    variance = np.diag(C)
    std_dev = np.sqrt(variance).reshape(-1, 1)
    std_matrix = np.matmul(std_dev, std_dev.T)
    R = C / std_matrix
    return R
