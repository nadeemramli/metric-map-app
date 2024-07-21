"""
Time Series Statistics
======================

This module provides statistical functions for time series analysis.
"""

import numpy as np
import pandas as pd

def simple_moving_average(data, window):
    """
    Calculate the simple moving average of the given data.

    Parameters:
    data (array-like): The input time series data.
    window (int): The window size for calculating the moving average.

    Returns:
    array: The simple moving average of the data.
    """
    result = data.rolling(window=window).mean()
    return result

def exponential_moving_average(data, span):
    """
    Calculate the exponential moving average of the given data.

    Parameters:
    data (array-like): The input time series data.
    span (int): The span for calculating the exponential moving average.

    Returns:
    array: The exponential moving average of the data.
    """
    return data.ewm(span=span, adjust=False).mean()

def weighted_moving_average(data, weights):
    """
    Calculate the weighted moving average of the given data.

    Parameters:
    data (array-like): The input time series data.
    weights (array-like): The weights to use for calculating the weighted moving average.

    Returns:
    array: The weighted moving average of the data.
    """
    window = len(weights)
    weights = np.array(weights)
    return data.rolling(window=window).apply(lambda x: np.sum(weights * x) / np.sum(weights))
