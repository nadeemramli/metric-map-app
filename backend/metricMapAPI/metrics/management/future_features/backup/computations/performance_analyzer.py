# performance_analyzer.py

import pandas as pd
import numpy as np
from scipy import stats
from typing import Any, List, Dict, Union
import json

class PerformanceData:
    def __init__(self, metric_id: int, data: List[Dict[str, Union[str, float]]]):
        self.metric_id = metric_id
        self.data = pd.DataFrame(data)
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data.set_index('date', inplace=True)

class PerformanceResult:
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

class PerformanceAnalyzer:
    def __init__(self, data: PerformanceData):
        self.data = data

    def forecast_vs_actual_comparison(self, forecast_data: List[Dict[str, Union[str, float]]]) -> PerformanceResult:
        forecast_df = pd.DataFrame(forecast_data)
        forecast_df['date'] = pd.to_datetime(forecast_df['date'])
        forecast_df.set_index('date', inplace=True)

        comparison = pd.merge(self.data.data, forecast_df, left_index=True, right_index=True, suffixes=('_actual', '_forecast'))
        comparison['difference'] = comparison['value_actual'] - comparison['value_forecast']
        comparison['percent_difference'] = (comparison['difference'] / comparison['value_forecast']) * 100

        return PerformanceResult(
            self.data.metric_id,
            'forecast_vs_actual',
            comparison.reset_index().to_dict(orient='records')
        )

    def calculate_probability(self, target_value: float) -> float:
        data = self.data.data['value'].values
        mean = np.mean(data)
        std_dev = np.std(data)
        probability = 1 - stats.norm.cdf(target_value, mean, std_dev)
        return probability

    def probability_analysis(self, target_value: float) -> PerformanceResult:
        data = self.data.data['value'].values
        probability = self.calculate_probability(target_value)
        
        return PerformanceResult(
            self.data.metric_id,
            'probability_analysis',
            {
                'mean': np.mean(data),
                'standard_deviation': np.std(data),
                'target': target_value,
                'probability_of_achieving_target': probability
            }
        )

    def calculate_progress(self, current_value: float, target_value: float, start_value: float) -> float:
        total_change = target_value - start_value
        current_change = current_value - start_value
        
        if total_change == 0:
            return 100 if current_value >= target_value else 0
        
        progress = (current_change / total_change) * 100
        return max(0, min(100, progress))

    def process_progress_tracking(self, target_value: float) -> PerformanceResult:
        current_value = self.data.data['value'].iloc[-1]
        start_value = self.data.data['value'].iloc[0]
        
        progress = self.calculate_progress(current_value, target_value, start_value)
        
        return PerformanceResult(
            self.data.metric_id,
            'progress_tracking',
            {
                'current_value': current_value,
                'target_value': target_value,
                'start_value': start_value,
                'progress_percentage': progress
            }
        )

    @classmethod
    def run_analysis(cls, metric_id: int, analysis_type: str, **kwargs) -> PerformanceResult:
        data = cls.get_historical_data(metric_id)
        analyzer = cls(data)
        
        if analysis_type == 'forecast_vs_actual':
            return analyzer.forecast_vs_actual_comparison(kwargs.get('forecast_data'))
        elif analysis_type == 'probability_analysis':
            return analyzer.probability_analysis(kwargs.get('target_value'))
        elif analysis_type == 'progress_tracking':
            return analyzer.process_progress_tracking(kwargs.get('target_value'))
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")

    @staticmethod
    def get_historical_data(metric_id: int) -> PerformanceData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy PerformanceData object
        dummy_data = [
            {'date': '2023-01-01', 'value': 100},
            {'date': '2023-01-02', 'value': 101},
            {'date': '2023-01-03', 'value': 99},
            # ... more data ...
        ]
        return PerformanceData(metric_id, dummy_data)

# You might want to move this to a separate utilities file if it's used across multiple modules
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)