# statistics_analyzer.py

import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis
from typing import List, Dict, Union, Any
import json

class StatisticsData:
    def __init__(self, statistics_id: int, data: pd.DataFrame):
        self.statistics_id = statistics_id
        self.data = data

class StatisticsResult:
    def __init__(self, statistics_id: int, analysis_type: str, result: Dict[str, Any]):
        self.statistics_id = statistics_id
        self.analysis_type = analysis_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'statistics_id': self.statistics_id,
            'analysis_type': self.analysis_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class StatisticsAnalyzer:
    def __init__(self, data: StatisticsData):
        self.data = data

    def calculate_advanced_stats(self, column: str) -> StatisticsResult:
        data = self.data.data[column]
        result = {
            'skewness': skew(data),
            'kurtosis': kurtosis(data, fisher=True),
            'percentiles': {
                '25': np.percentile(data, 25),
                '50': np.percentile(data, 50),
                '75': np.percentile(data, 75)
            }
        }
        return StatisticsResult(self.data.statistics_id, 'advanced_stats', result)

    def calculate_aggregated_views(self) -> StatisticsResult:
        df = self.data.data.copy()
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        
        monthly_data = df.resample('M').agg(['mean', 'min', 'max'])
        yearly_data = df.resample('Y').agg(['mean', 'min', 'max'])
        
        result = {
            'monthly_aggregation': monthly_data.to_dict(),
            'yearly_aggregation': yearly_data.to_dict()
        }
        return StatisticsResult(self.data.statistics_id, 'aggregated_views', result)

    def calculate_basic_stats(self, column: str) -> StatisticsResult:
        data = self.data.data[column]
        result = {
            'mean': np.mean(data),
            'median': np.median(data),
            'standard_deviation': np.std(data),
            'coefficient_of_variation': np.std(data) / np.mean(data),
            'standard_error': np.std(data) / np.sqrt(len(data))
        }
        return StatisticsResult(self.data.statistics_id, 'basic_stats', result)

    def calculate_technical_indicators(self, high_col: str, low_col: str, close_col: str, k_window: int, d_window: int, rsi_window: int) -> StatisticsResult:
        df = self.data.data.copy()
        
        # Stochastic Oscillator
        low_min = df[low_col].rolling(window=k_window).min()
        high_max = df[high_col].rolling(window=k_window).max()
        k = 100 * (df[close_col] - low_min) / (high_max - low_min)
        k = k.clip(0, 100)
        d = k.rolling(window=d_window).mean()
        
        # RSI
        delta = df[close_col].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=rsi_window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=rsi_window).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        result = {
            'stochastic_oscillator': {
                'k': k.tolist(),
                'd': d.tolist()
            },
            'rsi': rsi.tolist()
        }
        return StatisticsResult(self.data.statistics_id, 'technical_indicators', result)

    @classmethod
    def run_analysis(cls, statistics_id: int, analysis_type: str, **kwargs) -> StatisticsResult:
        data = cls.get_statistics_data(statistics_id)
        analyzer = cls(data)
        
        if analysis_type == 'advanced_stats':
            return analyzer.calculate_advanced_stats(kwargs['column'])
        elif analysis_type == 'aggregated_views':
            return analyzer.calculate_aggregated_views()
        elif analysis_type == 'basic_stats':
            return analyzer.calculate_basic_stats(kwargs['column'])
        elif analysis_type == 'technical_indicators':
            return analyzer.calculate_technical_indicators(
                kwargs['high_col'], kwargs['low_col'], kwargs['close_col'],
                kwargs['k_window'], kwargs['d_window'], kwargs['rsi_window']
            )
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")

    @staticmethod
    def get_statistics_data(statistics_id: int) -> StatisticsData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy StatisticsData object
        dummy_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=100),
            'value': np.random.rand(100),
            'high': np.random.rand(100) + 1,
            'low': np.random.rand(100),
            'close': np.random.rand(100) + 0.5
        })
        return StatisticsData(statistics_id, dummy_data)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)