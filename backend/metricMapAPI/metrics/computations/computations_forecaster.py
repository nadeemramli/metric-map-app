# forecasting.py

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
from prophet import Prophet
import logging
from .data_preparation import get_prepared_data
from .feature_engineering import FeatureEngineering

logger = logging.getLogger(__name__)

class Forecaster:
    def __init__(self, metric_id: int):
        self.metric_id = metric_id
        self.df, self.metadata = get_prepared_data(metric_id)
        self.fe = FeatureEngineering(metric_id)
        self.dynamic_params = self.fe.compute_dynamic_parameters()
        self.metric = self.fe.metric

    def sarima_forecast(self, steps: int = 30):
        """Generate SARIMA forecast for the metric."""
        try:
            if self.df.empty or len(self.df) < 2:
                logger.warning(f"Insufficient data for SARIMA forecast for metric {self.metric_id}")
                return pd.DataFrame()
            
            ts = self.df['value']
            
            forecasting_model = self.dynamic_params.get('forecasting_model')
            if forecasting_model != 'sarima':
                logger.warning(f"SARIMA model not recommended for metric {self.metric_id}. Using it anyway.")
            
            seasonality_period = self.dynamic_params.get('seasonality_period', 1)
            
            auto_arima_model = auto_arima(ts, seasonal=True, m=seasonality_period, suppress_warnings=True, error_action="ignore")
            order = auto_arima_model.order
            seasonal_order = auto_arima_model.seasonal_order

            model = SARIMAX(ts, order=order, seasonal_order=seasonal_order, enforce_stationarity=False, enforce_invertibility=False)
            results = model.fit()

            forecast = results.get_forecast(steps=steps)
            forecast_mean = forecast.predicted_mean
            conf_int = forecast.conf_int()

            forecast_df = pd.DataFrame({
                'forecast': forecast_mean,
                'lower_bound': conf_int.iloc[:, 0],
                'upper_bound': conf_int.iloc[:, 1]
            })
            
            logger.info(f"Generated SARIMA forecast for metric {self.metric_id}")
            return forecast_df
        except Exception as e:
            logger.error(f"Error generating SARIMA forecast for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame()
 
    def prophet_forecast(self, periods: int = 30):
        """Generate Prophet forecast for the metric."""
        try:
            if self.df.empty or len(self.df) < 2:
                logger.warning(f"Insufficient data for Prophet forecast for metric {self.metric_id}")
                return pd.DataFrame()

            forecasting_model = self.dynamic_params.get('forecasting_model')
            if forecasting_model != 'prophet':
                logger.warning(f"Prophet model not recommended for metric {self.metric_id}. Using it anyway.")
            
            df = self.df.reset_index().rename(columns={'date': 'ds', 'value': 'y'})
            model = Prophet()
            model.fit(df)
            future = model.make_future_dataframe(periods=periods)
            forecast = model.predict(future)
            
            forecast_df = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods).rename(columns={
                'ds': 'date',
                'yhat': 'forecast',
                'yhat_lower': 'lower_bound',
                'yhat_upper': 'upper_bound'
            }).set_index('date')
            
            logger.info(f"Generated Prophet forecast for metric {self.metric_id}")
            return forecast_df
        except Exception as e:
            logger.error(f"Error generating Prophet forecast for metric {self.metric_id}: {str(e)}")
            return pd.DataFrame()