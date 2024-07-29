import pytest
from metrics.computations.relationship_analyzer import RelationshipAnalyzer
import pandas as pd
import numpy as np

@pytest.fixture
def sample_relationship_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'metric1': np.random.randint(1000, 10000, 366),
        'metric2': np.random.randint(100, 1000, 366),
        'metric3': np.random.uniform(0.1, 0.9, 366)
    })

def test_calculate_correlation(sample_relationship_data):
    analyzer = RelationshipAnalyzer(sample_relationship_data)
    correlation = analyzer.calculate_correlation('metric1', 'metric2')
    assert -1 <= correlation <= 1

def test_perform_regression(sample_relationship_data):
    analyzer = RelationshipAnalyzer(sample_relationship_data)
    regression = analyzer.perform_regression('metric1', ['metric2', 'metric3'])
    assert 'r_squared' in regression
    assert 'coefficients' in regression

def test_detect_multicollinearity(sample_relationship_data):
    analyzer = RelationshipAnalyzer(sample_relationship_data)
    multicollinearity = analyzer.detect_multicollinearity(['metric1', 'metric2', 'metric3'])
    assert isinstance(multicollinearity, dict)
    assert all(0 <= vif <= 10 for vif in multicollinearity.values())