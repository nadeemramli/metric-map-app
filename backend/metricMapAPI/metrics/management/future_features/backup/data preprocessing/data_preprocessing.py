"""
This module contains functions for data 
preprocessing, including outlier 
detection and data transformation.
"""
from statistics import mean, stdev as standard_deviation
import numpy as np
from scipy import stats

def detect_outliers(data, method='iqr'):
    """
    Detect outliers in a dataset using the specified method.

    Parameters:
    data (list): A list of numerical values.
    method (str): The method to use for outlier detection ('iqr' or 'z_score').

    Returns:
    list: A list of outliers.
    """
    if method == 'iqr':
        q1, q3 = np.percentile(data, [25, 75])
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        iqrResultMethod = [x for x in data if x < lower_bound or x > upper_bound]
        return iqrResultMethod
    
    if method == 'z_score':
        mean_val = mean(data)
        std_dev = standard_deviation(data)
        zResultMethod = [x for x in data if abs((x - mean_val) / std_dev) > 3]
        return zResultMethod

def log_transform(data):
    """
    Apply a log transformation to the data.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    list: A list of log-transformed values.
    """
    return [np.log(x) for x in data if x > 0]

def box_cox_transform(data):
    """
    Apply a Box-Cox transformation to the data.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    list: A list of Box-Cox transformed values.
    """
    transformed_data, _ = stats.boxcox(data)
    return transformed_data
