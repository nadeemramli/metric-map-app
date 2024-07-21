import pytest
import pandas as pd
import numpy as np
from metrics.computations.impact_utils.ab_testing_analysis import ab_test_analysis


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_ab_test_analysis():
    data_a = np.random.normal(10, 2, 100)
    data_b = np.random.normal(11, 2, 100)
    result = ab_test_analysis(data_a, data_b)
    assert 't_statistic' in result
    assert 'p_value' in result
    assert 'mean_a' in result
    assert 'mean_b' in result