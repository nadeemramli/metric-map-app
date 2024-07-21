import pytest
import numpy as np
from metrics.computations.impact_utils.anomaly_detection import detect_anomalies

def test_detect_anomalies():
    # Test with a simple dataset containing obvious anomalies
    data = [1, 2, 3, 4, 5, 100, 6, 7, 8, 9]
    anomalies = detect_anomalies(data, contamination=0.1)
    assert sum(anomalies) == 1  # Only one anomaly should be detected
    assert anomalies[5] == True  # The 6th element (100) should be the anomaly

    # Test with a normal distribution and artificially introduced anomalies
    np.random.seed(42)
    normal_data = np.random.normal(0, 1, 1000)
    anomaly_data = np.concatenate([normal_data, np.random.uniform(10, 20, 10)])
    anomalies = detect_anomalies(anomaly_data, contamination=0.01)
    assert 9 <= sum(anomalies) <= 11  # Allow for slight variation
    assert all(anomalies[-10:])  # Ensure the last 10 elements are detected as anomalies

    # Test with different contamination levels
    data = list(range(100)) + [1000]  # One obvious anomaly
    anomalies_high = detect_anomalies(data, contamination=0.1)
    anomalies_low = detect_anomalies(data, contamination=0.01)
    assert sum(anomalies_high) > sum(anomalies_low)  # Higher contamination should detect more anomalies

    # Test with empty input
    with pytest.raises(ValueError):
        detect_anomalies([], contamination=0.1)

    # Test with invalid contamination value
    with pytest.raises(ValueError):
        detect_anomalies(data, contamination=1.1)
    with pytest.raises(ValueError):
        detect_anomalies(data, contamination=-0.1)