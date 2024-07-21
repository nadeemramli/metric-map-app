"""
This module contains functions for training and evaluating regression models.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_regression_model(data, target):
    """
    Train a linear regression model.

    Parameters:
        data (pd.DataFrame): DataFrame containing features and target.
        target (str): Target column name.

    Returns:
        LinearRegression: Trained linear regression model.
    """
    X = data.drop(columns=[target])
    y = data[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

def evaluate_regression_model(model, X_test, y_test):
    """
    Evaluate the regression model using test data.

    Parameters:
        model (LinearRegression): Trained linear regression model.
        X_test (pd.DataFrame): Test feature data.
        y_test (pd.Series): Test target data.

    Returns:
        float: Mean squared error of the model.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse

# Add necessary imports and ensure they are used.
