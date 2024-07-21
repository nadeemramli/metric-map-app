import pytest
import pandas as pd
import numpy as np
from metrics.computations.impact_utils.predictive_maintenance import train_predictive_model, predict_failure

@pytest.fixture
def sample_data():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    y = X[:, 0] + 2*X[:, 1] - X[:, 2] + np.random.randn(100)*0.1
    df = pd.DataFrame(X, columns=['sensor1', 'sensor2', 'sensor3'])
    df['failure_time'] = y
    return df

def test_train_predictive_model(sample_data):
    model = train_predictive_model(sample_data, 'failure_time')
    assert hasattr(model, 'predict')
    assert hasattr(model, 'feature_importances_')

def test_predict_failure(sample_data):
    model = train_predictive_model(sample_data, 'failure_time')
    new_data = sample_data.drop('failure_time', axis=1).iloc[:10]
    predictions = predict_failure(model, new_data)
    
    assert isinstance(predictions, np.ndarray)
    assert len(predictions) == len(new_data)
    assert all(isinstance(pred, (float, np.float64)) for pred in predictions)