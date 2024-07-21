from metricMapAPI.celery_app.celery import app
from metrics.computations import (
    generate_automated_suggestions, generate_custom_visualization,
    detect_outliers, log_transform, box_cox_transform,
    decision_support_dashboard, update_historical_data,
    calculate_performance_metrics, simulate_scenario,
    handle_missing_values, normalize_data
)

@app.task
def import_historical_data_task(metric_id, data):
    # Implement logic to import historical data
    pass

@app.task
def historical_data_update_task(existing_data, new_data):
    return update_historical_data(existing_data, new_data)

@app.task
def automated_suggestion_task(historical_data):
    return generate_automated_suggestions(historical_data)

@app.task
def decision_support_dashboard_task(historical_data, forecast_periods=30):
    return decision_support_dashboard(historical_data, forecast_periods)

@app.task
def custom_visualization_task(data, chart_type='line'):
    return generate_custom_visualization(data, chart_type)

@app.task
def performance_dashboard_task(historical_data, current_date):
    return calculate_performance_metrics(historical_data, current_date)

@app.task
def detect_outliers_task(data):
    return detect_outliers(data)

@app.task
def log_transform_task(data):
    return log_transform(data)

@app.task
def box_cox_transform_task(data):
    return box_cox_transform(data)

@app.task
def handle_missing_values_task(data):
    return handle_missing_values(data)

@app.task
def normalize_data_task(data):
    return normalize_data(data)

@app.task
def simulate_scenario_task(base_data, scenario_params):
    return simulate_scenario(base_data, scenario_params)