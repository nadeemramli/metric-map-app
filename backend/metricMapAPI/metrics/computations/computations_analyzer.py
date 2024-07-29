# analyze.py

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

logger = logging.getLogger(__name__)

class Analyzer:
    def __init__(self, df: pd.DataFrame, metadata: dict):
        self.df = df
        self.metadata = metadata

    def calculate_technical_indicators(self, window: int = 14) -> None:
        """Calculate technical indicators for the metric.

        Args:
            window (int): The window size for calculating indicators.
        """
        try:
            # Stochastic Oscillator
            low_min = self.df['value'].rolling(window=window).min()
            high_max = self.df['value'].rolling(window=window).max()
            k = 100 * (self.df['value'] - low_min) / (high_max - low_min)
            d = k.rolling(window=3).mean()
            
            # RSI
            delta = self.df['value'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            
            logger.info(f"Calculated technical indicators for metric {self.metric.id}")
        except Exception as e:
            logger.error(f"Error calculating technical indicators for metric {self.metric.id}: {str(e)}")
            raise

    def calculate_moving_averages(self, periods: List[int] = [10, 20, 50, 100, 200]) -> None:
        """Calculate moving averages for the metric.

        Args:
            periods (List[int]): List of periods for which to calculate moving averages.
        """
        try:
            MovingAverage.objects.filter(metric=self.metric, tenant=self.tenant, project=self.project).delete() # type: ignore
            for period in periods:
                sma = self.df['value'].rolling(window=period).mean()
                ema = self.df['value'].ewm(span=period, adjust=False).mean()
                weights = np.arange(1, period + 1)
                wma = self.df['value'].rolling(window=period).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
                
            logger.info(f"Calculated and saved moving averages for metric {self.metric.id}")
        except Exception as e:
            logger.error(f"Error calculating moving averages for metric {self.metric.id}: {str(e)}")
            raise

    def analyze_trend(self, window: int = 30) -> None:
        """Analyze the trend of the metric data."""
        try:
            if len(self.df) < window:
                logger.warning(f"Not enough data for trend analysis for metric {self.metric.id}")
                return

            ts = self.df['value']
            X = np.arange(len(ts)).reshape(-1, 1)
            y = ts.values.reshape(-1, 1)
            
            model = LinearRegression()
            model.fit(X, y)
            
            slope = model.coef_[0][0]
            intercept = model.intercept_[0]
            r_squared = model.score(X, y)
            
            # Perform Mann-Kendall test for trend
            tau, p_value = kendalltau(X.ravel(), y.ravel())
            
            # Determine trend type based on slope and Mann-Kendall test
            alpha = 0.1  # significance level
            if p_value < alpha:
                trend_type = 'increasing' if tau > 0 else 'decreasing'
            else:
                # If Mann-Kendall test is not significant, use the slope direction
                trend_type = 'increasing' if slope > 0 else 'decreasing' if slope < 0 else 'stable'
            
            logger.info(f"Analyzed and saved trend for metric {self.metric.id}: {trend_type} (slope: {slope}, Mann-Kendall p-value: {p_value}, tau: {tau})")
        except Exception as e:
            logger.error(f"Error analyzing trend for metric {self.metric.id}: {str(e)}")
            raise

    def detect_trend_changes(self) -> None:
        """Detect trend changes using Pettitt's test."""
        try:
            def pettitt_test(x: np.ndarray) -> Tuple[int, float]:
                n = len(x)
                k = range(n)
                t = [np.sum(np.sign(x[i] - x[j]) for j in range(i)) for i in k]
                k_max = max(abs(i) for i in t)
                change_point = t.index(k_max) if k_max in t else t.index(-k_max)
                p_value = 2 * np.exp(-6 * k_max**2 / (n**3 + n**2))
                return change_point, p_value

            change_point, p_value = pettitt_test(self.df['value'].values)
            change_date = self.df.index[change_point]
            change_type = 'upward' if self.df['value'].iloc[change_point] < self.df['value'].iloc[change_point+1] else 'downward'
            
            TrendChangePoint.objects.create(
                metric=self.metric,
                tenant=self.tenant,
                date=change_date,
                change_type=change_type,
                significance=1 - p_value
            ) # type: ignore
            logger.info(f"Detected and saved trend change point for metric {self.metric.id}")
        except Exception as e:
            logger.error(f"Error detecting trend changes for metric {self.metric.id}: {str(e)}")
            raise
     
    def detect_seasonality(self) -> None:
        """Detect seasonality in the metric data."""
        try:
            if len(self.df) < 2:
                logger.warning(f"Not enough data for seasonality detection for metric {self.metric.id}")
                return

            ts = self.df['value']
            
            # If we don't have enough data for seasonal_decompose, use a simpler method
            if len(ts) < 728:
                # Simple seasonality strength estimation
                seasonal_diff = ts.diff(365).dropna()
                trend_diff = ts.diff().dropna()
                
                if len(seasonal_diff) > 0 and len(trend_diff) > 0:
                    seasonality_strength = 1 - np.var(seasonal_diff) / np.var(trend_diff)
                    seasonality_strength = max(0, min(seasonality_strength, 1))  # Ensure strength is between 0 and 1
                else:
                    seasonality_strength = 0
                
                period = 365
            else:
                result = seasonal_decompose(ts, model='additive', period=365)
                seasonality_strength = 1 - np.var(result.resid) / np.var(result.seasonal + result.resid)
                period = 365

                logger.info(f"Detected and saved seasonality for metric {self.metric.id} with strength {seasonality_strength}")
            else:
                logger.info(f"No significant seasonality detected for metric {self.metric.id}")

        except Exception as e:
            logger.error(f"Error detecting seasonality for metric {self.metric.id}: {str(e)}")
            raise