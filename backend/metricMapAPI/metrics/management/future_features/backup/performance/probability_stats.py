"""
This module provides statistical functions to calculate the probability of achieving or exceeding a target value
based on a given dataset. It uses the normal distribution model to estimate these probabilities.
"""

import numpy as np
from scipy import stats

def calculate_probability(data, target_value):
    """
    Functions:
    calculate_probability(data, target_value): Calculates the probability of achieving a value greater than or
        equal to the target value based on the dataset's mean and standard deviation.
    """
    mean = np.mean(data)
    std_dev = np.std(data)
    probability = 1 - stats.norm.cdf(target_value, mean, std_dev)
    return probability

def probability_analysis(historical_data, target_value):
    """
    Functions:
    probability_analysis(historical_data, target_value): Provides a detailed analysis including the mean,
        standard deviation, target value, and the probability of achieving that target.
    """
    data = [point['value'] for point in historical_data]
    probability = calculate_probability(data, target_value)
    return {
        'mean': np.mean(data),
        'standard_deviation': np.std(data),
        'target': target_value,
        'probability_of_achieving_target': probability
    }

"""
Example:
    >>> data = [100, 102, 98, 97, 105]
    >>> target_value = 103
    >>> probability = calculate_probability(data, target_value)
    >>> print(f"Probability of achieving target: {probability:.2f}")
    >>> detailed_analysis = probability_analysis(data, target_value)
    >>> print(detailed_analysis)

Notes:
    - This module uses numpy for statistical calculations and scipy for calculating cumulative distribution functions.
    - The function returns a float value representing the probability and a dictionary for detailed analysis, which
      includes mean, standard deviation, and probability calculations based on historical data.
    - The normal distribution assumption requires the data to be sufficiently symmetric and bell-shaped, which
      may not hold true for all datasets.
"""