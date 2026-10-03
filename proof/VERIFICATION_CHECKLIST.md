# Verification checklist

## Code-side
- [x] no frontend
- [x] frozen causal-standard architecture
- [x] atomic all-candidate consensus resolution
- [x] independent source re-fetch and validator re-evaluation
- [x] strict candidate/criterion/result validation
- [x] deterministic REQUIRED/SUPPORTING logic
- [x] deterministic minimum-source availability
- [x] deterministic multiple-sufficient-causes handling
- [x] domain-separated hashes
- [x] typed consumer source and replay guard
- [x] static/preflight tests

## Toolchain and repository
- [x] repository tooling installed in CI
- [x] preflight passes
- [x] Python compilation passes
- [x] GenVM lint/validation passes for both contracts
- [x] Direct Mode tests pass without weakening assertions
- [x] fixture URLs pinned to immutable full-source SHA
- [x] final GitHub Actions run passes on final repository commit
- [x] final repository contains no frontend or generated/cache artifacts

## Stable Studionet proof
- [x] stable Studionet / chain 61999 verified
- [x] finalized CausalGate deployment
- [x] live case configured with immutable evidence sources
- [x] competing candidate causes registered
- [x] case sealed
- [x] case resolved atomically once
- [x] real candidate dispositions and final result recorded
- [x] finalized CausalActionGate deployment
- [x] correct pinned consumer action succeeded
- [x] wrong definition hash rejected
- [x] wrong candidate/exclusivity rejected
- [x] replay rejected
- [x] DEPLOYMENT.md contains real finalized proof
- [x] final preflight completed successfully

## Canonical references

- Live-proof verification commit: `6771baae90bd8fdbb0613763cf489139827694f5`
- Live-proof CI run for that commit: `37140339053`
- Deployed contract source commit: `067dc16f86b4c35d63feb0b9a9fc6e9ef71efbbe`
- Immutable fixture commit: `65f8ce6da8a0e14bad39bd8e51ce801194e590b1`
- Canonical deployment and transaction evidence: `DEPLOYMENT.md`
