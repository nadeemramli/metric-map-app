"""
This module provides functionality for updating a dataset of historical data with new incoming data.
It ensures the combined data is sorted by date and retains continuity and integrity.

We also need to add bulk import and export function here
"""

import pandas as pd

def update_historical_data(historical_data, new_data):
    """
    Functions:
    update_historical_data(historical_data, new_data): Updates an existing historical data DataFrame
        by appending new data, sorting by date, and resetting the index for continuity.
    """
    updated_data = pd.concat([historical_data, new_data], ignore_index=True)
    updated_data = updated_data.sort_values('date').reset_index(drop=True)
    return updated_data

"""
Example:
    >>> historical_data = pd.DataFrame({
        'date': ['2021-01-01', '2021-01-02'],
        'value': [100, 200]
    })
    >>> new_data = pd.DataFrame({
        'date': ['2021-01-03'],
        'value': [150]
    })
    >>> updated_data = update_historical_data(historical_data, new_data)
    >>> print(updated_data)

Notes:
    - The historical_data and new_data should both be Pandas DataFrame objects containing at least a 'date' column.
    - The function returns a DataFrame that integrates new data into the historical data, ensuring it is sorted by date.
    - This utility is particularly useful in time series analysis where data continuity is crucial.
"""