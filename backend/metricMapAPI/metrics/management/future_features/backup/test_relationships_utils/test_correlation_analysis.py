import pytest
import numpy as np
from metrics.computations.relationships_utils.correlation_analysis import pearson_correlation, spearman_correlation

@pytest.fixture
def sample_data():
    np.random.seed(42)
    x = np.random.rand(100)
    y = 2 * x + np.random.normal(0, 0.1, 100)
    return x, y

def test_pearson_correlation(sample_data):
    x, y = sample_data
    correlation = pearson_correlation(x, y)
    assert -1 <= correlation <= 1
    assert correlation > 0.9  # Strong positive correlation

def test_spearman_correlation(sample_data):
    x, y = sample_data
    correlation = spearman_correlation(x, y)
    assert -1 <= correlation <= 1
    assert correlation > 0.9  # Strong positive correlation

def test_correlation_edge_cases():
    x = [1, 2, 3]
    y = [1, 1, 1]
    assert pearson_correlation(x, y) == 0
    assert spearman_correlation(x, y) == 0