# forecasting.py

import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
from prophet import Prophet
import logging
from .data_preparation import DataPreparation
from .feature_engineering import FeatureEngineering
from django.apps import apps

logger = logging.getLogger(__name__)

class Forecaster:
    def __init__(self, metric_id: int, prepared_data=None, dynamic_params=None, engineered_features=None):
        self.metric_id = metric_id
        if prepared_data is not None:
            self.df, self.metadata = prepared_data
        else:
            Metric = apps.get_model('metrics', 'Metric')
            metric = Metric.objects.get(id=metric_id)
            data_prep = DataPreparation(metric_id, metric.tenant)
            self.df, self.metadata = data_prep.prepare_data()
        
        self.fe = FeatureEngineering(metric_id)
        self.features = engineered_features if engineered_features is not None else self.fe.engineer_features()
        self.dynamic_params = dynamic_params if dynamic_params is not None else self.fe.compute_dynamic_parameters()
        self.metric = self.get_metric()
        self.tenant = self.metric.tenant
        self.project = self.metric.project
    
    def get_metric(self):
        Metric = apps.get_model('metrics', 'Metric')
        return Metric.objects.get(id=self.metric_id)

    def forecast(self):
        sarima_results = self.sarima_forecast()
        prophet_results = self.prophet_forecast()
        return {
            'sarima': sarima_results,
            'prophet': prophet_results
        }

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