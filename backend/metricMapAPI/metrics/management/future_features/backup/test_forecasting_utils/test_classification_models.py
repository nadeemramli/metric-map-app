import pytest
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from metrics.computations.forecasting_utils.classification_models import train_classifier, evaluate_classifier

@pytest.fixture
def sample_data():
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    return pd.DataFrame(X), pd.Series(y)

def test_train_classifier(sample_data):
    X, y = sample_data
    model = train_classifier(X, y)
    assert model is not None
    assert hasattr(model, 'predict')

def test_evaluate_classifier(sample_data):
    X, y = sample_data
    model = train_classifier(X, y)
    accuracy = evaluate_classifier(model, X, y)
    assert 0 <= accuracy <= 1