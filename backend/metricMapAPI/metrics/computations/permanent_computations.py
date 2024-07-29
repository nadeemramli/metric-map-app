"""Module for performing permanent computations on metrics data."""

from typing import Dict, List, Optional, Tuple

import logging
import numpy as np
import pandas as pd
from prophet import Prophet
from scipy import stats
from sklearn.impute import SimpleImputer
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
from scipy.stats import kendalltau
from pmdarima import auto_arima
from sklearn.linear_model import LinearRegression
import networkx as nx
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

from ..models import (
    Metric, DataQualityScore, HistoricalData, Anomaly, Trend, Forecast,
    SeasonalityResult, TrendChangePoint, MovingAverage,
    NetworkAnalysisResult, Connection, Correlation, TechnicalIndicator
)

# permanent_computations.py

from data_preparation import DataPreparation
from computations_analyzer import Analyzer
from computations_forecaster import Forecaster
from computations_anomalies import AnomalyDetector
from computations_relationships import RelationshipAnalyzer
import logging
from utils import log_exceptions, validate_metadata
from config import config

logger = logging.getLogger(__name__)

class PermanentComputations:
    def __init__(self, metric_ids: List[int]):
        self.metric_ids = metric_ids
        self.metrics_data: Dict[int, pd.DataFrame] = {}
        self.metrics_metadata: Dict[int, dict] = {}

    @log_exceptions
    def run_all_computations(self):
        logger.info(f"Starting all computations for metrics: {self.metric_ids}")
        try:
            self._prepare_data()
            
            # Check data quality
            if self.data_quality_score and self.data_quality_score.overall_score < 0.7:
                logger.warning(f"Data quality score for metric {self.metric.id} is low. Skipping computations.")
                return
            
            self._perform_analysis()
            self._perform_forecasting()
            self._detect_anomalies()
            self._compute_relationships()
            logger.info(f"Completed all computations for metrics: {self.metric_ids}")
        except Exception as e:
            logger.error(f"Error during computations: {str(e)}")
            raise

    def _prepare_data(self):
        for metric_id in self.metric_ids:
            logger.info(f"Preparing data for metric {metric_id}")
            data_prep = DataPreparation(metric_id)
            df, metadata = data_prep.prepare_data()
            if not df.empty:
                self.metrics_data[metric_id] = df
                self.metrics_metadata[metric_id] = metadata
                logger.info(f"Successfully prepared data for metric {metric_id}")
            else:
                logger.warning(f"No data available for metric {metric_id}")

    def _perform_analysis(self):
        for metric_id, df in self.metrics_data.items():
            logger.info(f"Performing analysis for metric {metric_id}")
            analyzer = Analyzer(df, self.metrics_metadata[metric_id])
            technical_indicators = analyzer.calculate_technical_indicators()
            trend_analysis = analyzer.analyze_trend()
            self._save_analysis_results(metric_id, technical_indicators, trend_analysis)

    def _perform_forecasting(self):
        for metric_id, df in self.metrics_data.items():
            logger.info(f"Performing forecasting for metric {metric_id}")
            forecaster = Forecaster(df, self.metrics_metadata[metric_id])
            sarima_forecast = forecaster.sarima_forecast()
            prophet_forecast = forecaster.prophet_forecast()
            self._save_forecast_results(metric_id, sarima_forecast, prophet_forecast)

    def _detect_anomalies(self):
        for metric_id, df in self.metrics_data.items():
            logger.info(f"Detecting anomalies for metric {metric_id}")
            anomaly_detector = AnomalyDetector(df, self.metrics_metadata[metric_id])
            anomalies = anomaly_detector.detect_anomalies()
            self._save_anomaly_results(metric_id, anomalies)

    def _compute_relationships(self):
        logger.info("Computing relationships between metrics")
        relationship_computer = RelationshipComputer(self.metrics_data, self.metrics_metadata)
        correlation_matrix = relationship_computer.calculate_correlation_matrix()
        network_analysis = relationship_computer.analyze_metric_network()
        relationship_summary = relationship_computer.generate_relationship_summary()
        self._save_relationship_results(correlation_matrix, network_analysis, relationship_summary)

    def _save_analysis_results(self, metric_id, technical_indicators, trend_analysis):
        # Implementation for saving analysis results
        pass

    def _save_forecast_results(self, metric_id, sarima_forecast, prophet_forecast):
        # Implementation for saving forecast results
        pass

    def _save_anomaly_results(self, metric_id, anomalies):
        # Implementation for saving anomaly results
        pass

    def _save_relationship_results(self, correlation_matrix, network_analysis, relationship_summary):
        # Implementation for saving relationship results
        pass


'''
All savings to database functions:
Forecast:
Forecast.objects.filter(metric=self.metric, tenant=self.tenant, model_used='SARIMA').delete()
            Forecast.objects.bulk_create([
                Forecast(
                    metric=self.metric,
                    tenant=self.tenant,
                    forecast_date=date,
                    model_used='SARIMA',
                    forecast_value=value,
                    lower_bound=lower,
                    upper_bound=upper
                ) for date, value, (lower, upper) in zip(
                    forecast_mean.index,
                    forecast_mean,
                    conf_int.values
                )
            ])

Forecast.objects.filter(metric=self.metric, tenant=self.tenant, project=self.project, model_used='Prophet').delete()
            Forecast.objects.bulk_create([
                Forecast(
                    metric=self.metric,
                    tenant=self.tenant,
                    project=self.project,
                    forecast_date=row['ds'],
                    model_used='Prophet',
                    forecast_value=row['yhat'],
                    lower_bound=row['yhat_lower'],
                    upper_bound=row['yhat_upper']
                ) for _, row in forecast.tail(periods).iterrows()
            ])

Analyzer:
TechnicalIndicator.objects.filter(metric=self.metric, project=self.project, tenant=self.tenant ).delete() # type: ignore
            TechnicalIndicator.objects.bulk_create([
                TechnicalIndicator(
                    metric=self.metric,
                    tenant=self.tenant,
                    project=self.project,
                    date=date,
                    stochastic_value=k_val,
                    rsi_value=rsi_val
                ) for date, k_val, rsi_val in zip(self.df.index, k, rsi)
            ]) # type: ignore

MovingAverage.objects.bulk_create([
                    MovingAverage(
                        metric=self.metric,
                        tenant=self.tenant,
                        project=self.project,
                        date=date,
                        ma_type='SMA',
                        period=period,
                        value=sma_value
                    ) for date, sma_value in sma.items()
                ] + [
                    MovingAverage(
                        metric=self.metric,
                        tenant=self.tenant,
                        project=self.project,
                        date=date,
                        ma_type='EMA',
                        period=period,
                        value=ema_value
                    ) for date, ema_value in ema.items()
                ] + [
                    MovingAverage(
                        metric=self.metric,
                        tenant=self.tenant,
                        project=self.project,
                        date=date,
                        ma_type='WMA',
                        period=period,
                        value=wma_value
                    ) for date, wma_value in wma.items()
                ]) # type: ignore

  Trend.objects.update_or_create(
                metric=self.metric,
                tenant=self.tenant,
                defaults={
                    'start_date': self.df.index[0],
                    'end_date': self.df.index[-1],
                    'trend_type': trend_type,
                    'trend_value': ts.iloc[-1],
                    'slope': slope,
                    'notes': f'Mann-Kendall p-value: {p_value}, tau: {tau}, R-squared: {r_squared}'
                }
            )

if seasonality_strength > 0:
                SeasonalityResult.objects.update_or_create(
                    metric=self.metric,
                    tenant=self.tenant,
                    defaults={
                        'seasonality_type': 'yearly',
                        'strength': seasonality_strength,
                        'period': period
                    }
                )


Anomalies:
with transaction.atomic():
                Anomaly.objects.filter(metric=self.metric, tenant=self.tenant).delete()
                Anomaly.objects.bulk_create([
                    Anomaly(
                        metric=self.metric,
                        tenant=self.tenant,
                        detection_date=index,
                        anomaly_value=row['value'],
                        anomaly_score=row['anomaly_score']
                    ) for index, row in anomalies.iterrows()
                ])


Relationships
Correlation.objects.update_or_create(
                metric1=self.metric,
                metric2=other_metric,
                defaults={
                    'lag': 0,
                    f'{correlation_type}_correlation': corr,
                    'p_value': p_value
                }
            ) # type: ignore

NetworkAnalysisResult.objects.create(
                metric=None,  # This is a global analysis
                analysis_type='PageRank_Community',
                result={
                    'pagerank': pagerank,
                    'communities': [list(c) for c in communities]
                }
            )

'''