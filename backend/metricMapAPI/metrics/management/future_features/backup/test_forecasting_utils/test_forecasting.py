import pytest
import numpy as np
import pandas as pd
from metrics.computations.forecasting_utils.forecasting import train_forecast_model, plot_forecast

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2020-01-01', end='2021-12-31', freq='D')
    values = [i + np.random.randn() * 10 for i in range(len(dates))]
    df = pd.DataFrame({'ds': dates, 'y': values})
    return df

def test_train_forecast_model(sample_data):
    model, forecast = train_forecast_model(sample_data, periods=30)
    
    assert hasattr(model, 'predict')
    assert isinstance(forecast, pd.DataFrame)
    assert len(forecast) == len(sample_data) + 30
    assert 'yhat' in forecast.columns

def test_plot_forecast(sample_data):
    model, forecast = train_forecast_model(sample_data, periods=30)
    fig = plot_forecast(model, forecast)
    
    assert fig is not None
    assert hasattr(fig, 'axes')