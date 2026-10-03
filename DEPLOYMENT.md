# Deployment evidence

Network target: **stable Studionet / chain 61999**  
RPC: `https://studio.genlayer.com/api`  
Explorer: `https://explorer-studio.genlayer.com`

No deployment evidence is invented. Replace `PENDING` only with finalized results actually produced.

## Canonical deployment

- CausalGate address: `PENDING`
- CausalGate deploy tx: `PENDING`
- CausalActionGate address: `PENDING`
- CausalActionGate deploy tx: `PENDING`
- canonical source commit: `PENDING`

## Live case

- case ID: `PENDING`
- create-case tx: `PENDING`
- evidence-source txs: `PENDING`
- candidate-cause txs: `PENDING`
- seal tx: `PENDING`
- resolve tx: `PENDING`
- definition hash: `PENDING`
- resolution hash: `PENDING`
- final result: `PENDING`
- winning candidate ID (if exclusive): `PENDING`

## Consumer proof

- correct pinned consume tx: `PENDING`
- wrong-definition-hash rejection evidence: `PENDING`
- wrong-candidate / exclusivity rejection evidence: `PENDING`
- replay rejection evidence: `PENDING`

## Verification

- `python scripts/preflight.py`: `PASS` (GitHub Actions run `37135760783`)
- `python -m compileall contracts scripts tests`: `PASS` (GitHub Actions run `37135760783`)
- `genvm-lint check contracts/causalgate.py`: `PASS` — 3 checks, validation passed
- `genvm-lint check contracts/causal_action_gate.py`: `PASS` — 3 checks, validation passed
- Direct Mode pytest: `PASS` — 26 passed, 1 live-only test skipped in 43.13s (GitHub Actions run `37135760783`)
- live stable Studionet lifecycle: `PENDING`
