#!/usr/bin/env python3
"""
Defines a function that sorts a pd.DataFrame by a specific column
"""


def high(df):
    """
    Sorts a pd.DataFrame by the High price column in descending order.

    Args:
        df: The input DataFrame.

    Returns:
        The sorted DataFrame.
    """
    # Use sort_values on the 'High' column
    # ascending=False forces the highest prices to appear at the top
    return df.sort_values(by='High', ascending=False)
