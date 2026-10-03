# Codex finishing handoff

CausalGate is substantially implemented, hardened, and already green under the pinned real GenLayer Direct Mode/lint toolchain. Preserve the architecture unless stable Studionet itself proves a concrete compatibility change is necessary.

Repository: `https://github.com/BeatyXO/CausalGate.git`

The live fixture URLs are pinned to immutable commit `65f8ce6da8a0e14bad39bd8e51ce801194e590b1`, which contains the fixture files. Do not repin merely because later source commits exist; repin only if you intentionally change fixture contents or the live lifecycle requires different immutable evidence.

## Already verified

GitHub Actions run `37135760783` on commit `8db459e78497f873de578cdcead78b5c434b523e` verified:
- preflight PASS;
- Python compilation PASS;
- both GenVM lint checks PASS;
- Direct Mode/full pytest: 26 passed, 1 skipped;
- the one skipped test is the authenticated/funded live Studionet lifecycle.

Code-side work already completed includes frozen causal standards, exact evidence-source freezing, competing hypotheses, one atomic all-candidate resolution per validator evidence cycle, independent validator re-fetch/re-evaluation, strict exact-shape model parsing, deterministic REQUIRED/SUPPORTING logic, minimum usable-source availability, explicit multiple-sufficient-cause handling, definition/result hashes, typed downstream consumer, replay protection, conservative public-source validation and adversarial tests.

## Remaining Codex work

1. Pull the current `main` branch and re-run preflight, compilation, both GenVM linters and pytest as a regression check. Do not redesign a green protocol.
2. Verify the effective network is stable `studionet`, chain ID `61999`, before every live write.
3. Execute the immutable Alpha-outage live lifecycle.
4. Deploy CausalGate and CausalActionGate.
5. Record only real finalized addresses, transactions, definition/resolution hashes and result evidence.
6. Prove the consumer succeeds for the correct pinned definition/candidate and rejects wrong definition hash, wrong candidate/exclusivity and action replay.
7. Update `DEPLOYMENT.md` only with evidence actually produced.
8. Run `python scripts/preflight.py --final`.
9. Commit/push the live-evidence changes and inspect the final GitHub state.

Do not weaken tests or consensus safeguards, change networks for convenience, or invent live evidence.
