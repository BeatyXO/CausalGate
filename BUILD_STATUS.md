# Build status

Pre-Codex handoff status only — not a live deployment claim.

Implemented and hardened before Codex handoff: frozen causal-standard schema; exact HTTPS evidence-surface freezing; competing candidate registration; atomic all-candidate resolution against one per-validator evidence fetch cycle; independent validator source re-fetch and semantic re-evaluation; strict exact-shape model parsing; deterministic REQUIRED/SUPPORTING causal logic; minimum source availability; deterministic multiple-sufficient-causes handling; domain-separated hashes; typed downstream consumer; replay protection; adversarial Direct Mode suite; preflight, CI and documentation.

Final ChatGPT hardening also added:
- literal IPv6 evidence hosts are rejected instead of receiving incomplete private-range validation;
- a source counts toward `min_sources_available` only when non-empty text actually enters the bounded evidence bundle;
- runtime-compatible typed `DynArray` initialization matching successful GenLayer reference ICs;
- runtime-compatible event emission for the pinned Direct Mode SDK;
- expanded adversarial coverage for threshold bounds, minimum-source bounds, supporting-evidence uncertainty, duplicate candidate statements, IPv6/local-source rejection, malformed/duplicate/omitted model rows and forged leader matrices.

## Verified locally

- `python scripts/preflight.py` — PASS;
- Python compilation — PASS;
- local/static pytest — 9 passed, with Direct Mode and live Studionet intentionally unavailable in this container.

## Verified by GitHub Actions with the pinned GenLayer tooling

GitHub Actions run `37135760783` on commit `8db459e78497f873de578cdcead78b5c434b523e` independently installed `genlayer-test==0.29.2` and `genvm-linter==0.11.0` and produced:

- preflight — PASS;
- Python compilation — PASS;
- `genvm-lint check contracts/causalgate.py` — PASS (`3 checks`, validation passed);
- `genvm-lint check contracts/causal_action_gate.py` — PASS (`3 checks`, validation passed);
- full pytest / Direct Mode — **26 passed, 1 skipped** in 43.13s;
- the single skipped test is the live Studionet lifecycle, which requires authenticated/funded stable-chain execution.

The live fixture URLs remain pinned to immutable commit `65f8ce6da8a0e14bad39bd8e51ce801194e590b1`, which contains the fixture files.

## Remaining work

Only environment-specific live work remains: deploy on stable Studionet chain `61999`, execute the real causal lifecycle and consumer proof, record finalized addresses/transactions/hashes in `DEPLOYMENT.md`, run `python scripts/preflight.py --final`, and push the final live-evidence commit.
