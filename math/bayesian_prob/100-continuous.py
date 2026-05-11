#!/usr/bin/env python3
"""Module to calculate continuous posterior for Bayesian probability"""
from scipy import special


def posterior(x, n, p1, p2):
    """Calculates the posterior probability for a range [p1, p2]"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        x1 = "x must be an integer that is greater than or equal to 0"
        raise ValueError(x1)
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or not (0 <= p1 <= 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or not (0 <= p2 <= 1):
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    # Beta distribution parameters
    a = x + 1
    b = n - x + 1
    # Posterior is CDF(p2) - CDF(p1)
    # special.betainc(a, b, x) returns the regularized incomplete beta function
    return special.betainc(a, b, p2) - special.betainc(a, b, p1)
