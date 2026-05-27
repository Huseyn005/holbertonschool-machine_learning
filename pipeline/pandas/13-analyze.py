#!/usr/bin/env python3
"""
Defines a function that computes descriptive statistics for a pd.DataFrame
"""
import pandas as pd


def analyze(df):
    """
    Computes descriptive statistics for all columns except Timestamp.

    Args:
        df: The input DataFrame.

    Returns:
        A new DataFrame containing the descriptive statistics (count, mean,
        std, min, 25%, 50%, 75%, max).
    """
    # 1. Drop the 'Timestamp' column if it exists in the standard columns
    # 2. Compute descriptive statistics using .describe()
    return df.drop(columns=['Timestamp'], errors='ignore').describe()
