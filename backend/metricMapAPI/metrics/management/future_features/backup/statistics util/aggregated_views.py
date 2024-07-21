"""
This module is designed to aggregate historical data into summarized views based on different time frames,
specifically monthly and yearly. It calculates the mean, minimum, and maximum values for each period.
"""
import pandas as pd

def calculate_aggregated_views(historical_data):
    """
    Functions:
    calculate_aggregated_views(historical_data): Aggregates data into monthly and yearly summaries, computing
        the mean, minimum, and maximum for each aggregation period.
    """
    df = pd.DataFrame(historical_data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    monthly_data = df.resample('M').agg(['mean', 'min', 'max'])
    yearly_data = df.resample('Y').agg(['mean', 'min', 'max'])
    
    return {
        'monthly_aggregation': monthly_data.to_dict(),
        'yearly_aggregation': yearly_data.to_dict()
    }

"""
Example:
    >>> historical_data = {
        'date': pd.date_range(start='2020-01-01', periods=365, freq='D'),
        'value': np.random.randint(100, 200, 365)
    }
    >>> aggregated_views = calculate_aggregated_views(historical_data)
    >>> print(aggregated_views)

Notes:
    - The function assumes the input data is a dictionary with 'date' and 'value' keys, where 'date' is used as a datetime index.
    - Pandas is used for data manipulation, particularly for setting datetime indices and resampling.
    - The function returns a dictionary with keys 'monthly_aggregation' and 'yearly_aggregation' containing detailed statistical summaries.
    - This module is useful for generating high-level insights from time-series data, aiding in the analysis of trends over longer periods.
"""