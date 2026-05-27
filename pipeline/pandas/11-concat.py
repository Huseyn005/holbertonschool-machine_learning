#!/usr/bin/env python3
"""
Defines a function that concatenates specific slices of two pd.DataFrames
"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """
    Indexes two dataframes on Timestamp, filters df2 up to 1417411920,
    and concatenates them with specific keys.

    Args:
        df1: The first DataFrame (coinbase).
        df2: The second DataFrame (bitstamp).

    Returns:
        The concatenated DataFrame with hierarchical indexing.
    """
    # Index both dataframes using the imported index function
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    # Filter bitstamp data up to and including timestamp 1417411920
    df2_filtered = df2_indexed.loc[:1417411920]

    # Concatenate df2 on top of df1 with specified multi-index keys
    return pd.concat(
        [df2_filtered, df1_indexed],
        keys=['bitstamp', 'coinbase']
    )
