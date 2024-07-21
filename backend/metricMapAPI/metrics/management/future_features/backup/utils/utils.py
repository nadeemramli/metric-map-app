"""
This module contains utility functions for handling missing values and normalizing data.
"""

from statistics import mean

def handle_missing_values(data):
    """
    Handle missing values in a list of data.

    Parameters:
    data (list): A list of numerical values, which may include None.

    Returns:
    list: A list with missing values replaced by the mean of the non-missing values.
    """
    valid_data = [x for x in data if x is not None]
    mean_value = sum(valid_data) / len(valid_data) if valid_data else 0
    return [x if x is not None else mean_value for x in data]

def normalize_data(data):
    """
    Normalize a list of data.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    list: A list of normalized values.
    """
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

