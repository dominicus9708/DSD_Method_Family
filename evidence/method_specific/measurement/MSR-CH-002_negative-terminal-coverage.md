# MSR-CH-002 — Negative-Terminal Coverage Challenge Result

Status: **EXECUTED — 60/60 PASS**  
Date: **2026-09-19**  
Case ID: `MSR-CH-002`  
Case class: `negative_terminal_coverage_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen identities

```text
PROTOCOL_COMMIT: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
PROTOCOL_BLOB: bc24a5e72adaf4a1b1e64203bd14b3e781810331

BOUNDARY_AMENDMENT_COMMIT: 7f09baa7e2bb2701b4f01471abbbd443d226a78a
BOUNDARY_AMENDMENT_BLOB: 1ac7933fc19d95e9070432de99deb5a0fd1d382c

PRECOMMIT_COMMIT: 5b06e49b39a41eb20c06b473a26bd90fea7e2cc6
PRECOMMIT_BLOB: a145467b141c58d7a8f5388487ed8175d34dde2a
```

No protocol, amendment, subcase, terminal expectation, or scoring rule was changed after precommit.

## 2. N1 — partially sufficient

Frozen task:

```text
ALTERNATIVES: A,B,C
REQUIRED_DISTINCTIONS: A-B, A-C, B-C
CANDIDATE: m_AB
CANDIDATE_SCOPE: A-B only
A -> RED
B -> BLUE
```

Execution:

```text
m_AB:
  A-B -> PAIRWISE_DISCRIMINATING
  A-C -> PAIRWISE_OUT_OF_SCOPE for m_AB
  B-C -> PAIRWISE_OUT_OF_SCOPE for m_AB

CANDIDATE_STATUS:
  MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
```

The declared plan covers and discriminates A-B, but supplies no candidate whose declared scope covers A-C or B-C. This is a plan-coverage limitation, not missing assessment data inside an applicable candidate.

Terminal:

```text
MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT
```

Preserved:

```text
PARTIALLY_SUFFICIENT != SUFFICIENT
PARTIALLY_SUFFICIENT != BLOCKED
CANDIDATE_FULL_SUCCESS_ON_ASSIGNED_SCOPE != PLAN_FULL_SUFFICIENCY
```

Conformance: `CONFORMANT`.

## 3. N2 — insufficient

Frozen task:

```text
ALTERNATIVES: D,E
REQUIRED_DISTINCTION: D-E
m_same(D) = SAME
m_same(E) = SAME
both defined and applicable
```

Execution:

```text
D-E -> PAIRWISE_NONDISCRIMINATING

CANDIDATE_STATUS:
  MEASUREMENT_NONDISCRIMINATING

PLAN_TERMINAL:
  MEASUREMENT_PLAN_INSUFFICIENT
```

All required assessment information is present. Therefore the equal defined readouts are not treated as missing data or blockage.

Preserved:

```text
NONDISCRIMINATING != BLOCKED
DEFINED_EQUAL_READOUT != MISSING_DATA
INSUFFICIENT != METHOD_FAILURE
```

Conformance: `CONFORMANT`.

## 4. N3 — blocked with separate inapplicable candidate

Frozen task:

```text
ALTERNATIVES: F,G
REQUIRED_DISTINCTION: F-G
```

Candidate `m_need_bridge`:

```text
applicable: yes
source value records: supplied
required measurement-to-alternative decision bridge: explicitly absent
```

Execution:

```text
m_need_bridge:
  pairwise assessment -> PAIRWISE_BLOCKED

CANDIDATE_STATUS:
  MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
```

Candidate `m_inapp`:

```text
declared domain: object class K
task object class: object class L

CANDIDATE_STATUS:
  MEASUREMENT_INAPPLICABLE
```

Plan terminal:

```text
MEASUREMENT_PLAN_BLOCKED
```

The absent bridge remains an explicit absence. It is not converted into a negative readout. The inapplicable candidate is likewise not converted into evidence against either alternative.

Preserved:

```text
MISSING_REQUIRED_BRIDGE != NEGATIVE_RESULT
INAPPLICABLE != NEGATIVE_RESULT
BLOCKED != INSUFFICIENT
BLOCKED != UNDERDETERMINED
```

Conformance: `CONFORMANT`.

## 5. N4 — out of scope

Frozen task:

```text
ALTERNATIVES: P,Q
REQUIRED_DISTINCTION: P-Q
TASK_SCOPE: regime R2
```

Only supplied candidate:

```text
m_R1
CANDIDATE_SCOPE: regime R1 only
R1 outcome map: complete
R2 extension: not declared
```

Execution:

```text
m_R1 relation requested under R2:
  PAIRWISE_OUT_OF_SCOPE

CANDIDATE_STATUS:
  MEASUREMENT_OUT_OF_SCOPE

PLAN_TERMINAL:
  MEASUREMENT_PLAN_OUT_OF_SCOPE
```

No R2 value is fabricated. The known scope mismatch is not interpreted as missing negative evidence.

Preserved:

```text
OUT_OF_SCOPE != INAPPLICABLE
OUT_OF_SCOPE != BLOCKED
OUT_OF_SCOPE != INSUFFICIENT
NO_DECLARED_SCOPE_EXTENSION != MISSING_NEGATIVE_RESULT
```

Conformance: `CONFORMANT`.

## 6. N5 — underdetermined

Frozen task:

```text
ALTERNATIVES: U,V
REQUIRED_DISTINCTION: U-V
CANDIDATE: m_amb
```

Two simultaneously admissible supplied bridges:

```text
B1:
  U -> LOW
  V -> HIGH
  => PAIRWISE_DISCRIMINATING

B2:
  U -> LOW
  V -> LOW
  => PAIRWISE_NONDISCRIMINATING

PRECEDENCE_RULE:
  none supplied
```

Execution:

```text
CANDIDATE_STATUS:
  MEASUREMENT_UNDERDETERMINED

PLAN_TERMINAL:
  MEASUREMENT_PLAN_UNDERDETERMINED
```

Nothing required is missing. The problem is competing admissible claim-relevant bridges with no frozen precedence.

Preserved:

```text
COMPETING_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
UNDERDETERMINED != BLOCKED
UNDERDETERMINED != LICENSE_TO_CHOOSE_POST_HOC
```

No bridge is chosen after seeing which result is preferred.

Conformance: `CONFORMANT`.

## 7. Candidate-status coverage after MSR-CH-001 + MSR-CH-002

```text
MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION:
  directly exercised in N1 by m_AB

MEASUREMENT_PARTIALLY_DISCRIMINATES:
  directly exercised in MSR-CH-001 by m_X, m_Y, m_AGG

MEASUREMENT_NONDISCRIMINATING:
  directly exercised in N2 by m_same

MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE:
  directly exercised in N3 by m_need_bridge

MEASUREMENT_INAPPLICABLE:
  directly exercised in N3 by m_inapp

MEASUREMENT_OUT_OF_SCOPE:
  directly exercised in N4 by m_R1

MEASUREMENT_UNDERDETERMINED:
  directly exercised in N5 by m_amb

ALL_SEVEN_CANDIDATE_STATUSES_DIRECTLY_EXERCISED: yes
```

## 8. Plan-terminal coverage after MSR-CH-001 + MSR-CH-002

```text
MEASUREMENT_PLAN_SUFFICIENT:
  MSR-CH-001

MEASUREMENT_PLAN_PARTIALLY_SUFFICIENT:
  MSR-CH-002-N1

MEASUREMENT_PLAN_INSUFFICIENT:
  MSR-CH-002-N2

MEASUREMENT_PLAN_BLOCKED:
  MSR-CH-002-N3

MEASUREMENT_PLAN_OUT_OF_SCOPE:
  MSR-CH-002-N4

MEASUREMENT_PLAN_UNDERDETERMINED:
  MSR-CH-002-N5

ALL_SIX_PLAN_TERMINALS_DIRECTLY_EXERCISED: yes
```

This direct coverage closes the terminal-enum gap before the later internal standardization audit.

## 9. Cross-subcase guards

All preserved:

```text
PARTIALLY_SUFFICIENT != SUFFICIENT
INSUFFICIENT != BLOCKED
BLOCKED != UNDERDETERMINED
OUT_OF_SCOPE != INAPPLICABLE
INAPPLICABLE != NEGATIVE_RESULT
NONDISCRIMINATING != MISSING_DATA
UNDERDETERMINED != LICENSE_TO_CHOOSE_POST_HOC

CONFORMANT_NEGATIVE_TERMINAL != METHOD_FAILURE
CONFORMANT_NEGATIVE_TERMINAL != METHOD_DELETION_PROOF
CONFORMANT_NEGATIVE_TERMINAL != METHOD_MERGER_PROOF
```

## 10. Validity-gate result

Each subcase satisfied every applicable `G1-G14` requirement.

Common gate interpretation:

```text
G1 PASS
  frozen task identity / alternatives / distinctions / scope

G2 PASS
  candidate identities/types/domains/scopes frozen

G3 PASS
  applicability and candidate statuses preserved

G4 NOT_APPLICABLE_WITH_REASON
  no separate Formation structural-difference handoff required by these fixtures

G5 PASS
  supplied bridges used as supplied; explicit absence retained in N3;
  no prediction/calibration/bridge invented

G6 PASS
  exact-label semantics frozen; no post-hoc threshold

G7 PASS
  required candidate relations evaluated or explicitly outside candidate scope

G8 NOT_APPLICABLE_WITH_REASON
  no joint-measurement inference is used in MSR-CH-002

G9 NOT_APPLICABLE_WITH_REASON
  no reduced/aggregate reconstruction claim is used in these subcases

G10 PASS
  bridge provenance/absence and roles retained

G11 PASS / NOT_APPLICABLE_WITH_REASON by subcase
  N4 regime scope is explicitly evaluated;
  static subcases N1/N2/N3/N5 make no dynamic-support claim

G12 PASS
  no neighboring method silently executed

G13 PASS
  no selected measurement relabeled as observed result

G14 PASS
  candidate status, plan terminal, conformance, gain, bounded claim emitted
```

Overall challenge conformance:

```text
MSR-CH-002_CONFORMANCE: CONFORMANT
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 11. Frozen scoring

### A. Immutability / common scope

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

### B. N1 partial sufficiency

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
B: 10/10
```

### C. N2 insufficiency

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
C: 10/10
```

### D. N3 blockage / inapplicability

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
D11 PASS
D12 PASS
D: 12/12
```

### E. N4 out-of-scope

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

### F. N5 underdetermination

```text
F1 PASS
F2 PASS
F3 PASS
F4 PASS
F5 PASS
F6 PASS
F7 PASS
F8 PASS
F9 PASS
F10 PASS
F: 10/10
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 60
PASSED: 60
FAILED: 0
TOTAL: 60/60 PASS
```

## 12. Method-gain and evidence interpretation

No baseline was run.

```text
MEASUREMENT_METHOD_GAIN_STATUS: NOT_ASSESSED
```

The challenge shows that Protocol v0.1 can preserve distinct negative/limited terminal meanings in the frozen constructed cases. It does not establish comparative superiority or external validity.

```text
SUCCESSFUL_DIRECT_MEASUREMENT_PILOT
  means conformant execution against the precommitted fixture

SUCCESSFUL_DIRECT_MEASUREMENT_PILOT
  != POSITIVE_MEASUREMENT_TERMINAL
```

## 13. Counter update authorized by precommit

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 1 -> 2
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 1 -> 2
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 0 -> 1

POSITIVE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 0
BASELINE_MEASUREMENT_CASES: 0
NO_GAIN_MEASUREMENT_CASES: 0
REPRODUCIBILITY_CASES: 0

EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_MEASUREMENT_EVIDENCE_STATUS: validation_in_progress

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 14. Maximum supported claim

MSR-CH-002 establishes only that the frozen Measurement Protocol can distinguish, in constructed internal fixtures:

```text
partial sufficiency
insufficiency
blockage
candidate inapplicability
task/candidate out-of-scope status
underdetermination from competing supplied bridges
```

without collapsing these statuses into one another or treating conformant negative terminals as method failure.

It does not establish external-domain adequacy, empirical truth, independent validation, comparative gain, or permanent method independence.

## 15. Next

Proceed to a separately precommitted direct method-boundary challenge against neighboring methods. The objective is not to prove permanent method survival, but to test whether Measurement's binding operation remains distinguishable under fair shared-artifact cases.
