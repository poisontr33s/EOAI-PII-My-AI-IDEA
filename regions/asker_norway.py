"""Reference deployment: Asker municipality, Akershus, Norway.

Segments represent characteristic coastal and inland road conditions
around Asker. Feature order matches FEATURE_NAMES in frostguard/data.py:
    [elevation_m, temp_forecast_c, humidity_pct, water_proximity_m]
"""
from frostguard.config import RegionConfig, RoadSegment

config = RegionConfig(
    region_name="Asker, Norway",
    segments=[
        RoadSegment("Coastal Road (Vollen)",   [5,   -1.2, 92,    20]),
        RoadSegment("Inland Road (Dikemark)",  [160, -3.0, 75,  1500]),
        RoadSegment("Fjord-side Road (Sætre)", [8,   -0.8, 91,    30]),
    ],
)
