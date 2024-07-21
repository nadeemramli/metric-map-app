"""
Basic Statistics
=================

This module provides basic statistical functions.
"""

def mean(data):
    """
    Calculate the mean of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The mean of the data.
    """
    return sum(data) / len(data)

def median(data):
    """
    Calculate the median of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The median of the data.
    """
    if not data:
        raise ValueError("Cannot calculate median of empty data")
    data = sorted(data)
    n = len(data)
    if n % 2 == 0:
        return (data[n // 2 - 1] + data[n // 2]) / 2
    return data[n // 2]

def standard_deviation(data):
    """
    Calculate the standard deviation of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The standard deviation of the data.
    """
    if not data:
        raise ValueError("Cannot calculate standard deviation of empty data")
    mean_value = mean(data)
    variance = sum((x - mean_value) ** 2 for x in data) / len(data)
    return variance ** 0.5

def coefficient_of_variation(data):
    """
    Calculate the coefficient of variation of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The coefficient of variation of the data.
    """
    return standard_deviation(data) / mean(data)

def standard_error(data):
    """
    Calculate the standard error of the given data.

    Parameters:
    data (array-like): The input data.

    Returns:
    float: The standard error of the data.
    """
    return standard_deviation(data) / (len(data) ** 0.5)

def check_empty_input(data):
    if not data:
        raise ValueError("Input data is empty")