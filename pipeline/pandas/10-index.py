#!/usr/bin/env python3
"""
Defines a function that sets a column as the index of a pd.DataFrame
"""


def index(df):
    """
    Sets the Timestamp column as the index of the dataframe.

    Args:
        df: The input DataFrame.

    Returns:
        The modified DataFrame with 'Timestamp' as the index axis.
    """
    # Use set_index to shift the target column into the row index position
    return df.set_index('Timestamp')
