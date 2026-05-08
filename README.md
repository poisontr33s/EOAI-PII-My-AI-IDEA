# FrostGuard: Localized Ice Prediction

Final project for the Building AI course

## Summary

FrostGuard is a predictive model designed to identify high-risk zones for black ice on municipal roads before they form. By combining micro-topography with local weather data, this Building AI course project aims to optimize snowplow and salting routes to improve winter road safety in complex coastal climates like Asker.

## Background

Winter road maintenance is often reactive or based on broad regional weather forecasts. However, ice forms based on hyper-local conditions (elevation, proximity to water, shadows from terrain). 
This creates several problems:
* **Safety risks:** Drivers encounter unexpected black ice in micro-climates where coastal moisture freezes rapidly.
* **Resource waste:** Municipalities salt entire road networks when only specific zones require it.
* **Environmental impact:** Over-salting damages local flora and freshwater systems flowing into the fjord.

The motivation is to make local roads safer while helping municipal maintenance crews deploy their limited resources (salt, grit, and plows) more efficiently. 

## How is it used?

The solution is designed to be used by municipal road maintenance dispatchers as a dashboard tool. 

Every evening, the system pulls the overnight weather forecast and cross-references it with the municipal road map. It highlights specific road segments in red (high risk of ice) or green (low risk). The dispatcher uses this map to prioritize the morning routes for the salting trucks, ensuring the most dangerous curves, steep hills, and moisture-heavy coastal roads are treated first.

<img width="1320" height="768" alt="image" src="https://github.com/user-attachments/assets/bbc02e6f-b800-487a-a91b-55b23370d941" />

## Pitch Video

### ▶️ [Watch FrostGuard Sample Pitch](https://github.com/user-attachments/assets/f24f51a9-44c0-4ab2-9e1d-578f91c5ad75)

*This short atmospheric pitch video presents the project concept with its generated visual and audio layer.*

## Data sources and AI methods

The project relies on two primary data sources:
1.  **Topographical Data:** Open-source map data (like OpenStreetMap or local government GIS data) detailing road elevation, curve sharpness, and proximity to water bodies.
2.  **Meteorological Data:** API feeds from the national meteorological institute providing temperature, humidity, and precipitation forecasts.

**AI Method:**
This is a binary classification problem (Ice vs. No Ice). A **Logistic Regression** model or a shallow **Neural Network** could be trained on historical weather data and past traffic accident/ice report logs. 

| Feature | Description |
| ----------- | ----------- |
| `elevation` | Height above sea level (meters) |
| `temp_forecast` | Expected overnight low (°C) |
| `humidity` | Relative humidity percentage |
| `water_proximity`| Distance to nearest open water (meters) |

## Project architecture note

FrostGuard is intentionally designed as a geographically agnostic classification system.

The first use case is coastal Asker, Norway, where black ice can form under highly local conditions near fjords, hills, shaded terrain, and moisture-heavy road segments.

The model does not attempt to memorize Asker as a map. Instead, it classifies road-surface risk from transferable environmental features:

| Feature | Role |
| --- | --- |
| `elevation` | Captures altitude-related freezing conditions |
| `temp_forecast` | Estimates overnight freezing risk |
| `humidity` | Captures available moisture for ice formation |
| `water_proximity` | Captures coastal/fjord moisture exposure |

This makes the architecture portable: the same classification pattern can be retrained for other regions, climates, and road hazards when the input features are replaced or extended.

## Challenges

The project does not solve the physical clearing of the roads; it only provides a prediction. 
Limitations include:
* **Data availability:** Historical logs of exactly where and when black ice formed in the past might be scarce, making initial training difficult.
* **Micro-climates:** Wind patterns and shadows from newly built structures might alter ice formation in ways the topographical data cannot capture.

### Risk asymmetry

False negatives are more dangerous than false positives.

A false positive may cause unnecessary salting or route prioritization.  
A false negative may leave a dangerous road untreated and increase accident risk.

For that reason, the first evaluation target should prioritize recall: the system should prefer warning too often over missing hazardous ice formation.

## What next?

**Real-Time Data Integration:** The immediate next step is transitioning from a purely predictive model to a real-time reactive system. This could be achieved by partnering with local public transit authorities to install basic temperature and friction sensors on buses, feeding live, ground-truth data back into the neural network to continuously update the risk map throughout the day.

**Global & Climatic Scalability:** Because the algorithm learns thermodynamics rather than memorizing local maps, the architecture is geographically agnostic and can be deployed anywhere in the world. Furthermore, by swapping the training features (e.g., replacing cold/humidity with solar radiation and asphalt age), the exact same AI methodology can be utilized to predict extreme summer hazards like road melting and rutting.

### Validation plan

A future version should be validated against a full winter season rather than isolated examples.

The model could be tested by comparing predicted high-risk road segments with:

- municipal salting logs
- public road incident reports
- bus-mounted temperature or friction sensors
- meteorological observations
- driver reports of black ice

The success metric should not only be accuracy. Because missed ice is the dangerous failure mode, recall and false-negative rate should be tracked explicitly.

## Acknowledgments

* Inspiration drawn from the Zen Robotics case study on optimizing physical, real-world tasks using data.
* Elements of AI / Building AI course materials by Reaktor and University of Helsinki.
* Visual and pitch media: Prototype material for ***Elements of AI*** — *Module* **2/2** — ***Building Your Own AI.***