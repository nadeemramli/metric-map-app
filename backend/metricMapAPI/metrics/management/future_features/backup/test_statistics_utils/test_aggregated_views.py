import pytest
import pandas as pd
import numpy as np
from metrics.computations.statistics_utils.aggregated_views import calculate_aggregated_views


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_calculate_aggregated_views(sample_data):
    result = calculate_aggregated_views(sample_data.to_dict('records'))
    assert 'monthly_aggregation' in result
    assert 'yearly_aggregation' in result