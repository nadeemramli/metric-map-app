import pytest
from metrics.computations.performance_analyzer import PerformanceAnalyzer
import pandas as pd
import numpy as np

@pytest.fixture
def sample_performance_data():
    return pd.DataFrame({
        'date': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'metric': np.random.randint(1000, 10000, 366)
    })

def test_calculate_kpis(sample_performance_data):
    analyzer = PerformanceAnalyzer(sample_performance_data)
    kpis = analyzer.calculate_kpis()
    assert 'average' in kpis
    assert 'median' in kpis
    assert 'std_dev' in kpis

def test_compare_periods(sample_performance_data):
    analyzer = PerformanceAnalyzer(sample_performance_data)
    comparison = analyzer.compare_periods('2020-01-01', '2020-06-30', '2020-07-01', '2020-12-31')
    assert 'period1_avg' in comparison
    assert 'period2_avg' in comparison
    assert 'percent_change' in comparison

def test_identify_trends(sample_performance_data):
    analyzer = PerformanceAnalyzer(sample_performance_data)
    trends = analyzer.identify_trends()
    assert 'overall_trend' in trends
    assert 'seasonal_patterns' in trends