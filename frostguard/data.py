"""FrostGuard training data loader.

FEATURE_NAMES is the authoritative in-code contract for feature ordering.
All RoadSegment.features lists in regions/ must match this order exactly.

NOTE: load_training_data() returns synthetic data for POC purposes only.
Replace this function with real validated data before any production use.
"""
import numpy as np
from typing import Tuple

FEATURE_NAMES = ["elevation_m", "temp_forecast_c", "humidity_pct", "water_proximity_m"]


def load_training_data() -> Tuple[np.ndarray, np.ndarray]:
    """Return synthetic training data matching FEATURE_NAMES order.

    Features: [elevation_m, temp_forecast_c, humidity_pct, water_proximity_m]
    Labels:   1 = black ice formed,  0 = no ice formed
    """
    X_train = np.array([
        [150, -2.5, 85, 2000],  # Inland hill, cold, high humidity -> ice likely
        [10,   1.5, 90,   50],  # Coastal road, just above freezing -> no ice
        [120, -0.5, 70, 5000],  # Inland flat, dry, at freezing -> no ice
        [5,   -1.0, 95,   10],  # Next to fjord, freezing, very humid -> ice likely
        [250, -5.0, 60, 8000],  # High elevation, cold but dry -> no ice
        [20,  -0.5, 88,  100],  # Low elevation near water, high humidity -> ice likely
    ])
    y_train = np.array([1, 0, 0, 1, 0, 1])
    return X_train, y_train
