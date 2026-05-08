"""FrostGuard entry point.

Usage
-----
    python run_frostguard.py

To target a different region, replace the import below with any module
under regions/ that exposes a `config` (RegionConfig) object.
The model, data loader, and prediction logic require no changes.

Available regions
-----------------
    from regions.asker_norway import config as region      # Asker municipality
    from regions.akershus_norway import config as region   # Broader Akershus county
    from regions.scotland_example import config as region  # Scottish Highlands
"""
from frostguard.data import load_training_data
from frostguard.model import train, evaluate
from frostguard.predict import predict_segments, print_predictions

# --- Swap region here -----------------------------------------------------------
from regions.asker_norway import config as region
# from regions.akershus_norway import config as region
# from regions.scotland_example import config as region
# --------------------------------------------------------------------------------


def main() -> None:
    X_train, y_train = load_training_data()
    model = train(X_train, y_train)
    evaluate(model, X_train, y_train)
    results = predict_segments(model, region)
    print_predictions(region.region_name, results)


if __name__ == "__main__":
    main()
