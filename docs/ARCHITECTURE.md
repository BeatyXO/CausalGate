# Architecture

CausalGate separates four layers: frozen causal-standard definition, independent evidence observation, bounded criterion classification, and deterministic causal outcome derivation. The model never returns ATTRIBUTED or chooses a winner.

## Atomic competing-hypothesis resolution

All candidates resolve in one nondeterministic transaction. Every validator fetches the same frozen URL set, records source availability, applies the same criteria to every candidate, and returns only the bounded assessment matrix. This prevents different candidate hypotheses from being evaluated against different evidence moments.

## Evidence surface

Exact HTTPS URLs are added only while DRAFT and committed into `definition_hash`. Basic private/local host patterns are rejected. After seal, source substitution is impossible without a new case.

## Criteria

Each criterion has a key, mode REQUIRED or SUPPORTING, expectation SUPPORTED or CONTRADICTED, and question. An expected CONTRADICTED status lets a creator encode a disqualifying proposition such as “an independently sufficient alternative cause explains the outcome.”

## Candidate derivation

Required criteria dominate. A definite opposite rejects; ambiguity/unavailability on a required criterion yields indeterminacy. Supporting criteria contribute only to the frozen threshold.

## Case derivation

Exactly one attributable candidate yields ATTRIBUTED. Multiple attributable candidates yield MULTIPLE_SUFFICIENT_CAUSES. No attributable candidate plus any indeterminate candidate yields INDETERMINATE; all rejected yields NOT_ATTRIBUTED.

## Consumer pinning

CausalActionGate pins case ID, candidate ID, expected definition hash, exclusive/non-exclusive policy, and action hash.
