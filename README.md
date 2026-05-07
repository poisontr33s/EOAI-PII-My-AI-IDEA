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

---

<img width="1320" height="768" alt="image" src="https://github.com/user-attachments/assets/bbc02e6f-b800-487a-a91b-55b23370d941" />



---

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

## Challenges

The project does not solve the physical clearing of the roads; it only provides a prediction. 
Limitations include:
* **Data availability:** Historical logs of exactly where and when black ice formed in the past might be scarce, making initial training difficult.
* **Micro-climates:** Wind patterns and shadows from newly built structures might alter ice formation in ways the topographical data cannot capture.

## What next?

**Real-Time Data Integration:** The immediate next step is transitioning from a purely predictive model to a real-time reactive system. This could be achieved by partnering with local public transit authorities to install basic temperature and friction sensors on buses, feeding live, ground-truth data back into the neural network to continuously update the risk map throughout the day.

**Global & Climatic Scalability:** Because the algorithm learns thermodynamics rather than memorizing local maps, the architecture is geographically agnostic and can be deployed anywhere in the world. Furthermore, by swapping the training features (e.g., replacing cold/humidity with solar radiation and asphalt age), the exact same AI methodology can be utilized to predict extreme summer hazards like road melting and rutting.

## Acknowledgments

* Inspiration drawn from the Zen Robotics case study on optimizing physical, real-world tasks using data.
* Elements of AI / Building AI course materials by Reaktor and University of Helsinki.
* Image: My Prototype for ***Elements of AI*** — *Module* **2/2** — ***Building your own AI.***

---



---
