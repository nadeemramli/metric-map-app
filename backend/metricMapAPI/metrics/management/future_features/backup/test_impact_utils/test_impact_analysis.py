import pytest
import numpy as np
from metrics.computations.impact_utils.impact_analysis import difference_in_differences, instrumental_variables

def test_difference_in_differences():
    before_treatment = [5, 6, 7, 8]
    after_treatment = [10, 12, 14, 16]
    before_control = [3, 4, 5, 6]
    after_control = [5, 6, 7, 8]
    
    effect = difference_in_differences(before_treatment, after_treatment, before_control, after_control)
    assert isinstance(effect, float)
    assert effect == 4.5  # (13 - 6.5) - (6.5 - 4.5) = 6.5 - 2 = 4.5

def test_instrumental_variables():
    np.random.seed(42)
    z = np.random.randn(100)
    x = 2 * z + np.random.randn(100)
    y = 3 * x + np.random.randn(100)
    
    model = instrumental_variables(y, x, z)
    assert hasattr(model, 'params')
    assert len(model.params) == 2
    assert abs(model.params[1] - 3) < 0.5  # Check if the estimated coefficient is close to 3