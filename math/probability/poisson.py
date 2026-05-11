#!/usr/bin/env python3
"""
Module for Poisson distribution
"""


def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of 'successes'
        """
        # Convert k to an integer
        k = int(k)

        # If k is out of range, return 0
        if k < 0:
            return 0

        # e is approximately 2.7182818285
        e = 2.7182818285
        
        # Calculate factorial of k
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        # PMF Formula: (e^-lambda * lambda^k) / k!
        pmf_value = (e ** -self.lambtha) * (self.lambtha ** k) / factorial
        
        return pmf_value

