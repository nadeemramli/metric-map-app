import pytest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from metrics.computations.impact_utils.experimentation import experiment_with_models, feedback_loop

@pytest.fixture
def sample_data():
    np.random.seed(42)
    X = np.random.rand(100, 3)
    y = X[:, 0] + 2*X[:, 1] + np.random.randn(100)*0.1
    df = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3'])
    df['target'] = y
    return df

def test_experiment_with_models(sample_data):
    features = ['feature1', 'feature2', 'feature3']
    target = 'target'
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor()
    }
    results = experiment_with_models(sample_data, features, target, models)
    
    assert isinstance(results, pd.DataFrame)
    assert 'model' in results.columns
    assert 'mse' in results.columns
    assert 'model_instance' in results.columns
    assert len(results) == len(models)

def test_feedback_loop(sample_data):
    model = LinearRegression()
    X = sample_data[['feature1', 'feature2', 'feature3']]
    y = sample_data['target']
    model.fit(X[:80], y[:80])
    
    new_data = X[80:]
    actuals = y[80:]
    
    error = feedback_loop(model, new_data, actuals)
    assert isinstance(error, float)
    assert error >= 0