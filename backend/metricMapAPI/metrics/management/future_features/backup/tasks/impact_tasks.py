from metricMapAPI.celery_app.celery import app
from metrics.computations import (
    ab_test_analysis, detect_anomalies, detect_changepoints,
    calculate_percent_change, experiment_with_models, feedback_loop,
    difference_in_differences, instrumental_variables, train_predictive_model,
    predict_failure, stochastic_oscillator, relative_strength_index, detect_trend
)

@app.task
def trend_analysis_task(metric_id):
    # Implement logic to fetch data for the metric
    historical_data = fetch_historical_data(metric_id)
    return perform_trend_analysis(historical_data)

@app.task
def experiment_with_models_task(data, features, target, models):
    return experiment_with_models(data, features, target, models)

@app.task
def ab_test_analysis_task(data_a, data_b):
    return ab_test_analysis(data_a, data_b)

@app.task
def detect_anomalies_task(data):
    return detect_anomalies(data)

@app.task
def detect_changepoints_task(data):
    return detect_changepoints(data)

@app.task
def calculate_percent_change_task(old_value, new_value):
    return calculate_percent_change(old_value, new_value)

@app.task
def feedback_loop_task(model, new_data):
    return feedback_loop(model, new_data)

@app.task
def difference_in_differences_task(treatment_group, control_group, pre_period, post_period):
    return difference_in_differences(treatment_group, control_group, pre_period, post_period)

@app.task
def instrumental_variables_task(X, y, z):
    return instrumental_variables(X, y, z)

@app.task
def train_predictive_model_task(X_train, y_train):
    return train_predictive_model(X_train, y_train)

@app.task
def predict_failure_task(model, X):
    return predict_failure(model, X)

@app.task
def stochastic_oscillator_task(data):
    return stochastic_oscillator(data)

@app.task
def relative_strength_index_task(data):
    return relative_strength_index(data)

@app.task
def detect_trend_task(data):
    return detect_trend(data)