#!/usr/bin/env python3
"""Module to calculate the sum of i squared"""


def summation_i_squared(n):
    """
    Calculates the sum of i^2 from 1 to n
    Returns the integer value of the sum, or 'OK' if n is not valid
    """
    # Check if n is a valid positive integer
    if not isinstance(n, int) or n < 0:
        return "OK"
    
    # Using the formula n(n+1)(2n+1) / 6
    return (n * (n + 1) * (2 * n + 1)) // 6
