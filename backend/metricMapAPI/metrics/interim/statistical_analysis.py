from .utils import cache_result, get_dataframe_from_historical_data
import numpy as np
from statsmodels.tsa.stattools import adfuller

@cache_result()
def calculate_advanced_stats(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    return {
        'skewness': df['value'].skew(),
        'kurtosis': df['value'].kurtosis(),
        'autocorrelation': df['value'].autocorr(),
        'stationarity': adfuller(df['value'])[1]  # p-value of ADF test
    }

@cache_result()
def calculate_aggregated_views(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    return {
        'daily': df.resample('D', on='date').mean().to_dict()['value'],
        'weekly': df.resample('W', on='date').mean().to_dict()['value'],
        'monthly': df.resample('M', on='date').mean().to_dict()['value']
    }

@cache_result()
def calculate_basic_stats(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    return {
        'mean': df['value'].mean(),
        'median': df['value'].median(),
        'std': df['value'].std(),
        'min': df['value'].min(),
        'max': df['value'].max()
    }
