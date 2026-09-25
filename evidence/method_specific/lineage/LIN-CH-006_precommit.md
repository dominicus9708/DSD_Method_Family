# LIN-CH-006 — Deterministic Same-Project Lineage Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE LEDGER FREEZE**  
Date: **2026-09-25**  
Challenge ID: `LIN-CH-006`  
Method: **Lineage / DSD 계보론**  
Protocol: **Lineage Protocol v0.1**  
Case class: `deterministic_same_project_retrace`  
Case origin: `same_project_retrace_of_strongest_reasonable_baseline`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Purpose

Determine whether the claim-relevant Lineage outputs of `LIN-CH-005` can be regenerated from immutable project artifacts using the frozen Lineage protocol and the strongest-reasonable-baseline precommit semantics.

This is same-project artifact-consistency evidence.

It is not blind or independent replication.

```text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
```

## 2. Frozen artifact chain

Derivation basis:

```text
P0 Lineage Protocol v0.1
   commit:
     f69f364985d604d2c883b14b2efa18535a6bbf6e
   blob:
     0ef686f3987b590e67e07b9ee5e4861c31e6e1ef

P1 LIN-CH-005 strongest-reasonable baseline precommit
   commit:
     d0c5b6c6d060c30a85856f93cbd53d4dc341515a
   blob:
     91dc9f6aeab1a1b101354b0ebbb2c4ae0eb123e1
```

Comparison target:

```text
P2 LIN-CH-005 strongest-reasonable baseline result
   commit:
     628d1f31de6060d943666f76cd05990423f35add
   blob:
     b2d0bca6e270d61dc378a2950876da935df8db48
```

Retrace ledger derivation must use only:

```text
P0 + P1
```

P2 is a comparison target, not a derivation source.

Because this is same-project work and prior context may be known, this challenge does not claim blindness.

The integrity claim is narrower:

```text
the reconstruction ledger must contain only consequences
of P0 + P1

and

no mismatch may be repaired after comparison against P2
```

## 3. Frozen retrace target

Reconstruct the Lineage side of LIN-CH-005:

```text
R1 versioned identity-rule semantics and non-retroactivity

R2 branch/merge base relation plus optional
   uniqueness/bijection/cardinality profiles

R3 dependency-aware multi-input successor claim

R4 direct-long-interval relation versus composed relation

R5 integrated conflict / underdetermination /
   neighboring-sidecar non-substitution
```

The B1 baseline is not re-executed.

This retrace does not increment baseline or NO_GAIN counters.

## 4. Frozen expected reconstruction basis

### R1 — versioned identity-rule semantics

```text
ID-RULE-v1:
  valid t0 -> t1
  stable registry member preserves identity

ID-RULE-v2:
  valid t1 -> t2
  transition requires explicit successor relation

explicit transition relation:
  cA -> cA2
```

Expected reconstruction:

```text
t0 -> t1:
  successor established through v1

t1 -> t2:
  successor established through supplied transition relation

v2 retroactive use:
  no

v1 extension across transition:
  no

rule/version provenance:
  retained
```

### R2 — branch/merge and optional stronger profiles

Base relation:

```text
a -> {b,c}
{d,e} -> f
```

Expected reconstruction:

```text
base relation:
  established

branching:
  retained

merging:
  retained

UNIQUE_SUCCESSOR_REQUIREMENT:
  unsatisfied

BIJECTION_REQUIREMENT:
  unsatisfied

CARDINALITY_CONSERVATION_REQUIREMENT:
  unsatisfied where the frozen sets differ

base relation remains established
```

### R3 — dependency-aware multi-input claim

```text
sort a:
  relation supplied and established

sort b:
  requires decoder DB-v3

DB-v3:
  unavailable
```

Expected:

```text
sort a:
  established

sort b prerequisite:
  unavailable

dependent component successor:
  LINEAGE_SUCCESSOR_BLOCKED

dependent state obligation:
  LINEAGE_TASK_BLOCKED

explicit negative:
  not inferred
```

### R4 — relation-algebra coherence

```text
L_01 = {(a0,a1)}
L_12 = {(a1,a2)}

L_12 o L_01
  =
{(a0,a2)}

direct L_02
  =
{(a0,a2),(a0,b2)}
```

Expected:

```text
composition inclusion:
  pass

LINEAGE_FAMILY_COHERENCE_STATUS:
  LINEAGE_FAMILY_COHERENT

direct L_02:
  retained separately

extra direct pair:
  (a0,b2) retained

composition == direct:
  not inferred
```

### R5 — conflict / underdetermination / sidecars

Q1:

```text
support and explicit-negation records
same frozen semantics
no precedence
```

Expected:

```text
LINEAGE_SUCCESSOR_CONFLICTING
```

Q2:

```text
two admissible relation schemas
different outcomes
no resolver
```

Expected:

```text
LINEAGE_SUCCESSOR_UNDERDETERMINED
```

Q3:

```text
explicit successor relation
plus Tracking / Transformation / Comparison /
Classification / Aggregation / Reconstruction / Audit sidecars
```

Expected:

```text
successor:
  established from supplied successor relation

sidecars:
  not promoted into independent identity criteria
```

Frozen run-level precedence:

```text
OUT_OF_SCOPE
> CONFLICTING
> UNDERDETERMINED
> BLOCKED
> ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

Expected run terminal:

```text
LINEAGE_TASK_CONFLICTING
```

Lower-level Q2 and Q3 states must remain visible.

## 5. Protocol-level reconstruction

The retrace must also regenerate:

```text
LINEAGE_PROTOCOL_CONFORMANCE:
  LINEAGE_PROTOCOL_CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
```

## 6. Reconstruction-ledger rule

After this precommit is frozen:

1. construct a dedicated retrace reconstruction ledger from P0 + P1;
2. commit that ledger before any formal comparison against P2;
3. then compare the committed ledger against P2;
4. record every claim-relevant mismatch;
5. do not repair the ledger after comparison.

Allowed mismatch labels:

```text
EXACT_MATCH
SEMANTIC_EQUIVALENT_MATCH
CLAIM_RELEVANT_MISMATCH
NONCLAIM_RELEVANT_WORDING_DIFFERENCE
```

No mismatch may be hidden by relabeling.

## 7. Frozen scoring — 56 checks

### A. Artifact and anti-post-hoc integrity — 10

```text
A1 P0 protocol commit/blob frozen
A2 P1 precommit commit/blob frozen
A3 P2 result commit/blob frozen as comparison target
A4 derivation basis limited to P0+P1
A5 P2 not used as derivation source
A6 retrace ledger committed before formal P2 comparison
A7 no live repair after comparison
A8 same-project/non-blind limitation stated
A9 external application remains no
A10 no baseline/NO_GAIN counter increment
```

### B. R1 version semantics — 10

```text
B1 t0->t1 identity established under v1
B2 t1->t2 requires explicit relation
B3 supplied transition relation establishes successor
B4 v2 not applied retroactively
B5 v1 not extended through transition
B6 rule/version provenance retained
B7 stable-background and transition semantics remain distinct
B8 no label continuity substitute
B9 no literal equality claim created
B10 R1 comparison target claim reproduced
```

### C. R2 branch/merge plus optional constraints — 10

```text
C1 branch retained
C2 merge retained
C3 base relation remains established
C4 unique-successor profile unsatisfied
C5 bijection profile unsatisfied
C6 cardinality profile unsatisfied where applicable
C7 optional-profile failure does not erase base relation
C8 branch/merge not treated as protocol failure
C9 no hidden uniqueness rule added
C10 R2 comparison target claim reproduced
```

### D. R3 prerequisite dependency closure — 8

```text
D1 sort-a relation established
D2 sort-b dependency on DB-v3 retained
D3 DB-v3 unavailable retained
D4 dependent relation BLOCKED
D5 dependent state obligation BLOCKED
D6 no explicit negative inferred
D7 prerequisite provenance retained
D8 R3 comparison target claim reproduced
```

### E. R4 relation-algebra coherence — 8

```text
E1 composition computed correctly
E2 composition inclusion passes
E3 family coherent
E4 direct L_02 retained separately
E5 extra direct pair retained
E6 composition=direct not inferred
E7 direct-vs-derived provenance retained
E8 R4 comparison target claim reproduced
```

### F. R5 integrated terminal and sidecar boundary — 8

```text
F1 Q1 conflict reconstructed
F2 Q2 underdetermination reconstructed
F3 Q3 successor established from successor relation
F4 Tracking sidecar not promoted
F5 other neighboring sidecars not promoted
F6 frozen terminal precedence reproduced
F7 lower-level Q2/Q3 states retained
F8 R5 comparison target claim reproduced
```

### G. Final retrace verdict — 2

```text
G1 claim-relevant mismatch count recorded exactly
G2 deterministic same-project retrace classification
   follows the frozen comparison result
```

```text
TOTAL_REQUIRED_CHECKS: 56
PASS_THRESHOLD: 56/56
PARTIAL_PASS_ALLOWED: no
```

## 8. Allowed counter changes on 56/56 PASS

```text
REPRODUCIBILITY_CASES:
  0 -> 1

SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once

CLAIM_RELEVANT_MISMATCHES:
  must equal 0 for PASS

POST_COMPARISON_CORRECTIONS:
  must equal 0 for PASS
```

Do not alter:

```text
DIRECT_LINEAGE_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_LINEAGE_PILOTS: 5
BASELINE_LINEAGE_CASES: 2
NO_GAIN_LINEAGE_CASES: 2
```

## 9. Interpretation lock

```text
SAME_PROJECT_DETERMINISTIC_RETRACE
  !=
INDEPENDENT_REPLICATION

DETERMINISTIC_MATCH
  !=
INDEPENDENT_VALIDATION

RETRACE_PASS
  !=
EXTERNAL_APPLICABILITY

RETRACE_PASS
  !=
METHOD_SUPERIORITY
```
