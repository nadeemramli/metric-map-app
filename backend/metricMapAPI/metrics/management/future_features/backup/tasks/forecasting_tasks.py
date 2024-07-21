from metricMapAPI.celery_app.celery import app
from metrics.computations.forecasting_utils.time_series_manager.py import TimeSeriesManager

@app.task
def run_forecast_task(metric_id: int, forecast_type: str, periods: int):
    result = TimeSeriesManager.run_forecast(metric_id, forecast_type, periods)
    return result.to_json()

@app.task
def run_analysis_task(metric_id: int, analysis_type: str):
    result = TimeSeriesManager.run_analysis(metric_id, analysis_type)
    return result.to_json()