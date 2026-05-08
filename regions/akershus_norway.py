"""Broader Akershus county deployment, Norway.

Demonstrates scalability beyond a single municipality. Akershus
(historically including Asker and surrounding municipalities) contains
varied terrain from fjord-side roads in Nesodden to inland elevation
in Nittedal and Jevnaker. Feature order matches FEATURE_NAMES in
frostguard/data.py:
    [elevation_m, temp_forecast_c, humidity_pct, water_proximity_m]
"""
from frostguard.config import RegionConfig, RoadSegment

config = RegionConfig(
    region_name="Akershus, Norway",
    segments=[
        RoadSegment("Fjord Road (Nesodden)",      [4,   -1.0, 93,    15]),
        RoadSegment("Coastal Road (Asker — Vollen)", [5, -1.2, 92,   20]),
        RoadSegment("Inland Hill (Asker — Dikemark)", [160, -3.0, 75, 1500]),
        RoadSegment("Valley Road (Lillestrøm)",   [105, -2.0, 80,  600]),
        RoadSegment("Upland Road (Nittedal)",     [280, -4.5, 65, 4000]),
        RoadSegment("Forest Road (Jevnaker)",     [320, -5.0, 60, 6000]),
    ],
)
