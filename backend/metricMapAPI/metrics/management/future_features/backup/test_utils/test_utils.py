import pytest
from metrics.computations.utils.utils import handle_missing_values, normalize_data

def test_handle_missing_values():
    data = [1, 2, None, 4, 5, None, 7]
    result = handle_missing_values(data)
    assert len(result) == len(data)
    assert all(x is not None for x in result)
    assert result[2] == 3.8  # Mean of non-missing values
    assert result[5] == 3.8

def test_normalize_data():
    data = [1, 2, 3, 4, 5]
    result = normalize_data(data)
    assert len(result) == len(data)
    assert min(result) == 0
    assert max(result) == 1
    assert result[2] == 0.5  # (3 - 1) / (5 - 1)