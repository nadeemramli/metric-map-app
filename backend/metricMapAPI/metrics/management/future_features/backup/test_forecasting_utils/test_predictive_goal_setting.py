import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.predictive_goal_setting import set_predictive_goal


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_set_predictive_goal(sample_data):
    result = set_predictive_goal(sample_data.to_dict('records'))
    assert 'predicted_goal' in result
    assert 'lower_bound' in result
    assert 'upper_bound' in result
    assert result['lower_bound'] < result['predicted_goal'] < result['upper_bound']
    assert isinstance(result['predicted_goal'], (int, float))
    assert isinstance(result['lower_bound'], (int, float))
    assert isinstance(result['upper_bound'], (int, float))