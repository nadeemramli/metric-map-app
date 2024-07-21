import pytest
import numpy as np
from metrics.computations.utils.data_preprocessing import detect_outliers, log_transform, box_cox_transform

@pytest.fixture
def sample_data():
    np.random.seed(42)
    return list(np.random.normal(0, 1, 1000)) + [10, -10]  # Add some outliers

def test_detect_outliers_iqr(sample_data):
    outliers = detect_outliers(sample_data, method='iqr')
    assert len(outliers) > 0
    assert 10 in outliers
    assert -10 in outliers

def test_detect_outliers_z_score(sample_data):
    outliers = detect_outliers(sample_data, method='z_score')
    assert len(outliers) > 0
    assert 10 in outliers
    assert -10 in outliers

def test_log_transform():
    data = [1, 10, 100, 1000]
    transformed = log_transform(data)
    assert len(transformed) == len(data)
    assert all(0 <= x <= 7 for x in transformed)

def test_box_cox_transform():
    data = [1, 2, 3, 4, 5]
    transformed = box_cox_transform(data)
    assert len(transformed) == len(data)
    assert all(isinstance(x, (float, np.floating)) for x in transformed)