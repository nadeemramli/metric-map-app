import pytest
from unittest.mock import Mock, patch
from metrics.tasks import (
    run_time_series_analysis,
    run_experiment,
    run_impact_analysis,
    run_relationship_analysis,
    run_statistics_analysis,
    run_dashboard_analysis,
    run_data_preprocessing,
    run_data_management
)
import numpy as np
import pandas as pd

@pytest.fixture
def sample_metric_data():
    dates = pd.date_range(start='1/1/2020', periods=100)
    values = np.cumsum(np.random.randn(100)) + 100
    return pd.DataFrame({'date': dates, 'value': values}).to_dict('records')

@pytest.fixture
def sample_experiment_data():
    return {
        'control': np.random.randn(100).tolist(),
        'variant': np.random.randn(100).tolist()
    }

@pytest.fixture
def mock_time_series_manager(monkeypatch):
    mock = Mock()
    mock.run_analysis.return_value = {'forecast': [1, 2, 3]}
    monkeypatch.setattr('metrics.computations.TimeSeriesManager', mock)
    return mock

@pytest.fixture
def mock_experiment_manager(monkeypatch):
    mock = Mock()
    mock.run_analysis.return_value = {'p_value': 0.05}
    monkeypatch.setattr('metrics.computations.ExperimentManager', mock)
    return mock

@pytest.fixture
def mock_impact_analyzer(monkeypatch):
    mock = Mock()
    mock.run_analysis.return_value = {'impact': 0.1}
    monkeypatch.setattr('metrics.computations.ImpactAnalyzer', mock)
    return mock

@pytest.fixture
def mock_relationship_analyzer(monkeypatch):
    mock = Mock()
    mock.run_analysis.return_value = {'correlation': 0.7}
    monkeypatch.setattr('metrics.computations.RelationshipAnalyzer', mock)
    return mock

@pytest.fixture
def mock_statistics_analyzer(monkeypatch):
    mock = Mock()
    mock.run_analysis.return_value = {'mean': 5.0}
    monkeypatch.setattr('metrics.computations.StatisticsAnalyzer', mock)
    return mock

@pytest.fixture
def mock_dashboard_manager(monkeypatch):
    mock = Mock()
    mock.run_analysis.return_value = {'kpis': {'revenue': 1000}}
    monkeypatch.setattr('metrics.computations.DashboardManager', mock)
    return mock

@pytest.fixture
def mock_data_preprocessor(monkeypatch):
    mock = Mock()
    mock.run_process.return_value = {'processed_data': [1, 2, 3]}
    monkeypatch.setattr('metrics.computations.DataPreprocessor', mock)
    return mock

@pytest.fixture
def mock_data_manager(monkeypatch):
    mock = Mock()
    mock.run_operation.return_value = {'status': 'success'}
    monkeypatch.setattr('metrics.computations.DataManager', mock)
    return mock

def test_run_time_series_analysis(sample_metric_data, mock_time_series_manager):
    result = run_time_series_analysis.delay(1, 'forecasting', data=sample_metric_data)
    assert result.successful()
    analysis_result = result.get()
    assert 'forecast' in analysis_result
    mock_time_series_manager.run_analysis.assert_called_once_with(1, 'forecasting', data=sample_metric_data)

def test_run_experiment(sample_experiment_data, mock_experiment_manager):
    result = run_experiment.delay(1, 'ab_test', data=sample_experiment_data)
    assert result.successful()
    experiment_result = result.get()
    assert 'p_value' in experiment_result
    mock_experiment_manager.run_analysis.assert_called_once_with(1, 'ab_test', data=sample_experiment_data)

def test_run_impact_analysis(sample_metric_data, mock_impact_analyzer):
    result = run_impact_analysis.delay(1, 'causal_impact', data=sample_metric_data)
    assert result.successful()
    impact_result = result.get()
    assert 'impact' in impact_result
    mock_impact_analyzer.run_analysis.assert_called_once_with(1, 'causal_impact', data=sample_metric_data)

def test_run_relationship_analysis(sample_metric_data, mock_relationship_analyzer):
    result = run_relationship_analysis.delay(1, 'correlation', data=sample_metric_data)
    assert result.successful()
    relationship_result = result.get()
    assert 'correlation' in relationship_result
    mock_relationship_analyzer.run_analysis.assert_called_once_with(1, 'correlation', data=sample_metric_data)

def test_run_statistics_analysis(sample_metric_data, mock_statistics_analyzer):
    result = run_statistics_analysis.delay(1, 'descriptive', data=sample_metric_data)
    assert result.successful()
    stats_result = result.get()
    assert 'mean' in stats_result
    mock_statistics_analyzer.run_analysis.assert_called_once_with(1, 'descriptive', data=sample_metric_data)

def test_run_dashboard_analysis(sample_metric_data, mock_dashboard_manager):
    result = run_dashboard_analysis.delay(1, 'performance', data=sample_metric_data)
    assert result.successful()
    dashboard_result = result.get()
    assert 'kpis' in dashboard_result
    mock_dashboard_manager.run_analysis.assert_called_once_with(1, 'performance', data=sample_metric_data)

def test_run_data_preprocessing(sample_metric_data, mock_data_preprocessor):
    result = run_data_preprocessing.delay(1, 'normalize', data=sample_metric_data)
    assert result.successful()
    preprocessing_result = result.get()
    assert 'processed_data' in preprocessing_result
    mock_data_preprocessor.run_process.assert_called_once_with(1, 'normalize', data=sample_metric_data)

def test_run_data_management(sample_metric_data, mock_data_manager):
    result = run_data_management.delay(1, 'update', data=sample_metric_data)
    assert result.successful()
    management_result = result.get()
    assert 'status' in management_result
    mock_data_manager.run_operation.assert_called_once_with(1, 'update', data=sample_metric_data)