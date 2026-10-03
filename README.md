# CausalGate

**Consensus-backed application of a frozen causal standard for GenLayer.**

CausalGate is a standalone reusable Intelligent Contract primitive. A case freezes an outcome, a bounded causal test, an evidence surface, and competing candidate causes. GenLayer validators independently fetch the same frozen evidence and classify every candidate against every criterion. Deterministic protocol logic — not the LLM — decides whether a candidate is attributable and whether the final case is `ATTRIBUTED`, `NOT_ATTRIBUTED`, `INDETERMINATE`, or `MULTIPLE_SUFFICIENT_CAUSES`.

There is **no frontend**.

## Why it exists

Smart contracts can easily record that Event A and Event B happened. Many downstream systems need a more constrained question: **does candidate A satisfy a predefined causal standard for outcome B, given this exact evidence surface?**

A weak implementation would ask an LLM “did A cause B?” and store yes/no. CausalGate deliberately does not do that.

The creator must define the causal standard **before** resolution. Validators only classify evidence against that frozen standard. The final attribution result is deterministic.

## Protocol

1. Create a DRAFT case with an outcome and frozen criterion schema.
2. Add 1–6 exact HTTPS evidence URLs.
3. Add 1–5 competing candidate causes.
4. Seal the case. Sealing freezes every criterion, source URL, and candidate into `definition_hash`.
5. `resolve_case` performs one atomic consensus evaluation across **all candidates using the same evidence fetch cycle**.
6. Validators independently re-fetch every source and re-evaluate every candidate/criterion.
7. Deterministic logic derives each candidate as `ATTRIBUTABLE`, `REJECTED`, or `INDETERMINATE`.
8. Deterministic case logic derives the final result.
9. `CausalActionGate` proves another IC can require a pinned causal result and reject replay.

## Frozen criterion model

Each criterion contains a stable key, mode `REQUIRED` or `SUPPORTING`, expected result `SUPPORTED` or `CONTRADICTED`, and a bounded causal proposition. The model may return only `SUPPORTED`, `CONTRADICTED`, `AMBIGUOUS`, or `UNAVAILABLE`.

For REQUIRED criteria, only the expected status satisfies the criterion. A definite opposite rejects the candidate; ambiguity/unavailability makes it indeterminate. SUPPORTING criteria use the creator-frozen threshold. A frozen minimum evidence-source availability prevents certainty when too much of the evidence surface is unavailable.

## Deterministic case result

- exactly one attributable candidate => `ATTRIBUTED`
- more than one attributable candidate => `MULTIPLE_SUFFICIENT_CAUSES`
- none attributable, but at least one indeterminate => `INDETERMINATE`
- every candidate rejected => `NOT_ATTRIBUTED`

The LLM never selects the winner and never chooses the case result.

## Why one atomic resolution matters

Assessing candidate causes in separate transactions could expose different candidates to different versions of a changing evidence page. CausalGate resolves every frozen candidate from one evidence-fetch cycle per validator, so competing hypotheses are judged against a common evidence moment.

## Hashes

- `CAUSALGATE_CANDIDATE_V1`
- `CAUSALGATE_DEFINITION_V1`
- `CAUSALGATE_RESOLUTION_V1`

Consumers pin the exact final `definition_hash`, not merely `case_id`.

## Consumer contract

`contracts/causal_action_gate.py` performs a real typed IC-to-IC read. A consumer can require attribution including a multiple-sufficient-causes result, or require **exclusive** attribution to one candidate. It also rejects replayed action hashes.

## Scope

CausalGate applies a user-declared causal standard to a frozen evidence surface. It is not a universal proof of causation and does not replace domain experts, courts, scientific methods, incident investigators, medical judgment, or legal standards.

## Stable network target

- alias: `studionet`
- chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- explorer: `https://explorer-studio.genlayer.com`

## Verification

```bash
python -m pip install -r requirements-test.txt
python scripts/preflight.py
python -m compileall contracts scripts tests
genvm-lint check contracts/causalgate.py
genvm-lint check contracts/causal_action_gate.py
pytest -q
```

Final gate after live proof:

```bash
python scripts/preflight.py --final
```
