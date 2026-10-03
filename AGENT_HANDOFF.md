# Codex finishing handoff

CausalGate is substantially implemented. Preserve the architecture unless the actual stable GenLayer runtime proves a compatibility change is necessary.

Remaining work is environment-specific: run real genlayer-test Direct Mode and genvm-lint; fix genuine runtime incompatibilities without weakening safeguards; pin fixtures to the immutable full-source commit; use stable studionet chain 61999 only; deploy CausalGate; execute the Alpha-outage lifecycle; deploy CausalActionGate; prove correct consume, wrong-definition, wrong-candidate/exclusivity and replay behavior; update DEPLOYMENT.md only with real evidence; run final preflight and push.
