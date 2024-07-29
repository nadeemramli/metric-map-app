import pytest
from metrics.computations.statistics_analyzer import StatisticsAnalyzer
import pandas as pd
import numpy as np

@pytest.fixture
def sample_statistics_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'value': np.random.randint(1000, 10000, 366)
    })

def test_calculate_descriptive_stats(sample_statistics_data):
    analyzer = StatisticsAnalyzer(sample_statistics_data)
    stats = analyzer.calculate_descriptive_stats('value')
    assert 'mean' in stats
    assert 'median' in stats
    assert 'std' in stats
    assert 'min' in stats
    assert 'max' in stats

def test_perform_hypothesis_test(sample_statistics_data):
    analyzer = StatisticsAnalyzer(sample_statistics_data)
    result = analyzer.perform_hypothesis_test('value', test_type='normality')
    assert 'statistic' in result
    assert 'p_value' in result

def test_calculate_confidence_interval(sample_statistics_data):
    analyzer = StatisticsAnalyzer(sample_statistics_data)
    ci = analyzer.calculate_confidence_interval('value')
    assert len(ci) == 2
    assert ci[0] < ci[1]