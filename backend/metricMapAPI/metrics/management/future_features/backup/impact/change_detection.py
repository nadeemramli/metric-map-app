import numpy as np

def detect_changepoints(data, threshold=1.5):
    """
    Detect changepoints in time series data using CUSUM algorithm.

    Parameters:
        data (array-like): Time series data.
        threshold (float): Threshold for detecting changepoints.

    Returns:
        set: Indices of detected changepoints.
    """
    data = np.asarray(data)
    if data.size == 0:
        raise ValueError("Input data cannot be empty")
    
    n = len(data)
    diff = np.diff(data)
    mean_diff = np.mean(diff)
    std_diff = np.std(diff)
    
    if std_diff == 0:
        return set()  # No changepoints if there's no variation
    
    s_pos = np.zeros(n-1)
    s_neg = np.zeros(n-1)
    changepoints = set()
    
    for i in range(1, n-1):
        s_pos[i] = max(0, s_pos[i-1] + (diff[i] - mean_diff) / std_diff)
        s_neg[i] = max(0, s_neg[i-1] - (diff[i] - mean_diff) / std_diff)
        
        if s_pos[i] > threshold or s_neg[i] > threshold:
            changepoints.add(i+1)  # Add 1 to get the correct index
            # Reset
            s_pos[i] = 0
            s_neg[i] = 0
    
    print(f"CUSUM positive: {s_pos}")
    print(f"CUSUM negative: {s_neg}")
    print(f"Detected changepoints: {changepoints}")
    
    return changepoints

def calculate_percent_change(data):
    """
    Calculate percent change in time series data.

    Parameters:
        data (pd.Series): Time series data.

    Returns:
        pd.Series: Percent change values.
    """
    percent_change = data.pct_change() * 100
    return percent_change