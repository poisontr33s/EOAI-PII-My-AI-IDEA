# Evaluation and risk

FrostGuard should be evaluated with the safety asymmetry of black ice in mind.

In this project, false negatives matter more than false positives.

A false positive means the system warns about ice that does not form. This may waste salt, time, or route capacity.

A false negative means the system misses ice that does form. This may leave a dangerous road untreated.

Because of this, the project should prioritize:

- recall
- false-negative rate
- high-risk segment detection
- human review before operational decisions

Accuracy alone is not enough.

## Validation method

A stronger future version should be validated across a full winter season.

Predictions should be compared against:

- salting logs
- incident reports
- weather observations
- bus-mounted sensor readings
- road-surface temperature measurements
- driver or maintenance crew reports

The model should not be trusted as an autonomous decision-maker. It should support human dispatchers by highlighting likely risk zones.

## Liability note

If a municipality uses FrostGuard-like predictions operationally, responsibility must remain clearly human-supervised.

The system should be framed as decision support, not automatic road safety authority.
