from .utils import cache_result, get_dataframe_from_historical_data
import pandas as pd
import numpy as np
from scipy import stats

@cache_result()
def ab_test_analysis(metric_id, control_group, treatment_group):
    df = get_dataframe_from_historical_data(metric_id)
    control_data = df[df['group'] == control_group]['value']
    treatment_data = df[df['group'] == treatment_group]['value']
    
    t_stat, p_value = stats.ttest_ind(control_data, treatment_data)
    
    return {
        "t_statistic": t_stat,
        "p_value": p_value,
        "control_mean": control_data.mean(),
        "treatment_mean": treatment_data.mean(),
        "difference": treatment_data.mean() - control_data.mean()
    }

@cache_result()
def difference_in_differences(metric_id, pre_period, post_period, control_group, treatment_group):
    df = get_dataframe_from_historical_data(metric_id)
    df['period'] = np.where(df['date'] < post_period, 'pre', 'post')
    
    control_pre = df[(df['group'] == control_group) & (df['period'] == 'pre')]['value'].mean()
    control_post = df[(df['group'] == control_group) & (df['period'] == 'post')]['value'].mean()
    treatment_pre = df[(df['group'] == treatment_group) & (df['period'] == 'pre')]['value'].mean()
    treatment_post = df[(df['group'] == treatment_group) & (df['period'] == 'post')]['value'].mean()
    
    did_estimate = (treatment_post - treatment_pre) - (control_post - control_pre)
    
    return {
        "difference_in_differences": did_estimate,
        "control_difference": control_post - control_pre,
        "treatment_difference": treatment_post - treatment_pre
    }

# Note: Implement other experiment analysis functions (instrumental_variables, anova, variance_decomposition) similarly
