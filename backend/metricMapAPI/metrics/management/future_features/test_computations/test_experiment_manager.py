import pytest
from metrics.computations.experiment_manager import ExperimentManager
import pandas as pd
import numpy as np

@pytest.fixture
def sample_experiment_data():
    return {
        'control': pd.DataFrame({
            'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
            'value': np.random.randint(1000, 10000, 366)
        }),
        'variant': pd.DataFrame({
            'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
            'value': np.random.randint(1000, 10000, 366)
        })
    }

def test_run_ab_test(sample_experiment_data):
    manager = ExperimentManager()
    result = manager.run_ab_test(sample_experiment_data['control'], sample_experiment_data['variant'])
    assert 'p_value' in result
    assert 'effect_size' in result

def test_calculate_sample_size():
    manager = ExperimentManager()
    sample_size = manager.calculate_sample_size(effect_size=0.1, alpha=0.05, power=0.8)
    assert isinstance(sample_size, int)
    assert sample_size > 0

def test_check_statistical_significance(sample_experiment_data):
    manager = ExperimentManager()
    is_significant = manager.check_statistical_significance(
        sample_experiment_data['control']['value'],
        sample_experiment_data['variant']['value']
    )
    assert isinstance(is_significant, bool)