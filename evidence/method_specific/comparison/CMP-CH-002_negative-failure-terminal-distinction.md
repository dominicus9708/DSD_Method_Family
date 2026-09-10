# CMP-CH-002 Result / DSD 비교론 Negative-Failure Terminal Distinction 결과

Status: **EXECUTED — 48/48 PASS**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`  
Precommit commit: `c852a688c3411c7d8568e2597262c4ec32a0355e`  
Precommit blob: `caec1bb29368cd291abd77ae7789ecfe50ac4a98`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-002
CASE_CLASS: negative_failure_terminal_distinction
CASE_ORIGIN: constructed_same_project
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: none
```

The precommit was fetched at its immutable commit before execution. No subject record, map family, coverage declaration, criterion, expected terminal state, or scoring item was changed.

## 2. N1 — non-exhaustive map failure remains underdetermined

Frozen family:

```text
F1 = {f11,f12}
```

Only `f11` is evaluated.

```text
f11(a0)=b1
f11(a1)=b0
```

`A1` contains `a0->a1`. Under `f11`, this maps to `b1->b0`, while `B1` contains only `b0->b1`.

Execution:

```text
f11 bijective: PASS
f11 relation preservation: FAIL
f12: UNTESTED
MAP_FAMILY_COVERAGE: non_exhaustive
UNTESTED_MAP_SET: {f12}
```

Therefore:

```text
CORRESPONDENCE_CLASS_RESULT: UNDETERMINED_CORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: underdetermined
TERMINAL_COMPARISON_STATUS: COMPARISON_UNDERDETERMINED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The failed evaluated map was not promoted into global noncorrespondence.

## 3. N2 — partial element coverage blocks strict-equivalence closure

Frozen map:

```text
f2(x0)=y0
f2(x1)=y1
```

Execution:

```text
f2 bijective: PASS
forward relation preservation: PASS
inverse supplied: PASS
readiness(x0)=DEFINED_ZERO
readiness(y0)=DEFINED_ZERO
readiness(x1)=DEFINED_NONZERO
readiness(y1)=RECORD_WITHHELD
properties coverage: partial
status_classes coverage: partial
UNRESOLVED_SET: {readiness(y1)}
```

The requested `STRICT_EQUIVALENCE_DECISION` requires all claim-relevant Property/status conditions to close. They do not.

Therefore:

```text
CORRESPONDENCE_CLASS_RESULT: UNDETERMINED_CORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: underdetermined
TERMINAL_COMPARISON_STATUS: COMPARISON_UNDERDETERMINED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Structural matches on the tested subset were preserved, but partial element coverage was not upgraded to global strict equivalence.

## 4. N3 — missing required semantic bridge is blocked, not different

The frozen task declares that `{0,1}` and `{COLD,HOT}` do not share a literal semantic coordinate system and requires a supplied bridge before substantive correspondence evaluation.

Execution:

```text
CLAIM_REQUIRED_BRIDGE: yes
BRIDGE_SUPPLIED: no
MAP_FAMILY_SOURCE: unavailable until bridge supplied
SUBSTANTIVE_MAP_EVALUATION_PERFORMED: no
UNSUPPLIED_TRANSFORMATION_PERFORMED: no
```

Therefore:

```text
CORRESPONDENCE_CLASS_RESULT: UNDETERMINED_CORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: not_evaluated
TERMINAL_COMPARISON_STATUS: COMPARISON_BLOCKED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No structural difference or noncorrespondence was fabricated from bridge absence.

## 5. N4 — forward success does not close required inverse evidence

Frozen forward map:

```text
f4(u0)=v0
f4(u1)=v1
```

The run freezes:

```text
MAP_PROPERTY_REQUIREMENT_PROFILE:
  bijective_required
  forward_relation_preservation_required
  inverse_preservation_required
REVERSE_DIRECTION_OR_INVERSE_POLICY: required_but_unverified
```

Execution of the frozen evaluated portion:

```text
f4 bijective: PASS
forward relation preservation: PASS
inverse-preservation evidence in this run: UNVERIFIED
UNRESOLVED_SET: {inverse_preservation}
```

This does not claim that inverse preservation is impossible. It records that the stronger requested closure was not evaluated inside the frozen run and is therefore not established by forward success alone.

Therefore:

```text
CORRESPONDENCE_CLASS_RESULT: UNDETERMINED_CORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: underdetermined
TERMINAL_COMPARISON_STATUS: COMPARISON_UNDERDETERMINED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

## 6. N5 — exhaustive all-map failure closes noncorrespondence

All bijections between the two 2-element sets are frozen and evaluated:

```text
g1(m0)=n0, g1(m1)=n1
g2(m0)=n1, g2(m1)=n0
```

`A5` contains `m0->m1`; `B5` has no directed relation.

Execution:

```text
g1 bijective: PASS
g1 relation preservation: FAIL

g2 bijective: PASS
g2 relation preservation: FAIL

MAP_FAMILY_COVERAGE: exhaustive
UNTESTED_MAP_SET: none
COMPARISON_ELEMENT_COVERAGE:
  coordinates_or_features: exhaustive
  relations: exhaustive
```

Every map in the frozen admissible family fails the required relation-preservation criterion.

Therefore:

```text
CORRESPONDENCE_CLASS_RESULT: NONCORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: no
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

This is the legitimate contrast with N1: exhaustive closure supports noncorrespondence, while a non-exhaustive failure-to-find does not.

## 7. Terminal-state comparison

```text
TASK   COMPARISON CLASS             TERMINAL STATUS
N1     UNDETERMINED_CORRESPONDENCE  COMPARISON_UNDERDETERMINED
N2     UNDETERMINED_CORRESPONDENCE  COMPARISON_UNDERDETERMINED
N3     UNDETERMINED_CORRESPONDENCE  COMPARISON_BLOCKED
N4     UNDETERMINED_CORRESPONDENCE  COMPARISON_UNDERDETERMINED
N5     NONCORRESPONDENCE             COMPARISON_RESOLVED
```

All five runs are `CONFORMANT`; all method-gain ledgers remain `NOT_ASSESSED`.

## 8. Preserved distinctions

```text
NONEXHAUSTIVE_MAP_FAILURE
!= RESOLVED_NONCORRESPONDENCE

PARTIAL_ELEMENT_COVERAGE
!= STRICT_EQUIVALENCE

MISSING_REQUIRED_BRIDGE
!= PROVEN_STRUCTURAL_DIFFERENCE

FORWARD_MAP_SUCCESS
!= VERIFIED_INVERSE_PRESERVATION

COMPARISON_UNDERDETERMINED
!= COMPARISON_BLOCKED

RESOLVED_NONCORRESPONDENCE
!= FAILURE_TO_FIND_UNDER_NONEXHAUSTIVE_SEARCH
```

## 9. Precommitted scoring

```text
A. immutable protocol / precommit discipline   8 / 8 PASS
B. N1 non-exhaustive map                       8 / 8 PASS
C. N2 partial element coverage                 8 / 8 PASS
D. N3 missing bridge                           8 / 8 PASS
E. N4 inverse evidence                         8 / 8 PASS
F. N5 exhaustive noncorrespondence             8 / 8 PASS

PRECOMMITTED_REQUIRED_CHECKS:                 48
PASSED:                                        48
FAILED:                                         0
CHALLENGE_VERDICT:                           PASS
```

No scoring item was deleted or weakened after execution.

## 10. Evidence increment

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
NEGATIVE_OR_FAILURE_COMPARISON_CASE_INCREMENT: +1
```

Post-run state:

```text
DIRECT_COMPARISON_PILOTS: 2
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
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

The challenge did not expose a Protocol-v0.1 contradiction.

## 12. Limits and method-registry discipline

This constructed negative/failure challenge establishes neither external applicability nor comparative method gain.

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
```

No method survival, deletion, merger, or absorption decision is made from this result.

## 13. Next

Run a separately precommitted direct method-boundary challenge `CMP-CH-003`. It should force Comparison to hand off hidden Analysis, Classification, Transformation, Audit, and Provenance/Lineage operations while preserving a legitimate Comparison result wherever the supplied comparison itself is still executable.
