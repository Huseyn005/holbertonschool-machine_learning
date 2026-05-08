#!/usr/bin/env python3
"""Module to calculate the sum of i squared"""


def summation_i_squared(n):
    """
    Calculates the sum of i^2 from 1 to n
    Returns the integer value of the sum, or None if n is not valid
    """
    if not isinstance(n, int) or n < 0:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
