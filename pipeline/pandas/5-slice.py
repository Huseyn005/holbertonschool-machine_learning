#!/usr/bin/env python3
"""
Defines a function that slices specific dimensions of a pd.DataFrame
"""


def slice(df):
    """
    Extracts specific columns and selects every 60th row.

    Args:
        df: The input DataFrame.

    Returns:
        The sliced DataFrame containing every 60th row of High,
        Low, Close, and Volume_(BTC).
    """
    # 1. Extract the specified columns
    # 2. Use standard Python slicing [::60] to grab every 60th row
    return df[['High', 'Low', 'Close', 'Volume_(BTC)']][::60]
