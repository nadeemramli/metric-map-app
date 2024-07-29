import unittest
from django.test import TestCase
from django.utils import timezone
import pandas as pd
import numpy as np

from ...models import (Metric, HistoricalData, DataQualityScore, Anomaly, Trend, 
                      Forecast, SeasonalityResult, TrendChangePoint, MovingAverage, 
                      TechnicalIndicator, Connection, Correlation)

from ...computations.permanent_computations import PermanentComputations

class TestPermanentComputationsRobustness(TestCase):
    def setUp(self):
        self.metric = Metric.objects.create(name="Test Metric", type="KPI", value_type="COUNT")
        self.dates = pd.date_range(end=timezone.now(), periods=1000)
        self.values = np.random.randint(1, 1000, 1000)
        
        for date, value in zip(self.dates, self.values):
            HistoricalData.objects.create(metric=self.metric, date=date, value=value)
        
        self.pc = PermanentComputations(self.metric.id)

    def test_large_dataset(self):
        self.pc.run_all_computations()
        self.assertTrue(Forecast.objects.filter(metric=self.metric).exists())
        self.assertTrue(Anomaly.objects.filter(metric=self.metric).exists())

    def test_missing_values(self):
        # Remove some values
        HistoricalData.objects.filter(metric=self.metric)[::10].delete()
        self.pc.run_all_computations()
        self.assertTrue(Forecast.objects.filter(metric=self.metric).exists())

    def test_extreme_values(self):
        # Introduce extreme values
        HistoricalData.objects.create(metric=self.metric, date=timezone.now(), value=1000000)
        HistoricalData.objects.create(metric=self.metric, date=timezone.now() + timezone.timedelta(days=1), value=-1000000)
        self.pc.run_all_computations()
        self.assertTrue(Anomaly.objects.filter(metric=self.metric, anomaly_value__in=[1000000, -1000000]).exists())

    def test_long_computation_time(self):
        import time
        start_time = time.time()
        self.pc.run_all_computations()
        end_time = time.time()
        self.assertLess(end_time - start_time, 30)  # Assuming it should take less than 30 seconds for 1000 data points

if __name__ == '__main__':
    unittest.main()