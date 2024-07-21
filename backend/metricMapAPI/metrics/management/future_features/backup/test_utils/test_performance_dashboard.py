import pytest
import pandas as pd
import numpy as np
from metrics.computations.utils.performance_dashboard import calculate_performance_metrics


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_calculate_performance_metrics(sample_data):
    result = calculate_performance_metrics(sample_data.to_dict('records'), '2023-12-31')
    assert 'lifetime' in result
    assert 'last_7_days' in result
    assert 'last_14_days' in result
    assert 'last_30_days' in result
    assert 'this_week' in result
    assert 'last_week' in result
    assert 'this_month' in result
    assert 'last_month' in result
    assert 'wow_change' in result
    assert 'mom_change' in result