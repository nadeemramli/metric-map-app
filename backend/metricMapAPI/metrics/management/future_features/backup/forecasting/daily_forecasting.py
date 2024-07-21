"""
This module provides functionality for performing daily forecasting on time-series data using the ARIMA model,
which is suitable for a wide range of time-series data applications, especially for relatively stable historical patterns.
"""
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def daily_forecast(historical_data, forecast_days=30):
    """
    Functions:
    daily_forecast(historical_data, forecast_days=30): Generates a forecast for the specified number of days using
        ARIMA model based on provided historical data.
    """
    df = pd.DataFrame(historical_data)
    df.set_index('date', inplace=True)
    
    model = ARIMA(df['value'], order=(1,1,1))
    results = model.fit()
    forecast = results.forecast(steps=forecast_days)
    
    return forecast.to_dict()

"""
Example:
    >>> historical_data = {
        'date': pd.date_range(start='2021-01-01', periods=365, freq='D'),
        'value': np.random.normal(100, 10, 365)
    }
    >>> forecast = daily_forecast(historical_data, forecast_days=30)
    >>> print(forecast)

Notes:
    - Input data should be a dictionary with 'date' and 'value' keys, where 'date' is converted into a datetime index.
    - The function returns a dictionary representing the forecasted values for the upcoming days.
    - The ARIMA model parameters are set to (1,1,1) by default, but these may need to be adjusted based on specific
      characteristics of the data.
    - Pandas is used for data manipulation, particularly for setting datetime indices, and statsmodels is used for
      the ARIMA model implementation.
"""