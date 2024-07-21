"""
Advanced Statistics
===================

This module provides advanced statistical functions.
"""

import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis as scipy_kurtosis

def calculate_skewness(data):
    """
    Calculate the skewness of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The skewness of the data.
    """
    return skew(data)

def calculate_kurtosis(data):
    """
    Calculate the kurtosis of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The kurtosis of the data.
    """
    return scipy_kurtosis(data, fisher=True)

def calculate_percentile(data, p):
    """
    Calculate the p-th percentile of the given data.

    Parameters:
    data (array-like): The input data.
    p (float): The percentile to compute, which must be between 0 and 100 inclusive.

    Returns:
    float: The p-th percentile of the data.
    """
    return np.percentile(data, p)
