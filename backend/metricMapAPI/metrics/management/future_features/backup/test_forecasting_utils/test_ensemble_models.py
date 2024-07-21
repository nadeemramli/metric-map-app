import pytest
import pandas as pd
import numpy as np
from sklearn.datasets import make_regression
from metrics.computations.forecasting_utils.ensemble_models import train_ensemble_model, evaluate_ensemble_model

@pytest.fixture
def sample_data():
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(5)])
    data['target'] = y
    return data

def test_train_ensemble_model(sample_data):
    model = train_ensemble_model(sample_data, 'target')
    assert model is not None
    assert hasattr(model, 'predict')

def test_evaluate_ensemble_model(sample_data):
    model = train_ensemble_model(sample_data, 'target')
    X_test = sample_data.drop(columns=['target'])
    y_test = sample_data['target']
    mse = evaluate_ensemble_model(model, X_test, y_test)
    assert mse >= 0