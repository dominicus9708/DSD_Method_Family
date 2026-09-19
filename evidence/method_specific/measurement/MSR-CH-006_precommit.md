# MSR-CH-006 Precommit — Deterministic Same-Project Retrace

Status: **PRECOMMITTED BEFORE RETRACE EXECUTION**  
Date: **2026-09-20**  
Method: **DSD Measurement / DSD 측정론**  
Protocol: **Measurement Protocol v0.1**

## 1. Case identity

```text
CASE_ID: MSR-CH-006
CASE_CLASS: deterministic_same_project_retrace
CASE_ORIGIN: same_project_retrace_of_prior_constructed_challenge
EVIDENCE_SCOPE_CLASS: method_specific
RETRACE_TARGET: MSR-CH-005
EXTERNAL_APPLICATION: no
BASELINE: none for evidence increment
```

Purpose: determine whether the claim-relevant DSD Measurement outputs of `MSR-CH-005` can be reconstructed deterministically from immutable project artifacts without modifying the protocol, task records, candidate identities, version/regime scope, decision rules, dynamic-support handoffs, bridge records, proxy/directness records, collision/reconstruction sidecars, ambiguity rules, or bounded-claim limits.

This is a same-project documentary retrace.

```text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
```

## 2. Frozen artifact chain

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
```

Retrace derivation must use `P0 + P1` only.

`P2` may be used only after the reconstructed DSD ledger has been frozen as a separate artifact.

No live web lookup, external corpus, new measurement candidate, new bridge, new threshold, new dynamic-support rule, new proxy/directness assignment, new reconstruction rule, or post-hoc scope change may repair a mismatch.

## 3. Frozen retrace target

Reconstruct the DSD Measurement side of five `MSR-CH-005` subcases:

```text
R1 version-scoped decision semantics
R2 dynamic distinguishability support
R3 mixed candidate quality + predeclared sufficient plan
R4 proxy + aggregate collision + reconstruction bounds
R5 competing bridge versions / underdetermination
```

The prior B1 baseline comparison is historical comparative evidence only and is not re-executed or recounted.

## 4. Frozen expected reconstruction basis

The following are not copied from P2. They are the precommitted consequences to be regenerated from P0+P1.

### R1 — version-scoped semantics

```text
raw(A)=0.6
raw(B)=0.4

V1:
  threshold=0.5
  A -> HIGH
  B -> LOW
  A-B -> PAIRWISE_DISCRIMINATING
  candidate -> MEASUREMENT_DISCRIMINATES_AT_DECLARED_RESOLUTION
  terminal -> MEASUREMENT_PLAN_SUFFICIENT

V2:
  threshold=0.7
  A -> LOW
  B -> LOW
  A-B -> PAIRWISE_NONDISCRIMINATING
  candidate -> MEASUREMENT_NONDISCRIMINATING
  terminal -> MEASUREMENT_PLAN_INSUFFICIENT
```

Preserve:

```text
SAME_RAW_VALUES != SAME_DECISION_SEMANTICS_ACROSS_VERSIONS
LATER_RULE != RETROACTIVE_RULE_FOR_EARLIER_TASK
```

### R2 — dynamic support

```text
t0:
  upstream difference exists
  local distinguishability support at L = NOT_YET_AVAILABLE
  local use of difference = prohibited
  negative-result inference = prohibited
  terminal -> MEASUREMENT_PLAN_BLOCKED

t1:
  support at L = AVAILABLE
  C -> RED
  D -> BLUE
  pair -> PAIRWISE_DISCRIMINATING
  terminal -> MEASUREMENT_PLAN_SUFFICIENT
```

Preserve:

```text
NOT_YET_DISTINGUISHABLE != NEGATIVE_EVIDENCE
UPSTREAM_DIFFERENCE != PRESENT_LOCAL_READOUT
```

### R3 — mixed candidate quality

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
  same partition as m1
  -> redundancy retained
  -> no new required distinction

m4:
  required bridge absent
  -> MEASUREMENT_BLOCKED_BY_MISSING_BRIDGE_OR_PREREQUISITE

m5:
  domain mismatch
  -> MEASUREMENT_INAPPLICABLE

predeclared joint {m1,m2}:
  E -> (0,0)
  F -> (1,0)
  G -> (1,1)
  -> all required pairs discriminate
  -> MEASUREMENT_PLAN_SUFFICIENT
```

No optimization or minimality claim is required from the DSD retrace.

### R4 — proxy / collision / reconstruction bound

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
  preserved

H/I aggregate collision:
  preserved

full support reconstruction:
  unavailable

true alternative:
  not established
```

Preserve:

```text
PROXY != DIRECT
EQUAL_AGGREGATE != EQUAL_SUPPORT
DISCRIMINATING_PROXY != FULL_RECONSTRUCTION
PLAN_SUFFICIENT != TRUE_ALTERNATIVE_IDENTIFIED
```

### R5 — competing bridges

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

candidate -> MEASUREMENT_UNDERDETERMINED
terminal -> MEASUREMENT_PLAN_UNDERDETERMINED
```

Preserve:

```text
MULTIPLE_ADMISSIBLE_BRIDGES != MISSING_BRIDGE
NO_PRECEDENCE != LICENSE_TO_CHOOSE_POST_HOC
```

## 5. Frozen protocol-level reconstruction

The retrace must also reconstruct:

```text
MEASUREMENT_PROTOCOL_CONFORMANCE: CONFORMANT
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no

MAXIMUM_SUPPORTED_CLAIM:
  discrimination/availability/scope judgments only under supplied records

NOT ESTABLISHED:
  observed experimental result
  true alternative
  diagnosis
  causality
  full reconstruction
  external empirical validity
```

The `NO_GAIN` baseline comparison result is not a Measurement protocol output and is not regenerated as part of the DSD retrace. It remains historical comparative evidence in P2.

## 6. Frozen comparison policy

Execution order:

```text
1 freeze this precommit
2 reconstruct DSD ledger from P0 + P1 only
3 freeze reconstructed ledger as its own immutable artifact
4 only then read/compare against P2
5 preserve every mismatch without repair
```

Required comparison dimensions:

```text
D1 R1 candidate/terminal/version semantics
D2 R2 temporal support and terminal semantics
D3 R3 candidate statuses/redundancy/joint terminal
D4 R4 proxy/collision/reconstruction/joint terminal
D5 R5 ambiguity/underdetermined terminal
D6 bounded-claim record
D7 protocol conformance/revision pressure
D8 preserved distinction ledger
```

## 7. Frozen scoring — 56 checks

### A. Artifact lock / comparison discipline — 10

```text
A1 P0 commit/blob fixed
A2 P1 commit/blob fixed
A3 P2 commit/blob fixed only as comparison target
A4 derivation basis limited to P0+P1
A5 no live external lookup
A6 no task/candidate/bridge/rule/scope modification
A7 P2 not used before reconstruction artifact freeze
A8 scoring fixed
A9 mismatch repair prohibited
A10 same-project/non-independent scope explicit
```

### B. Five-subcase reconstruction — 24

```text
B1 R1 V1 A/B decision classes exact
B2 R1 V1 pair discriminating
B3 R1 V1 terminal sufficient
B4 R1 V2 A/B decision classes exact
B5 R1 V2 pair nondiscriminating
B6 R1 V2 terminal insufficient
B7 R1 version scope preserved

B8 R2 t0 support not-yet-available retained
B9 R2 t0 no negative-evidence conversion
B10 R2 t0 terminal blocked
B11 R2 t1 pair discriminating
B12 R2 t1 terminal sufficient

B13 R3 m1 partial
B14 R3 m2 partial
B15 R3 m3 redundancy retained
B16 R3 m4 blocked
B17 R3 m5 inapplicable
B18 R3 {m1,m2} terminal sufficient

B19 R4 direct/proxy roles retained
B20 R4 H/I aggregate collision retained
B21 R4 full support reconstruction unavailable
B22 R4 joint terminal sufficient

B23 R5 candidate underdetermined
B24 R5 terminal underdetermined
```

### C. Scope / distinction / bounded-claim reconstruction — 10

```text
C1 version distinction guard retained
C2 dynamic non-arrival guard retained
C3 redundancy/no-new-information guard retained
C4 proxy/direct guard retained
C5 aggregate/support guard retained
C6 reconstruction-bound guard retained
C7 bridge-ambiguity guard retained
C8 observed result not fabricated
C9 true alternative/diagnosis/causality not inferred
C10 maximum supported claim remains bounded
```

### D. Post-freeze exact comparison against P2 — 8

```text
D1 R1 claim-relevant outputs match P2
D2 R2 claim-relevant outputs match P2
D3 R3 claim-relevant outputs match P2
D4 R4 claim-relevant outputs match P2
D5 R5 claim-relevant outputs match P2
D6 bounded-claim/conformance outputs match P2
D7 preserved distinctions match P2
D8 post-comparison corrections = 0
```

### E. Evidence-scope discipline — 4

```text
E1 reproducibility increment limited to same-project retrace
E2 no independent-replication/validation claim
E3 no external-applicability/maturity-promotion claim
E4 no survival/merger/absorption/deletion conclusion
```

```text
TOTAL_REQUIRED_CHECKS: 56
PASS_THRESHOLD: 56/56
PARTIAL_PASS_ALLOWED: no
```

## 8. Evidence-count lock

Before execution:

```text
DIRECT_MEASUREMENT_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_MEASUREMENT_PILOTS: 5
BASELINE_MEASUREMENT_CASES: 2
NO_GAIN_MEASUREMENT_CASES: 2
STRONGEST_REASONABLE_BASELINE_MEASUREMENT:
  established_at_constructed_evidence_level

REPRODUCIBILITY_CASES: 0
EXTERNAL_MEASUREMENT_APPLICATIONS: 0
INDEPENDENT_MEASUREMENT_VALIDATION: not established
MEASUREMENT_INTERNAL_STANDARDIZATION_STATUS: developing
```

A 56/56 PASS may add exactly:

```text
REPRODUCIBILITY_CASES: 0 -> 1
SAME_PROJECT_DETERMINISTIC_RETRACE: established_once
```

It does not add direct pilots, baseline cases, NO_GAIN cases, external applications, independent replication, independent validation, or maturity promotion.

## 9. Next if passed

Proceed to frozen-axis internal standardization audit.

External validation remains deferred.
