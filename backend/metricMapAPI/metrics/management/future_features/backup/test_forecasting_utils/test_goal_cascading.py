import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.goal_cascading import cascade_goals 


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_cascade_goals():
    result = cascade_goals(1000, 5)
    assert 'organization_goal' in result
    assert 'team_goals' in result
    assert len(result['team_goals']) == 5
