import pytest
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from metrics.computations.utils.scenario_simulation import simulate_scenario

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_simulate_scenario(sample_data):
    scenario_params = {
        'growth_rate': 0.05,
        'noise_level': 0.1,
        'seasonality': 5
    }
    result = simulate_scenario(sample_data, scenario_params)
    assert len(result) == len(sample_data)
    assert 'value' in result.columns
    assert not result['value'].equals(sample_data['value'])