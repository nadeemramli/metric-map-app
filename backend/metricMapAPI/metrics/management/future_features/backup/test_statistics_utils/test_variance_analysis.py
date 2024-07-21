import pytest
import numpy as np
from metrics.computations.statistics_utils.variance_analysis import anova, variance_decomposition

def test_anova():
    group1 = [1, 2, 3, 4, 5]
    group2 = [2, 3, 4, 5, 6]
    group3 = [3, 4, 5, 6, 7]
    f_value, p_value = anova([group1, group2, group3])
    assert isinstance(f_value, float)
    assert isinstance(p_value, float)
    assert 0 <= p_value <= 1

def test_variance_decomposition():
    data = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4])
    result = variance_decomposition(data)
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert abs(result['trend'] + result['seasonal'] + result['residual'] - np.var(data)) < 1e-10