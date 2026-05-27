#!/usr/bin/env python3
"""
Defines a function that drops rows with missing data based on a column
"""


def prune(df):
    """
    Removes rows from a pd.DataFrame where the 'Close' column has NaN values.

    Args:
        df: The input DataFrame.

    Returns:
        The modified DataFrame with NaN entries dropped from 'Close'.
    """
    # Use dropna targeting specifically the 'Close' subset of data
    return df.dropna(subset=['Close'])
