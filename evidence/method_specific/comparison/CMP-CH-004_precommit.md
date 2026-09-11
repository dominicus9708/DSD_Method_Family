# CMP-CH-004 Precommit / DSD 비교론 Competent-Baseline NO_GAIN Challenge 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-004
CASE_CLASS: competent_baseline_no_gain_challenge
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B0_TYPED_COMPARISON_LEDGER
```

Purpose: compare DSD Comparison against a competent non-DSD comparison ledger that receives the same claim-relevant information and is explicitly allowed to preserve all distinctions needed by the frozen task. A fair `NO_GAIN` result is acceptable and does not count as method failure.

This is the first successful-baseline category attempt for Comparison. It is **not** frozen as the strongest-reasonable-baseline test; a materially richer baseline challenge is reserved for the next stage.

## 2. Common task family

Five subcases are frozen:

```text
Q1 strict structural equivalence with typed Property/status preservation
Q2 encoded correspondence requiring an explicit bridge
Q3 non-exhaustive map-family failure remaining underdetermined
Q4 aggregate-readout collision with structural noncorrespondence
Q5 missing claim-required bridge producing blocked comparison
```

All tasks use the same comparison ledgers:

```text
TERMINAL_COMPARISON_STATUS
COMPARISON_PROTOCOL_CONFORMANCE
COMPARISON_METHOD_GAIN_STATUS
```

DSD conformance is evaluated only for the DSD run. The baseline is evaluated for task correctness and retraceability, not for DSD-protocol conformance.

## 3. Q1 — strict equivalence with typed status

Subjects:

```text
A1
  nodes: {a0,a1}
  relation: {a0->a1}
  readiness(a0): DEFINED_ZERO
  readiness(a1): DEFINED_NONZERO

B1
  nodes: {b0,b1}
  relation: {b0->b1}
  readiness(b0): DEFINED_ZERO
  readiness(b1): DEFINED_NONZERO
```

Map and coverage:

```text
f1(a0)=b0
f1(a1)=b1
MAP_FAMILY_COVERAGE: exhaustive relative to singleton {f1}
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  forward_relation_preservation_required
  inverse_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_and_supplied
COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: exhaustive
  properties: exhaustive
  status_classes: exhaustive
```

Expected result for DSD and B0:

```text
CORRESPONDENCE_CLASS: STRICT_EQUIVALENT
STRUCTURAL_EQUIVALENCE: yes
STATUS_DISTINCTIONS_PRESERVED: yes
TERMINAL: COMPARISON_RESOLVED
```

## 4. Q2 — encoded correspondence

Subjects:

```text
A2 states: {0,1}
A2 transition: 0->1
status(0): DEFINED_ZERO
status(1): DEFINED_NONZERO

B2 states: {OFF,ON}
B2 transition: OFF->ON
status(OFF): DEFINED_ZERO
status(ON): DEFINED_NONZERO
```

Supplied bridge:

```text
e(0)=OFF
e(1)=ON
ENCODING_OR_BRIDGE_RULE: e
BRIDGE_PROVENANCE: supplied_in_task
```

Coverage:

```text
MAP_FAMILY_COVERAGE: exhaustive relative to supplied bridge {e}
COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive under e
  relations: exhaustive
  properties: exhaustive
  status_classes: exhaustive
```

Expected result for DSD and B0:

```text
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
DIRECT_CORRESPONDENCE_RELABELLING: prohibited
TERMINAL: COMPARISON_RESOLVED
```

The bridge being bijective does not erase the fact that the comparison is bridge-dependent.

## 5. Q3 — non-exhaustive failure

Subjects:

```text
A3 nodes: {u0,u1}
A3 relation: {u0->u1}

B3 nodes: {v0,v1}
B3 relation: {v0->v1}
```

Candidate map family:

```text
F3 = {g31,g32}

g31(u0)=v1
g31(u1)=v0
  evaluated
  bijective: yes
  relation preservation: fail

g32(u0)=v0
g32(u1)=v1
  UNTESTED in frozen run

MAP_FAMILY_COVERAGE: non_exhaustive
UNTESTED_MAP_SET: {g32}
```

Expected result for DSD and B0:

```text
CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
GLOBAL_NONCORRESPONDENCE: not_established
TERMINAL: COMPARISON_UNDERDETERMINED
```

## 6. Q4 — aggregate collision without structural equivalence

Subjects and readout:

```text
A4 support: {x0,x1,x2}
values: {1,1,2}
aggregate readout: 4

B4 support: {y0}
values: {4}
aggregate readout: 4
```

Frozen strict-comparison family:

```text
EQUIVALENCE_CRITERION:
  support-cardinality equality required
  bijection over support required
  matched value decomposition required

MAP_FAMILY_COVERAGE: exhaustive by cardinality argument
COMPARISON_ELEMENT_COVERAGE:
  support/cardinality: exhaustive
  value decomposition: exhaustive
AGGREGATE_COLLISION_POLICY:
  equal readout does not establish structural equivalence
```

Expected result for DSD and B0:

```text
AGGREGATE_READOUT_COMPARISON: equal
STRUCTURAL_EQUIVALENCE: no
CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen strict family
TERMINAL: COMPARISON_RESOLVED
```

## 7. Q5 — missing required bridge

Subjects:

```text
A5 labels/states: {COLD,HOT}
B5 labels/states: {0,1}
```

Frozen task rule:

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
CLAIM_REQUIRED_SEMANTIC_BRIDGE: yes
BRIDGE_SUPPLIED: no
MAP_FAMILY_SOURCE: unavailable until bridge supplied
PRECOMPARISON_TRANSFORMATION_POLICY: transformation_not_permitted_in_comparison
```

Expected result for DSD and B0:

```text
SUBSTANTIVE_MAP_EVALUATION: not_performed
STRUCTURAL_DIFFERENCE_FROM_BRIDGE_ABSENCE: not_claimed
CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
TERMINAL: COMPARISON_BLOCKED
```

## 8. Competent baseline freeze

Baseline identity:

```text
B0_TYPED_COMPARISON_LEDGER
```

B0 receives exactly the same:

```text
subject identities and visible structures
relation records
Property/status records
map definitions and tested/untested flags
map-family coverage declarations
comparison-element coverage declarations
required map properties
reverse/inverse requirements
encoding/bridge rule and bridge provenance
aggregate readouts
strict-equivalence criteria
aggregate-collision policy
claim-required bridge flags
terminal-status rules
```

B0 is explicitly competent to:

```text
1. distinguish STRICT_EQUIVALENT, ENCODED_CORRESPONDENCE,
   NONCORRESPONDENCE, and UNDETERMINED_CORRESPONDENCE;
2. preserve DEFINED_ZERO and DEFINED_NONZERO as distinct status classes;
3. preserve tested vs untested maps and non-exhaustive coverage;
4. avoid global noncorrespondence from one failed map;
5. preserve bridge provenance and keep bridge-dependent comparison encoded;
6. separate equal aggregate readout from structural equivalence;
7. return COMPARISON_RESOLVED, COMPARISON_UNDERDETERMINED,
   or COMPARISON_BLOCKED under the same frozen terminal rules;
8. preserve unresolved and failure records needed for retraceability.
```

B0 is not required to use DSD terminology internally, but its frozen task outputs must be translated one-to-one into the comparison classes and terminal labels above for scoring.

B0 must not be weakened after precommit.

## 9. Frozen gain criteria

```text
G1 RELATION_CLASS_SEPARATION_GAIN
  established only if DSD preserves a claim-relevant relation-class distinction that B0 loses.

G2 STATUS_DISTINCTION_GAIN
  established only if DSD preserves a claim-relevant Property/status distinction that B0 loses.

G3 COVERAGE_AND_CLOSURE_GAIN
  established only if DSD handles tested/untested maps, map-family coverage, or closure more correctly than B0.

G4 BRIDGE_PROVENANCE_GAIN
  established only if DSD preserves encoded/bridge-dependent or missing-bridge status more correctly than B0.

G5 AGGREGATE_COLLISION_GAIN
  established only if DSD avoids an aggregate-to-structure overclaim that B0 makes.

G6 TERMINAL_AND_RETRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant terminal/unresolved/failure trace that B0 cannot reconstruct from the same inputs.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> challenge FAIL.
If one or more G1-G6 are established against a correct B0 -> GAIN_ESTABLISHED.
If DSD and B0 are both correct and B0 matches all six dimensions -> NO_GAIN.
Otherwise -> challenge FAIL / unresolved according to the frozen scoring record.
```

No efficiency, elegance, vocabulary, implementation cost, or practical-domain advantage is scored.

## 10. Expected baseline outputs

```text
Q1 B0 -> STRICT_EQUIVALENT / COMPARISON_RESOLVED
Q2 B0 -> ENCODED_CORRESPONDENCE / COMPARISON_RESOLVED
Q3 B0 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_UNDERDETERMINED
Q4 B0 -> NONCORRESPONDENCE / COMPARISON_RESOLVED
Q5 B0 -> UNDETERMINED_CORRESPONDENCE / COMPARISON_BLOCKED
```

Expected DSD outputs are identical on these five task-level results.

## 11. Precommitted scoring

Total required checks: **50**.

```text
A. immutable protocol / precommit / fairness: 8
  A1 Protocol commit fixed
  A2 five subcases fixed
  A3 B0 identity and capabilities fixed
  A4 same claim-relevant inputs frozen
  A5 gain criteria G1-G6 fixed
  A6 scoring fixed
  A7 B0 may not be weakened post-hoc
  A8 no task/rule revision after execution begins

B. DSD task execution: 15
  B1-B5 exact Q1-Q5 relation-class results
  B6-B10 exact Q1-Q5 terminal results
  B11 Q1 typed statuses preserved
  B12 Q2 encoded status preserved
  B13 Q3 untested map retained
  B14 Q4 aggregate equality kept separate from structure
  B15 Q5 no difference fabricated from missing bridge

C. B0 task execution: 15
  C1-C5 exact Q1-Q5 relation-class results
  C6-C10 exact Q1-Q5 terminal results
  C11 Q1 typed statuses preserved
  C12 Q2 bridge provenance preserved
  C13 Q3 untested map retained
  C14 Q4 aggregate equality kept separate from structure
  C15 Q5 no difference fabricated from missing bridge

D. comparative gain: 8
  D1-D6 G1-G6 each NOT_ESTABLISHED when B0 matches
  D7 final method gain = NO_GAIN when D1-D6 all hold
  D8 NO_GAIN not interpreted as method failure/absorption evidence

E. scope and protocol pressure: 4
  E1 all DSD subcases CONFORMANT
  E2 protocol revision not required if no contradiction appears
  E3 no external/reproducibility/maturity claim
  E4 no survival/merger/absorption/deletion conclusion
```

Decision:

```text
50/50 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a fixture defect is discovered, preserve this Case ID as failed and correct prospectively under a new Case ID.

## 12. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 3
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
```

A 50/50 PASS with final `NO_GAIN` may add exactly:

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NO_GAIN_COMPARISON_CASE_INCREMENT: +1
BASELINE_COMPARISON_CASE_INCREMENT: +1
```

It does not establish strongest-reasonable-baseline coverage, external applicability, reproducibility, independent validation, maturity, method survival, non-merger, or permanent independence.
