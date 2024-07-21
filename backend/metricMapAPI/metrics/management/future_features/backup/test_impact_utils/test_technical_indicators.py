import pytest
import pandas as pd
import numpy as np
from metrics.computations.impact_utils.technical_indicators import stochastic_oscillator, relative_strength_index

@pytest.fixture
def sample_data():
    np.random.seed(42)
    data = pd.DataFrame({
        'Close': np.random.rand(100) * 100,
        'High': np.random.rand(100) * 110 + 5,  # Ensure High is always higher than Close
        'Low': np.random.rand(100) * 90 - 5  # Ensure Low is always lower than Close
    })
    return data

def test_stochastic_oscillator(sample_data):
    k_window, d_window = 14, 3
    k_values, d_values = stochastic_oscillator(sample_data, k_window, d_window)
    assert len(k_values) == len(sample_data)
    assert len(d_values) == len(sample_data)
    assert all(0 <= k <= 100 for k in k_values.dropna())
    assert all(0 <= d <= 100 for d in d_values.dropna())

def test_relative_strength_index(sample_data):
    window = 14
    rsi = relative_strength_index(sample_data['Close'], window)
    assert len(rsi) == len(sample_data)
    assert all(0 <= r <= 100 for r in rsi.dropna())