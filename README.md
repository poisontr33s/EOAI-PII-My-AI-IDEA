# FrostGuard: Localized Ice Prediction

Final project for the Building AI course

## Summary

FrostGuard is a predictive model designed to identify high-risk zones for black ice on municipal roads before they form. By combining micro-topography with local weather data, this Building AI course project aims to optimize snowplow and salting routes to improve winter road safety.

## Background

Winter road maintenance is often reactive or based on broad regional weather forecasts. However, ice forms based on hyper-local conditions (elevation, proximity to water, shadows from terrain). 
This creates several problems:
* **Safety risks:** Drivers encounter unexpected black ice in micro-climates.
* **Resource waste:** Municipalities salt entire road networks when only specific zones require it.
* **Environmental impact:** Over-salting damages local flora and freshwater systems.

My motivation is to make local roads safer while helping municipal maintenance crews deploy their limited resources (salt, grit, and plows) more efficiently. 

## How is it used?

The solution is designed to be used by municipal road maintenance dispatchers as a dashboard tool. 

Every evening, the system pulls the overnight weather forecast and cross-references it with the municipal road map. It highlights specific road segments in red (high risk of ice) or green (low risk). The dispatcher uses this map to prioritize the morning routes for the salting trucks, ensuring the most dangerous curves and hills are treated first.

![Black ice on road](https://upload.wikimedia.org/wikipedia/commons/4/41/Black_ice_on_road.jpg)

## Data sources and AI methods

The project relies on two primary data sources:
1.  **Topographical Data:** Open-source map data (like OpenStreetMap or local government GIS data) detailing road elevation, curve sharpness, and proximity to water bodies (like fjords or lakes).
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

The next step would be to transition from a purely predictive model to a real-time reactive model. This could be achieved by partnering with a local public transit authority to install basic temperature and friction sensors on buses, feeding live, ground-truth data back into the neural network to continuously update the risk map throughout the day.

## Acknowledgments

* Inspiration drawn from the Zen Robotics case study on optimizing physical, real-world tasks using data.
* Elements of AI / Building AI course materials by Reaktor and University of Helsinki.
* Image: [Black ice on road](https://commons.wikimedia.org/wiki/File:Black_ice_on_road.jpg) by Tennen-Gas / Licensed under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
