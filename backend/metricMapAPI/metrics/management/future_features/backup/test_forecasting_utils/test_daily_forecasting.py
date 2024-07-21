import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.daily_forecasting import daily_forecast


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_daily_forecast(sample_data):
    result = daily_forecast(sample_data.to_dict('records'))
    assert len(result) == 30
