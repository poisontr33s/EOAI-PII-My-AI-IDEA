"""Portability example: Scottish Coastal Highlands, UK.

Demonstrates that the same classification architecture applies to
any region with equivalent environmental prerequisites.
Feature order matches FEATURE_NAMES in frostguard/data.py:
    [elevation_m, temp_forecast_c, humidity_pct, water_proximity_m]
"""
from frostguard.config import RegionConfig, RoadSegment

config = RegionConfig(
    region_name="Scottish Coastal Highlands",
    segments=[
        RoadSegment("A87 Coastal Highway", [10,  -0.5, 98,    50]),
        RoadSegment("A82 Loch Ness Road",  [35,  -1.5, 89,   200]),
        RoadSegment("A9 Highland Pass",    [420, -4.0, 72,  3000]),
    ],
)
