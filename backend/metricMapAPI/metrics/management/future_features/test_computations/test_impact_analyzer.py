import pytest
from metrics.computations.impact_analyzer import ImpactAnalyzer
import pandas as pd
import numpy as np

@pytest.fixture
def sample_impact_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'metric1': np.random.randint(1000, 10000, 366),
        'metric2': np.random.randint(100, 1000, 366),
        'event': np.random.choice([0, 1], 366, p=[0.9, 0.1])
    })

def test_measure_impact(sample_impact_data):
    analyzer = ImpactAnalyzer(sample_impact_data)
    impact = analyzer.measure_impact('metric1', 'event')
    assert 'effect_size' in impact
    assert 'p_value' in impact

def test_calculate_roi(sample_impact_data):
    analyzer = ImpactAnalyzer(sample_impact_data)
    roi = analyzer.calculate_roi('metric1', 'metric2')
    assert isinstance(roi, float)

def test_perform_causal_inference(sample_impact_data):
    analyzer = ImpactAnalyzer(sample_impact_data)
    causal_effect = analyzer.perform_causal_inference('metric1', 'event', ['metric2'])
    assert 'ate' in causal_effect  # Average Treatment Effect