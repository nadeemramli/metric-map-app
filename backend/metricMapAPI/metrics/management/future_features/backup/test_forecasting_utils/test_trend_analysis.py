import pytest
import pandas as pd
import numpy as np
from metrics.computations.impact_utils.trend_analysis import detect_trend, decompose_time_series

@pytest.fixture
def sample_data():
    date_rng = pd.date_range(start='2020-01-01', end='2021-12-31', freq='D')
    data = pd.Series(np.arange(len(date_rng)) * 0.1 + np.random.randn(len(date_rng)) * 0.01, index=date_rng)
    return data

def test_detect_trend(sample_data):
    trend = detect_trend(sample_data)
    assert isinstance(trend, pd.Series)
    assert len(trend) > 0  # Ensure we have some trend data
    assert len(trend) <= len(sample_data)  # The trend might be shorter due to NaN removal
    assert not trend.isnull().any()  # Ensure no NaN values in the trend
    assert trend.std() < sample_data.std()  # Trend should be smoother than original data

def test_decompose_time_series(sample_data):
    trend, seasonal, residual = decompose_time_series(sample_data)
    assert isinstance(trend, pd.Series)
    assert isinstance(seasonal, pd.Series)
    assert isinstance(residual, pd.Series)
    assert len(trend) == len(sample_data)
    assert len(seasonal) == len(sample_data)
    assert len(residual) == len(sample_data)