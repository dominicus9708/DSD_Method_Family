# MSR-CH-005 — Strongest-Reasonable Non-DSD Baseline Result

Status: **EXECUTED — 64/64 PASS / NO_GAIN**  
Date: **2026-09-19**  
Case ID: `MSR-CH-005`  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
MEASUREMENT_PROTOCOL_COMMIT:
  70af7c3ddc618be34d0ff76fcc1ce63c895fc950

MEASUREMENT_PROTOCOL_BLOB:
  bc24a5e72adaf4a1b1e64203bd14b3e781810331

PRECOMMIT_COMMIT:
  7722081d8b3612fd1c151aac63f7482c6cb882b7

PRECOMMIT_BLOB:
  5465898b17847ed627cb48fe98c678c77a4e7b4d

BASELINE_ID:
  B1_STRONG_DISTINGUISHABILITY_ENGINE
```

No DSD protocol, B1 capability, fixture, gain axis, or scoring item was changed after precommit.

## 2. Fairness result

```text
EQUAL_CLAIM_RELEVANT_INFORMATION: yes
B1_WEAKENED_POST_HOC: no
DSD_HIDDEN_FAVORABLE_INPUTS: 0
B1_WITHHELD_CLAIM_RELEVANT_INPUTS: 0
EXTERNAL_EVALUATOR_USED: no
EXTERNAL_APPLICATION_COUNTED: no
```

B1 was allowed its full precommitted integrated capabilities, including finite candidate-subset search.

## 3. R1 — version-scoped decision semantics

Frozen raw records:

```text
A -> 0.6
B -> 0.4
```

### V1 / t0

```text
HIGH iff x >= 0.5
LOW  iff x < 0.5
```

DSD:

```text
A -> HIGH
B -> LOW
A-B -> PAIRWISE_DISCRIMINATING
candidate -> MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
plan -> MEASUREMENT_PLAN_SUFFICIENT
```

B1:

```text
A -> HIGH
B -> LOW
pair -> discriminating
plan -> B1_PLAN_SUFFICIENT
```

### V2 / t1

```text
HIGH iff x >= 0.7
LOW  iff x < 0.7
```

DSD:

```text
A -> LOW
B -> LOW
A-B -> PAIRWISE_NONDISCRIMINATING
candidate -> MEASUREMENT_NONDISCRIMINATING
plan -> MEASUREMENT_PLAN_INSUFFICIENT
```

B1:

```text
A -> LOW
B -> LOW
pair -> nondiscriminating
plan -> B1_PLAN_INSUFFICIENT
```

Both preserved:

```text
SAME_RAW_VALUES != SAME_DECISION_SEMANTICS_ACROSS_VERSIONS
LATER_RULE != RETROACTIVE_RULE_FOR_EARLIER_TASK
```

R1 claim-relevant result: `BASELINE_MATCH`.

## 4. R2 — dynamic distinguishability support

Frozen handoff:

```text
location: L

t0:
  upstream structural difference: exists
  distinguishability support at L: NOT_YET_AVAILABLE

t1:
  distinguishability support at L: AVAILABLE

once available:
  C -> RED
  D -> BLUE
```

### t0

DSD preserves the supplied support state as a prerequisite that is not yet satisfied at the measurement location/time.

```text
present local discriminating evidence from upstream difference:
  prohibited

negative-result inference:
  prohibited

candidate usability:
  blocked at declared t0 by unavailable dynamic support

plan:
  MEASUREMENT_PLAN_BLOCKED
```

B1:

```text
present local evidence:
  unavailable at t0

negative-result inference:
  prohibited

plan:
  B1_PLAN_BLOCKED_BY_AVAILABILITY
```

### t1

DSD:

```text
C -> RED
D -> BLUE
pair -> PAIRWISE_DISCRIMINATING
plan -> MEASUREMENT_PLAN_SUFFICIENT
```

B1:

```text
C -> RED
D -> BLUE
pair -> discriminating
plan -> B1_PLAN_SUFFICIENT
```

Both preserved:

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
UPSTREAM_DIFFERENCE != PRESENT_LOCAL_READOUT
```

R2 claim-relevant result: `BASELINE_MATCH`.

## 5. R3 — finite plan search under mixed candidate quality

Frozen candidates:

```text
m1:
  E -> 0
  F -> 1
  G -> 1

m2:
  E -> 0
  F -> 0
  G -> 1

m3:
  exact duplicate of m1

m4:
  applicable
  required bridge absent

m5:
  domain Z
  task object class Y
```

DSD execution:

```text
m1:
  E-F discriminate
  E-G discriminate
  F-G nondiscriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m2:
  E-F nondiscriminate
  E-G discriminate
  F-G discriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m3:
  same discrimination partition as m1
  redundancy sidecar preserved
  no new required distinction added

m4:
  MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE

m5:
  MEASUREMENT_INAPPLICABLE

predeclared joint {m1,m2}:
  E -> (0,0)
  F -> (1,0)
  G -> (1,1)
  -> all required pairs discriminate
  -> MEASUREMENT_PLAN_SUFFICIENT
```

B1 execution:

```text
m1 -> partial
m2 -> partial
m3 -> redundant duplicate of m1
m4 -> blocked
m5 -> inapplicable

finite usable-subset search:
  {m1} -> insufficient
  {m2} -> insufficient
  {m3} -> insufficient
  {m1,m3} -> insufficient
  {m1,m2} -> sufficient
  {m2,m3} -> sufficient

minimal sufficient cardinality:
  2

one minimal sufficient plan:
  {m1,m2}
```

B1's additional finite-search capability is real, but it is outside Measurement Protocol v0.1's frozen binding task and therefore is not treated as DSD protocol failure.

Both preserve:

```text
MORE_CANDIDATES != MORE_INFORMATION
REDUNDANT_CANDIDATE != NEW_DISCRIMINATION
BASELINE_EXTRA_SEARCH_CAPABILITY != DSD_PROTOCOL_FAILURE
```

R3 claim-relevant Measurement outputs: `BASELINE_MATCH`.

## 6. R4 — proxy, aggregate collision, bounded reconstruction

Frozen candidates:

```text
m_direct:
  H -> P
  I -> Q
  J -> Q
  role: direct

m_proxy:
  H support {+2,-2} -> aggregate 0
  I support {0}     -> aggregate 0
  J support {+3}    -> aggregate 3
  role: proxy via aggregate handoff
```

DSD:

```text
m_direct:
  H-I discriminate
  H-J discriminate
  I-J nondiscriminate
  -> partial

m_proxy:
  H-I nondiscriminate
  H-J discriminate
  I-J discriminate
  -> partial

joint:
  H -> (P,0)
  I -> (Q,0)
  J -> (Q,3)
  -> all required pairs discriminate
  -> MEASUREMENT_PLAN_SUFFICIENT

H/I aggregate collision:
  retained

proxy/directness:
  retained

full support reconstruction:
  unavailable

true alternative:
  not identified
```

B1 reproduced the same pairwise and joint partition, retained proxy/direct roles, retained the H/I collision and noninjectivity sidecar, and retained the reconstruction-unavailable record.

Both preserved:

```text
PROXY != DIRECT
EQUAL_AGGREGATE != EQUAL_SUPPORT
DISCRIMINATING_PROXY != FULL_RECONSTRUCTION
PLAN_SUFFICIENT != TRUE_ALTERNATIVE_IDENTIFIED
```

R4 claim-relevant result: `BASELINE_MATCH`.

## 7. R5 — competing bridge versions

Frozen bridges:

```text
V1:
  K -> OPEN
  L -> CLOSED
  -> discriminating

V2:
  K -> OPEN
  L -> OPEN
  -> nondiscriminating

both admissible
precedence: none
```

DSD:

```text
candidate -> MEASUREMENT_UNDERDETERMINED
plan -> MEASUREMENT_PLAN_UNDERDETERMINED
```

B1:

```text
candidate -> B1_UNDERDETERMINED
plan -> B1_PLAN_UNDERDETERMINED
```

Both retained both bridge versions and made no post-hoc choice.

```text
MULTIPLE_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
NO_PRECEDENCE != LICENSE_TO_CHOOSE_POST_HOC
```

R5 claim-relevant result: `BASELINE_MATCH`.

## 8. Bounded-claim comparison

DSD maximum claim remained limited to discrimination adequacy under the frozen supplied records.

B1 also emitted:

```text
MAXIMUM_SUPPORTED_CLAIM:
  only the recorded discrimination/availability/scope judgments
  under the supplied task records

NOT ESTABLISHED:
  true alternative
  diagnosis
  causality
  full reconstruction
  external empirical validity
```

Neither side fabricated an observed result.

```text
BOUNDED_CLAIM_RESULT: BASELINE_MATCH
```

## 9. Traceability comparison

B1 retained:

```text
task/version identity
candidate identities
status records
bridge identities
decision-rule versions
pairwise tables
joint signatures
search ledger for R3
collision/reconstruction sidecars
dynamic-support state
maximum-claim record
```

Every claim-relevant B1 decision in R1-R5 is deterministically retraceable from its frozen record.

DSD likewise retained its protocol-required ledgers.

```text
TRACEABILITY_RESULT: BASELINE_MATCH
```

This does not establish project-level reproducibility because MSR-CH-005 is a baseline comparison, not a separately precommitted retrace.

## 10. Frozen gain-axis result

```text
G1 VERSION_SCOPE_GAIN:
  BASELINE_MATCH

G2 DYNAMIC_AVAILABILITY_GAIN:
  BASELINE_MATCH

G3 PLAN_AND_REDUNDANCY_GAIN:
  BASELINE_MATCH

G4 PROXY_LOSS_RECONSTRUCTION_GAIN:
  BASELINE_MATCH

G5 AMBIGUITY_GAIN:
  BASELINE_MATCH

G6 BOUNDED_CLAIM_GAIN:
  BASELINE_MATCH

G7 TRACEABILITY_GAIN:
  BASELINE_MATCH
```

Therefore:

```text
MEASUREMENT_METHOD_GAIN_STATUS:
  NO_GAIN

STRONGEST_REASONABLE_BASELINE_MEASUREMENT:
  established_at_constructed_evidence_level
```

No DSD-specific advantage was established against B1 in these frozen constructed subcases.

## 11. Frozen scoring

### A. Immutable fairness

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS

A: 8/8
```

### B. DSD execution

```text
B1 PASS
B2 PASS
B3 PASS
B4 PASS
B5 PASS
B6 PASS
B7 PASS
B8 PASS
B9 PASS
B10 PASS
B11 PASS
B12 PASS
B13 PASS
B14 PASS
B15 PASS
B16 PASS
B17 PASS
B18 PASS

B: 18/18
```

### C. B1 execution

```text
C1 PASS
C2 PASS
C3 PASS
C4 PASS
C5 PASS
C6 PASS
C7 PASS
C8 PASS
C9 PASS
C10 PASS
C11 PASS
C12 PASS
C13 PASS
C14 PASS
C15 PASS
C16 PASS
C17 PASS
C18 PASS

C: 18/18
```

### D. Comparative gain

```text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS
D9 PASS
D10 PASS

D: 10/10
```

### E. Scope / protocol pressure

```text
E1 PASS
E2 PASS
E3 PASS
E4 PASS
E5 PASS
E6 PASS
E7 PASS
E8 PASS
E9 PASS
E10 PASS

E: 10/10
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 64
PASSED: 64
FAILED: 0
TOTAL: 64/64 PASS
```

## 12. Protocol pressure

```text
MSR-CH-005_CONFORMANCE: CONFORMANT
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

R1-R5 did not expose a contradiction in Measurement Protocol v0.1.

## 13. NO_GAIN interpretation

```text
NO_GAIN
  = strongest-reasonable B1 matched all seven precommitted
    claim-relevant gain dimensions under equal information access
    in these constructed fixtures
```

It does not mean:

```text
Measurement failed
Measurement should be removed
Measurement should merge into another method
Measurement has no organizational/interface value
B1 is universally superior
future tasks cannot expose a DSD advantage
```

Preserved:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != METHOD_DELETION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
```

## 14. Counter update

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 4 -> 5
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 4 -> 5

POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 1

BASELINE_MEASUREMENT_CASES: 1 -> 2
NO_GAIN_MEASUREMENT_CASES: 1 -> 2

STRONGEST_REASONABLE_BASELINE_MEASUREMENT:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES: 0

EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established

MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 15. Maximum supported claim

MSR-CH-005 establishes only that a deliberately strong, integrated non-DSD distinguishability engine matched the frozen DSD Measurement claim-relevant outputs across R1-R5 under equal information access.

It establishes strongest-reasonable-baseline coverage only at the constructed-evidence level.

It does not establish:

```text
external applicability
independent validation
reproducibility
practical superiority
permanent method independence
permanent redundancy
maturity promotion
```

## 16. Next

Proceed to deterministic same-project retrace from immutable Measurement artifacts.

The retrace must be separately precommitted and may establish only same-project reproducibility/artifact-consistency evidence, not independent replication or external validity.
