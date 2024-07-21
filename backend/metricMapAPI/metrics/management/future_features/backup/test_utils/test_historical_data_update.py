import pytest
import pandas as pd
import numpy as np
from metrics.computations.utils.historical_data_update import update_historical_data


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_update_historical_data(sample_data):
    new_data = pd.DataFrame({
        'date': pd.date_range(start='2024-01-01', end='2024-01-10', freq='D'),
        'value': np.random.randn(10).cumsum() + 100
    })
    result = update_historical_data(sample_data, new_data)
    assert len(result) == len(sample_data) + 10
    assert result.index.is_monotonic_increasing