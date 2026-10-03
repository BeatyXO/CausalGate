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

## Finishing environment
- [ ] install repository tooling
- [ ] preflight and Python compilation
- [ ] GenVM lint both contracts
- [ ] all Direct Mode tests pass without weakening assertions
- [ ] pin fixture commit to immutable full-source SHA
- [ ] verify studionet / chain 61999
- [ ] finalized CausalGate deployment
- [ ] live case configured, sealed and resolved once
- [ ] real candidate dispositions/result recorded
- [ ] finalized CausalActionGate deployment
- [ ] correct pinned consumer action succeeds when permitted
- [ ] wrong definition hash rejects
- [ ] wrong candidate/exclusivity rejects
- [ ] replay rejects
- [ ] DEPLOYMENT.md contains only real proof
- [ ] final preflight and clean remote
