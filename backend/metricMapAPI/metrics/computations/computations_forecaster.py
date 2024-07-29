# forecasting.py

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
from prophet import Prophet
import logging

logger = logging.getLogger(__name__)

class Forecaster:
    def __init__(self, df: pd.DataFrame, metadata: dict):
        self.df = df
        self.metadata = metadata

    def sarima_forecast(self, steps: int = 30, order: Tuple[int, int, int] = (1, 1, 1), seasonal_order: Tuple[int, int, int, int] = (1, 1, 1, 12)) -> None:
         """Generate SARIMA forecast for the metric.

        Args:
            steps (int): Number of steps to forecast.
            order (Tuple[int, int, int]): The (p,d,q) order of the model for the number of AR parameters, differences, and MA parameters.
            seasonal_order (Tuple[int, int, int, int]): The (P,D,Q,s) order of the seasonal component of the model.
        """
        try:
            if self.df.empty:
                logger.warning(f"No data available for SARIMA forecast for metric {self.metric.id}")
                return
            
            ts = self.df['value']
            
            # Find optimal parameters
            auto_arima_model = auto_arima(ts, seasonal=True, m=12, suppress_warnings=True, error_action="ignore")
            order = auto_arima_model.order
            seasonal_order = auto_arima_model.seasonal_order

            model = SARIMAX(ts, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
            results = model.fit()

            forecast = results.get_forecast(steps=steps)
            forecast_mean = forecast.predicted_mean
            conf_int = forecast.conf_int()

            return pd.DataFrame({
                'forecast': forecast_mean,
                'lower_bound': conf_int.iloc[:, 0],
                'upper_bound': conf_int.iloc[:, 1]
            })
        except Exception as e:
            logger.error(f"Error generating SARIMA forecast: {str(e)}")
            return pd.DataFrame()
 
    def prophet_forecast(self, periods: int = 30) -> None:
        """Generate Prophet forecast for the metric.

        Args:
            periods (int): Number of periods to forecast.
        """
        try:
            df = self.df.reset_index().rename(columns={'date': 'ds', 'value': 'y'})
            model = Prophet()
            model.fit(df)
            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)
            
            logger.info(f"Generated and saved Prophet forecast for metric {self.metric.id}")
        except Exception as e:
            logger.error(f"Error generating Prophet forecast for metric {self.metric.id}: {str(e)}")
            raise