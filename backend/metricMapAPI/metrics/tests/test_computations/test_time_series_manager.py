import pytest
from metrics.computations.time_series_manager import TimeSeriesManager
import pandas as pd
import numpy as np

@pytest.fixture
def sample_time_series_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'value': np.random.randint(1000, 10000, 366)
    })

def test_decompose_time_series(sample_time_series_data):
    manager = TimeSeriesManager(sample_time_series_data)
    decomposition = manager.decompose_time_series()
    assert 'trend' in decomposition
    assert 'seasonal' in decomposition
    assert 'residual' in decomposition

def test_forecast_arima(sample_time_series_data):
    manager = TimeSeriesManager(sample_time_series_data)
    forecast = manager.forecast_arima(steps=30)
    assert len(forecast) == 30

def test_detect_anomalies(sample_time_series_data):
    manager = TimeSeriesManager(sample_time_series_data)
    anomalies = manager.detect_anomalies()
    assert isinstance(anomalies, pd.Series)
    assert anomalies.dtype == bool

def test_perform_cross_correlation(sample_time_series_data):
    manager = TimeSeriesManager(sample_time_series_data)
    other_series = pd.Series(np.random.randint(100, 1000, 366))
    ccf = manager.perform_cross_correlation(other_series)
    assert isinstance(ccf, pd.Series)