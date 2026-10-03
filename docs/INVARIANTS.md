# Protocol invariants

1. Only the case creator may configure a DRAFT case.
2. Criteria, evidence URLs, candidates, thresholds and outcome freeze at seal.
3. Oversized fields are rejected, never silently truncated.
4. Criterion and candidate keys are normalized and unique.
5. Evidence URLs must use HTTPS and obvious private/local targets are rejected.
6. Duplicate evidence URLs are rejected.
7. At least one candidate and enough configured sources are required before seal.
8. definition_hash commits to the full causal test, evidence surface and competing set.
9. A SEALED case resolves at most once.
10. All candidate causes are evaluated in one consensus resolution against one evidence-fetch cycle per validator.
11. Model output covers every candidate exactly once and every criterion exactly once.
12. Unknown/duplicate/omitted candidate or criterion rows and unknown statuses fail closed.
13. Validators independently fetch and re-evaluate evidence.
14. Free-form notes never decide attribution.
15. REQUIRED criteria cannot be overridden by supporting threshold.
16. A definite opposite on REQUIRED rejects the candidate.
17. Ambiguous/unavailable REQUIRED evidence cannot become support.
18. Minimum source availability is deterministic and frozen.
19. The LLM never writes candidate disposition or case result.
20. Multiple attributable causes are represented explicitly rather than forced into one winner.
21. FINALIZED cases are immutable.
22. Consumers pin exact definition_hash and action hashes are replay protected.
23. No frontend is part of the primitive.
