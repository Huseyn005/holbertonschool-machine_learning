#!/usr/bin/env python3
"""
Defines a function that computes descriptive statistics for a pd.DataFrame
"""


def analyze(df):
    """
    Computes descriptive statistics for all columns except Timestamp.

    Args:
        df: The input DataFrame.

    Returns:
        A new DataFrame containing the descriptive statistics.
    """
    return df.drop(columns=['Timestamp'], errors='ignore').describe()
