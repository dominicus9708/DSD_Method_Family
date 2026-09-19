# MSR-CH-006 — Deterministic Same-Project Retrace Result

Status: **EXECUTED — 56/56 PASS**  
Date: **2026-09-20**  
Case ID: `MSR-CH-006`  
Case class: `deterministic_same_project_retrace`  
Case origin: `same_project_retrace_of_prior_constructed_challenge`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen artifact identities

```text
P0 Measurement Protocol v0.1
commit: 70af7c3ddc618be34d0ff76fcc1ce63c895fc950
blob:   bc24a5e72adaf4a1b1e64203bd14b3e781810331

P1 MSR-CH-005 precommit
commit: 7722081d8b3612fd1c151aac63f7482c6cb882b7
blob:   5465898b17847ed627cb48fe98c678c77a4e7b4d

P2 MSR-CH-005 result comparison target
commit: 5a9c018d4a2b3b9ddf16fffee2fe36460d03b6b1
blob:   6e29b6918b230dab50e36b06717dd0e369185856

MSR-CH-006 precommit
commit: 25d32656d5aa50f5f4c3f15b0fa042d27e5f47a1
blob:   a6a31c2a036638fa0c844fb3b4f22af6ccb86dac

MSR-CH-006 reconstruction ledger
commit: 7f9f6c93934dfbc7733d90189570feed3e6381d4
blob:   0aab658db1c9d8975bef4151371587b264742b19
```

The reconstruction ledger was committed before P2 was opened for comparison.

```text
DERIVATION_BASIS:
  P0 + P1 only

P2_USED_DURING_DERIVATION:
  no

POST_RECONSTRUCTION_COMPARISON_TARGET:
  P2

POST_HOC_CORRECTIONS_AFTER_COMPARISON:
  0
```

## 2. R1 retrace — version-scoped decision semantics

Reconstructed from P0+P1:

```text
V1:
  A=0.6 -> HIGH
  B=0.4 -> LOW
  A-B -> PAIRWISE_DISCRIMINATING
  candidate -> MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
  plan -> MEASUREMENT_PLAN_SUFFICIENT

V2:
  A=0.6 -> LOW
  B=0.4 -> LOW
  A-B -> PAIRWISE_NONDISCRIMINATING
  candidate -> MEASUREMENT_NONDISCRIMINATING
  plan -> MEASUREMENT_PLAN_INSUFFICIENT
```

Compared with P2:

```text
R1_CLAIM_RELEVANT_MATCH: exact
R1_TERMINAL_MATCH: exact
R1_VERSION_SCOPE_MATCH: exact
```

Preserved:

```text
SAME_RAW_VALUES != SAME_DECISION_SEMANTICS_ACROSS_VERSIONS
LATER_RULE != RETROACTIVE_RULE_FOR_EARLIER_TASK
```

## 3. R2 retrace — dynamic distinguishability support

Reconstructed:

```text
t0:
  support at L -> NOT_YET_AVAILABLE
  upstream difference not usable as present local evidence
  non-arrival not converted to negative evidence
  plan -> MEASUREMENT_PLAN_BLOCKED

t1:
  support at L -> AVAILABLE
  C -> RED
  D -> BLUE
  pair -> PAIRWISE_DISCRIMINATING
  plan -> MEASUREMENT_PLAN_SUFFICIENT
```

Compared with P2:

```text
R2_T0_AVAILABILITY_MATCH: exact
R2_T0_TERMINAL_MATCH: exact
R2_T1_PAIRWISE_MATCH: exact
R2_T1_TERMINAL_MATCH: exact
```

Preserved:

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
UPSTREAM_DIFFERENCE != PRESENT_LOCAL_READOUT
```

## 4. R3 retrace — mixed candidate quality

Reconstructed:

```text
m1 -> MEASUREMENT_PARTIALLY_DISCRIMINATES
m2 -> MEASUREMENT_PARTIALLY_DISCRIMINATES
m3 -> redundant; no new required distinction
m4 -> MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE
m5 -> MEASUREMENT_INAPPLICABLE

joint {m1,m2}:
  E -> (0,0)
  F -> (1,0)
  G -> (1,1)
  -> all required pairs discriminate
  -> MEASUREMENT_PLAN_SUFFICIENT
```

Compared with P2:

```text
R3_m1_MATCH: exact
R3_m2_MATCH: exact
R3_m3_REDUNDANCY_MATCH: exact
R3_m4_MATCH: exact
R3_m5_MATCH: exact
R3_JOINT_TERMINAL_MATCH: exact
```

The DSD retrace does not add B1's finite-search/minimality claim.

```text
BASELINE_EXTRA_SEARCH_CAPABILITY != DSD_PROTOCOL_FAILURE
```

## 5. R4 retrace — proxy, aggregate collision, reconstruction bound

Reconstructed:

```text
m_direct:
  H-I discriminate
  H-J discriminate
  I-J nondiscriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

m_proxy:
  H aggregate 0
  I aggregate 0
  J aggregate 3
  H-I nondiscriminate
  H-J discriminate
  I-J discriminate
  -> MEASUREMENT_PARTIALLY_DISCRIMINATES

joint:
  H -> (P,0)
  I -> (Q,0)
  J -> (Q,3)
  -> MEASUREMENT_PLAN_SUFFICIENT

proxy/directness:
  retained

H/I collision:
  retained

noninjectivity:
  retained

full support reconstruction:
  unavailable

true alternative:
  not established
```

Compared with P2:

```text
R4_PAIRWISE_MATCH: exact
R4_JOINT_MATCH: exact
R4_PROXY_DIRECTNESS_MATCH: exact
R4_COLLISION_MATCH: exact
R4_RECONSTRUCTION_BOUND_MATCH: exact
R4_TRUE_ALTERNATIVE_BOUND_MATCH: exact
```

Preserved:

```text
PROXY != DIRECT
EQUAL_AGGREGATE != EQUAL_SUPPORT
DISCRIMINATING_PROXY != FULL_RECONSTRUCTION
PLAN_SUFFICIENT != TRUE_ALTERNATIVE_IDENTIFIED
```

## 6. R5 retrace — competing bridge versions

Reconstructed:

```text
V1:
  K -> OPEN
  L -> CLOSED
  -> PAIRWISE_DISCRIMINATING

V2:
  K -> OPEN
  L -> OPEN
  -> PAIRWISE_NONDISCRIMINATING

both admissible
precedence: none

candidate -> MEASUREMENT_UNDERDETERMINED
plan -> MEASUREMENT_PLAN_UNDERDETERMINED
```

Compared with P2:

```text
R5_BRIDGE_CONTENT_MATCH: exact
R5_AMBIGUITY_MATCH: exact
R5_CANDIDATE_STATUS_MATCH: exact
R5_TERMINAL_MATCH: exact
```

Preserved:

```text
MULTIPLE_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
NO_PRECEDENCE != LICENSE_TO_CHOOSE_POST_HOC
```

## 7. Bounded-claim and conformance retrace

Reconstructed before P2 comparison:

```text
MEASUREMENT_PROTOCOL_CONFORMANCE:
  CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

Maximum supported claim remained limited to:

```text
discrimination
availability
scope
candidate status
plan terminal

under the frozen supplied records and semantics
```

Not established:

```text
observed experimental result
true alternative
diagnosis
causality
full structural reconstruction
external empirical validity
independent validation
```

Comparison:

```text
BOUNDED_CLAIM_MATCH_WITH_P2: exact
CONFORMANCE_MATCH_WITH_P2: exact
PROTOCOL_PRESSURE_MATCH_WITH_P2: exact
```

## 8. Exact comparison summary

```text
R1: exact match
R2: exact match
R3: exact match
R4: exact match
R5: exact match

BOUNDING_RECORD: exact match
CONFORMANCE_RECORD: exact match
DISTINCTION_LEDGER: exact match

POST_COMPARISON_CORRECTIONS: 0
CLAIM_RELEVANT_MISMATCHES: 0
```

## 9. Frozen scoring

### A. Artifact lock / comparison discipline

```text
A1 PASS
A2 PASS
A3 PASS
A4 PASS
A5 PASS
A6 PASS
A7 PASS
A8 PASS
A9 PASS
A10 PASS

A: 10/10
```

### B. Five-subcase reconstruction

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
B19 PASS
B20 PASS
B21 PASS
B22 PASS
B23 PASS
B24 PASS

B: 24/24
```

### C. Scope / distinction / bounded claim

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

### D. Post-freeze comparison against P2

```text
D1 PASS
D2 PASS
D3 PASS
D4 PASS
D5 PASS
D6 PASS
D7 PASS
D8 PASS

D: 8/8
```

### E. Evidence-scope discipline

```text
E1 PASS
E2 PASS
E3 PASS
E4 PASS

E: 4/4
```

Final:

```text
TOTAL_REQUIRED_CHECKS: 56
PASSED: 56
FAILED: 0

RETRACE_VERDICT:
  PASS
```

## 10. Evidence interpretation

```text
SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once

REPRODUCIBILITY_CASES:
  0 -> 1
```

This means the frozen DSD Measurement claim-relevant outputs of MSR-CH-005 were reconstructible from immutable same-project protocol/precommit artifacts and matched the frozen result artifact exactly.

It does not mean:

```text
independent replication
blind replication
independent validation
external applicability
empirical validation
practical superiority
```

Preserved:

```text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
```

## 11. Counter update

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 5
POSITIVE_MEASUREMENT_CASES: 1
NEGATIVE_OR_FAILURE_MEASUREMENT_CASES: 1
METHOD_BOUNDARY_MEASUREMENT_CASES: 1
BASELINE_MEASUREMENT_CASES: 2
NO_GAIN_MEASUREMENT_CASES: 2

STRONGEST_REASONABLE_BASELINE_MEASUREMENT:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES: 1
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once

EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
INDEPENDENT_REPLICATION: not established

MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_MEASUREMENT_EVIDENCE_STATUS:
  validation_in_progress

PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No direct-pilot, baseline, NO_GAIN, or external-application counter was incremented by the retrace.

## 12. Maximum supported claim

MSR-CH-006 establishes only deterministic same-project retraceability of the frozen MSR-CH-005 DSD Measurement outputs from immutable project artifacts.

It does not establish independent replication or external validation.

## 13. Next

Proceed to the frozen-axis internal standardization audit.

That audit may evaluate whether Measurement Protocol v0.1 should be promoted to internal-standard status, held as developing, or returned for protocol revision.

External validation remains deferred.
