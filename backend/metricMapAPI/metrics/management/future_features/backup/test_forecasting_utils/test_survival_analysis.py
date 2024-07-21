import pytest
import pandas as pd
from metrics.computations.forecasting_utils.survival_analysis import fit_kaplan_meier, plot_survival_function

@pytest.fixture
def sample_data():
    data = pd.DataFrame({
        'duration': [5, 6, 2, 4, 9, 8, 7, 4, 5, 2],
        'event': [1, 1, 0, 1, 1, 1, 1, 0, 1, 0]
    })
    return data

def test_fit_kaplan_meier(sample_data):
    kmf = fit_kaplan_meier(sample_data, 'duration', 'event')
    assert hasattr(kmf, 'survival_function_')
    assert hasattr(kmf, 'confidence_interval_')

def test_plot_survival_function(sample_data):
    kmf = fit_kaplan_meier(sample_data, 'duration', 'event')
    fig = plot_survival_function(kmf)
    assert fig is not None
    assert hasattr(fig, 'axes')