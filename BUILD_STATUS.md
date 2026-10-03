# Build status

Pre-Codex handoff status only — not a deployment claim.

Implemented before Codex/live-runtime handoff: frozen causal-standard schema; exact HTTPS evidence-surface freezing; competing candidate registration; atomic all-candidate resolution against one per-validator evidence fetch cycle; independent validator source re-fetch and semantic re-evaluation; strict exact-shape model parsing; deterministic REQUIRED/SUPPORTING causal logic; minimum source availability; deterministic multiple-sufficient-causes handling; domain-separated hashes; typed downstream consumer; adversarial Direct Mode suite; preflight, CI and documentation.

Additional hardening completed in the final ChatGPT pass:
- literal IPv6 evidence hosts are rejected instead of receiving incomplete private-range validation;
- a source counts toward `min_sources_available` only when non-empty text actually enters the bounded evidence bundle;
- Direct Mode coverage was expanded for threshold bounds, minimum-source bounds, supporting-evidence uncertainty, duplicate candidate statements and IPv6/local-source rejection.

Verified in the packaging environment:
- `python scripts/preflight.py` — PASS;
- Python compilation — PASS;
- local/static pytest — 9 passed;
- Direct Mode module skipped because `genlayer-test` is not installed in this container;
- live Studionet specification skipped because authenticated/funded stable Studionet execution is unavailable here.

Current stable package references were independently checked on 2026-10-03: `genlayer-test==0.29.2` and `genvm-linter==0.11.0` are stable PyPI releases. Studionet remains chain `61999` at `https://studio.genlayer.com/api`.

Still requires a GenLayer-enabled finishing environment: real Direct Mode execution, GenVM lint, any genuine runtime fixes they expose, stable Studionet deployment, real transaction evidence, final deployment documentation and `python scripts/preflight.py --final`.
