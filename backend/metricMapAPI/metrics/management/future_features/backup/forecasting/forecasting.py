"""
This module contains functions for time series forecasting.
"""

import pandas as pd
from prophet import Prophet

def train_forecast_model(data, periods):
    """
    Train a Prophet forecast model.

    Parameters:
        data (pd.DataFrame): Time series data with 'ds' and 'y' columns.
        periods (int): Number of periods to forecast.

    Returns:
        model: Trained Prophet model.
    """
    model = Prophet()
    model.fit(data)
    
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return model, forecast

def plot_forecast(model, forecast):
    """
    Plot the forecast results.

    Parameters:
        model (Prophet): Trained Prophet model.
        forecast (pd.DataFrame): Forecasted data.

    Returns:
        None
    """
    fig = model.plot(forecast)
    return fig

# Ensure fbprophet is installed and available for import.
