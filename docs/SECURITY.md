# Security model

A forged leader cannot safely flip a blocking causal criterion to support because validators independently fetch the frozen sources and independently re-run the bounded classification. Model output that changes candidate/criterion shape or invents statuses fails closed.

Fetched web evidence is untrusted data. The prompt explicitly forbids following instructions embedded in sources, labels, outcome text, candidate statements or criterion text. Independent validation and deterministic result derivation remain primary defenses.

Source substitution is prevented by sealing exact URLs into the case definition. Sources must use HTTPS; obvious loopback/private IPv4 targets, `.local` hosts and literal IPv6 hosts are rejected as defense in depth. This URL screening is deliberately conservative and is not presented as a complete network-security boundary; GenLayer's web sandbox remains relevant.

A source counts toward the frozen `min_sources_available` threshold only if non-empty text actually survives the contract's bounded evidence collection and enters that validator's evidence bundle. A successful remote request with no usable bounded text does not count as available evidence.

Atomic all-candidate resolution avoids evidence-time drift between competing hypotheses: every candidate is judged from one source-fetch cycle per validator. A frozen minimum source-availability rule prevents false certainty during source outages. Because leaders and validators fetch independently, differing source availability or material classifications causes disagreement rather than silently finalizing inconsistent evidence states.

The protocol explicitly allows `MULTIPLE_SUFFICIENT_CAUSES` instead of forcing false uniqueness. Required criteria dominate candidate disposition; ambiguous or unavailable required evidence cannot become support. Supporting criteria only satisfy the creator-frozen threshold and cannot override a failed required criterion.

The sample `CausalActionGate` pins the exact case definition hash and protects action replay. Consumers may choose ordinary attribution (including a candidate in a multiple-sufficient result) or require exclusive attribution to one candidate.

CausalGate proves only that consensus-backed evidence classifications satisfy the standard actually frozen. It does not certify that the creator's causal standard is scientifically, legally, medically, operationally or philosophically sufficient for a domain.
