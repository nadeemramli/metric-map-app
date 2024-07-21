import pytest
import pandas as pd
import numpy as np
from metrics.computations.utils.automated_suggestions import generate_automated_suggestions


@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_generate_automated_suggestions(sample_data):
    result = generate_automated_suggestions(sample_data.to_dict('records'))
    assert isinstance(result, list)
    assert all(isinstance(suggestion, str) for suggestion in result)