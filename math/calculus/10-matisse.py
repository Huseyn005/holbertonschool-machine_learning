#!/usr/bin/env python3
"""Module to calculate the derivative of a polynomial"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial
    poly: list of coefficients (index is the power)
    Returns: a new list of coefficients
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    # A constant (e.g., [5]) has a derivative of 0 -> [0]
    if len(poly) == 1:
        return [0]

    # Calculate derivative: coefficient * power (index)
    # The first element (index 0) drops out
    derivative = [poly[i] * i for i in range(1, len(poly))]

    return derivative
