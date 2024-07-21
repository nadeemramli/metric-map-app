import pytest
import pandas as pd
import numpy as np
import tensorflow as tf
from metrics.computations.forecasting_utils.time_series_models import decompose_time_series, sarima_forecast, lstm_forecast

@pytest.fixture
def sample_data():
    np.random.seed(42)
    date_rng = pd.date_range(start='2020-01-01', end='2021-12-31', freq='D')
    data = pd.Series(np.random.randn(len(date_rng)), index=date_rng)
    return data

def test_decompose_time_series(sample_data):
    trend, seasonal, residual = decompose_time_series(sample_data, model='additive', freq=365)
    assert len(trend) == len(sample_data)
    assert len(seasonal) == len(sample_data)
    assert len(residual) == len(sample_data)

def test_sarima_forecast(sample_data):
    order = (1, 1, 1)
    seasonal_order = (1, 1, 1, 12)
    forecast = sarima_forecast(sample_data, order, seasonal_order)
    assert len(forecast) == len(sample_data)
    assert isinstance(forecast, pd.Series)

def test_lstm_forecast(sample_data):
    look_back = 10
    model = lstm_forecast(sample_data.values.reshape(-1, 1), look_back)
    assert isinstance(model, tf.keras.models.Sequential)
    assert len(model.layers) > 0