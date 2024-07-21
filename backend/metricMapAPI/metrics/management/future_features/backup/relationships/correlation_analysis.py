"""
Correlation Analysis
====================

This module provides functions for analyzing correlations between variables.
"""

def pearson_correlation(x, y):
    """
    Calculate the Pearson correlation coefficient between two variables.

    Parameters:
    x (array-like): The first variable.
    y (array-like): The second variable.

    Returns:
    float: The Pearson correlation coefficient.
    """
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_sq = sum(xi ** 2 for xi in x)
    sum_y_sq = sum(yi ** 2 for yi in y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x_sq - sum_x ** 2) * (n * sum_y_sq - sum_y ** 2)) ** 0.5
    return numerator / denominator if denominator != 0 else 0

def spearman_correlation(x, y):
    """
    Calculate the Spearman rank correlation coefficient between two variables.

    Parameters:
    x (array-like): The first variable.
    y (array-like): The second variable.

    Returns:
    float: The Spearman rank correlation coefficient.
    """
    rank_x = {val: rank for rank, val in enumerate(sorted(x), 1)}
    rank_y = {val: rank for rank, val in enumerate(sorted(y), 1)}
    ranked_x = [rank_x[val] for val in x]
    ranked_y = [rank_y[val] for val in y]
    return pearson_correlation(ranked_x, ranked_y)
