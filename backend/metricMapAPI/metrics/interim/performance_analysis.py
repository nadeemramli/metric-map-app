from .utils import cache_result, get_dataframe_from_historical_data
from django.apps import apps
import pandas as pd
import numpy as np
from scipy import stats

@cache_result()
def forecast_vs_actual_comparison(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    Forecast = apps.get_model('metrics', 'Forecast')
    forecasts = Forecast.objects.filter(metric_id=metric_id)
    
    comparison = []
    for forecast in forecasts:
        actual = df[df['date'] == forecast.forecast_date]['value'].values[0] if not df[df['date'] == forecast.forecast_date].empty else None
        comparison.append({
            'date': forecast.forecast_date,
            'forecast': forecast.forecast_value,
            'actual': actual,
            'difference': actual - forecast.forecast_value if actual is not None else None
        })
    
    return comparison

@cache_result()
def probability_analysis(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    MetricTarget = apps.get_model('metrics', 'MetricTarget')
    target = MetricTarget.objects.filter(metric_id=metric_id).order_by('-target_date').first()
    
    if not target:
        return {"error": "No target set for this metric"}
    
    # Assuming we're using a simple normal distribution for probability
    mean = df['value'].mean()
    std = df['value'].std()
    z_score = (target.target_value - mean) / std
    probability = 1 - stats.norm.cdf(z_score)
    
    return {
        "target_value": target.target_value,
        "target_date": target.target_date,
        "probability_of_achieving": probability
    }

@cache_result()
def process_progress_tracking(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    Forecast = apps.get_model('metrics', 'Forecast')
    latest_forecast = Forecast.objects.filter(metric_id=metric_id).order_by('-forecast_date').first()
    
    if not latest_forecast:
        return {"error": "No forecast available for this metric"}
    
    actual_latest = df['value'].iloc[-1]
    progress_percentage = (actual_latest / latest_forecast.forecast_value) * 100
    days_left = (latest_forecast.forecast_date - df['date'].iloc[-1]).days
    
    return {
        "current_value": actual_latest,
        "forecast_value": latest_forecast.forecast_value,
        "progress_percentage": progress_percentage,
        "days_left": days_left
    }
