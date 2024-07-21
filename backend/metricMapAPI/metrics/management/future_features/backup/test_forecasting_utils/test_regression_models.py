import pytest
import pandas as pd
import numpy as np
from metrics.computations.forecasting_utils.regression_models import train_regression_model, evaluate_regression_model

@pytest.fixture
def sample_data():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    y = 2*X[:, 0] + 3*X[:, 1] - X[:, 2] + np.random.randn(100)*0.1
    df = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3'])
    df['target'] = y
    return df

def test_train_regression_model(sample_data):
    model = train_regression_model(sample_data, 'target')
    assert hasattr(model, 'predict')
    assert hasattr(model, 'coef_')
    assert len(model.coef_) == 3

def test_evaluate_regression_model(sample_data):
    model = train_regression_model(sample_data, 'target')
    X_test = sample_data.drop('target', axis=1)
    y_test = sample_data['target']
    mse = evaluate_regression_model(model, X_test, y_test)
    assert isinstance(mse, float)
    assert mse >= 0