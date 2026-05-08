#!/usr/bin/env python3
"""Module to calculate the integral of a polynomial"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial
    poly: list of coefficients (index is the power)
    C: integer representing the integration constant
    Returns: a new list of coefficients as small as possible
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not isinstance(C, int):
        return None

    # The integral of [0] is just [C]
    if poly == [0]:
        return [C]

    # Initialize integral list with the constant C at index 0
    integral = [C]

    for i in range(len(poly)):
        # Calculate new coefficient: poly[i] / (i + 1)
        val = poly[i] / (i + 1)

        # Convert to integer if it is a whole number (e.g., 5.0 -> 5)
        if val == int(val):
            val = int(val)

        integral.append(val)

    # The returned list should be as small as possible
    # Removing trailing zeros that don't affect the polynomial
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
