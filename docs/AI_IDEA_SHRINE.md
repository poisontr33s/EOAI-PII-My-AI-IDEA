# FrostGuard — AI idea shrine

FrostGuard is a localized black ice prediction concept for municipal winter road maintenance.

The core idea is not “AI for road safety” in general. The project is narrower and stronger than that:

> FrostGuard predicts where invisible black ice is likely to form before it becomes visible.

The first use case is Asker, Norway, where coastal moisture, elevation, terrain shadows, and overnight temperature shifts can create dangerous hyper-local ice conditions.

The project treats black ice as a classification problem:

- input: environmental and road-segment features
- output: ice risk / no ice risk
- user: municipal road maintenance dispatcher
- action: prioritize salting and road treatment routes

The important design principle is portability.

FrostGuard should learn road-surface risk conditions, not local place names. Asker is the first test surface, not the final boundary of the idea.

## Canonical project sentence

FrostGuard is a portable, human-supervised, false-negative-sensitive AI risk classifier for invisible winter road hazards.
