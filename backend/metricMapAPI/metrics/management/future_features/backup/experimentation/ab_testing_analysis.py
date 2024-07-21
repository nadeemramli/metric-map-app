"""
This module is designed to perform A/B testing analysis, providing statistical insights to compare the performance
of two different datasets typically representing two variations of a similar entity.
"""
from scipy import stats

def ab_test_analysis(data_a, data_b):
    """
    Functions:
    ab_test_analysis(data_a, data_b): Computes the t-statistic and p-value to evaluate the differences between
        two independent samples.
    """
    t_stat, p_value = stats.ttest_ind(data_a, data_b)
    
    return {
        't_statistic': t_stat,
        'p_value': p_value,
        'mean_a': sum(data_a) / len(data_a),
        'mean_b': sum(data_b) / len(data_b)
    }

"""
Example:
    >>> data_a = [23, 21, 19, 25, 22]
    >>> data_b = [17, 20, 18, 21, 20]
    >>> results = ab_test_analysis(data_a, data_b)
    >>> print(results)

Notes:
    - This function uses the `ttest_ind` from `scipy.stats` to determine if there are significant differences between the two groups.
    - The function returns a dictionary with the t-statistic, p-value, and the means of both groups.
    - A lower p-value (< 0.05 typically) suggests that the observed differences are statistically significant.
    - It is assumed that both datasets passed to the function are lists of numeric values.
"""