"""
This module contains functions for performing variance analysis on data sets. 
It includes methods for calculating standard deviation, variance, and other related statistics.
"""

import numpy as np
from scipy import stats

def anova(groups):
    """
    Perform ANOVA (Analysis of Variance) test.

    Parameters:
        groups: List of groups with their values.

    Returns:
        f_value, p_value: ANOVA test results.
    """
    f_value, p_value = stats.f_oneway(*groups)
    return f_value, p_value

def variance_decomposition(data):
    """
    Perform variance decomposition.

    Parameters:
        data: Time series data.

    Returns:
        components: Decomposed variance components.
    """
    mean = np.mean(data)
    total_variance = np.var(data)
    trend = np.mean([data[i + 1] - data[i] for i in range(len(data) - 1)])
    seasonal = np.mean([data[i] - mean for i in range(len(data))])
    residual = total_variance - (trend + seasonal)
    return {'trend': trend, 'seasonal': seasonal, 'residual': residual}
