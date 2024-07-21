"""
This module provides functionality for training and evaluating classification models specifically using
Random Forest classifiers. It includes functions to train a model with training data and evaluate its 
accuracy with test data.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_classifier(X_train, y_train):
    """
    Train a RandomForest classifier.

    Parameters:
        X_train (pd.DataFrame): Training feature data.
        y_train (pd.Series): Training target data.

    Returns:
        RandomForestClassifier: Trained classifier.
    """
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

def evaluate_classifier(model, X_test, y_test):
    """
    Evaluate the classifier using test data.

    Parameters:
        model (RandomForestClassifier): Trained classifier.
        X_test (pd.DataFrame): Test feature data.
        y_test (pd.Series): Test target data.

    Returns:
        float: Accuracy of the classifier.
    """
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Remove unused import and add a final newline.

"""
Example:
    >>> from sklearn.model_selection import train_test_split
    >>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    >>> model = train_classifier(X_train, y_train)
    >>> accuracy = evaluate_classifier(model, X_test, y_test)
    >>> print(f"Model Accuracy: {accuracy:.2f}%")

Notes:
    - The RandomForestClassifier from sklearn.ensemble is used due to its efficacy across a variety of classification tasks.
    - Accuracy is computed using sklearn.metrics.accuracy_score.
    - This module assumes that input data is preprocessed and suitable for model training.
"""