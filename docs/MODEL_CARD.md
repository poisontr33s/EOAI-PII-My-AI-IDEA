# FrostGuard model card

## Model purpose

FrostGuard is a proof-of-concept model for predicting black ice risk on municipal road segments.

## Intended use

The intended user is a municipal road maintenance dispatcher or planning team.

The model should help prioritize road treatment routes before dangerous black ice becomes visible.

## Not intended for

The model is not intended to:

- replace human road maintenance judgment
- automatically control salting trucks
- provide legal guarantees of road safety
- predict every local ice event without sensor feedback

## Current model type

The current proof of concept uses logistic regression.

This is appropriate for a small educational prototype because it is explainable, lightweight, and aligned with binary classification.

## Important safety note

False negatives are the most dangerous failure mode.

A future model should be tuned and evaluated to avoid missing actual black ice events, even if this increases false positives.
