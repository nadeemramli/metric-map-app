import pytest
from metrics.computations.dashboard_manager import DashboardManager
import pandas as pd
import numpy as np

@pytest.fixture
def sample_dashboard_data():
    return {
        'metrics': ['revenue', 'users', 'conversion_rate'],
        'date_range': pd.date_range(start='1/1/2020', end='1/1/2021', freq='D'),
        'values': {
            'revenue': np.random.randint(1000, 10000, 366),
            'users': np.random.randint(100, 1000, 366),
            'conversion_rate': np.random.uniform(0.01, 0.1, 366)
        }
    }

def test_create_dashboard(sample_dashboard_data):
    manager = DashboardManager(sample_dashboard_data)
    dashboard = manager.create_dashboard()
    assert 'revenue' in dashboard
    assert 'users' in dashboard
    assert 'conversion_rate' in dashboard

def test_generate_summary(sample_dashboard_data):
    manager = DashboardManager(sample_dashboard_data)
    summary = manager.generate_summary()
    assert 'revenue' in summary
    assert 'total' in summary['revenue']
    assert 'average' in summary['revenue']

def test_detect_anomalies(sample_dashboard_data):
    manager = DashboardManager(sample_dashboard_data)
    anomalies = manager.detect_anomalies()
    assert 'revenue' in anomalies
    assert 'users' in anomalies
    assert 'conversion_rate' in anomalies

def test_generate_insights(sample_dashboard_data):
    manager = DashboardManager(sample_dashboard_data)
    insights = manager.generate_insights()
    assert len(insights) > 0
    assert all(isinstance(insight, str) for insight in insights)