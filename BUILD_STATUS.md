# Build status

**Final verified state — live deployment complete.**

CausalGate is implemented, hardened, tested, deployed on stable Studionet, and backed by finalized consumer proof. This file reflects the completed repository state rather than the earlier pre-Codex handoff.

## Implemented protocol

The final implementation includes:

- frozen causal-standard schema;
- exact HTTPS evidence-surface freezing;
- competing candidate registration;
- atomic all-candidate resolution against one per-validator evidence-fetch cycle;
- independent validator source re-fetch and semantic re-evaluation;
- strict exact-shape model parsing;
- deterministic REQUIRED/SUPPORTING causal logic;
- minimum usable-source availability;
- deterministic multiple-sufficient-causes handling;
- domain-separated candidate, definition and resolution hashes;
- typed downstream `CausalActionGate` consumer;
- definition-hash pinning and action replay protection;
- conservative public-source validation;
- adversarial Direct Mode coverage;
- preflight, CI and reviewer-facing documentation.

Additional hardening includes:

- literal IPv6 evidence hosts are rejected instead of receiving incomplete private-range validation;
- a source counts toward `min_sources_available` only when non-empty text actually enters the bounded evidence bundle;
- runtime-compatible typed `DynArray` initialization;
- runtime-compatible event emission for the pinned GenLayer tooling;
- adversarial coverage for threshold bounds, minimum-source bounds, supporting-evidence uncertainty, duplicate candidate statements, IPv6/local-source rejection, malformed/duplicate/omitted model rows and forged leader matrices.

## Final automated verification

GitHub Actions run `37140339053` on final repository commit `6771baae90bd8fdbb0613763cf489139827694f5` completed successfully:

- `python scripts/preflight.py` — PASS;
- Python compilation — PASS;
- `genvm-lint check contracts/causalgate.py` — PASS, validation passed;
- `genvm-lint check contracts/causal_action_gate.py` — PASS, validation passed;
- Direct Mode/full pytest — **26 passed, 1 skipped** in 55.69s;
- the sole skipped test is the authenticated live Studionet lifecycle, which was executed separately and is documented in `DEPLOYMENT.md`.

The deployed contract source is commit `067dc16f86b4c35d63feb0b9a9fc6e9ef71efbbe`. The contract blobs at final repository HEAD are identical to that deployed source.

## Final live verification

Stable Studionet / chain `61999` proof is complete and recorded in `DEPLOYMENT.md`:

- CausalGate deployed and finalized;
- CausalActionGate deployed and finalized;
- Alpha outage case configured with three immutable evidence sources and three competing causes;
- case sealed with a non-empty definition hash;
- atomic causal resolution finalized;
- result: `ATTRIBUTED`, exclusive winner candidate `1`;
- correct pinned consumer action succeeded;
- wrong-definition request rejected;
- rejected-candidate/exclusivity request rejected;
- action replay rejected;
- final preflight completed successfully.

Live evidence fixtures remain pinned to immutable commit `65f8ce6da8a0e14bad39bd8e51ce801194e590b1`.

## Status

**No implementation or deployment work remains for the submitted CausalGate lifecycle.**

Future changes should be treated as a new revision and should not overwrite or reinterpret the finalized evidence documented for this deployment.
