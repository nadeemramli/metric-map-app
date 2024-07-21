"""
This module provides functionality to compare forecasted data against actual historical data. It merges the two data sets
based on the date, calculates differences and percent differences between the forecasted and actual values.
"""

import pandas as pd

def forecast_vs_actual_comparison(historical_data, forecast_data):
    """
    Functions:
    forecast_vs_actual_comparison(historical_data, forecast_data): Compares actual data against forecast data to assess
        the accuracy and deviation of forecasts.
    """
    
    actual_df = pd.DataFrame(historical_data)
    forecast_df = pd.DataFrame(forecast_data)
    
    comparison = pd.merge(actual_df, forecast_df, on='date', suffixes=('_actual', '_forecast'))
    comparison['difference'] = comparison['value_actual'] - comparison['value_forecast']
    comparison['percent_difference'] = (comparison['difference'] / comparison['value_forecast']) * 100
    
    return comparison.to_dict()

"""
Example:
    >>> historical_data = {'date': ['2022-01-01', '2022-01-02'], 'value': [100, 110]}
    >>> forecast_data = {'date': ['2022-01-01', '2022-01-02'], 'value': [95, 105]}
    >>> comparison = forecast_vs_actual_comparison(historical_data, forecast_data)
    >>> print(comparison)

Notes:
    - Input data should be provided as dictionaries with 'date' and 'value' keys, where 'date' is the common key used
      for merging the datasets.
    - The function returns a dictionary with each date's actual values, forecast values, absolute differences, and
      percent differences.
    - Pandas is used for data manipulation, particularly for merging datasets and computing differences.
"""