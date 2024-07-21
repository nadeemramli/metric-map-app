"""
This module facilitates the creation of a performance dashboard by calculating key performance indicators (KPIs)
over various time periods using historical data. It provides insights into performance trends and changes over
time, including comparisons against average values.
"""

import pandas as pd

def calculate_performance_metrics(historical_data, current_date):
    """
    Functions:
    calculate_performance_metrics(historical_data, current_date): Computes several metrics to analyze the performance
        of data across different time frames such as daily, weekly, and monthly intervals.
    """
    df = pd.DataFrame(historical_data)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    current_date = pd.to_datetime(current_date)
    
    # Helper function for percentage change
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

    # Calculate week-over-week and month-over-month changes
    metrics['wow_change'] = pct_change(metrics['this_week'], metrics['last_week'])
    metrics['mom_change'] = pct_change(metrics['this_month'], metrics['last_month'])

    # This week vs average weekly
    avg_weekly = df.resample('W')['value'].mean().mean()
    metrics['week_vs_avg_weekly'] = pct_change(metrics['this_week'], avg_weekly)

    # This month vs average monthly
    avg_monthly = df.resample('M')['value'].mean().mean()
    metrics['month_vs_avg_monthly'] = pct_change(metrics['this_month'], avg_monthly)

    return metrics

"""
Example:
    >>> historical_data = {
        'date': ['2021-01-01', '2021-01-02', ...],
        'value': [100, 105, ...]
    }
    >>> current_date = '2021-02-01'
    >>> performance_metrics = calculate_performance_metrics(historical_data, current_date)
    >>> print(performance_metrics)

Notes:
    - The function calculates average values and percentage changes for the last 7, 14, and 30 days, as well as for
      this and last week/month.
    - It utilizes Pandas for data manipulation, especially for time-based indexing and resampling.
    - The function returns a dictionary with KPIs such as mean values for specified periods and percentage changes
      between the current and previous periods, along with comparisons against average weekly and monthly values.
    - Input data should be a dictionary with 'date' and 'value' keys, where 'date' is parsed into a datetime format.
"""
