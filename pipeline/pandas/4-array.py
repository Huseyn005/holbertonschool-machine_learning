#!/usr/bin/env python3
"""
Defines a function that converts a slice of a pd.DataFrame to a np.ndarray
"""
import pandas as pd


def array(df):
    """
    Selects the last 10 rows of the High and Close columns from a DataFrame
    and converts them into a numpy.ndarray.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        np.ndarray: The numpy array of the selected values.
    """
    # Select the High and Close columns, then grab the last 10 rows using tail
    # Convert the resulting sliced DataFrame to a NumPy array using .to_numpy()
    return df[['High', 'Close']].tail(10).to_numpy()
