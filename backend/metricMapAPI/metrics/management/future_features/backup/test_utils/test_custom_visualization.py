import pytest
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
from metrics.computations.utils.custom_visualization import generate_custom_visualization

@pytest.fixture
def sample_data():
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    return pd.DataFrame({'date': dates, 'value': values})

def test_generate_custom_visualization(sample_data):
    result = generate_custom_visualization(sample_data)
    assert isinstance(result, str)
    assert len(result) > 0
    assert result.startswith('iVBORw0KGgo')  # This is how a base64 encoded PNG typically starts