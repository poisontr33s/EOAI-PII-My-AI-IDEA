"""FrostGuard model: training and evaluation.

Uses class_weight="balanced" to bias toward recall.
False negatives (missed ice) are the dangerous failure mode.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, precision_score, confusion_matrix
from typing import Tuple


def train(X_train: np.ndarray, y_train: np.ndarray) -> LogisticRegression:
    """Train and return a balanced logistic regression classifier."""
    model = LogisticRegression(class_weight="balanced", random_state=42)
    model.fit(X_train, y_train)
    return model


def evaluate(model: LogisticRegression, X: np.ndarray, y_true: np.ndarray) -> None:
    """Print recall-first evaluation. Recall is the primary safety metric.

    WARNING: POC uses synthetic data. Results do not reflect real-world performance.
    """
    y_pred = model.predict(X)
    recall = recall_score(y_true, y_pred, zero_division=0)
    precision = precision_score(y_true, y_pred, zero_division=0)
    cm = confusion_matrix(y_true, y_pred)

    print("\n--- Model Evaluation (WARNING: POC uses synthetic data) ---")
    print(f"Recall (primary):   {recall:.2f}  ← missed ice is the dangerous failure")
    print(f"Precision:          {precision:.2f}")
    print(f"Confusion matrix:\n{cm}")
