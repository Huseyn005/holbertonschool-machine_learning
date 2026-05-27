#!/usr/bin/env python3
"""
Creates a specific pandas DataFrame from a dictionary and saves it into 'df'.
"""
import pandas as pd

# Define the dictionary with the requested data
data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}

# Define the explicit row index labels
row_labels = ['A', 'B', 'C', 'D']

# Create the DataFrame and save it into the required variable 'df'
df = pd.DataFrame(data, index=row_labels)
