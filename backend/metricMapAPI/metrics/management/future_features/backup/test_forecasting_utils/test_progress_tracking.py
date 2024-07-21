import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.progress_tracking import calculate_progress, process_progress_tracking

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_calculate_progress():
    result = calculate_progress(75, 100, 50)
    assert 0 <= result <= 100
