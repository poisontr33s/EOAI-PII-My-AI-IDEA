import numpy as np
from sklearn.linear_model import LogisticRegression

# 1. GENERATE SYNTHETIC TRAINING DATA
# Features: [elevation (m), temp_forecast (C), humidity (%), water_proximity (m)]
# We create dummy data to simulate historical road conditions.

X_train = np.array([
    [150, -2.5, 85, 2000],  # Inland hill, cold, high humidity -> Ice likely
    [10,   1.5, 90, 50],    # Coastal road, just above freezing -> No Ice
    [120, -0.5, 70, 5000],  # Inland flat, dry, freezing -> No Ice
    [5,   -1.0, 95, 10],    # Right next to the fjord, freezing, very humid -> Ice likely
    [250, -5.0, 60, 8000],  # High elevation, very cold but dry -> No Ice
    [20,  -0.5, 88, 100]    # Low elevation near water, high humidity -> Ice likely
])

# Labels: 1 = Black Ice formed, 0 = No Ice formed
y_train = np.array([1, 0, 0, 1, 0, 1])

# 2. TRAIN THE AI MODEL
# We use Logistic Regression, a core concept from the Elements of AI course.
model = LogisticRegression()
model.fit(X_train, y_train)

# 3. TEST THE PROTOTYPE ON NEW, UNSEEN ROADS (The "Asker" Scenarios)
# Let's predict the ice risk for three hypothetical road segments tonight.

print("--- FrostGuard Prediction Prototype ---\n")

# Scenario A: Vollen coastal road (low elevation, near fjord, high humidity)
road_a = np.array([[5, -1.2, 92, 20]])
prob_a = model.predict_proba(road_a)[0][1]
print(f"Coastal Road (Vollen): {prob_a * 100:.1f}% risk of black ice.")

# Scenario B: Dikemark inland (higher elevation, further from water, drier)
road_b = np.array([[160, -3.0, 75, 1500]])
prob_b = model.predict_proba(road_b)[0][1]
print(f"Inland Road (Dikemark): {prob_b * 100:.1f}% risk of black ice.")

# Scenario C: Asker Sentrum (moderate elevation, moderate humidity)
road_c = np.array([[100, 0.5, 80, 4000]])
prob_c = model.predict_proba(road_c)[0][1]
print(f"City Center (Asker Sentrum): {prob_c * 100:.1f}% risk of black ice.")
