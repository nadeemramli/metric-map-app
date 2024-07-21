import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.forecast_vs_actual import forecast_vs_actual_comparison


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_forecast_vs_actual_comparison(sample_data):
    forecast_data = sample_data.copy()
    forecast_data['value'] += np.random.randn(len(forecast_data)) * 10
    result = forecast_vs_actual_comparison(sample_data.to_dict('records'), forecast_data.to_dict('records'))
    assert 'value_actual' in result
    assert 'value_forecast' in result
    assert 'difference' in result
    assert 'percent_difference' in result