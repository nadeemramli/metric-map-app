import pytest
import pandas as pd
import numpy as np
from metrics.computations.utils.decision_support_dashboard import decision_support_dashboard


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_decision_support_dashboard(sample_data):
    result = decision_support_dashboard(sample_data.to_dict('records'))
    assert 'real_time_data' in result
    assert 'predictive_insights' in result