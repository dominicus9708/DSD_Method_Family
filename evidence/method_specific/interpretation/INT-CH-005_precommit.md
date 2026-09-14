# INT-CH-005 Precommit / DSD Interpretation Competent-Baseline NO_GAIN Challenge

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-15**  
Method: **DSD Interpretation / DSD 해석론**  
Protocol: **Interpretation Protocol v0.1**  
Protocol commit at freeze: `40110a8a779f0ac6ff93ede6414544b8ec548fdf`  
Protocol blob at freeze: `dc3c3a46ba170b3b7565a59a7113c473fb02b463`

## 1. Case identity

```text
CASE_ID: INT-CH-005
CASE_CLASS: competent_baseline_no_gain_challenge
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: B0_SOURCE_CONTEXT_READING_EVALUATOR
```

Purpose: compare DSD Interpretation with a competent non-DSD reading evaluator that receives exactly the same claim-relevant source, role, context, bridge, candidate-reading, ambiguity/conflict, scope, and claim-strength records.

A fair `NO_GAIN` result is explicitly admissible. `NO_GAIN` is not method failure and does not establish merger, absorption, deletion, or permanent redundancy.

This is the first competent-baseline case for Interpretation. It is not the strongest-reasonable-baseline test; that is reserved for a later separately frozen case.

## 2. Frozen common task family

Five entirely constructed subcases are frozen:

```text
Q1 bridge-dependent supported reading against an unsupported alternative
Q2 legitimate resolved-multi interpretation
Q3 source silence requiring underdetermination rather than negation
Q4 missing claim-required bridge requiring blockage
Q5 original-context record separated from later reception
```

No external text, legal record, historical corpus, scientific corpus, or Sunzi material is used.

## 3. Q1 — bridge-dependent single supported reading

Source:

```text
S1: "Entry is permitted only when mark M is present."
```

Frozen bridge:

```text
B1: in this fixture, "only when" maps to M being a necessary condition for permitted entry.
```

Candidate readings:

```text
R1A: M is necessary for permitted entry
R1B: M is sufficient by itself for permitted entry
```

Expected for DSD and B0:

```text
R1A -> SUPPORTED / BRIDGE_DEPENDENT_INTERPRETATION
R1B -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
TERMINAL -> INTERPRETATION_RESOLVED_SINGLE
```

Forbidden: upgrading necessity to sufficiency.

## 4. Q2 — legitimate resolved plurality

Source/context:

```text
S2: "The symbol may denote alpha or beta under grammar G."
CONTEXT_G: both values are licensed; no precedence rule exists.
```

Candidate readings:

```text
R2A: symbol = alpha
R2B: symbol = beta
```

Expected for DSD and B0:

```text
R2A -> SUPPORTED
R2B -> SUPPORTED
READING_RELATION -> mutually_exclusive at token-value resolution
TERMINAL -> INTERPRETATION_RESOLVED_MULTI
```

Forbidden: forcing a single reading or relabelling legitimate plurality as method failure.

## 5. Q3 — source silence

Source:

```text
S3: "Unit K crossed the threshold."
```

Question: did Unit K carry a key?

Candidate readings:

```text
R3A: carried a key
R3B: did not carry a key
```

No context or bridge licenses either claim.

Expected for DSD and B0:

```text
R3A -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
R3B -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET
TERMINAL -> INTERPRETATION_UNDERDETERMINED
```

Forbidden: source silence -> negative claim.

## 6. Q4 — missing semantic bridge

Source:

```text
S4: "state = X7"
```

Question: does X7 mean safe or unsafe?

Required codebook bridge: not supplied.

Expected for DSD and B0:

```text
safe reading   -> BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
unsafe reading -> BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE
TERMINAL -> INTERPRETATION_BLOCKED
```

Forbidden: guessing from label shape, naming convention, or unstated domain knowledge.

## 7. Q5 — original context vs later reception

Primary source:

```text
S5: "The bell is sounded before opening."
```

Context record:

```text
C5-original: fixture procedure states that the bell is a readiness signal.
```

Later-reception record:

```text
L5-later: a later commentary calls the bell a ceremonial honor.
```

Question: what function is supported in the declared original-context scope?

Candidate readings:

```text
R5A: readiness signal
R5B: ceremonial honor in the original procedure
```

Expected for DSD and B0:

```text
R5A -> SUPPORTED / CONTEXT_SUPPORTED_INFERENCE
R5B -> NOT_SUPPORTED_WITHIN_DECLARED_SOURCE_SET for original-context scope
TERMINAL -> INTERPRETATION_RESOLVED_SINGLE
```

Later reception is retained as a separate record and is not silently promoted to original context.

## 8. Competent baseline freeze

Baseline identity:

```text
B0_SOURCE_CONTEXT_READING_EVALUATOR
```

B0 receives exactly the same:

```text
source identities and source text
source roles
context records and context provenance
bridge records and bridge applicability
candidate-reading sets
reading-relation records
ambiguity/conflict policy
temporal and perspective scope
requested output resolution
claim-strength categories
missing-source / source-silence policy
later-reception role record
```

B0 is explicitly competent to:

```text
1 preserve primary source, context, and later reception as distinct records;
2 apply supplied bridges without inventing unsupplied bridges;
3 preserve necessity/sufficiency distinctions;
4 retain multiple supported readings when no precedence rule exists;
5 preserve source silence without turning it into negation;
6 block evaluation when a claim-required bridge is absent;
7 keep original-context claims separate from later reception;
8 preserve enough source-to-reading trace to deterministically retrace its verdicts.
```

B0 does not need DSD terminology internally. For scoring, its outputs are mapped one-to-one to the frozen Interpretation statuses above.

B0 may not be weakened after this precommit.

## 9. Frozen gain criteria

```text
G1 SOURCE_ROLE_SEPARATION_GAIN
  established only if DSD preserves a claim-relevant source/context/later-reception distinction that B0 loses.

G2 BRIDGE_DISCIPLINE_GAIN
  established only if DSD preserves necessary bridge/applicability semantics more correctly than B0.

G3 MULTI_READING_GAIN
  established only if DSD handles legitimate plurality more correctly than B0.

G4 SILENCE_AND_BLOCKAGE_GAIN
  established only if DSD preserves silence, missing bridge, underdetermination, or blockage more correctly than B0.

G5 CLAIM_STRENGTH_GAIN
  established only if DSD preserves direct/context/bridge-dependent claim strength more correctly than B0.

G6 TRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant source-to-reading derivation trace that B0 cannot reconstruct from the same inputs.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> challenge FAIL.
If one or more G1-G6 are established against a correct B0 -> GAIN_ESTABLISHED.
If DSD and B0 are both correct and B0 matches all six dimensions -> NO_GAIN.
Otherwise -> challenge FAIL or unresolved according to the frozen scoring record.
```

No implementation speed, elegance, terminology, pedagogical clarity, external practical benefit, or independent-evaluator result is scored.

## 10. Frozen expected task-level outputs

```text
Q1 DSD/B0 -> R1A supported, R1B not supported, RESOLVED_SINGLE
Q2 DSD/B0 -> R2A+R2B supported, RESOLVED_MULTI
Q3 DSD/B0 -> both not supported, UNDERDETERMINED
Q4 DSD/B0 -> both blocked, BLOCKED
Q5 DSD/B0 -> readiness supported, ceremonial-original not supported, RESOLVED_SINGLE
```

All five DSD executions are expected to be `INTERPRETATION_PROTOCOL_CONFORMANCE: CONFORMANT` if executed correctly.

## 11. Frozen scoring

```text
A. immutable protocol / precommit / fairness          8
B. DSD task execution                                15
C. B0 task execution                                 15
D. comparative gain                                   8
E. scope and protocol pressure                        4
TOTAL                                                 50
```

Detailed check lock:

```text
A1 protocol commit/blob fixed
A2 five subcases fixed
A3 baseline identity/capabilities fixed
A4 same claim-relevant inputs frozen
A5 gain criteria G1-G6 fixed
A6 scoring fixed
A7 baseline may not be weakened post-hoc
A8 no source/context/bridge/reading-policy revision after execution begins

B1-B5 exact terminal outputs Q1-Q5
B6 Q1 necessity not upgraded to sufficiency
B7 Q1 claim strength preserved
B8 Q2 both supported readings retained
B9 Q2 plurality not relabelled underdetermination merely because plural
B10 Q3 silence not converted to negation
B11 Q3 underdetermination retained
B12 Q4 no X7 semantic guess
B13 Q4 blockage retained
B14 Q5 later reception not promoted to original context
B15 all five DSD executions CONFORMANT

C1-C5 exact terminal outputs Q1-Q5
C6 Q1 necessity/sufficiency preserved
C7 Q1 bridge-dependent derivation trace sufficient
C8 Q2 both supported readings retained
C9 Q2 no hidden precedence
C10 Q3 silence preserved
C11 Q3 underdetermination retained
C12 Q4 no X7 semantic guess
C13 Q4 blockage retained
C14 Q5 original/later role separation preserved
C15 B0 trace sufficient to reconstruct all five verdicts

D1-D6 G1-G6 each NOT_ESTABLISHED if B0 matches
D7 final method gain = NO_GAIN when D1-D6 hold
D8 NO_GAIN not interpreted as method failure/merger/absorption/deletion evidence

E1 protocol revision not required if no contradiction appears
E2 no strongest-reasonable-baseline claim
E3 no external/reproducibility/maturity claim
E4 no permanent survival/independence/redundancy conclusion
```

Decision:

```text
50/50 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a challenge-design defect is discovered, this Case ID is preserved as failed and any correction must use a new Case ID.

## 12. Evidence-count lock

Before execution:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 3
METHOD_BOUNDARY_INTERPRETATION_CASES: 1
BASELINE_INTERPRETATION_CASES: 0
NO_GAIN_INTERPRETATION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
```

A 50/50 PASS with final `NO_GAIN` may add exactly:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: +1
BASELINE_INTERPRETATION_CASES: +1
NO_GAIN_INTERPRETATION_CASES: +1
```

It does not establish strongest-reasonable-baseline coverage, reproducibility, external applicability, independent validation, maturity, method survival, non-merger, or permanent independence.

## 13. Next if passed

Precommit and execute a materially richer strongest-reasonable-baseline Interpretation challenge. External validation remains deferred until the internal standardization sequence is complete.
