# Deployment evidence

Network: **stable Studionet / chain 61999**
RPC: `https://studio.genlayer.com/api`
Explorer: [GenLayer Studio Explorer](https://explorer-studio.genlayer.com)

All transaction hashes and contract addresses below are from finalized live Studionet transactions. The deployed source is commit `067dc16f86b4c35d63feb0b9a9fc6e9ef71efbbe`.

## Canonical deployment

| Contract | Finalized address | Deployment transaction |
|---|---|---|
| CausalGate | `0x0e2744A55E5B79f90202305D433f75aA271cbD31` | [`0x8f4f98071ae861c1f3af07ce53576a8a999b22c7f7cf0d071fb3030f2fabc843`](https://explorer-studio.genlayer.com/tx/0x8f4f98071ae861c1f3af07ce53576a8a999b22c7f7cf0d071fb3030f2fabc843) |
| CausalActionGate | `0x1B7E1ebF25A30b564887eB288286eBFfef42a2Ba` | [`0x1f4a7d4f05bf798afc7346dd80ebecda47f087ba7167f3298696190f8877e58a`](https://explorer-studio.genlayer.com/tx/0x1f4a7d4f05bf798afc7346dd80ebecda47f087ba7167f3298696190f8877e58a) |

Both deployment receipts finalized successfully. CausalActionGate was constructed with the CausalGate address above.

## Alpha outage case

- Case ID: `1`
- Create-case transaction: [`0x91fc2a063e697d343cf975645f90592399bdaf20620be5ae9e88deb34f61a2d2`](https://explorer-studio.genlayer.com/tx/0x91fc2a063e697d343cf975645f90592399bdaf20620be5ae9e88deb34f61a2d2)
- Outcome: Alpha Marketplace unavailable from 10:02 to 11:34 UTC
- Supporting threshold: `1`
- Minimum usable sources: `2`

### Frozen evidence surface

All three sources were reported AVAILABLE in the finalized resolution. Each URL is pinned to fixture commit `65f8ce6da8a0e14bad39bd8e51ce801194e590b1`.

| Source | Immutable URL | Write transaction |
|---|---|---|
| Provider incident | `https://raw.githubusercontent.com/BeatyXO/CausalGate/65f8ce6da8a0e14bad39bd8e51ce801194e590b1/fixtures/provider_incident.txt` | [`0x28c1fdabe445860cabcf43250a92ddc4440cc145b721747672fb7b4d24489530`](https://explorer-studio.genlayer.com/tx/0x28c1fdabe445860cabcf43250a92ddc4440cc145b721747672fb7b4d24489530) |
| Deployment report | `https://raw.githubusercontent.com/BeatyXO/CausalGate/65f8ce6da8a0e14bad39bd8e51ce801194e590b1/fixtures/deployment_report.txt` | [`0x6ada1838427bba0925638429767f6d2f9b9924d186e8c320aca27222f8425fb6`](https://explorer-studio.genlayer.com/tx/0x6ada1838427bba0925638429767f6d2f9b9924d186e8c320aca27222f8425fb6) |
| Traffic report | `https://raw.githubusercontent.com/BeatyXO/CausalGate/65f8ce6da8a0e14bad39bd8e51ce801194e590b1/fixtures/traffic_report.txt` | [`0x669bd465850fd9d250f6199842365930553ef9ea10e97095c073a0d6afb5e7ae`](https://explorer-studio.genlayer.com/tx/0x669bd465850fd9d250f6199842365930553ef9ea10e97095c073a0d6afb5e7ae) |

### Competing candidates

| Candidate ID | Frozen cause | Registration transaction |
|---:|---|---|
| 1 | Nimbus regional networking outage caused Alpha Marketplace unavailability. | [`0xbdb912dc27bf314c29dab2091ad6f33387e3b3bc4c40cf693930864be9964c12`](https://explorer-studio.genlayer.com/tx/0xbdb912dc27bf314c29dab2091ad6f33387e3b3bc4c40cf693930864be9964c12) |
| 2 | The prior Alpha software deployment caused the outage. | [`0x7f469a95370940d9e4986ccfc6487d0fa522632a3838e35da926f4c6e444983e`](https://explorer-studio.genlayer.com/tx/0x7f469a95370940d9e4986ccfc6487d0fa522632a3838e35da926f4c6e444983e) |
| 3 | A denial-of-service attack caused the outage. | [`0xb1dbb058029afa2588e5340c17560880884db0cc71ccbcb4f5a6aa9f53f7fcca`](https://explorer-studio.genlayer.com/tx/0xb1dbb058029afa2588e5340c17560880884db0cc71ccbcb4f5a6aa9f53f7fcca) |

### Seal and atomic resolution

- Seal transaction: [`0xc0680f988d7f6617558a2293cf197e545f86d7af12055e4b66eb8f95c61343fb`](https://explorer-studio.genlayer.com/tx/0xc0680f988d7f6617558a2293cf197e545f86d7af12055e4b66eb8f95c61343fb)
- Definition hash: `e2b9360d5b9fc8b127fa0140b54845ff562d770629100b286136fc0434788d0d`
- Resolve transaction: [`0x11acad70aeefacb84de8c2fdd9919c257ce66e97d806c7eb8c4d69cb886e708a`](https://explorer-studio.genlayer.com/tx/0x11acad70aeefacb84de8c2fdd9919c257ce66e97d806c7eb8c4d69cb886e708a)
- Resolution hash: `d7b232be5eb95e75e7774bc0b044e5c621c9c16309e960b69b723e66e24635d8`
- Final result: `ATTRIBUTED`
- Winning candidate ID: `1` (exclusive)

The validators reached consensus on the same atomic candidate/criterion matrix. Source states were `AVAILABLE` for source IDs 1, 2, and 3.

| Candidate | Temporal link | Mechanism link | Scope link | Independent alternative | Contemporaneous reporting | Derived state |
|---:|---|---|---|---|---|---|
| 1 — provider outage | SUPPORTED | SUPPORTED | SUPPORTED | CONTRADICTED | SUPPORTED | ATTRIBUTABLE |
| 2 — deployment | CONTRADICTED | CONTRADICTED | CONTRADICTED | SUPPORTED | CONTRADICTED | REJECTED |
| 3 — DDoS | CONTRADICTED | CONTRADICTED | CONTRADICTED | SUPPORTED | CONTRADICTED | REJECTED |

The contract deterministically derived `ATTRIBUTED` from candidate 1 being attributable and candidates 2 and 3 being rejected.

## CausalActionGate proof

- Successful exclusive action for case 1 / candidate 1, pinned to the exact definition hash and action hash `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`: [`0x6cd4777d700b824df52dbf4e628ae2140583311c5e0beaa8af0a6b295ec1f7a8`](https://explorer-studio.genlayer.com/tx/0x6cd4777d700b824df52dbf4e628ae2140583311c5e0beaa8af0a6b295ec1f7a8). Finalized successfully; `is_consumed` returned `true`.
- Wrong definition hash rejection: [`0x63956a45b06663111d45a35d0717b9099968bfe96b4fec85e5cd3fe13e427225`](https://explorer-studio.genlayer.com/tx/0x63956a45b06663111d45a35d0717b9099968bfe96b4fec85e5cd3fe13e427225). Finalized with execution result `ERROR` and payload `causal attribution requirement not satisfied`.
- Rejected candidate / exclusivity rejection (candidate 2, `require_exclusive=true`): [`0xffac3aa315190657f4149db1ddb61ac40004246dd3bfa4c067f2e5b57460c631`](https://explorer-studio.genlayer.com/tx/0xffac3aa315190657f4149db1ddb61ac40004246dd3bfa4c067f2e5b57460c631). Finalized with execution result `ERROR` and payload `causal attribution requirement not satisfied`.
- Replay rejection (reused action hash `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`): [`0xfd0973f52ddacac4514bf94e59fb2c2b8d2334499368dfaaf729e15a22ff0060`](https://explorer-studio.genlayer.com/tx/0xfd0973f52ddacac4514bf94e59fb2c2b8d2334499368dfaaf729e15a22ff0060). Finalized with execution result `ERROR` and payload `action already consumed`.

## Verification

### Runtime-specific adjustment

No contract code changed. `scripts/preflight.py` was narrowly corrected so the final fixture-placeholder check scans only the fixture README and live lifecycle specification; the pinning utility legitimately contains the placeholder token as its replacement template. The frozen fixture URLs and protocol were not changed.

### Live workspace

- `python scripts/preflight.py --final`: PASS
- `python -m compileall contracts scripts tests`: PASS
- `genvm-lint check contracts/causalgate.py`: 3 lint checks passed; SDK validation could not load the cached SDK in this Windows workspace (`WinError 5: Access is denied`).
- `genvm-lint check contracts/causal_action_gate.py`: 3 lint checks passed; SDK validation could not load the cached SDK in this Windows workspace (`WinError 5: Access is denied`).
- `pytest -q`: 9 passed, 17 failed, 1 skipped. The Direct Mode cases fail while the Windows test harness attempts to unlink open temporary files (`WinError 32`); the skipped test is the authenticated live lifecycle, which was executed separately above.

### Final GitHub Actions verification

GitHub Actions run [37140339053](https://github.com/BeatyXO/CausalGate/actions/runs/37140339053) passed on final repository commit `6771baae90bd8fdbb0613763cf489139827694f5`: preflight PASS, Python compilation PASS, both GenVM lint and validation checks PASS (3 lint checks each), and Direct Mode pytest **26 passed, 1 skipped** in 55.69s. The sole skip is the authenticated live lifecycle, which was completed separately and is recorded above.

The deployed contract source remains commit `067dc16f86b4c35d63feb0b9a9fc6e9ef71efbbe`; both contract blobs are identical at final repository HEAD, so the post-deployment documentation cleanup introduced no contract drift.

The runner emitted non-blocking notices that `actions/checkout@v4` and `actions/setup-python@v5` are currently forced onto Node.js 24, and that `ubuntu-latest` will migrate to Ubuntu 26 on 2026-10-19.
