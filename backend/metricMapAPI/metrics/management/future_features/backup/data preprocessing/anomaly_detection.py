"""
Anomaly Detection
=================

This module provides functions for detecting anomalies in time series data.
"""

import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(data, contamination=0.1):
    """
    Detect anomalies in the given data using Isolation Forest.

    Parameters:
    data (array-like): The input data for anomaly detection.
    contamination (float): The proportion of outliers in the data set.

    Returns:
    array: A boolean array indicating whether each point is an anomaly.
    """
    model = IsolationForest(contamination=contamination)
    data = np.array(data).reshape(-1, 1)
    model.fit(data)
    anomalies = model.predict(data)
    
    return anomalies == -1
