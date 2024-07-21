"""
This module provides advanced tools for trend analysis in time series data, including seasonal decomposition,
simple moving averages (SMA), exponential moving averages (EMA), and forecasting with Exponential Smoothing.
"""
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def advanced_trend_analysis(historical_data, forecast_periods=30):
    """
    Functions:
    advanced_trend_analysis(historical_data, forecast_periods=30): Performs comprehensive trend analysis on
        historical data and generates forecasts for the specified number of future periods.
    """
    df = pd.DataFrame(historical_data)
    df.set_index('date', inplace=True)

    # Seasonal Decomposition
    decomposition = seasonal_decompose(df['value'], model='additive', period=30)

    # Moving Averages
    df['SMA'] = df['value'].rolling(window=7).mean()
    df['EMA'] = df['value'].ewm(span=7, adjust=False).mean()

    # Exponential Smoothing for Forecasting
    model = ExponentialSmoothing(df['value'], trend='add', seasonal='add', seasonal_periods=30)
    fitted_model = model.fit()
    forecast = fitted_model.forecast(forecast_periods)

    return {
        'trend': decomposition.trend.to_dict(),
        'seasonal': decomposition.seasonal.to_dict(),
        'residual': decomposition.resid.to_dict(),
        'SMA': df['SMA'].to_dict(),
        'EMA': df['EMA'].to_dict(),
        'forecast': forecast.to_dict()
    }

"""
Example:
    >>> historical_data = {
        'date': pd.date_range(start='2021-01-01', periods=365, freq='D'),
        'value': np.random.normal(100, 10, 365)
    }
    >>> results = advanced_trend_analysis(historical_data)
    >>> print(results)

Notes:
    - Input data should be a dictionary with 'date' and 'value' keys, where 'date' is converted into a datetime index.
    - The function uses `seasonal_decompose` from `statsmodels.tsa` for decomposition and `ExponentialSmoothing` for
      forecasting.
    - Outputs include dictionaries for trend, seasonal, and residual components from the decomposition, as well as
      SMA, EMA, and forecast values.
    - This module is ideal for analyzing data with potential seasonal effects and underlying trends.
"""