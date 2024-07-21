from metrics.computations.forecasting_utils import *
from metrics.computations.impact_utils import *
from metrics.computations.relationships_utils import *
from metrics.computations.statistics_utils import *
from metrics.computations.utils import *

def test_forecasting_imports():
    assert callable(advanced_trend_analysis)
    assert callable(train_classifier)
    assert callable(evaluate_classifier)
    assert callable(daily_forecast)
    assert callable(train_ensemble_model)
    assert callable(evaluate_ensemble_model)
    assert callable(forecast_vs_actual_comparison)
    assert callable(train_forecast_model)
    assert callable(plot_forecast)
    assert callable(cascade_goals)
    assert callable(model_performance_scenario)
    assert callable(set_predictive_goal)
    assert callable(calculate_progress)
    assert callable(process_progress_tracking)
    assert callable(train_regression_model)
    assert callable(evaluate_regression_model)
    assert callable(fit_kaplan_meier)
    assert callable(plot_survival_function)
    assert callable(decompose_time_series)
    assert callable(sarima_forecast)
    assert callable(lstm_forecast)

def test_impact_imports():
    assert callable(ab_test_analysis)
    assert callable(detect_anomalies)
    assert callable(detect_changepoints)
    assert callable(calculate_percent_change)
    assert callable(experiment_with_models)
    assert callable(feedback_loop)
    assert callable(difference_in_differences)
    assert callable(instrumental_variables)
    assert callable(train_predictive_model)
    assert callable(predict_failure)
    assert callable(stochastic_oscillator)
    assert callable(relative_strength_index)
    assert callable(detect_trend)
    assert callable(decompose_time_series)

def test_relationships_imports():
    assert callable(lagged_correlation_test)
    assert callable(pearsonr)
    assert callable(kmeans_clustering)
    assert callable(pearson_correlation)
    assert callable(spearman_correlation)
    assert callable(build_metric_network)
    assert callable(centrality_measures)
    assert callable(recommend_items)
    
def test_statistics_imports():
    assert callable(calculate_skewness)
    assert callable(calculate_kurtosis)
    assert callable(calculate_percentile)
    assert callable(calculate_aggregated_views)
    assert callable(mean)
    assert callable(median)
    assert callable(standard_deviation)
    assert callable(coefficient_of_variation)
    assert callable(standard_error)
    assert callable(check_empty_input)
    assert callable(calculate_probability)
    assert callable(probability_analysis)
    assert callable(simple_moving_average)
    assert callable(exponential_moving_average)
    assert callable(weighted_moving_average)
    assert callable(anova)
    assert callable(variance_decomposition)

def test_utils_imports():
    assert callable(generate_automated_suggestions)
    assert callable(generate_custom_visualization)
    assert callable(detect_outliers)
    assert callable(log_transform)
    assert callable(box_cox_transform)
    assert callable(decision_support_dashboard)
    assert callable(update_historical_data)
    assert callable(calculate_performance_metrics)
    assert callable(simulate_scenario)
    assert callable(handle_missing_values)
    assert callable(normalize_data)