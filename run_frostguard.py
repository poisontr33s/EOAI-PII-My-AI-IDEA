"""FrostGuard entry point.

Usage
-----
    python run_frostguard.py

To target a different region, replace the import below with any module
under regions/ that exposes a `config` (RegionConfig) object. The
model, data loader, and prediction logic require no changes.

Example
-------
    # Swap Asker for the Scottish Highlands:
    from regions.scotland_example import config as region
"""
from frostguard.data import load_training_data
from frostguard.model import train, evaluate
from frostguard.predict import predict_segments, print_predictions

# --- Swap region here -----------------------------------------------------------
from regions.asker_norway import config as region
# from regions.scotland_example import config as region
# --------------------------------------------------------------------------------


def main() -> None:
    # 1. Load training data (synthetic POC — replace loader for production)
    X_train, y_train = load_training_data()

    # 2. Train
    model = train(X_train, y_train)

    # 3. Evaluate — recall is the primary safety metric
    evaluate(model, X_train, y_train)

    # 4. Predict road segments for the configured region
    results = predict_segments(model, region)
    print_predictions(region.region_name, results)


if __name__ == "__main__":
    main()
