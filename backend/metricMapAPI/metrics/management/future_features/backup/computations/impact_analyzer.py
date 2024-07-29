# impact_analyzer.py

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from typing import List, Dict, Union, Any
import json

class ImpactData:
    def __init__(self, impact_id: int, data: pd.DataFrame):
        self.impact_id = impact_id
        self.data = data

class ImpactResult:
    def __init__(self, impact_id: int, analysis_type: str, result: Dict[str, Any]):
        self.impact_id = impact_id
        self.analysis_type = analysis_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'impact_id': self.impact_id,
            'analysis_type': self.analysis_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class ImpactAnalyzer:
    def __init__(self, data: ImpactData):
        self.data = data

    def difference_in_differences(self, before_treatment: List[float], after_treatment: List[float],
                                  before_control: List[float], after_control: List[float]) -> ImpactResult:
        treatment_effect = (
            (np.mean(after_treatment) - np.mean(before_treatment)) - 
            (np.mean(after_control) - np.mean(before_control))
        )
        return ImpactResult(
            self.data.impact_id,
            'difference_in_differences',
            {'treatment_effect': treatment_effect}
        )

    def instrumental_variables(self, y: List[float], x: List[float], z: List[float]) -> ImpactResult:
        y, x, z = map(np.array, [y, x, z])
        
        first_stage = sm.OLS(x, sm.add_constant(z)).fit()
        x_hat = first_stage.predict(sm.add_constant(z))
        
        second_stage = sm.OLS(y, sm.add_constant(x_hat)).fit()
        
        return ImpactResult(
            self.data.impact_id,
            'instrumental_variables',
            {
                'coefficients': second_stage.params.tolist(),
                'p_values': second_stage.pvalues.tolist(),
                'r_squared': second_stage.rsquared
            }
        )

    def detect_changepoints(self, data: List[float], threshold: float = 1.5) -> ImpactResult:
        data = np.asarray(data)
        if data.size == 0:
            raise ValueError("Input data cannot be empty")
        
        n = len(data)
        diff = np.diff(data)
        mean_diff = np.mean(diff)
        std_diff = np.std(diff)
        
        if std_diff == 0:
            return ImpactResult(self.data.impact_id, 'change_detection', {'changepoints': []})
        
        s_pos = np.zeros(n-1)
        s_neg = np.zeros(n-1)
        changepoints = []
        
        for i in range(1, n-1):
            s_pos[i] = max(0, s_pos[i-1] + (diff[i] - mean_diff) / std_diff)
            s_neg[i] = max(0, s_neg[i-1] - (diff[i] - mean_diff) / std_diff)
            
            if s_pos[i] > threshold or s_neg[i] > threshold:
                changepoints.append(i+1)
                s_pos[i] = 0
                s_neg[i] = 0
        
        return ImpactResult(
            self.data.impact_id,
            'change_detection',
            {
                'changepoints': changepoints,
                'cusum_positive': s_pos.tolist(),
                'cusum_negative': s_neg.tolist()
            }
        )

    def calculate_percent_change(self, data: pd.Series) -> ImpactResult:
        percent_change = data.pct_change() * 100
        return ImpactResult(
            self.data.impact_id,
            'percent_change',
            {'percent_change': percent_change.tolist()}
        )

    def train_regression_model(self, features: List[str], target: str) -> ImpactResult:
        X = self.data.data[features]
        y = self.data.data[target]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        mse = self.evaluate_regression_model(model, X_test, y_test)
        
        return ImpactResult(
            self.data.impact_id,
            'regression_model',
            {
                'coefficients': model.coef_.tolist(),
                'intercept': model.intercept_,
                'mse': mse,
                'features': features
            }
        )

    def evaluate_regression_model(self, model: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series) -> float:
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        return mse

    @classmethod
    def run_analysis(cls, impact_id: int, analysis_type: str, **kwargs) -> ImpactResult:
        data = cls.get_impact_data(impact_id)
        analyzer = cls(data)
        
        if analysis_type == 'difference_in_differences':
            return analyzer.difference_in_differences(
                kwargs['before_treatment'], kwargs['after_treatment'],
                kwargs['before_control'], kwargs['after_control']
            )
        elif analysis_type == 'instrumental_variables':
            return analyzer.instrumental_variables(kwargs['y'], kwargs['x'], kwargs['z'])
        elif analysis_type == 'change_detection':
            return analyzer.detect_changepoints(kwargs['data'], kwargs.get('threshold', 1.5))
        elif analysis_type == 'percent_change':
            return analyzer.calculate_percent_change(data.data[kwargs['column']])
        elif analysis_type == 'regression_model':
            return analyzer.train_regression_model(kwargs['features'], kwargs['target'])
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")

    @staticmethod
    def get_impact_data(impact_id: int) -> ImpactData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy ImpactData object
        dummy_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=100),
            'metric': np.random.rand(100),
            'action1': np.random.choice([0, 1], size=100),
            'action2': np.random.choice([0, 1], size=100)
        })
        return ImpactData(impact_id, dummy_data)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)