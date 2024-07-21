"""
This module contains functions for survival analysis. This can be useful when we integrated with Cohort LTV data
"""

from lifelines import KaplanMeierFitter
import pandas as pd

def fit_kaplan_meier(data, duration_col, event_col):
    """
    Fit a Kaplan-Meier survival model.

    Parameters:
        data (pd.DataFrame): DataFrame containing duration and event columns.
        duration_col (str): Name of the duration column.
        event_col (str): Name of the event column.

    Returns:
        KaplanMeierFitter: Fitted Kaplan-Meier model.
    """
    kmf = KaplanMeierFitter()
    kmf.fit(data[duration_col], event_observed=data[event_col])
    return kmf

def plot_survival_function(kmf):
    """
    Plot the survival function.

    Parameters:
        kmf (KaplanMeierFitter): Fitted Kaplan-Meier model.

    Returns:
        None
    """
    fig = kmf.plot_survival_function()
    return fig

# Ensure lifelines is installed and available for import.
