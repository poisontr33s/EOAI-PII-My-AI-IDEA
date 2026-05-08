"""FrostGuard schema: RegionConfig and RoadSegment dataclasses.

No geographic names or data live here — only the data contract.
Place-specific configurations belong in the regions/ package.
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class RoadSegment:
    name: str              # Display label only — never passed to the model
    features: List[float]  # Must match FEATURE_NAMES order defined in data.py


@dataclass
class RegionConfig:
    region_name: str
    segments: List[RoadSegment] = field(default_factory=list)
