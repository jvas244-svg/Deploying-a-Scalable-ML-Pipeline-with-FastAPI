import pytest
# TODO: add necessary import
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from ml.data import apply_label
from ml.model import compute_model_metrics, inference, train_model

# TODO: implement the first test. Change the function name and input as needed
def test_apply_labels():
    """
    Test that binary labels convert to correct string
    """
    assert apply_label(np.array([1])) == ">50K"
    assert apply_label(np.array([0])) == "<=50K"

# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Test that training returns a RandomForest model
    """
    X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    y_train = np.array([0, 0, 1, 1])

    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test precision, recall, and F1 calculation
    """
    y = np.array([0, 1, 1, 0])
    preds = np.array([0, 1, 0, 0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == 1.0
    assert recall == 0.5
    assert round(fbeta, 2) == 0.67