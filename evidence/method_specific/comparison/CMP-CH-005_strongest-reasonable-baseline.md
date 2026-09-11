# CMP-CH-005 Result / DSD 비교론 Strongest-Reasonable-Baseline 결과

Status: **EXECUTED — 60/60 PASS / NO_GAIN**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`  
Precommit commit: `ad542304a184303c7898ef8506afe167735683c5`  
Precommit blob: `cbefe2e0948a5b14343b8202fd2461192ce603df`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-005
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_STRONG_TYPED_COMPARISON_ENGINE
```

The immutable precommit was fetched before execution. No subcase, expected output, baseline capability, gain criterion, or scoring item was changed.

## 2. R1 — earliest justified first branch

Stage-by-stage execution:

```text
S0: A1=0, B1=0
  value preserved: yes
  readiness DEFINED_ZERO preserved: yes

S1: A1=1, B1=1
  value preserved: yes
  readiness DEFINED_NONZERO preserved: yes

S2: A1=2, B1=3
  value preserved: no
  readiness DEFINED_NONZERO preserved: yes

S3: A1=4, B1=4
  value preserved: yes
```

All claim-relevant stages before S2 were explicitly checked and preserved. Therefore:

```text
EARLIER_STAGE_CLOSURE: {S0,S1} verified preserved
FIRST_JUSTIFIED_BRANCH_POINT: S2
S3_RECONVERGENCE_ERASES_BRANCH: no
CORRESPONDENCE_CLASS: PARTIAL_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

`S3` equality records later re-convergence but does not move or erase the earlier justified divergence.

B1 execution from the same records returned exactly the same first-branch and terminal result.

## 3. R2 — directional correspondence without strict equivalence

Forward execution:

```text
f2(a0)=b0
f2(a1)=b1
injective: yes
mapped relation a0->a1 maps to b0->b1: preserved
```

Global strict-equivalence closure:

```text
B2 target node b2 lies outside image(f2)
surjectivity: no
bijection: no
global inverse over B2: unavailable
```

Therefore:

```text
FORWARD_DIRECT_CORRESPONDENCE: established
STRICT_EQUIVALENCE: no
CORRESPONDENCE_CLASS: DIRECT_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 preserved the same image remainder and returned the same result.

## 4. R3 — partial versus global element coverage

Execution:

```text
f3 bijective: yes
node coverage: exhaustive
relation coverage: exhaustive
readiness coverage: exhaustive
readiness statuses: preserved
mode coverage: partial
mode(u1): RECORD_WITHHELD
mode(v1): DEFINED_NONZERO
```

No value was invented for `mode(u1)` and no mismatch was inferred merely from the withheld record.

```text
UNCOVERED_ELEMENT_SET: {mode(u1) <-> mode(v1)}
CORRESPONDENCE_CLASS: PARTIAL_CORRESPONDENCE
STRICT_EQUIVALENCE: not_established
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

The terminal is resolved because the requested output level was explicitly `PARTIAL_COMPARISON`, while global equivalence remains unclosed.

B1 retained the same uncovered-element set and returned the same partial result.

## 5. R4 — supplied representation bridge and provenance

Bridge execution:

```text
e4(0)=OFF
e4(1)=IDLE
e4(2)=ON
0->1 maps to OFF->IDLE: preserved
1->2 maps to IDLE->ON: preserved
BRIDGE_PROVENANCE: supplied_external_to_comparison_fixture
HIDDEN_TRANSFORMATION_PERFORMED: no
```

Therefore:

```text
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
DIRECT_CORRESPONDENCE_RELABELLING: no
REPRESENTATION_PROVENANCE_PRESERVED: yes
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 also retained bridge dependence and provenance instead of relabeling the result as direct correspondence.

## 6. R5 — dynamic trajectory equivalence separated from lineage

Trajectory execution:

```text
t0: A5=(0,0), B5=(0,0) -> preserved
t1: A5=(1,1), B5=(1,1) -> preserved
t2: A5=(2,2), B5=(2,2) -> preserved
TIME_SAMPLE_COVERAGE: exhaustive relative to frozen task
```

At the declared sampled-trajectory resolution:

```text
DYNAMIC_TRAJECTORY_CORRESPONDENCE: STRICT_EQUIVALENT
```

Lineage ledger:

```text
LINEAGE_ID(A5): LA
LINEAGE_ID(B5): LB
LA != LB
LINEAGE_RELATION: DISTINCT_LINEAGES
LINEAGE_IDENTITY: no
```

Therefore:

```text
TRAJECTORY_EQUIVALENCE_UPGRADED_TO_IDENTITY: no
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 preserved the same separation between trajectory correspondence and lineage identity.

## 7. DSD versus B1 task-level comparison

```text
SUBCASE  DSD MAIN RESULT                         B1 MAIN RESULT
R1       PARTIAL / FIRST_BRANCH S2              PARTIAL / FIRST_BRANCH S2
R2       DIRECT / strict equivalence no         DIRECT / strict equivalence no
R3       PARTIAL / global equivalence unclosed  PARTIAL / global equivalence unclosed
R4       ENCODED / provenance preserved         ENCODED / provenance preserved
R5       trajectory STRICT_EQUIVALENT            trajectory STRICT_EQUIVALENT
         lineage DISTINCT                        lineage DISTINCT
```

All five terminals:

```text
DSD: COMPARISON_RESOLVED
B1:  COMPARISON_RESOLVED
```

Claim-relevant auxiliary distinctions also matched:

```text
R1 earlier-stage closure and later reconvergence
R2 target remainder and missing global inverse
R3 uncovered element set
R4 bridge dependence and provenance
R5 trajectory-vs-lineage separation
```

## 8. Gain evaluation

```text
G1 FIRST_BRANCH_CLOSURE_GAIN: NOT_ESTABLISHED
  B1 identified S2 only after preserving S0/S1 closure and did not erase it at S3.

G2 DIRECTIONAL_MAP_AND_INVERSE_GAIN: NOT_ESTABLISHED
  B1 preserved forward correspondence while refusing strict equivalence without surjectivity/inverse coverage.

G3 ELEMENT_COVERAGE_DISCIPLINE_GAIN: NOT_ESTABLISHED
  B1 preserved the partial mode coverage and uncovered-element set.

G4 BRIDGE_AND_REPRESENTATION_PROVENANCE_GAIN: NOT_ESTABLISHED
  B1 kept R4 bridge-dependent and preserved bridge provenance.

G5 DYNAMIC_VS_LINEAGE_SEPARATION_GAIN: NOT_ESTABLISHED
  B1 separated sampled-trajectory equivalence from supplied distinct lineage identities.

G6 STATUS_AND_RELATION_TRACE_GAIN: NOT_ESTABLISHED
  B1 preserved the same status/relation traces used by the frozen tasks.

G7 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED
  B1 preserved enough frozen records to reconstruct all five decisions.
```

Therefore:

```text
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

This is a successful strongest-reasonable-baseline comparison at constructed-evidence level. It is not a DSD superiority result.

## 9. Precommitted scoring

```text
A. immutable/fairness discipline       8 / 8 PASS
B. DSD execution                      18 / 18 PASS
C. B1 execution                       18 / 18 PASS
D. comparative gain                    9 / 9 PASS
E. scope/protocol pressure             7 / 7 PASS

PRECOMMITTED_REQUIRED_CHECKS:         60
PASSED:                                60
FAILED:                                 0
CHALLENGE_VERDICT:                   PASS
```

No scoring item was removed, weakened, or reinterpreted after execution.

## 10. Evidence increment

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NO_GAIN_COMPARISON_CASE_INCREMENT: +1
BASELINE_COMPARISON_CASE_INCREMENT: +1
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

Post-run state:

```text
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 11. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No Protocol-v0.1 contradiction or fixture defect appeared.

## 12. Scope limits and registry discipline

This result establishes only the strongest-reasonable-baseline category at **constructed-evidence level**.

It does not establish:

```text
external applicability
reproducibility
independent validation
practical superiority
method maturity
permanent method independence
```

And:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
```

## 13. Next

Run the first external Comparison application `CMP-APP-001`, using a stable public source that supplies the compared records and a defensible external comparison criterion rather than inventing both inside the project fixture.
