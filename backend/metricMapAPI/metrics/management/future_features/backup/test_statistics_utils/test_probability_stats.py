import pytest
import pandas as pd
import numpy as np
from metrics.computations.statistics_utils.probability_stats import probability_analysis

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_probability_analysis(sample_data):
    
    result = probability_analysis(sample_data.to_dict('records'), 110)
    assert 'mean' in result
    assert 'standard_deviation' in result
    assert 'target' in result
    assert 'probability_of_achieving_target' in result
    assert 0 <= result['probability_of_achieving_target'] <= 1