"""
This module contains functions for ensemble models.
"""

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

def train_ensemble_model(data, target):
    """
    Train an ensemble model.

    Parameters:
        data (pd.DataFrame): DataFrame containing features and target.
        target (str): Target column name.

    Returns:
        model: Trained ensemble model.
    """
    X = data.drop(columns=[target])
    y = data[target]

    model = GradientBoostingRegressor()
    model.fit(X, y)

    return model

def evaluate_ensemble_model(model, X_test, y_test):
    """
    Evaluate the ensemble model using test data.

    Parameters:
        model (GradientBoostingRegressor): Trained ensemble model.
        X_test (pd.DataFrame): Test feature data.
        y_test (pd.Series): Test target data.

    Returns:
        float: Mean squared error of the model.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Remove unused import and trailing whitespaces.
