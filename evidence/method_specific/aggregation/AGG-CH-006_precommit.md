# AGG-CH-006 — Deterministic Same-Project Aggregation Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE LEDGER FREEZE**  
Date: **2026-09-27**  
Challenge ID: `AGG-CH-006`  
Method: **Aggregation / DSD 집계론**  
Protocol: **Aggregation Protocol v0.1**  
Case class: `deterministic_same_project_retrace`  
Case origin: `same_project_retrace_of_strongest_reasonable_baseline`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Purpose

Determine whether the claim-relevant Aggregation-side outputs of `AGG-CH-005` can be regenerated from immutable project artifacts using the frozen Aggregation protocol and the strongest-reasonable-baseline precommit semantics.

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
P0 Aggregation Protocol v0.1
   commit:
     85b4263ad47cd10acd2230add542f381bd5d6a05
   blob:
     5ac926aa40594126b42dac99762ff33fe87450f1

P1 AGG-CH-005 strongest-reasonable baseline precommit
   commit:
     da2bb2cb33d51f902e0a9a956846a13c0403a46a
   blob:
     d384d7f1c7a4fae71ad46ae12e7cbf504a8dc0d4
```

Comparison target:

```text
P2 AGG-CH-005 strongest-reasonable baseline result
   commit:
     6ffcd054ab94cdf143c0cd9fb644e5d214a479d2
   blob:
     d17c650e2f3f4635664f1bb6c6796edd67b54516
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

Reconstruct the Aggregation side of AGG-CH-005:

```text
R1 versioned aggregation-rule semantics,
   non-retroactivity, and postprocessing separation

R2 exact operator kernel, collision witness,
   and declared-class injectivity

R3 admitted countable extension with
   absolute-summability evidence and exact sum

R4 multi-coordinate inverse dependency closure

R5 integrated conflict / underdetermination /
   neighboring-sidecar non-substitution /
   deterministic ledger and rerun identifiers
```

The B1 baseline is not re-executed.

This retrace does not increment baseline or NO_GAIN counters.

## 4. Frozen expected reconstruction basis

### R1 — versioned aggregation rule and postprocessing

```text
TASK_VERSION:
  1

AGG-RULE-v1:
  finite direct sum
  valid task version 1

AGG-RULE-v2:
  weighted finite operator
  valid task version 2 only

POST-v1:
  downstream equal-weight average

T(c1)=(2,1)
T(c2)=(-1,3)
T(c0)=(0,0)
```

Expected reconstruction:

```text
primary rule:
  AGG-RULE-v1

primary aggregate:
  (1,4)

AGG-RULE-v2 retroactive substitution:
  no

POST-v1:
  (1/3,4/3)

postprocessing replaces primary aggregate:
  no

rule/version provenance:
  retained
```

### R2 — kernel and declared-class injectivity

```text
S(x,y,z):
  (x+z,y+z)

A:
  {(x,y,0): x,y in R}
```

Expected reconstruction:

```text
ker(S):
  span{(-1,-1,1)}

global injectivity:
  not established

S restricted to A:
  injective

outside-A collision witness:
  (0,0,0)
  (-1,-1,1)
  both map to (0,0)

declared-class injectivity:
  established

declared-class -> global promotion:
  no
```

### R3 — admitted countable extension

```text
T_n:
  (2^-n,2^-(n+1))
  n >= 1

absolute-norm majorant:
  ||T_n||_1 = 3 * 2^-(n+1)
```

Expected reconstruction:

```text
sum ||T_n||_1:
  3/2

countable domain:
  admitted

countable aggregate:
  (1,1/2)

finite-core relabel:
  no

countable support/convergence provenance:
  retained
```

### R4 — inverse dependency closure

```text
Y1 channel aggregate:
  available / established

Y2 property aggregate:
  available / established

D1 channel support sidecar:
  available

D2 property support sidecar:
  available

D3 cross-coordinate coupling:
  requires XC-v3

XC-v3:
  unavailable
```

Expected reconstruction:

```text
Y1:
  remains established

Y2:
  remains established

combined-coordinate inverse claim:
  BLOCKED

evaluable negative reconstruction inferred:
  no

coordinatewise evidence promoted to combined reconstruction:
  no
```

### R5 — conflict / underdetermination / sidecars / rerun

Q1:

```text
same MAP-v7 identity
two equally applicable definitions:
  direct sum
  normalized mean
no precedence
```

Expected:

```text
CONFLICT
```

Q2:

```text
two admissible injectivity classes
different outcomes
no resolver
```

Expected:

```text
UNDERDETERMINED
```

Q3:

```text
forward aggregate established

sidecars:
  Tracking provenance
  Lineage identity
  Comparison similarity
  Classification class
  Reconstruction candidate
  Audit conformance
```

Expected:

```text
forward aggregate:
  established from aggregation rule

neighboring sidecars:
  not promoted into aggregation/source-identity criteria
```

Frozen run precedence:

```text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
```

Expected run terminal:

```text
AGGREGATION_TASK_CONFLICTING
```

Lower-level Q2/Q3 states remain visible.

Deterministic ledger/rerun identifiers remain present.

## 5. Protocol-level reconstruction

The retrace must also regenerate:

```text
AGGREGATION_PROTOCOL_CONFORMANCE:
  AGGREGATION_PROTOCOL_CONFORMANT

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

Allowed comparison labels:

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

### B. R1 versioned-rule / postprocessing semantics — 10

```text
B1 task version retained
B2 AGG-RULE-v1 selected
B3 primary aggregate reconstructed as (1,4)
B4 AGG-RULE-v2 not retroactively substituted
B5 POST-v1 reconstructed as (1/3,4/3)
B6 primary/postprocessing separation retained
B7 rule/version provenance retained
B8 direct finite sum semantics retained
B9 no hidden weighted-rule substitution
B10 R1 comparison-target claim reproduced
```

### C. R2 kernel / declared-class injectivity — 10

```text
C1 kernel equations reconstructed
C2 ker(S)=span{(-1,-1,1)}
C3 nontrivial kernel retained
C4 global injectivity not established
C5 declared class A retained
C6 S restricted to A is injective
C7 outside-A collision witness retained
C8 class-local -> global promotion prohibited
C9 collision/injectivity scope provenance retained
C10 R2 comparison-target claim reproduced
```

### D. R3 countable extension — 8

```text
D1 absolute-norm majorant reconstructed
D2 majorant sum reconstructed as 3/2
D3 countable domain admitted
D4 first coordinate sum reconstructed as 1
D5 second coordinate sum reconstructed as 1/2
D6 aggregate reconstructed as (1,1/2)
D7 finite-core relabel prohibited
D8 R3 comparison-target claim reproduced
```

### E. R4 inverse dependency closure — 8

```text
E1 Y1 remains established
E2 Y2 remains established
E3 D1 availability retained
E4 D2 availability retained
E5 XC-v3 unavailability retained
E6 combined inverse claim BLOCKED
E7 no evaluable negative / coordinatewise promotion
E8 R4 comparison-target claim reproduced
```

### F. R5 integrated terminal / sidecar / rerun boundary — 8

```text
F1 Q1 conflict reconstructed
F2 Q2 underdetermination reconstructed
F3 Q3 forward aggregate remains established
F4 neighboring sidecars not promoted
F5 frozen terminal precedence reproduced
F6 lower-level Q2/Q3 states retained
F7 deterministic ledger/rerun identifiers retained
F8 R5 comparison-target claim reproduced
```

### G. Final retrace verdict — 2

```text
G1 claim-relevant mismatch count recorded exactly
G2 deterministic same-project retrace classification
   follows the frozen comparison result
```

```text
TOTAL_REQUIRED_CHECKS:
  56

PASS_THRESHOLD:
  56/56

PARTIAL_PASS_ALLOWED:
  no
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
DIRECT_AGGREGATION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_AGGREGATION_PILOTS:
  5

BASELINE_AGGREGATION_CASES:
  2

NO_GAIN_AGGREGATION_CASES:
  2
```

## 9. Interpretation lock

```text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
RETRACE_PASS != METHOD_SUPERIORITY
```
