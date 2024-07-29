# data_preprocessor.py

import numpy as np
from scipy import stats
from sklearn.ensemble import IsolationForest
from typing import List, Dict, Union, Any
import json

class PreprocessorData:
    def __init__(self, preprocessor_id: int, data: np.ndarray):
        self.preprocessor_id = preprocessor_id
        self.data = data

class PreprocessorResult:
    def __init__(self, preprocessor_id: int, process_type: str, result: Dict[str, Any]):
        self.preprocessor_id = preprocessor_id
        self.process_type = process_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'preprocessor_id': self.preprocessor_id,
            'process_type': self.process_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class DataPreprocessor:
    def __init__(self, data: PreprocessorData):
        self.data = data

    def detect_anomalies(self, contamination: float = 0.1) -> PreprocessorResult:
        model = IsolationForest(contamination=contamination)
        data = self.data.data.reshape(-1, 1)
        model.fit(data)
        anomalies = model.predict(data)
        
        return PreprocessorResult(
            self.data.preprocessor_id,
            'anomaly_detection',
            {'anomalies': (anomalies == -1).tolist()}
        )

    def detect_outliers(self, method: str = 'iqr') -> PreprocessorResult:
        data = self.data.data
        if method == 'iqr':
            q1, q3 = np.percentile(data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = [x for x in data if x < lower_bound or x > upper_bound]
        elif method == 'z_score':
            mean_val = np.mean(data)
            std_dev = np.std(data)
            outliers = [x for x in data if abs((x - mean_val) / std_dev) > 3]
        else:
            raise ValueError(f"Unknown outlier detection method: {method}")
        
        return PreprocessorResult(
            self.data.preprocessor_id,
            'outlier_detection',
            {'outliers': outliers}
        )

    def log_transform(self) -> PreprocessorResult:
        transformed_data = np.log(self.data.data[self.data.data > 0])
        return PreprocessorResult(
            self.data.preprocessor_id,
            'log_transform',
            {'transformed_data': transformed_data.tolist()}
        )

    def box_cox_transform(self) -> PreprocessorResult:
        transformed_data, _ = stats.boxcox(self.data.data)
        return PreprocessorResult(
            self.data.preprocessor_id,
            'box_cox_transform',
            {'transformed_data': transformed_data.tolist()}
        )

    def handle_missing_values(self) -> PreprocessorResult:
        data = self.data.data
        valid_data = data[~np.isnan(data)]
        mean_value = np.mean(valid_data) if valid_data.size > 0 else 0
        filled_data = np.where(np.isnan(data), mean_value, data)
        return PreprocessorResult(
            self.data.preprocessor_id,
            'handle_missing_values',
            {'filled_data': filled_data.tolist()}
        )

    def normalize_data(self) -> PreprocessorResult:
        data = self.data.data
        min_val = np.min(data)
        max_val = np.max(data)
        normalized_data = (data - min_val) / (max_val - min_val)
        return PreprocessorResult(
            self.data.preprocessor_id,
            'normalize_data',
            {'normalized_data': normalized_data.tolist()}
        )

    @classmethod
    def run_process(cls, preprocessor_id: int, process_type: str, **kwargs) -> PreprocessorResult:
        data = cls.get_preprocessor_data(preprocessor_id)
        preprocessor = cls(data)
        
        if process_type == 'anomaly_detection':
            return preprocessor.detect_anomalies(kwargs.get('contamination', 0.1))
        elif process_type == 'outlier_detection':
            return preprocessor.detect_outliers(kwargs.get('method', 'iqr'))
        elif process_type == 'log_transform':
            return preprocessor.log_transform()
        elif process_type == 'box_cox_transform':
            return preprocessor.box_cox_transform()
        elif process_type == 'handle_missing_values':
            return preprocessor.handle_missing_values()
        elif process_type == 'normalize_data':
            return preprocessor.normalize_data()
        else:
            raise ValueError(f"Unknown process type: {process_type}")

    @staticmethod
    def get_preprocessor_data(preprocessor_id: int) -> PreprocessorData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy PreprocessorData object
        dummy_data = np.random.rand(100) * 100
        return PreprocessorData(preprocessor_id, dummy_data)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)