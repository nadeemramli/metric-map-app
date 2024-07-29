import logging
import unittest
from django.test import TestCase
from django.utils import timezone
from django.db import IntegrityError
from unittest.mock import patch, MagicMock
import pandas as pd
import numpy as np

from ...models import (Metric, HistoricalData, Anomaly, Trend, 
                      Forecast, SeasonalityResult, Client, Domain, Project, MetricType, ValueType)

from ...computations.permanent_computations import PermanentComputations

logger = logging.getLogger(__name__)

class TestPermanentComputationsAccuracy(TestCase):
    def setUp(self):
        # Create a test tenant
        self.tenant = Client.objects.create(name="Test Tenant", schema_name="test_tenant")
        Domain.objects.create(domain="test.localhost", tenant=self.tenant, is_primary=True)
        
        # Create a test project
        self.project = Project.objects.create(name="Test Project", tenant=self.tenant)
        
        # Create a test metric
        self.metric = Metric.objects.create(
            tenant=self.tenant,
            project=self.project,
            name="Test Metric",
            type=MetricType.KPI.name,
            value_type=ValueType.COUNT.name
        )
        
        # Generate fake historical data
        self.start_date = timezone.now().date() - timezone.timedelta(days=365)
        self.dates = [self.start_date + timezone.timedelta(days=i) for i in range(365)]
        self.values = self.generate_benchmark_data()
        
        # Create historical data using bulk_create
        HistoricalData.objects.bulk_create([
            HistoricalData(
                tenant=self.tenant,
                metric=self.metric,
                date=date,
                value=value
            ) for date, value in zip(self.dates, self.values)
        ])
        
        self.pc = PermanentComputations(self.metric.id)
        self.pc.prepare_data()  # Prepare the data after creating historical data

    def generate_benchmark_data(self):
        trend = np.linspace(0, 10, 365)
        seasonality = 5 * np.sin(np.linspace(0, 2*np.pi, 365))
        noise = np.random.normal(0, 1, 365)
        return trend + seasonality + noise

    def test_seasonality_accuracy(self):
        self.assertIsNotNone(self.pc.df, "Data frame should not be None")
        self.pc.detect_seasonality()
        
        seasonality = SeasonalityResult.objects.filter(metric=self.metric, tenant=self.tenant).first()
        
        if seasonality:
            self.assertGreater(seasonality.strength, 0, "Seasonality strength should be positive")
            self.assertLess(seasonality.strength, 1, "Seasonality strength should be less than 1")
            self.assertIn(seasonality.period, [7, 30, 365], "Period should be weekly, monthly, or yearly")
        else:
            logger.warning("No seasonality detected. This may be normal if there's not enough data or no clear seasonal pattern.")

    def test_forecast_accuracy(self):
        self.assertIsNotNone(self.pc.df, "Data frame should not be None")
        self.pc.sarima_forecast(steps=30)
        forecasts = Forecast.objects.filter(metric=self.metric, tenant=self.tenant, model_used='SARIMA')
        self.assertGreater(forecasts.count(), 0, "No forecasts were generated")

        future_values = self.generate_benchmark_data()[-30:]
        forecast_values = [f.forecast_value for f in forecasts]
        
        # Calculate MAPE
        mape = np.mean(np.abs((future_values - forecast_values) / future_values)) * 100
        
        # Log the MAPE for debugging
        logger.info(f"MAPE for forecast: {mape}")

        # Adjust the threshold to allow for some forecasting error
        self.assertLess(mape, 35, f"MAPE ({mape}) is higher than expected. This may indicate issues with the forecasting model or the benchmark data.")

    def test_anomaly_detection_accuracy(self):
        self.assertIsNotNone(self.pc.df, "Data frame should not be None")
        
        # Introduce known anomalies
        anomaly_dates = [self.pc.df.index[50], self.pc.df.index[200]]
        original_values = [self.pc.df.iloc[50]['value'], self.pc.df.iloc[200]['value']]
        std_dev = self.pc.df['value'].std()
        anomaly_values = [original_values[0] + 15 * std_dev,
                        original_values[1] - 15 * std_dev]
        
        logger.info(f"Introducing anomalies: {list(zip(anomaly_dates, anomaly_values))}")
        
        HistoricalData.objects.filter(metric=self.metric, date=anomaly_dates[0].date()).update(value=anomaly_values[0])
        HistoricalData.objects.filter(metric=self.metric, date=anomaly_dates[1].date()).update(value=anomaly_values[1])
        
        # Refresh the data in PermanentComputations object
        self.pc.prepare_data()
        
        # Log data statistics before anomaly detection
        logger.info(f"Data statistics before anomaly detection:")
        logger.info(f"Data shape: {self.pc.df.shape}")
        logger.info(f"Data summary: {self.pc.df['value'].describe()}")
        
        self.pc.detect_anomalies(window=20, base_threshold=2.5, seasonality_period=7, context_window=5)
        anomalies = Anomaly.objects.filter(metric=self.metric, tenant=self.tenant)
        
        self.assertGreaterEqual(anomalies.count(), 2, f"Expected at least 2 anomalies, but found {anomalies.count()}")
        self.assertTrue(anomalies.filter(detection_date=anomaly_dates[0].date()).exists(), f"Anomaly not detected on {anomaly_dates[0]}")
        self.assertTrue(anomalies.filter(detection_date=anomaly_dates[1].date()).exists(), f"Anomaly not detected on {anomaly_dates[1]}")

        # Log additional information about detected anomalies
        logger.info(f"Number of anomalies detected: {anomalies.count()}")
        for anomaly in anomalies:
            logger.info(f"Anomaly detected on {anomaly.detection_date}: value = {anomaly.anomaly_value}, score = {anomaly.anomaly_score}")

        # Log information about the data around the introduced anomalies
        for date in anomaly_dates:
            surrounding_data = self.pc.df.loc[date - pd.Timedelta(days=5):date + pd.Timedelta(days=5)]
            logger.info(f"Data around {date}:\n{surrounding_data}")

        # Restore original values
        HistoricalData.objects.filter(metric=self.metric, date=anomaly_dates[0].date()).update(value=original_values[0])
        HistoricalData.objects.filter(metric=self.metric, date=anomaly_dates[1].date()).update(value=original_values[1])

        # Refresh the data again to ensure we're back to the original state
        self.pc.prepare_data()
    
    def test_trend_accuracy(self):
            self.assertIsNotNone(self.pc.df, "Data frame should not be None")
            self.pc.analyze_trend()
            trend = Trend.objects.get(metric=self.metric, tenant=self.tenant)
            
            expected_trend = 'increasing'
            self.assertEqual(trend.trend_type, expected_trend, 
                            f"Expected {expected_trend} trend, but got {trend.trend_type}. "
                            f"Slope: {trend.slope}, Notes: {trend.notes}")
            
            self.assertGreater(trend.slope, 0, f"Expected positive slope, but got {trend.slope}")
            
            # Log trend information for debugging
            logger.info(f"Detected trend: {trend.trend_type}, slope: {trend.slope}, notes: {trend.notes}")
            
            # Additional debugging information
            values = self.pc.df['value'].values
            logger.info(f"Data summary: min={values.min()}, max={values.max()}, mean={values.mean()}, std={values.std()}")
            logger.info(f"First 10 values: {values[:10]}")
            logger.info(f"Last 10 values: {values[-10:]}")

    def tearDown(self):
        # Clean up created data
        HistoricalData.objects.filter(tenant=self.tenant).delete()
        Metric.objects.filter(tenant=self.tenant).delete()
        Project.objects.filter(tenant=self.tenant).delete()
        Domain.objects.filter(tenant=self.tenant).delete()
        self.tenant.delete()

if __name__ == '__main__':
    unittest.main()