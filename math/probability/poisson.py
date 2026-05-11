#!/usr/bin/env python3
"""
Module for Poisson distribution
"""


class Poisson:
    """
    Class that represents a poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize Poisson distribution
        """
        if data is None:
            # Handle case where data is not provided
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            # Handle case where data is provided
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")        
            # Calculate lambtha (mean of the data)
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of 'successes'
        """
        # Convert k to an integer
        k = int(k)
        # If k is out of range, return 0
        if k < 0:
            return 0
        # Euler's number (approximate value as per requirements)
        e = 2.7182818285 
        # Calculate factorial of k
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        # PMF Formula: (e^-lambda * lambda^k) / k!
        pmf_value = (e ** -self.lambtha) * (self.lambtha ** k) / factorial
        return pmf_value

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of 'successes'
        """
        # Convert k to an integer
        k = int(k)
        # If k is out of range, return 0
        if k < 0:
            return 0
        # Sum the PMF values from 0 up to k
        # F(k; lambda) = Sum from i=0 to k of PMF(i)
        cumulative_prob = 0
        for i in range(k + 1):
            cumulative_prob += self.pmf(i)
        return cumulative_prob
