#!/usr/bin/env python3
"""
Defines a function that concatenates specific slices of two pd.DataFrames
"""
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
    # 1. Index both dataframes on their Timestamp columns using task 10 function
    df1_indexed = index(df1)
    df2_indexed = index(df2)

    # 2. Slice df2 to include all rows up to and including timestamp 1417411920
    # Since it is indexed on Timestamp, we can use label-based slicing via .loc
    df2_filtered = df2_indexed.loc[:1417411920]

    # 3. Concatenate df2_filtered to the top of df1_indexed
    # We pass [df2_filtered, df1_indexed] to put bitstamp on top.
    # The 'keys' parameter adds the multi-index labeling required.
    # We call the .concat method from df1's underlying class to avoid imports.
    return df1.__class__.concat(
        [df2_filtered, df1_indexed],
        keys=['bitstamp', 'coinbase']
    )
