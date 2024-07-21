# tasks.py

from celery import shared_task
from .computations import TimeSeriesManager, ExperimentManager, ImpactAnalyzer, RelationshipAnalyzer, StatisticsAnalyzer, DashboardManager, DataPreprocessor, DataManager

@shared_task
def run_time_series_analysis(metric_id, analysis_type, **params):
    return TimeSeriesManager.run_analysis(metric_id, analysis_type, **params)

@shared_task
def run_experiment(experiment_id, experiment_type, **params):
    return ExperimentManager.run_analysis(experiment_id, experiment_type, **params)

@shared_task
def run_impact_analysis(metric_id, analysis_type, **params):
    return ImpactAnalyzer.run_analysis(metric_id, analysis_type, **params) 

@shared_task
def run_relationship_analysis(metric_id, analysis_type, **params):
    return RelationshipAnalyzer.run_analysis(metric_id, analysis_type, **params)

@shared_task
def run_statistics_analysis(metric_id, analysis_type, **params):
    return StatisticsAnalyzer.run_analysis(metric_id, analysis_type, **params)

@shared_task
def run_dashboard_analysis(dashboard_id, analysis_type, **params):
    return DashboardManager.run_analysis(dashboard_id, analysis_type, **params)

@shared_task
def run_data_preprocessing(metric_id, process_type, **params):
    return DataPreprocessor.run_process(metric_id, process_type, **params)

@shared_task
def run_data_management(metric_id, operation_type, **params):
    return DataManager.run_operation(metric_id, operation_type, **params)