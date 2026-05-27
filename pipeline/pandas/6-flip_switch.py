#!/usr/bin/env python3
"""
Defines a function that reverses and transposes a pd.DataFrame
"""


def flip_switch(df):
    """
    Sorts a DataFrame in reverse chronological order and transposes it.

    Args:
        df: The input DataFrame.

    Returns:
        The transformed DataFrame (reversed and transposed).
    """
    # 1. Reverse the rows using standard slicing [::-1]
    # 2. Transpose the rows into columns using the .T attribute
    return df[::-1].T
