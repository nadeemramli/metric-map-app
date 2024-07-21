import pytest
import numpy as np
from metrics.computations.statistics_utils.basic_stats import mean, median, standard_deviation, coefficient_of_variation, standard_error

def test_mean():
    assert mean([1, 2, 3, 4, 5]) == 3
    assert mean([0, 0, 0, 0]) == 0
    assert mean([-1, 0, 1]) == 0
    assert abs(mean([1.5, 2.5, 3.5]) - 2.5) < 1e-10

def test_median():
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 3, 4]) == 2.5
    assert median([5, 2, 1, 4, 3]) == 3
    assert median([-1, 0, 1]) == 0

def test_standard_deviation():
    assert abs(standard_deviation([1, 2, 3, 4, 5]) - 1.414213562) < 1e-9
    assert standard_deviation([1, 1, 1, 1]) == 0
    assert abs(standard_deviation([-2, -1, 0, 1, 2]) - 1.414213562) < 1e-9

def test_coefficient_of_variation():
    assert abs(coefficient_of_variation([1, 2, 3, 4, 5]) - 0.4714045207) < 1e-9
    assert np.isclose(coefficient_of_variation([10, 20, 30, 40, 50]),
                      coefficient_of_variation([1, 2, 3, 4, 5]))

def test_standard_error():
    assert abs(standard_error([1, 2, 3, 4, 5]) - 0.6324555320) < 1e-9
    assert abs(standard_error([1, 1, 1, 1]) - 0) < 1e-10
    assert abs(standard_error([-2, -1, 0, 1, 2]) - 0.6324555320) < 1e-9

def test_empty_input():
    with pytest.raises(ZeroDivisionError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        standard_deviation([])
    with pytest.raises(ValueError):
        coefficient_of_variation([])
    with pytest.raises(ValueError):
        standard_error([])