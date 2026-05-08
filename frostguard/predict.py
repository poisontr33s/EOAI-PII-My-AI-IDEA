"""FrostGuard prediction runner."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from typing import List, Tuple

from frostguard.config import RegionConfig

HIGH_RISK_THRESHOLD = 60.0  # percent — segments at or above this get dispatcher flag


def predict_segments(
    model: LogisticRegression, region: RegionConfig
) -> List[Tuple[str, float]]:
    """Return (segment_name, risk_pct) for every segment in the region."""
    results = []
    for segment in region.segments:
        features = np.array([segment.features])
        risk_pct = model.predict_proba(features)[0][1] * 100
        results.append((segment.name, risk_pct))
    return results


def print_predictions(region_name: str, results: List[Tuple[str, float]]) -> None:
    """Print risk predictions, flagging high-risk segments for dispatcher review."""
    print(f"\n--- FrostGuard: {region_name} ---")
    for name, risk_pct in results:
        flag = (
            "  ⚠️  HIGH RISK — recommend dispatcher review"
            if risk_pct >= HIGH_RISK_THRESHOLD
            else ""
        )
        print(f"{name}: {risk_pct:.1f}% risk of black ice.{flag}")
