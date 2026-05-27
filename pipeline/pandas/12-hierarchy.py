#!/usr/bin/env python3
"""
Defines a function that creates a rearranged MultiIndex DataFrame
"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Concatenates two DataFrames between specific timestamps, adds keys,
    and rearranges the MultiIndex levels so Timestamp is the first level.

    Args:
        df1: The first DataFrame (coinbase).
        df2: The second DataFrame (bitstamp).

    Returns:
        The transformed DataFrame with swapped index levels sorted
        in chronological order.
    """
    # 1. Index both dataframes on their Timestamp columns
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    # 2. Slice both dataframes to include only timestamps from
    # 1417411980 to 1417417980 inclusive
    df1_filtered = df1_indexed.loc[1417411980:1417417980]
    df2_filtered = df2_indexed.loc[1417411980:1417417980]

    # 3. Concatenate bitstamp on top of coinbase with structural keys
    df = pd.concat([df2_filtered, df1_filtered], keys=['bitstamp', 'coinbase'])

    # 4. Rearrange MultiIndex levels so Timestamp is level 0 and keys are level 1
    # .swaplevel(0, 1) switches their order positions
    df = df.swaplevel(0, 1)

    # 5. Sort the data chronologically by index (Timestamp first)
    df = df.sort_index()

    return df
