import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.performance_scenario_modelling import model_performance_scenario 


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_model_performance_scenario(sample_data):
    scenario_params = {'forecast_periods': 30, 'growth_rate': 0.05}
    result = model_performance_scenario(sample_data.to_dict('records'), scenario_params)
    assert 'original_forecast' in result
    assert 'adjusted_forecast' in result