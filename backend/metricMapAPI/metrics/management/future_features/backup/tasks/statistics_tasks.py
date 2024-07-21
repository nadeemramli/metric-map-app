from metricMapAPI.celery_app.celery import app
from metrics.computations import (
    calculate_skewness, calculate_kurtosis, calculate_percentile,
    calculate_aggregated_views, mean, median, standard_deviation,
    coefficient_of_variation, standard_error, check_empty_input,
    calculate_probability, probability_analysis, simple_moving_average,
    exponential_moving_average, weighted_moving_average, anova,
    variance_decomposition
)

@app.task
def advanced_statistics_task(metric_id):
    # Implement logic to fetch data for the metric
    historical_data = fetch_historical_data(metric_id)
    return calculate_advanced_statistics(historical_data)

@app.task
def probability_analysis_task(historical_data, target_value):
    return probability_analysis(historical_data, target_value)

@app.task
def aggregated_views_task(historical_data):
    return calculate_aggregated_views(historical_data)

@app.task
def calculate_skewness_task(data):
    return calculate_skewness(data)

@app.task
def calculate_kurtosis_task(data):
    return calculate_kurtosis(data)

@app.task
def calculate_percentile_task(data, percentile):
    return calculate_percentile(data, percentile)

@app.task
def mean_task(data):
    return mean(data)

@app.task
def median_task(data):
    return median(data)

@app.task
def standard_deviation_task(data):
    return standard_deviation(data)

@app.task
def coefficient_of_variation_task(data):
    return coefficient_of_variation(data)

@app.task
def standard_error_task(data):
    return standard_error(data)

@app.task
def check_empty_input_task(data):
    return check_empty_input(data)

@app.task
def calculate_probability_task(data, event):
    return calculate_probability(data, event)

@app.task
def simple_moving_average_task(data, window):
    return simple_moving_average(data, window)

@app.task
def exponential_moving_average_task(data, span):
    return exponential_moving_average(data, span)

@app.task
def weighted_moving_average_task(data, weights):
    return weighted_moving_average(data, weights)

@app.task
def anova_task(groups):
    return anova(groups)

@app.task
def variance_decomposition_task(data):
    return variance_decomposition(data)