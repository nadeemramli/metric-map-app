import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def experiment_with_models(data, features, target, models):
    """
    Experiment with different models on the provided dataset.

    Parameters:
        data (pd.DataFrame): Dataset containing features and target.
        features (list): List of feature column names.
        target (str): Target column name.
        models (dict): Dictionary of models to experiment with.

    Returns:
        pd.DataFrame: DataFrame containing model performance metrics.
    """
    X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2)
    results = []
    
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        
        results.append({
            'model': model_name,
            'mse': mse,
            'model_instance': model
        })
    
    return pd.DataFrame(results)

def feedback_loop(model, new_data, actuals):
    """
    Update model based on new data and actual values.

    Parameters:
        model (object): Trained model instance.
        new_data (pd.DataFrame): New data for making predictions.
        actuals (pd.Series): Actual values for the new data.

    Returns:
        float: Mean squared error after the update.
    """
    predictions = model.predict(new_data)
    error = mean_squared_error(actuals, predictions)
    
    # Update model or process based on feedback
    model.fit(new_data, actuals)
    
    return error

# Remove trailing whitespaces and add a final newline.
