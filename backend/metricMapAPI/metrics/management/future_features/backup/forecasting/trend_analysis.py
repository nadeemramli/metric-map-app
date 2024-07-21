"""
This module contains functions for trend analysis in time series data.
"""
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

def detect_trend(data):
    # Ensure the data is a pandas Series with a DatetimeIndex
    if not isinstance(data.index, pd.DatetimeIndex):
        data = pd.Series(data.values, index=pd.date_range(start='2020-01-01', periods=len(data)))

    """
    Detect trend in time series data.

    Parameters:
        data (pd.Series): Time series data.

    Returns:
        pd.Series: Trend component of the data.
    """
    result = seasonal_decompose(data, model='additive', period=365)
    return result.trend.dropna()

def decompose_time_series(data):
    """
    Decompose time series into seasonal, trend, and residual components.

    Parameters:
        data (pd.Series): Time series data.

    Returns:
        tuple: Trend, seasonal, and residual components of the time series.
    """
    result = seasonal_decompose(data, model='additive', period=12)
    return result.trend, result.seasonal, result.resid
