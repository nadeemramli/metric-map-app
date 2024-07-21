"""
This module provides functionalities for tracking progress towards a goal over time, based on historical data. 
It calculates the percentage of goal achieved, adjusting for various start and target values.
"""

import pandas as pd

def calculate_progress(current_value, target_value, start_value):
    """
    Functions:
    calculate_progress(current_value, target_value, start_value): Calculates the progress made towards a target as a 
        percentage of the total change required from the start value.
    """
    total_change = target_value - start_value
    current_change = current_value - start_value
    
    if total_change == 0:
        return 100 if current_value >= target_value else 0
    
    progress = (current_change / total_change) * 100
    return max(0, min(100, progress))

def process_progress_tracking(historical_data, target_value):
    """
    Functions:
    process_progress_tracking(historical_data, target_value): Processes a dataset to determine the current progress 
        towards a target based on historical values.
    """
    df = pd.DataFrame(historical_data)
    current_value = df['value'].iloc[-1]
    start_value = df['value'].iloc[0]
    
    progress = calculate_progress(current_value, target_value, start_value)
    
    return {
        'current_value': current_value,
        'target_value': target_value,
        'start_value': start_value,
        'progress_percentage': progress
    }

"""
Example:
    >>> historical_data = {'date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'value': [50, 75, 95]}
    >>> target_value = 100
    >>> progress_data = process_progress_tracking(historical_data, target_value)
    >>> print(progress_data)

Notes:
    - This module uses pandas for handling and manipulating the dataset provided as historical data.
    - It returns a dictionary containing the current, start, and target values along with the calculated progress percentage.
    - The progress is bounded between 0% and 100%, regardless of whether the current value exceeds the target.
    - The calculate_progress function is robust against zero total change scenarios, providing sensible outputs.
"""