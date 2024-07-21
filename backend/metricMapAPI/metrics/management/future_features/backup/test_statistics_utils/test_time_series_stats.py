import pytest
import pandas as pd
import numpy as np
from metrics.computations.statistics_utils.time_series_stats import simple_moving_average, exponential_moving_average, weighted_moving_average

@pytest.fixture
def sample_data():
    return pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def test_simple_moving_average(sample_data):
    result = simple_moving_average(sample_data, window=3)
    assert len(result) == len(sample_data)
    assert pd.isna(result.iloc[0])
    assert pd.isna(result.iloc[1])
    assert result.iloc[2] == 2.0
    assert result.iloc[-1] == 9.0

def test_exponential_moving_average(sample_data):
    result = exponential_moving_average(sample_data, span=3)
    assert len(result) == len(sample_data)
    assert result.iloc[0] == 1.0
    assert result.iloc[-1] > result.iloc[0]

def test_weighted_moving_average(sample_data):
    weights = [0.1, 0.2, 0.7]
    result = weighted_moving_average(sample_data, weights)
    
    # Print out the results for inspection
    print("\nWeighted Moving Average Results:")
    for i, val in enumerate(result):
        print(f"Index {i}: {val}")
    
    assert len(result) == len(sample_data)
    assert pd.isna(result.iloc[0])
    assert pd.isna(result.iloc[1])
    
    # We'll update these assertions after seeing the actual output
    assert np.isclose(result.iloc[2], 2.60, atol=1e-2)
    assert np.isclose(result.iloc[3], 3.60, atol=1e-2)
    assert np.isclose(result.iloc[4], 4.60, atol=1e-2)
    assert np.isclose(result.iloc[5], 5.60, atol=1e-2)
    assert np.isclose(result.iloc[-1], 9.60, atol=1e-2)