# Data contract

FrostGuard uses environmental and road-segment features to estimate black ice risk.

## Current proof-of-concept features

| Feature | Unit | Meaning |
| --- | --- | --- |
| `elevation` | meters | Height above sea level |
| `temp_forecast` | Celsius | Expected overnight low temperature |
| `humidity` | percentage | Relative humidity |
| `water_proximity` | meters | Distance to nearest open water |

## Current label

| Label | Meaning |
| --- | --- |
| `1` | Black ice formed |
| `0` | No black ice formed |

## Portability rule

The model should not depend on Asker-specific place names.

A future implementation can retrain the same classification structure for other locations if the required features are available.

## Known limitations

The current proof of concept uses synthetic training data.

A real system would require validated historical observations, road-surface data, and local maintenance records.
