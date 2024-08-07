import pandas as pd
from django.core.cache import cache
from functools import wraps

def cache_result(timeout=300):  # Cache for 5 minutes by default
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{':'.join(map(str, args))}:{':'.join(f'{k}={v}' for k, v in kwargs.items())}"
            result = cache.get(cache_key)
            if result is None:
                result = func(*args, **kwargs)
                cache.set(cache_key, result, timeout)
            return result
        return wrapper
    return decorator

def get_dataframe_from_historical_data(metric_id):
    HistoricalData = apps.get_model('metrics', 'HistoricalData')
    data = HistoricalData.objects.filter(metric_id=metric_id).order_by('date')
    return pd.DataFrame(list(data.values()))
