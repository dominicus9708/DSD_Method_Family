# CMP-CH-001 Positive Direct Comparison Result / DSD 비교론 첫 직접 양성 시험

Status: **EXECUTED — 40/40 PASS**  
Date: **2026-09-10**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`  
Precommit commit: `16c4b15f93d66299a2a3890f436e1aff0076713c`  
Precommit blob: `1c87d4261022a07175796bce16e794f9d0c77f31`

## 1. Evidence identity

```text
CASE_ID: CMP-CH-001
CASE_CLASS: positive_direct_comparison_challenge
CASE_ORIGIN: constructed_same_project
METHOD_DIRECTLY_TESTED: DSD Comparison
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
BASELINE: none
```

The immutable precommit was fetched by commit before execution. No subject record, map/bridge family, criterion, coverage declaration, expected outcome, or scoring item was altered after execution began.

## 2. T1 — strict equivalence with sufficient closure

Frozen map:

```text
f1(a0)=b0
f1(a1)=b1
f1(a2)=b2
```

Execution:

```text
node cardinality A1/B1: 3 / 3
f1 injective: PASS
f1 surjective: PASS
f1 bijective: PASS
forward relations:
  a0->a1 maps to b0->b1: PASS
  a1->a2 maps to b1->b2: PASS
inverse relations:
  b0->b1 maps back to a0->a1: PASS
  b1->b2 maps back to a1->a2: PASS
Property-status preservation:
  DEFINED_ZERO -> DEFINED_ZERO: PASS
  DEFINED_NONZERO -> DEFINED_NONZERO: PASS
  DEFINED_ZERO -> DEFINED_ZERO: PASS
```

Coverage:

```text
MAP_FAMILY_COVERAGE: exhaustive over frozen singleton {f1}
COMPARISON_ELEMENT_COVERAGE:
  coordinates/features: exhaustive
  relations: exhaustive
  properties: exhaustive
  status classes: exhaustive
```

Result:

```text
CORRESPONDENCE_CLASS_RESULT: STRICT_EQUIVALENT
STRUCTURAL_EQUIVALENCE_RESULT: yes
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The strict-equivalence claim is closed by the frozen bijection, forward/inverse relation preservation, and exact mapped Property-status preservation.

## 3. T2 — direct correspondence weaker than strict equivalence

Frozen map:

```text
f2(x0)=y0
f2(x1)=y1
```

Execution:

```text
f2 injective: PASS
mapped relation x0->x1 -> y0->y1: PASS
mapped Property statuses:
  x0 DEFINED_ZERO -> y0 DEFINED_ZERO: PASS
  x1 DEFINED_NONZERO -> y1 DEFINED_NONZERO: PASS
unmapped target element: y2
surjective onto full B2: FAIL / not required for requested direct-correspondence criterion
```

Coverage:

```text
MAP_FAMILY_COVERAGE: exhaustive over frozen singleton {f2}
COMPARISON_ELEMENT_COVERAGE:
  exhaustive over A2-domain and mapped B2 subset
```

Result:

```text
CORRESPONDENCE_CLASS_RESULT: DIRECT_CORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: no
UNTESTED_OR_UNRESOLVED_SET_FOR_REQUESTED_CLASS: none
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

`y2` prevents bijective strict equivalence but does not invalidate the weaker one-way direct correspondence explicitly requested and frozen for T2.

```text
INJECTIVE_DIRECT_CORRESPONDENCE
!= STRICT_EQUIVALENCE
```

## 4. T3 — encoded correspondence through supplied bridge

Frozen bridge:

```text
e(0)=OFF
e(1)=ON
```

Execution:

```text
bridge explicitly used: yes
e injective: PASS
e surjective over supplied B3 state set: PASS
e bijective: PASS
transition 0->1 maps to OFF->ON: PASS
inverse transition preservation: PASS
Property statuses:
  0 DEFINED_ZERO -> OFF DEFINED_ZERO: PASS
  1 DEFINED_NONZERO -> ON DEFINED_NONZERO: PASS
literal label equality 0=OFF or 1=ON: not claimed
```

Representation provenance remained explicit:

```text
A3 original labels: {0,1}
B3 original labels: {OFF,ON}
claim-relevant bridge: supplied e
hidden normalization/transformation: none
```

Result:

```text
ENCODING_OR_BRIDGE_USED: e
CORRESPONDENCE_CLASS_RESULT: ENCODED_CORRESPONDENCE
STRUCTURAL_EQUIVALENCE_RESULT: equivalent_under_supplied_encoding_only
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The bridge's bijectivity does not erase the fact that the correspondence is encoded.

```text
ENCODED_CORRESPONDENCE
!= DIRECT_CORRESPONDENCE
```

## 5. T4 — equal aggregate readout, structural non-equivalence

Frozen supplied readouts:

```text
A4 terms: {1,1,2}
A4 support cardinality: 3
A4 aggregate readout: 4

B4 terms: {4}
B4 support cardinality: 1
B4 aggregate readout: 4
```

Aggregate comparison:

```text
AGGREGATE_READOUT_COMPARISON_RESULT: equal
```

Structural criterion requires a bijection between support sets. By finite cardinality:

```text
|support(A4)| = 3
|support(B4)| = 1
3 != 1
there exists no bijection support(A4) -> support(B4)
```

Therefore the frozen bijection family is exhaustively closed by impossibility rather than by testing an arbitrary single failed map.

Result:

```text
CORRESPONDENCE_CLASS_RESULT: NONCORRESPONDENCE under the frozen strict structural family
STRUCTURAL_EQUIVALENCE_RESULT: no
AGGREGATE_READOUT_COMPARISON_RESULT: equal
SUPPORT_RECONSTRUCTION_FROM_AGGREGATE: not permitted
DECOMPOSITION_RECONSTRUCTION_FROM_AGGREGATE: not permitted
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Thus the protocol preserved:

```text
AGGREGATE_EQUALITY
!= STRUCTURAL_EQUIVALENCE
```

## 6. Cross-task relation separation

The four frozen task instances produced four deliberately distinct relation outcomes:

```text
T1 -> STRICT_EQUIVALENT
T2 -> DIRECT_CORRESPONDENCE
T3 -> ENCODED_CORRESPONDENCE
T4 -> NONCORRESPONDENCE under frozen strict structural family
```

No relation class was upgraded by terminology, aggregate equality, or successful encoding alone.

Required distinctions all survived:

```text
STRICT_EQUIVALENT != DIRECT_CORRESPONDENCE
DIRECT_CORRESPONDENCE != ENCODED_CORRESPONDENCE
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
INJECTIVE_EMBEDDING != BIJECTIVE_EQUIVALENCE
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
```

## 7. Three-ledger result

All four task instances:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

This challenge contains no competent baseline, so correct Comparison execution cannot be promoted into `GAIN_ESTABLISHED` or `NO_GAIN`.

## 8. Precommitted scoring

```text
A. immutable protocol / precommit discipline   8 / 8 PASS
B. T1 strict-equivalence checks                8 / 8 PASS
C. T2 weaker-direct checks                     8 / 8 PASS
D. T3 encoded checks                           8 / 8 PASS
E. T4 aggregate-collision checks               8 / 8 PASS

PRECOMMITTED_REQUIRED_CHECKS:                 40
PASSED:                                        40
FAILED:                                         0
CHALLENGE_VERDICT:                           PASS
```

No post-hoc exception, criterion change, or expected-output rewrite was used.

## 9. Evidence increment

```text
DIRECT_COMPARISON_PILOT_INCREMENT: +1
POSITIVE_COMPARISON_CASE_INCREMENT: +1
```

Post-run state:

```text
DIRECT_COMPARISON_PILOTS: 1
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 0
BOUNDARY_COMPARISON_CASES: 0
NO_GAIN_COMPARISON_CASES: 0
BASELINE_COMPARISON_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPARISON_APPLICATIONS: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 10. Protocol pressure and limits

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
METHOD_SURVIVAL_OR_MERGER_DECISION_FROM_THIS_CASE: none
```

This result establishes only that Protocol v0.1 handled this first constructed positive challenge as precommitted. It does not establish external applicability, reproducibility, comparative gain, independent validation, method maturity, or permanent method independence.

## 11. Next

Run a separately precommitted `CMP-CH-002` negative/failure challenge that distinguishes at least:

```text
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
resolved NONCORRESPONDENCE where closure is actually sufficient
```

and pressures non-exhaustive map-family closure, partial element coverage, missing claim-required bridge, and missing reverse/inverse evidence without treating uncertainty as structural difference.
