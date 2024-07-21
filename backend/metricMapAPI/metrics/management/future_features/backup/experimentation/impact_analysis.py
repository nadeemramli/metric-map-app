"""
This module contains functions for impact analysis, including Difference-in-Differences (DiD) and Instrumental Variables (IV) methods.
"""

import numpy as np
import statsmodels.api as sm

def difference_in_differences(before_treatment, after_treatment, before_control, after_control):
    """
    Calculate the treatment effect using Difference-in-Differences (DiD).

    Parameters:
    before_treatment (array-like): Outcome values for the treatment group before the treatment.
    after_treatment (array-like): Outcome values for the treatment group after the treatment.
    before_control (array-like): Outcome values for the control group before the treatment.
    after_control (array-like): Outcome values for the control group after the treatment.

    Returns:
    float: Estimated treatment effect.
    """
    before_treatment = np.array(before_treatment)
    after_treatment = np.array(after_treatment)
    before_control = np.array(before_control)
    after_control = np.array(after_control)
    
    treatment_effect = (
        (np.mean(after_treatment) - np.mean(before_treatment)) - 
        (np.mean(after_control) - np.mean(before_control))
    )
    return treatment_effect

def instrumental_variables(y, x, z):
    """
    Estimate the causal effect using Instrumental Variables (IV).

    Parameters:
    y (array-like): Dependent variable.
    x (array-like): Endogenous explanatory variable.
    z (array-like): Instrumental variable.

    Returns:
    model: Fitted IV model.
    """
    y = np.array(y)
    x = np.array(x)
    z = np.array(z)
    
    # First stage regression: Regress x on z to get the predicted values of x
    first_stage = sm.OLS(x, sm.add_constant(z)).fit()
    x_hat = first_stage.predict(sm.add_constant(z))
    
    # Second stage regression: Regress y on the predicted values of x
    second_stage = sm.OLS(y, sm.add_constant(x_hat)).fit()
    return second_stage

# Example usage:

# Difference-in-Differences
before_treatment = [5, 6, 7, 8]
after_treatment = [10, 12, 14, 16]
before_control = [3, 4, 5, 6]
after_control = [5, 6, 7, 8]

treatment_effect = difference_in_differences(
    before_treatment, after_treatment, before_control, after_control
)
print(f"Treatment Effect (DiD): {treatment_effect}")

# Instrumental Variables
y = [1, 2, 3, 4, 5]
x = [2, 3, 4, 5, 6]
z = [0.5, 1.5, 2.5, 3.5, 4.5]

iv_model = instrumental_variables(y, x, z)
print(iv_model.summary())
