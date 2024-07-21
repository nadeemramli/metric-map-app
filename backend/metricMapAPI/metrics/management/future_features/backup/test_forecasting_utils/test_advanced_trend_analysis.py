import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.advanced_trend_analysis import advanced_trend_analysis


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_advanced_trend_analysis(sample_data):
    result = advanced_trend_analysis(sample_data.to_dict('records'))
    assert 'trend' in result
    assert 'seasonal' in result
    assert 'residual' in result
    assert 'SMA' in result
    assert 'EMA' in result
    assert 'forecast' in result