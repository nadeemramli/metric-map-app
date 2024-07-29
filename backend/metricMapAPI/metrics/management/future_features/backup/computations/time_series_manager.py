# time_series_manager.py

import pandas as pd
import numpy as np
from typing import List, Dict, Union, Any
import json
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)

class TimeSeriesData:
    def __init__(self, metric_id: int, data: List[Dict[str, Union[str, float]]]):
        self.metric_id = metric_id
        self.data = pd.DataFrame(data)
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data.set_index('date', inplace=True)

class AnalysisResult:
    def __init__(self, metric_id: int, analysis_type: str, result: Dict[str, Any]):
        self.metric_id = metric_id
        self.analysis_type = analysis_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'metric_id': self.metric_id,
            'analysis_type': self.analysis_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class TimeSeriesManager:
    def __init__(self, data: TimeSeriesData):
        self.data = data

    def decompose(self) -> AnalysisResult:
        result = seasonal_decompose(self.data.data['value'], model='additive', period=30)
        return AnalysisResult(
            self.data.metric_id,
            'decomposition',
            {
                'trend': result.trend,
                'seasonal': result.seasonal,
                'residual': result.resid
            }
        )

    def detect_anomalies(self) -> AnalysisResult:
        mean = self.data.data['value'].mean()
        std = self.data.data['value'].std()
        threshold = 3
        anomalies = self.data.data[abs(self.data.data['value'] - mean) > threshold * std]
        return AnalysisResult(
            self.data.metric_id,
            'anomaly_detection',
            {
                'anomalies': anomalies
            }
        )

    def analyze_trend(self) -> AnalysisResult:
        trend = self.data.data['value'].rolling(window=7).mean()
        return AnalysisResult(
            self.data.metric_id,
            'trend_analysis',
            {
                'trend': trend
            }
        )

    def arima_forecast(self, periods: int) -> AnalysisResult:
        model = ARIMA(self.data.data['value'], order=(1,1,1))
        results = model.fit()
        forecast = results.forecast(steps=periods)
        return AnalysisResult(
            self.data.metric_id,
            'arima_forecast',
            {
                'forecast': forecast
            }
        )

    def prophet_forecast(self, periods: int) -> AnalysisResult:
        df = self.data.data.reset_index().rename(columns={'date': 'ds', 'value': 'y'})
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=periods)
        forecast = model.predict(future)
        return AnalysisResult(
            self.data.metric_id,
            'prophet_forecast',
            {
                'forecast': forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
            }
        )

    def lstm_forecast(self, periods: int) -> AnalysisResult:
        values = self.data.data['value'].values.reshape(-1, 1)
        model = Sequential([
            LSTM(50, activation='relu', input_shape=(1, 1)),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mse')
        model.fit(values[:-1], values[1:], epochs=200, verbose=0)
        
        last_value = values[-1]
        forecast = []
        for _ in range(periods):
            pred = model.predict(last_value.reshape(1, 1, 1))
            forecast.append(pred[0, 0])
            last_value = pred
        
        return AnalysisResult(
            self.data.metric_id,
            'lstm_forecast',
            {
                'forecast': forecast
            }
        )

    @staticmethod
    def get_historical_data(metric_id: int) -> TimeSeriesData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy TimeSeriesData object
        dummy_data = [
            {'date': '2023-01-01', 'value': 100},
            {'date': '2023-01-02', 'value': 101},
            {'date': '2023-01-03', 'value': 99},
            # ... more data ...
        ]
        return TimeSeriesData(metric_id, dummy_data)

    @staticmethod
    def save_forecast(forecast: AnalysisResult):
        # This method should be implemented to save the forecast to your database
        print(f"Saving forecast for metric {forecast.metric_id}")
        print(forecast.to_json())

    @staticmethod
    def save_anomaly(anomaly: AnalysisResult):
        # This method should be implemented to save anomalies to your database
        print(f"Saving anomalies for metric {anomaly.metric_id}")
        print(anomaly.to_json())

    @staticmethod
    def save_trend(trend: AnalysisResult):
        # This method should be implemented to save trend to your database
        print(f"Saving trend for metric {trend.metric_id}")
        print(trend.to_json())

    @classmethod
    def run_analysis(cls, metric_id: int, analysis_type: str) -> AnalysisResult:
        data = cls.get_historical_data(metric_id)
        manager = cls(data)
        if analysis_type == 'decomposition':
            result = manager.decompose()
        elif analysis_type == 'anomaly_detection':
            result = manager.detect_anomalies()
            cls.save_anomaly(result)
        elif analysis_type == 'trend_analysis':
            result = manager.analyze_trend()
            cls.save_trend(result)
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")
        return result

    @classmethod
    def run_forecast(cls, metric_id: int, forecast_type: str, periods: int) -> AnalysisResult:
        data = cls.get_historical_data(metric_id)
        manager = cls(data)
        if forecast_type == 'arima':
            result = manager.arima_forecast(periods)
        elif forecast_type == 'prophet':
            result = manager.prophet_forecast(periods)
        elif forecast_type == 'lstm':
            result = manager.lstm_forecast(periods)
        else:
            raise ValueError(f"Unknown forecast type: {forecast_type}")
        cls.save_forecast(result)
        return result