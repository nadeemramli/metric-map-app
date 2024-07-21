import pytest
import numpy as np
import pandas as pd
from scipy import stats
from metrics.computations.relationships_utils.causal_inference_utils import lagged_correlation_test

def generate_causal_data(size=1000):
    np.random.seed(42)
    x = np.random.normal(0, 1, size)
    y = np.zeros(size)
    for i in range(1, size):
        y[i] = 0.7 * y[i-1] + 0.3 * x[i-1] + 0.1 * np.random.normal(0, 1)
    return pd.Series(x), pd.Series(y)


def test_lagged_correlation():
    x, y = generate_causal_data()
    results = lagged_correlation_test(x, y, max_lag=10)
    
    # Print p-values for debugging
    for lag, p_value in results.items():
        print(f"Lag {lag}: p-value = {p_value}")
    
    # Check if at least one p-value is small (indicating causality)
    significant_causality = any(p_value < 0.05 for p_value in results.values())
    assert significant_causality, "No significant lagged correlation detected"
    
    # Check if the lag with the smallest p-value is close to 1 (our simulated lag)
    min_p_value_lag = min(results, key=results.get)
    assert 1 <= min_p_value_lag <= 3, f"Expected strongest correlation around lag 1, but found it at lag {min_p_value_lag}"

def test_granger_causality_test_invalid_input():
    # Test with non-Series input
    with pytest.raises(AttributeError):
        lagged_correlation_test([1, 2, 3], [4, 5, 6])
    
    # Test with Series of different lengths
    x = pd.Series(np.random.randn(100))
    y = pd.Series(np.random.randn(50))
    with pytest.raises(ValueError):
        lagged_correlation_test(x, y)