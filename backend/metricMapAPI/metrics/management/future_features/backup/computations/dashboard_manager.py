# dashboard_manager.py

import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from typing import List, Dict, Union, Any
import json

class DashboardData:
    def __init__(self, dashboard_id: int, data: pd.DataFrame):
        self.dashboard_id = dashboard_id
        self.data = data

class DashboardResult:
    def __init__(self, dashboard_id: int, analysis_type: str, result: Dict[str, Any]):
        self.dashboard_id = dashboard_id
        self.analysis_type = analysis_type
        self.result = result

    def to_json(self):
        return json.dumps({
            'dashboard_id': self.dashboard_id,
            'analysis_type': self.analysis_type,
            'result': self.result
        }, cls=CustomJSONEncoder)

class DashboardManager:
    def __init__(self, data: DashboardData):
        self.data = data

    def generate_automated_suggestions(self) -> DashboardResult:
        df = self.data.data.copy()
        recent_trend = df['value'].tail(30).pct_change().mean()
        overall_trend = df['value'].pct_change().mean()
        
        suggestions = []
        
        if recent_trend > overall_trend:
            suggestions.append("Recent performance is above average. Consider setting more ambitious targets.")
        elif recent_trend < overall_trend:
            suggestions.append("Recent performance is below average. Review recent changes or external factors.")
        
        if df['value'].tail(7).std() > df['value'].std() * 1.5:
            suggestions.append("Recent volatility is high. Monitor closely and consider stabilizing factors.")
        
        return DashboardResult(self.data.dashboard_id, 'automated_suggestions', {'suggestions': suggestions})

    def decision_support_dashboard(self, forecast_periods: int = 30) -> DashboardResult:
        df = self.data.data.copy()
        df.set_index('date', inplace=True)
        
        real_time_data = df.iloc[-1].to_dict()
        
        model = ARIMA(df['value'], order=(1,1,1))
        results = model.fit()
        forecast = results.forecast(steps=forecast_periods)
        
        return DashboardResult(
            self.data.dashboard_id,
            'decision_support',
            {
                'real_time_data': real_time_data,
                'predictive_insights': forecast.to_dict()
            }
        )

    def calculate_performance_metrics(self, current_date: str) -> DashboardResult:
        df = self.data.data.copy()
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)

        current_date = pd.to_datetime(current_date)
        
        def pct_change(current, previous):
            return ((current - previous) / previous) * 100 if previous != 0 else 0

        metrics = {
            'lifetime': df['value'].mean(),
            'last_7_days': df.last('7D')['value'].mean(),
            'last_14_days': df.last('14D')['value'].mean(),
            'last_30_days': df.last('30D')['value'].mean(),
            'this_week': df[df.index.to_period('W') == current_date.to_period('W')]['value'].mean(),
            'last_week': df[df.index.to_period('W') == (current_date - pd.Timedelta(weeks=1)).to_period('W')]['value'].mean(),
            'this_month': df[df.index.to_period('M') == current_date.to_period('M')]['value'].mean(),
            'last_month': df[df.index.to_period('M') == (current_date - pd.Timedelta(days=30)).to_period('M')]['value'].mean(),
        }

        metrics['wow_change'] = pct_change(metrics['this_week'], metrics['last_week'])
        metrics['mom_change'] = pct_change(metrics['this_month'], metrics['last_month'])

        avg_weekly = df.resample('W')['value'].mean().mean()
        metrics['week_vs_avg_weekly'] = pct_change(metrics['this_week'], avg_weekly)

        avg_monthly = df.resample('M')['value'].mean().mean()
        metrics['month_vs_avg_monthly'] = pct_change(metrics['this_month'], avg_monthly)

        return DashboardResult(self.data.dashboard_id, 'performance_metrics', metrics)

    def simulate_scenario(self, scenario_params: Dict[str, float]) -> DashboardResult:
        simulated_data = self.data.data.copy()
        
        if 'growth_rate' in scenario_params:
            growth_rate = scenario_params['growth_rate']
            simulated_data['value'] *= (1 + growth_rate)
        
        if 'noise_level' in scenario_params:
            noise_level = scenario_params['noise_level']
            noise = np.random.normal(0, noise_level, len(simulated_data))
            simulated_data['value'] += noise
        
        if 'seasonality' in scenario_params:
            seasonality = scenario_params['seasonality']
            simulated_data['value'] += seasonality * np.sin(np.arange(len(simulated_data)) * (2 * np.pi / 365))
        
        return DashboardResult(
            self.data.dashboard_id,
            'scenario_simulation',
            {'simulated_data': simulated_data.to_dict(orient='records')}
        )

    @classmethod
    def run_analysis(cls, dashboard_id: int, analysis_type: str, **kwargs) -> DashboardResult:
        data = cls.get_dashboard_data(dashboard_id)
        manager = cls(data)
        
        if analysis_type == 'automated_suggestions':
            return manager.generate_automated_suggestions()
        elif analysis_type == 'decision_support':
            return manager.decision_support_dashboard(kwargs.get('forecast_periods', 30))
        elif analysis_type == 'performance_metrics':
            return manager.calculate_performance_metrics(kwargs['current_date'])
        elif analysis_type == 'scenario_simulation':
            return manager.simulate_scenario(kwargs['scenario_params'])
        else:
            raise ValueError(f"Unknown analysis type: {analysis_type}")

    @staticmethod
    def get_dashboard_data(dashboard_id: int) -> DashboardData:
        # This method should be implemented to fetch data from your database
        # For now, we'll return a dummy DashboardData object
        dummy_data = pd.DataFrame({
            'date': pd.date_range(start='2023-01-01', periods=365),
            'value': np.random.rand(365) * 100 + 50
        })
        return DashboardData(dashboard_id, dummy_data)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, pd.DataFrame):
            return obj.to_dict(orient='records')
        if isinstance(obj, pd.Timestamp):
            return obj.isoformat()
        return super().default(obj)