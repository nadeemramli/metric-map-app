# experiment_manager.py

import pandas as pd
import numpy as np
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
from typing import List, Dict, Union, Any
import json

class ExperimentData:
    def __init__(self, experiment_id: int, data: pd.DataFrame):
        self.experiment_id = experiment_id
        self.data = data

class ExperimentResult:
    def __init__(self, experiment_id: int, analysis_type: str, result: Dict[str, Any]):
        self.experiment_id = experiment_id
        self.analysis_type = analysis_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'experiment_id': self.experiment_id,
            'analysis_type': self.analysis_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class ExperimentManager:
    def __init__(self, data: ExperimentData):
        self.data = data

    def ab_test_analysis(self, data_a: List[float], data_b: List[float]) -> ExperimentResult:
        t_stat, p_value = stats.ttest_ind(data_a, data_b)
        return ExperimentResult(
            self.data.experiment_id,
            'ab_test',
            {
                't_statistic': t_stat,
                'p_value': p_value,
                'mean_a': np.mean(data_a),
                'mean_b': np.mean(data_b)
            }
        )

    def experiment_with_models(self, features: List[str], target: str, models: Dict) -> ExperimentResult:
        X_train, X_test, y_train, y_test = train_test_split(self.data.data[features], self.data.data[target], test_size=0.2)
        results = []
        
        for model_name, model in models.items():
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            
            results.append({
                'model': model_name,
                'mse': mse,
                'model_instance': model
            })
        
        return ExperimentResult(
            self.data.experiment_id,
            'model_experiment',
            {'results': results}
        )

    def feedback_loop(self, model, new_data: pd.DataFrame, actuals: pd.Series) -> ExperimentResult:
        predictions = model.predict(new_data)
        error = mean_squared_error(actuals, predictions)
        
        # Update model or process based on feedback
        model.fit(new_data, actuals)
        
        return ExperimentResult(
            self.data.experiment_id,
            'feedback_loop',
            {'error': error}
        )

    def difference_in_differences(self, before_treatment: List[float], after_treatment: List[float],
                                  before_control: List[float], after_control: List[float]) -> ExperimentResult:
        treatment_effect = (
            (np.mean(after_treatment) - np.mean(before_treatment)) - 
            (np.mean(after_control) - np.mean(before_control))
        )
        return ExperimentResult(
            self.data.experiment_id,
            'difference_in_differences',
            {'treatment_effect': treatment_effect}
        )

    def instrumental_variables(self, y: List[float], x: List[float], z: List[float]) -> ExperimentResult:
        y, x, z = map(np.array, [y, x, z])
        
        # First stage regression
        first_stage = sm.OLS(x, sm.add_constant(z)).fit()
        x_hat = first_stage.predict(sm.add_constant(z))
        
        # Second stage regression
        second_stage = sm.OLS(y, sm.add_constant(x_hat)).fit()
        
        return ExperimentResult(
            self.data.experiment_id,
            'instrumental_variables',
            {
                'coefficients': second_stage.params.tolist(),
                'p_values': second_stage.pvalues.tolist(),
                'r_squared': second_stage.rsquared
            }
        )

    def anova(self, groups: List[List[float]]) -> ExperimentResult:
        f_value, p_value = stats.f_oneway(*groups)
        return ExperimentResult(
            self.data.experiment_id,
            'anova',
            {'f_value': f_value, 'p_value': p_value}
        )

    def variance_decomposition(self, time_series: List[float]) -> ExperimentResult:
        mean = np.mean(time_series)
        total_variance = np.var(time_series)
        trend = np.mean([time_series[i + 1] - time_series[i] for i in range(len(time_series) - 1)])
        seasonal = np.mean([time_series[i] - mean for i in range(len(time_series))])
        residual = total_variance - (trend + seasonal)
        
        return ExperimentResult(
            self.data.experiment_id,
            'variance_decomposition',
            {'trend': trend, 'seasonal': seasonal, 'residual': residual}
        )

    @classmethod
    def run_analysis(cls, experiment_id: int, analysis_type: str, **kwargs) -> ExperimentResult:
        data = cls.get_experiment_data(experiment_id)
        manager = cls(data)
        
        if analysis_type == 'ab_test':
            return manager.ab_test_analysis(kwargs['data_a'], kwargs['data_b'])
        elif analysis_type == 'model_experiment':
            return manager.experiment_with_models(kwargs['features'], kwargs['target'], kwargs['models'])
        elif analysis_type == 'feedback_loop':
            return manager.feedback_loop(kwargs['model'], kwargs['new_data'], kwargs['actuals'])
        elif analysis_type == 'difference_in_differences':
            return manager.difference_in_differences(
                kwargs['before_treatment'], kwargs['after_treatment'],
                kwargs['before_control'], kwargs['after_control']
            )
        elif analysis_type == 'instrumental_variables':
            return manager.instrumental_variables(kwargs['y'], kwargs['x'], kwargs['z'])
        elif analysis_type == 'anova':
            return manager.anova(kwargs['groups'])
        elif analysis_type == 'variance_decomposition':
            return manager.variance_decomposition(kwargs['time_series'])
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")

    @staticmethod
    def get_experiment_data(experiment_id: int) -> ExperimentData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy ExperimentData object
        dummy_data = pd.DataFrame({
            'feature1': np.random.rand(100),
            'feature2': np.random.rand(100),
            'target': np.random.rand(100)
        })
        return ExperimentData(experiment_id, dummy_data)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)