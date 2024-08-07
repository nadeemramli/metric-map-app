from .utils import cache_result, get_dataframe_from_historical_data
import pandas as pd

@cache_result()
def generate_automated_suggestions(metric_id):
    df = get_dataframe_from_historical_data(metric_id)
    suggestions = []
    
    recent_trend = df['value'].tail(30).mean()
    overall_trend = df['value'].mean()
    
    if recent_trend > overall_trend:
        suggestions.append("Recent performance is above average. Consider setting more ambitious targets.")
    elif recent_trend < overall_trend:
        suggestions.append("Recent performance is below average. Review recent changes or external factors.")
    
    if df['value'].tail(7).std() > df['value'].std() * 1.5:
        suggestions.append("Recent volatility is high. Monitor closely and consider stabilizing factors.")
    
    return {'suggestions': suggestions}

@cache_result()
def performance_dashboard(metric_id, current_date=None):
    df = get_dataframe_from_historical_data(metric_id)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    current_date = pd.to_datetime(current_date) if current_date else pd.Timestamp.now()
    
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
    
    return metrics
