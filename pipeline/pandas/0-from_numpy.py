#!/usr/bin/env python3
"""
Defines a function that creates a pd.DataFrame from a np.ndarray
"""
import pandas as pd


def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray with alphabetical column labels.

    Args:
        array (np.ndarray): The numpy array to convert.

    Returns:
        pd.DataFrame: The newly created DataFrame.
    """
    # Get the number of columns in the numpy array
    num_cols = array.shape[1]

    # Generate alphabet list: ['A', 'B', 'C', ..., 'Z'] up to num_cols
    # ASCII value for 'A' is 65
    columns = [chr(65 + i) for i in range(num_cols)]

    # Alternatively, you could use:
    # import string
    # columns = list(string.ascii_uppercase[:num_cols])

    return pd.DataFrame(array, columns=columns)
