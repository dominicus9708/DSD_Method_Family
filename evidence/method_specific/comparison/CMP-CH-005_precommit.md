# CMP-CH-005 Precommit / DSD 비교론 Strongest-Reasonable-Baseline Challenge 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-005
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_STRONG_TYPED_COMPARISON_ENGINE
```

Purpose: test a materially richer Comparison workload against a strong non-DSD engine that receives exactly the same claim-relevant records and is allowed to preserve all comparison distinctions. `NO_GAIN` is explicitly acceptable.

## 2. Frozen subcases

```text
R1 earliest justified first branch under complete prior-stage coverage
R2 directional direct correspondence with failed strict-equivalence closure
R3 partial-vs-global comparison-element coverage
R4 supplied representation bridge with provenance-preserving encoded correspondence
R5 dynamic trajectory equivalence separated from supplied lineage nonidentity
```

All five subcases use the same three ledgers:

```text
TERMINAL_COMPARISON_STATUS
COMPARISON_PROTOCOL_CONFORMANCE
COMPARISON_METHOD_GAIN_STATUS
```

## 3. R1 — earliest justified first branch

Two stage-indexed subjects are frozen:

```text
A1:
  S0: value 0, readiness DEFINED_ZERO
  S1: value 1, readiness DEFINED_NONZERO
  S2: value 2, readiness DEFINED_NONZERO
  S3: value 4, readiness DEFINED_NONZERO

B1:
  S0: value 0, readiness DEFINED_ZERO
  S1: value 1, readiness DEFINED_NONZERO
  S2: value 3, readiness DEFINED_NONZERO
  S3: value 4, readiness DEFINED_NONZERO
```

Frozen stage map:

```text
S0 <-> S0
S1 <-> S1
S2 <-> S2
S3 <-> S3
FIRST_BRANCH_SEARCH_BASIS: ordered stages S0,S1,S2,S3
FIRST_BRANCH_SEARCH_COVERAGE: exhaustive through S3
```

Required checks:

```text
S0 preserved: yes
S1 preserved: yes
S2 value preservation: no
S3 value equality does not erase S2 divergence
```

Expected DSD and B1 output:

```text
CORRESPONDENCE_CLASS: PARTIAL_CORRESPONDENCE
FIRST_JUSTIFIED_BRANCH_POINT: S2
EARLIER_STAGE_CLOSURE: {S0,S1} verified preserved
TERMINAL: COMPARISON_RESOLVED
```

`S3` re-convergence does not move the earliest justified branch past `S2`.

## 4. R2 — directionality and strict-equivalence closure

Subjects:

```text
A2 nodes: {a0,a1}
relation: {a0->a1}

B2 nodes: {b0,b1,b2}
relation: {b0->b1, b1->b2}
```

Supplied forward map:

```text
f2(a0)=b0
f2(a1)=b1
```

Frozen requirements:

```text
forward injective map allowed for DIRECT_CORRESPONDENCE
strict equivalence requires bijection + reverse/inverse coverage over all target nodes
MAP_FAMILY_COVERAGE: exhaustive relative to supplied forward map family {f2}
COMPARISON_ELEMENT_COVERAGE: exhaustive for mapped A2 image and target-cardinality check
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_for_strict_equivalence
```

Expected DSD and B1 output:

```text
FORWARD_DIRECT_CORRESPONDENCE: established
STRICT_EQUIVALENCE: no
REASON: b2 lies outside image(f2); bijection/global inverse unavailable
CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
```

## 5. R3 — partial versus global element coverage

Subjects share the same two-node chain and same supplied map.

```text
A3 nodes: {u0,u1}
relation: {u0->u1}
readiness(u0): DEFINED_ZERO
readiness(u1): DEFINED_NONZERO
mode(u1): RECORD_WITHHELD

B3 nodes: {v0,v1}
relation: {v0->v1}
readiness(v0): DEFINED_ZERO
readiness(v1): DEFINED_NONZERO
mode(v1): DEFINED_NONZERO
```

Map:

```text
f3(u0)=v0
f3(u1)=v1
bijection: yes
relations: preserved
readiness: preserved
mode(u1): unavailable, therefore not compared
```

Coverage:

```text
MAP_FAMILY_COVERAGE: exhaustive relative to {f3}
COMPARISON_ELEMENT_COVERAGE:
  nodes: exhaustive
  relations: exhaustive
  readiness: exhaustive
  mode: partial
CLAIMED_OUTPUT_LEVEL: PARTIAL_COMPARISON
```

Expected DSD and B1 output:

```text
CORRESPONDENCE_CLASS: PARTIAL_CORRESPONDENCE
STRICT_EQUIVALENCE: not_established
UNCOVERED_ELEMENT_SET: {mode(u1) <-> mode(v1)}
TERMINAL: COMPARISON_RESOLVED
```

The task is resolved at the explicitly requested partial-output level; global equivalence remains unclosed.

## 6. R4 — supplied representation bridge and provenance

Raw subjects:

```text
A4 state labels: {0,1,2}
transition: {0->1,1->2}

B4 state labels: {OFF,IDLE,ON}
transition: {OFF->IDLE,IDLE->ON}
```

Supplied bridge artifact:

```text
e4(0)=OFF
e4(1)=IDLE
e4(2)=ON
BRIDGE_PROVENANCE: supplied_external_to_comparison_fixture
PRECOMPARISON_TRANSFORMATION_POLICY: no hidden transformation; use supplied bridge only
```

Expected DSD and B1 output:

```text
transition preservation under e4: yes
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
DIRECT_CORRESPONDENCE_RELABELLING: prohibited
REPRESENTATION_PROVENANCE_PRESERVED: yes
TERMINAL: COMPARISON_RESOLVED
```

## 7. R5 — dynamic similarity separated from lineage identity

Frozen trajectory snapshots:

```text
t0: A5=(0,0), B5=(0,0)
t1: A5=(1,1), B5=(1,1)
t2: A5=(2,2), B5=(2,2)
```

Trajectory comparison coverage:

```text
TIME_SAMPLE_SET: {t0,t1,t2}
TIME_SAMPLE_COVERAGE: exhaustive relative to frozen task
coordinate map: identity
trajectory relation preservation: yes at all frozen samples
```

Supplied lineage records:

```text
LINEAGE_ID(A5): LA
LINEAGE_ID(B5): LB
LA != LB
LINEAGE_EVIDENCE_SOURCE: supplied_in_fixture
LINEAGE_IDENTITY_CLAIM_POLICY: lineage identity may be decided only from supplied lineage evidence
```

Expected DSD and B1 output:

```text
DYNAMIC_TRAJECTORY_CORRESPONDENCE: STRICT_EQUIVALENT at frozen sampled-trajectory resolution
LINEAGE_IDENTITY: no
LINEAGE_RELATION: DISTINCT_LINEAGES
TERMINAL: COMPARISON_RESOLVED
```

Trajectory equivalence is not upgraded to identity.

## 8. Strong baseline freeze

Baseline identity:

```text
B1_STRONG_TYPED_COMPARISON_ENGINE
```

B1 receives exactly the same:

```text
subject and stage identities
visible values, relations, Property/status records
stage order and first-branch search coverage
all supplied maps and map-family coverage
map property requirements
forward/reverse/inverse policies
comparison-element coverage and uncovered-element records
claim/output level
representation/bridge artifacts and provenance
precomparison-transformation policy
trajectory samples and sample coverage
lineage records and lineage claim policy
terminal-status rules
```

B1 is explicitly competent to:

```text
1. identify earliest justified divergence only after closing all earlier frozen stages;
2. preserve later re-convergence without erasing an earlier divergence;
3. distinguish forward direct correspondence from strict equivalence;
4. track image/surjectivity/inverse-coverage failures;
5. distinguish map-family coverage from comparison-element coverage;
6. produce PARTIAL_CORRESPONDENCE when the requested output level is partial;
7. preserve uncovered-element sets;
8. preserve representation/bridge provenance and encoded correspondence;
9. compare frozen dynamic trajectories while separately applying supplied lineage evidence;
10. preserve terminal states and full retrace records.
```

B1 must not be weakened after precommit.

## 9. Frozen gain criteria

```text
G1 FIRST_BRANCH_CLOSURE_GAIN
G2 DIRECTIONAL_MAP_AND_INVERSE_GAIN
G3 ELEMENT_COVERAGE_DISCIPLINE_GAIN
G4 BRIDGE_AND_REPRESENTATION_PROVENANCE_GAIN
G5 DYNAMIC_VS_LINEAGE_SEPARATION_GAIN
G6 STATUS_AND_RELATION_TRACE_GAIN
G7 TERMINAL_AND_RETRACEABILITY_GAIN
```

A criterion is `ESTABLISHED` only if DSD is correct and preserves a claim-relevant distinction that B1 loses despite receiving the same frozen information.

Decision rule:

```text
DSD incorrect or NONCONFORMANT -> FAIL
one or more G1-G7 established against correct B1 -> GAIN_ESTABLISHED
DSD and B1 both correct and B1 matches all seven dimensions -> NO_GAIN
fixture ambiguity/defect -> FAIL and correct prospectively under a new Case ID
```

No efficiency, terminology, elegance, implementation effort, or practical-domain advantage is scored.

## 10. Expected task-level outputs

```text
R1 DSD = B1
  PARTIAL_CORRESPONDENCE
  FIRST_BRANCH_POINT S2
  COMPARISON_RESOLVED

R2 DSD = B1
  DIRECT_CORRESPONDENCE
  strict equivalence no
  COMPARISON_RESOLVED

R3 DSD = B1
  PARTIAL_CORRESPONDENCE
  strict equivalence not_established
  COMPARISON_RESOLVED

R4 DSD = B1
  ENCODED_CORRESPONDENCE
  bridge provenance preserved
  COMPARISON_RESOLVED

R5 DSD = B1
  sampled-trajectory STRICT_EQUIVALENT
  lineage identity no / DISTINCT_LINEAGES
  COMPARISON_RESOLVED
```

## 11. Precommitted scoring

Total required checks: **60**.

```text
A. immutable/fairness discipline: 8
B. DSD execution: 18
C. B1 execution: 18
D. comparative gain: 9
E. scope/protocol pressure: 7
```

Detailed checks:

```text
A1 Protocol commit fixed
A2 R1-R5 frozen
A3 B1 capabilities frozen
A4 same claim-relevant inputs frozen
A5 G1-G7 frozen
A6 scoring frozen
A7 baseline weakening prohibited
A8 no post-hoc task/rule changes

B1-B5 exact R1-R5 main relation outputs
B6-B10 exact R1-R5 terminal outputs
B11 R1 earliest branch S2 with S0/S1 closed
B12 R1 S3 reconvergence does not erase S2 branch
B13 R2 forward correspondence != strict equivalence
B14 R2 target remainder b2 preserved
B15 R3 uncovered mode element preserved
B16 R4 bridge provenance preserved and encoded label retained
B17 R5 trajectory equivalence separated from lineage nonidentity
B18 all five DSD runs CONFORMANT

C1-C5 exact R1-R5 main relation outputs
C6-C10 exact R1-R5 terminal outputs
C11-C17 same seven claim-relevant discipline checks as B11-B17
C18 B1 full task retraceability preserved

D1-D7 G1-G7 NOT_ESTABLISHED if B1 matches
D8 final method gain = NO_GAIN when D1-D7 all hold
D9 NO_GAIN not interpreted as method failure/absorption/redundancy proof

E1 Protocol revision not required if no contradiction appears
E2 shared-core reopen not required if no contradiction appears
E3 strongest-reasonable-baseline claim limited to constructed-evidence level
E4 no external applicability claim
E5 no reproducibility/independent-validation claim
E6 no maturity claim
E7 no survival/merger/absorption/deletion conclusion
```

Decision:

```text
60/60 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

## 12. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 4
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 1
BASELINE_COMPARISON_CASES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
EXTERNAL_COMPARISON_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
```

A 60/60 PASS with `NO_GAIN` may add exactly:

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NO_GAIN_COMPARISON_CASE_INCREMENT: +1
BASELINE_COMPARISON_CASE_INCREMENT: +1
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

No external, reproducibility, independent-validation, maturity, survival, merger, absorption, deletion, or permanent-independence claim follows automatically.
