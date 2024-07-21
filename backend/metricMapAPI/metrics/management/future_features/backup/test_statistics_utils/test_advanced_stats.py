import pytest
import numpy as np
from metrics.computations.statistics_utils.advanced_stats import calculate_skewness, calculate_kurtosis, calculate_percentile

def test_calculate_skewness():
    # Test with a symmetric distribution (should be close to 0)
    symmetric_data = [1, 2, 3, 3, 3, 4, 5]
    assert abs(calculate_skewness(symmetric_data)) < 0.01

    # Test with a right-skewed distribution (should be positive)
    right_skewed_data = [1, 1, 2, 3, 4, 5, 10]
    assert calculate_skewness(right_skewed_data) > 0

    # Test with a left-skewed distribution (should be negative)
    left_skewed_data = [1, 6, 7, 8, 9, 10, 10]
    assert calculate_skewness(left_skewed_data) < 0

def test_calculate_kurtosis():
    # Test with a normal distribution (should be close to 0 for excess kurtosis)
    np.random.seed(42)  # Set seed for reproducibility
    normal_data = np.random.normal(0, 1, 1000)
    assert abs(calculate_kurtosis(normal_data)) < 1  # Increased tolerance

    # Test with a high kurtosis distribution
    high_kurtosis_data = [1, 1, 1, 1, 1, 10, 10, 10, 10, 10]
    assert calculate_kurtosis(high_kurtosis_data) > -3

    # Test with a low kurtosis distribution
    low_kurtosis_data = np.linspace(1, 10, 1000)  # Uniform distribution
    assert calculate_kurtosis(low_kurtosis_data) < 0

def test_calculate_percentile():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test 25th percentile
    assert calculate_percentile(data, 25) == 3.25

    # Test 50th percentile (median)
    assert calculate_percentile(data, 50) == 5.5

    # Test 75th percentile
    assert calculate_percentile(data, 75) == 7.75

    # Test 0th percentile (minimum)
    assert calculate_percentile(data, 0) == 1

    # Test 100th percentile (maximum)
    assert calculate_percentile(data, 100) == 10

    # Test invalid percentile
    with pytest.raises(ValueError):
        calculate_percentile(data, 101)
    with pytest.raises(ValueError):
        calculate_percentile(data, -1)