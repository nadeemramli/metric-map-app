import pytest
import numpy as np
import pandas as pd
from metrics.computations.impact_utils.change_detection import detect_changepoints, calculate_percent_change

def test_detect_changepoints():
    # Test with obvious changepoints
    data = [1, 2, 3, 10, 11, 12, 4, 5, 6]
    changepoints = detect_changepoints(data, threshold=1.5)
    print(f"Resulting changepoints: {changepoints}")
    assert changepoints == {3, 6}  # Changepoints should be detected at indices 3 and 6

    # Test with no changepoints
    data = [1, 2, 3, 4, 5, 6]
    changepoints = detect_changepoints(data, threshold=2)
    assert len(changepoints) == 0

    # Test with different threshold
    data = [1, 2, 3, 5, 6, 7]
    changepoints_low = detect_changepoints(data, threshold=1)
    changepoints_high = detect_changepoints(data, threshold=3)
    assert len(changepoints_low) >= len(changepoints_high)

    # Test with random data
    np.random.seed(42)
    data = np.random.normal(0, 1, 1000)
    data[500:] += 5  # Add a shift at index 500
    changepoints = detect_changepoints(data, threshold=3)
    assert 500 in changepoints, f"Changepoint at 500 not detected. Detected changepoints: {changepoints}"

def test_detect_changepoints_invalid_input():
    # Test with empty input
    with pytest.raises(ValueError):
        detect_changepoints([])

    # Test with non-numeric input
    with pytest.raises(TypeError):
        detect_changepoints(['a', 'b', 'c'])

def test_calculate_percent_change():
    # Test with simple increasing data
    data = pd.Series([100, 110, 121, 133.1])
    expected = pd.Series([np.nan, 10.0, 10.0, 10.0])
    pd.testing.assert_series_equal(calculate_percent_change(data), expected, atol=1e-2)

    # Test with decreasing data
    data = pd.Series([100, 90, 81, 72.9])
    expected = pd.Series([np.nan, -10.0, -10.0, -10.0])
    pd.testing.assert_series_equal(calculate_percent_change(data), expected, atol=1e-2)

    # Test with mixed data
    data = pd.Series([100, 120, 90, 110])
    expected = pd.Series([np.nan, 20.0, -25.0, 22.22222])
    pd.testing.assert_series_equal(calculate_percent_change(data), expected, atol=1e-2)

    # Test with zeros
    data = pd.Series([0, 100, 0, 100])
    result = calculate_percent_change(data)
    assert np.isnan(result[0])
    assert np.isinf(result[1])
    assert result[2] == -100.0
    assert np.isinf(result[3])

def test_calculate_percent_change_invalid_input():
    # Test with non-Series input
    with pytest.raises(AttributeError):
        calculate_percent_change([1])