# Submission summary

**Title:** CausalGate — Consensus-Backed Causal Attribution Primitive

CausalGate lets another contract consume causal attribution without handing an LLM unrestricted authority to answer “what caused this?” A creator first freezes an outcome, competing candidate causes, an exact HTTPS evidence surface, and a causal test whose criteria specify REQUIRED/SUPPORTING mode plus expected semantic direction. Resolution is atomic across all competing candidates: validators independently re-fetch the frozen evidence and classify every candidate/criterion as SUPPORTED, CONTRADICTED, AMBIGUOUS or UNAVAILABLE. Deterministic code derives candidate dispositions and then the case result, including explicit MULTIPLE_SUFFICIENT_CAUSES rather than forcing a false winner. Minimum evidence availability, source substitution protection, exact-schema parsing and definition-hash pinning are built in. CausalActionGate demonstrates typed IC-to-IC enforcement with exclusive/non-exclusive attribution modes and replay protection.

No frontend is part of this submission.
