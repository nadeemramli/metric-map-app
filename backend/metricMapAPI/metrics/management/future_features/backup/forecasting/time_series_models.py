"""
This module contains functions for time series modeling using various methods.
"""
import numpy  as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX

def decompose_time_series(data, model='multiplicative', freq=None):
    """
    Decompose time series into trend, seasonal, and residual components.

    Parameters:
        data (pd.Series): Time series data.
        model (str): Type of decomposition ('additive' or 'multiplicative').
        freq (int): Frequency of the time series.

    Returns:
        tuple: Trend, seasonal, and residual components of the time series.
    """
    result = seasonal_decompose(data, model=model, period=freq)
    return result.trend, result.seasonal, result.resid

def sarima_forecast(data, order, seasonal_order):
    """
    Perform SARIMA forecasting.

    Parameters:
        data (pd.Series): Time series data.
        order (tuple): ARIMA order (p, d, q).
        seasonal_order (tuple): Seasonal order (P, D, Q, s).

    Returns:
        pd.Series: Forecasted values.
    """
    model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit(disp=False)
    forecast = model_fit.forecast(steps=len(data))
    return forecast

def lstm_forecast(data, look_back):
    """
    Perform LSTM forecasting.

    Parameters:
        data (pd.Series): Time series data.
        look_back (int): Number of past time steps to use as input features.

    Returns:
        Sequential: Trained LSTM model.
    """
    # Prepare the data
    X, y = [], []
    for i in range(len(data) - look_back - 1):
        X.append(data[i:(i + look_back), 0])
        y.append(data[i + look_back, 0])
    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    # Build the LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Train the model
    model.fit(X, y, epochs=20, batch_size=1, verbose=2)
    return model

# Ensure tensorflow and statsmodels are installed and available for import.
