# CMP-CH-004 Result / DSD 비교론 Competent-Baseline NO_GAIN 결과

Status: **EXECUTED — 50/50 PASS / NO_GAIN**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`  
Precommit commit: `0d96d6ba83e25f2e14dba47c309cb74da7c71bad`  
Precommit blob: `1c5917a6b854321605ce1d22e63201f5cadb3c7f`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-004
CASE_CLASS: competent_baseline_no_gain_challenge
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B0_TYPED_COMPARISON_LEDGER
```

The precommit was fetched from its immutable commit before execution. No subject record, map, bridge, coverage declaration, baseline capability, gain criterion, terminal rule, or scoring item was changed.

## 2. Q1 — strict equivalence with typed status

DSD execution:

```text
f1 bijective: PASS
forward relation preservation: PASS
inverse preservation: PASS
readiness(a0)=DEFINED_ZERO <-> readiness(b0)=DEFINED_ZERO
readiness(a1)=DEFINED_NONZERO <-> readiness(b1)=DEFINED_NONZERO
status distinctions preserved: PASS
map-family coverage: exhaustive relative to {f1}
element coverage: exhaustive at frozen resolution

CORRESPONDENCE_CLASS: STRICT_EQUIVALENT
STRUCTURAL_EQUIVALENCE: yes
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution from the same records:

```text
bijection: PASS
forward/inverse relation checks: PASS
typed status preservation: PASS
CORRESPONDENCE_CLASS: STRICT_EQUIVALENT
TERMINAL: COMPARISON_RESOLVED
```

No claim-relevant difference appears.

## 3. Q2 — encoded correspondence

DSD execution:

```text
e(0)=OFF
e(1)=ON
bridge provenance: supplied_in_task
transition preservation under e: PASS
status preservation under e: PASS
bridge required for the frozen correspondence: yes

CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
DIRECT_CORRESPONDENCE_RELABELLING: no
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
bridge e retained as supplied provenance
transition/status preservation: PASS
bridge-dependent result retained
CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL: COMPARISON_RESOLVED
```

B0 did not erase bridge dependence merely because `e` is bijective.

## 4. Q3 — non-exhaustive map failure

DSD execution:

```text
g31 evaluated:
  bijective: PASS
  relation preservation: FAIL

g32:
  UNTESTED

MAP_FAMILY_COVERAGE: non_exhaustive
UNTESTED_MAP_SET: {g32}
GLOBAL_NONCORRESPONDENCE: not_established

CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_UNDERDETERMINED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
g31 failure retained
g32 retained as UNTESTED
non-exhaustive coverage retained
global noncorrespondence not asserted
CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
TERMINAL: COMPARISON_UNDERDETERMINED
```

Both systems preserve the untested remainder.

## 5. Q4 — aggregate collision without structural equivalence

DSD execution:

```text
A4 aggregate readout: 4
B4 aggregate readout: 4
AGGREGATE_READOUT_COMPARISON: equal

support cardinality:
  A4 = 3
  B4 = 1
  -> different

bijection over support required: impossible by cardinality
matched decomposition criterion: not satisfied

STRUCTURAL_EQUIVALENCE: no
CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen strict family
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
aggregate equality retained
support cardinality mismatch retained
no support bijection inferred
no structural equivalence inferred
CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen strict family
TERMINAL: COMPARISON_RESOLVED
```

Both preserve:

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
```

## 6. Q5 — missing claim-required bridge

DSD execution:

```text
CLAIM_REQUIRED_SEMANTIC_BRIDGE: yes
BRIDGE_SUPPLIED: no
SUBSTANTIVE_MAP_EVALUATION: not_performed
STRUCTURAL_DIFFERENCE_FROM_BRIDGE_ABSENCE: not_claimed
UNSUPPLIED_TRANSFORMATION: not_performed

CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_BLOCKED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

B0 execution:

```text
required bridge missing
substantive cross-semantic comparison not performed
no structural-difference claim fabricated
CORRESPONDENCE_CLASS: UNDETERMINED_CORRESPONDENCE
TERMINAL: COMPARISON_BLOCKED
```

Again the task-level result is identical.

## 7. DSD and B0 task-level comparison

```text
TASK   DSD RELATION                    DSD TERMINAL                  B0 RELATION                     B0 TERMINAL
Q1     STRICT_EQUIVALENT               COMPARISON_RESOLVED           STRICT_EQUIVALENT               COMPARISON_RESOLVED
Q2     ENCODED_CORRESPONDENCE          COMPARISON_RESOLVED           ENCODED_CORRESPONDENCE          COMPARISON_RESOLVED
Q3     UNDETERMINED_CORRESPONDENCE     COMPARISON_UNDERDETERMINED    UNDETERMINED_CORRESPONDENCE     COMPARISON_UNDERDETERMINED
Q4     NONCORRESPONDENCE               COMPARISON_RESOLVED           NONCORRESPONDENCE               COMPARISON_RESOLVED
Q5     UNDETERMINED_CORRESPONDENCE     COMPARISON_BLOCKED            UNDETERMINED_CORRESPONDENCE     COMPARISON_BLOCKED
```

Claim-relevant auxiliary distinctions also match:

```text
Q1 typed Property/status distinction: DSD preserved / B0 preserved
Q2 bridge provenance and encoded label: DSD preserved / B0 preserved
Q3 tested-vs-untested map remainder: DSD preserved / B0 preserved
Q4 aggregate-vs-structure distinction: DSD preserved / B0 preserved
Q5 missing bridge vs proven difference: DSD preserved / B0 preserved
```

## 8. Gain evaluation

```text
G1 RELATION_CLASS_SEPARATION_GAIN: NOT_ESTABLISHED
  B0 preserved the same relation-class distinctions.

G2 STATUS_DISTINCTION_GAIN: NOT_ESTABLISHED
  B0 preserved DEFINED_ZERO versus DEFINED_NONZERO in Q1.

G3 COVERAGE_AND_CLOSURE_GAIN: NOT_ESTABLISHED
  B0 retained the same tested/untested map and non-exhaustive closure discipline in Q3.

G4 BRIDGE_PROVENANCE_GAIN: NOT_ESTABLISHED
  B0 retained both supplied bridge dependence in Q2 and missing-bridge blockage in Q5.

G5 AGGREGATE_COLLISION_GAIN: NOT_ESTABLISHED
  B0 also refused to upgrade equal aggregate readout into structural equivalence in Q4.

G6 TERMINAL_AND_RETRACEABILITY_GAIN: NOT_ESTABLISHED
  B0 preserved enough task, map, bridge, coverage, and unresolved-state records to reconstruct every frozen task verdict.
```

Therefore:

```text
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

This is a successful comparative result, not a method failure. A competent typed comparison ledger supplied with the same semantics can match DSD on these frozen dimensions.

## 9. Three-ledger DSD result

Across the five DSD runs:

```text
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

Terminal status is task-specific as frozen above, and the comparative ledger is:

```text
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

Correctness/conformance remains separate from comparative gain.

## 10. Precommitted scoring

```text
A. immutable protocol / precommit / fairness   8 / 8 PASS
B. DSD task execution                         15 / 15 PASS
C. B0 task execution                          15 / 15 PASS
D. comparative gain                            8 / 8 PASS
E. scope and protocol pressure                 4 / 4 PASS

PRECOMMITTED_REQUIRED_CHECKS:                 50
PASSED:                                        50
FAILED:                                         0
CHALLENGE_VERDICT:                           PASS
```

No scoring item was deleted, weakened, or reinterpreted after execution.

## 11. Evidence increment

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NO_GAIN_COMPARISON_CASE_INCREMENT: +1
BASELINE_COMPARISON_CASE_INCREMENT: +1
```

Post-run state:

```text
DIRECT_COMPARISON_PILOTS: 4
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 1
BASELINE_COMPARISON_CASES: 1
STRONGEST_REASONABLE_BASELINE_COMPARISON: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 12. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No Protocol-v0.1 contradiction or fixture defect appeared in this run.

## 13. Limits and method-registry discipline

This case does not establish strongest-reasonable-baseline coverage, external applicability, reproducibility, independent validation, or maturity.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
```

No method survival, merger, absorption, deletion, redundancy, or permanent-independence conclusion is drawn.

## 14. Next

Run a separately precommitted `CMP-CH-005` strongest-reasonable-baseline comparison with materially richer comparison demands, including first-branch closure, directional/inverse requirements, representation/bridge provenance, partial-vs-global coverage, and possibly lineage-gated dynamic comparison. The baseline must again receive all claim-relevant information and may legitimately produce another `NO_GAIN`.
