#!/usr/bin/env python3
"""
Defines a function that renames and modifies a specific pd.DataFrame
"""
import pandas as pd


def rename(df):
    """
    Renames the Timestamp column to Datetime, converts the values to
    datetime objects, and filters to display only Datetime and Close.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The modified DataFrame with only Datetime and Close.
    """
    # Rename the column
    df = df.rename(columns={'Timestamp': 'Datetime'})

    # Convert UNIX timestamp to datetime
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')

    # Return only the requested columns
    return df[['Datetime', 'Close']]
