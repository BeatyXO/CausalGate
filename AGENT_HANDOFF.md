# Codex finishing handoff

CausalGate is substantially implemented and hardened. Preserve the architecture unless the actual stable GenLayer runtime proves a concrete compatibility change is necessary.

The repository is already published at `BeatyXO/CausalGate`. Its live fixture URLs are pinned to immutable commit `65f8ce6da8a0e14bad39bd8e51ce801194e590b1`, which contains the fixture files. Do not repin merely because later source commits exist; repin only if you intentionally change fixture contents or the live lifecycle needs different immutable evidence.

Code-side work already completed includes frozen causal standards, exact evidence-source freezing, competing hypotheses, one atomic all-candidate resolution per validator evidence cycle, independent validator re-fetch/re-evaluation, strict exact-shape model parsing, deterministic REQUIRED/SUPPORTING logic, minimum source availability, explicit multiple-sufficient-cause handling, definition/result hashes, typed downstream consumer, replay protection, conservative public-source validation and adversarial tests.

Remaining work is environment-specific:
1. install the pinned stable test/lint tooling;
2. run real `genlayer-test` Direct Mode and both `genvm-lint` checks;
3. fix only genuine runtime incompatibilities without weakening protocol safeguards;
4. use stable `studionet`, chain 61999, only;
5. execute the immutable Alpha-outage live lifecycle;
6. deploy CausalGate and CausalActionGate;
7. prove correct consume, wrong-definition, wrong-candidate/exclusivity and replay behavior;
8. update `DEPLOYMENT.md` only with real finalized evidence;
9. run `python scripts/preflight.py --final`;
10. commit/push and inspect final GitHub state.
