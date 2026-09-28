# CPR-CH-006 — Deterministic Same-Project Compression Retrace Precommit

Status: **PRECOMMITTED BEFORE RETRACE LEDGER FREEZE**  
Date: **2026-09-29**  
Challenge ID: `CPR-CH-006`  
Method: **Compression / DSD 압축론**  
Protocol: **Compression Protocol v0.1**  
Case class: `deterministic_same_project_retrace`  
Case origin: `same_project_retrace_of_strongest_reasonable_baseline`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Purpose

Determine whether the claim-relevant Compression-side outputs of `CPR-CH-005` can be regenerated from immutable project artifacts using the frozen Compression protocol and the strongest-reasonable-baseline precommit semantics.

This is same-project artifact-consistency evidence.

It is not blind or independent replication.

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
~~~

## 2. Frozen artifact chain

Derivation basis:

~~~text
P0 Compression Protocol v0.1
   commit:
     b1efa06e4c715e08ce2558a608c7f09aa22172bd
   blob:
     4d67d800e107229f91c16cf5b0235928124482b2

P1 CPR-CH-005 strongest-reasonable baseline precommit
   commit:
     f55ec8c5818e75184ef941d72467fec9951abc0d
   blob:
     2c9d7f02ab43a0f37b9765c669b2c26f9d919e1a
~~~

Comparison target:

~~~text
P2 CPR-CH-005 strongest-reasonable baseline result
   commit:
     e438dfa356faf18c733a6b60119de86ca94c7cae
   blob:
     d9f905def2a94a3585fe14c1ac9885114ba4c68d
~~~

Retrace ledger derivation must use only:

~~~text
P0 + P1
~~~

P2 is a comparison target, not a derivation source.

Because this is same-project work and prior context may be known, this challenge does not claim blindness.

The integrity claim is narrower:

~~~text
the reconstruction ledger must contain only consequences
of P0 + P1

and

no mismatch may be repaired after comparison against P2
~~~

## 3. Frozen retrace target

Reconstruct the Compression side of CPR-CH-005:

~~~text
R1 versioned purpose/map semantics,
   non-retroactivity, purpose-safe collisions,
   and strict reduction

R2 exact linear kernel/fiber analysis,
   declared-class losslessness,
   and no global injectivity promotion

R3 required-sidecar dependency closure
   and total package accounting

R4 multi-stage local success versus
   end-to-end original-purpose failure

R5 integrated purpose conflict /
   alternative-metric underdetermination /
   neighboring-sidecar non-substitution /
   deterministic ledger and rerun identifiers
~~~

The B1 baseline is not re-executed.

This retrace does not increment baseline or NO_GAIN counters.

## 4. Frozen expected reconstruction basis

### R1 — versioned purpose/map registry

~~~text
TASK-v1

PURPOSE-v1:
  preserve group + status
  detail may merge

PURPOSE-v2:
  preserve group + status + detail
  valid TASK-v2 only

MAP-v1:
  C(group,detail,status)=(group,status)
  valid TASK-v1

MAP-v2:
  identity map
  valid TASK-v2 only

source:
  x1=(A,a1,NONZERO)
  x2=(A,a2,NONZERO)
  x3=(B,b1,ZERO)
  x4=(B,b2,ZERO)

metric:
  FIELD_UNIT_COUNT-v1

source cost:
  12

reduced cost:
  8
~~~

Expected reconstruction:

~~~text
TASK-v1 selects PURPOSE-v1 + MAP-v1

collision fibers:
  {x1,x2}
  {x3,x4}

both collisions:
  purpose-safe

strict reduction:
  established

PURPOSE-v2 retroactive substitution:
  no

MAP-v2 retroactive substitution:
  no

rule/version provenance:
  retained

task terminal:
  COMPRESSION_TASK_ESTABLISHED
~~~

### R2 — exact kernel and declared-class losslessness

~~~text
C(x,y,z):
  (x+z,y+z)

A:
  {(x,y,0): x,y in R}
~~~

Expected reconstruction:

~~~text
ker(C):
  span{(-1,-1,1)}

global injectivity:
  not established

C restricted to A:
  injective

LOSSLESS_ON_DECLARED_CLASS:
  established

outside-A collision witness:
  (0,0,0)
  (-1,-1,1)
  both map to (0,0)

strict per-record reduction:
  3 -> 2

declared-class -> global promotion:
  no
~~~

### R3 — required-sidecar package accounting

~~~text
source:
  4 records x 3 fields

SOURCE_COST:
  12 PACKAGE_FIELD_UNIT-v1

main reduced output:
  4 records x 1 field

MAIN_OUTPUT_COST:
  4

required sidecar:
  4 records x 2 fields

REQUIRED_SIDECAR_COST:
  8

accounting scope:
  output_plus_required_sidecars
~~~

Expected reconstruction:

~~~text
required-sidecar dependency:
  satisfied

REDUCED_PACKAGE_COST:
  12

main output shrinkage:
  yes

strict total package reduction:
  not established

task terminal:
  COMPRESSION_TASK_NOT_ESTABLISHED

required sidecar omitted to manufacture success:
  no
~~~

### R4 — end-to-end chain validation

~~~text
source:
  x1=(A,a,0)
  x2=(A,b,1)
  x3=(B,c,0)
  x4=(B,d,1)

original P0:
  preserve group + status
  detail may merge

C1(group,detail,status):
  (group,status)

C2(group,status):
  group

stage-2 local purpose:
  preserve group only
~~~

Expected reconstruction:

~~~text
stage 1 local:
  established

stage 2 local:
  established

full chain:
  C2 o C1

x1/x2:
  destructive collision relative to original P0

x3/x4:
  destructive collision relative to original P0

end-to-end original-purpose:
  not established

COMPOSITION_END_TO_END:
  not established

local-stage successes:
  retained
~~~

### R5 — conflict / alternative metric / sidecars / rerun

Q1:

~~~text
same PURPOSE-RULE-v7

record A:
  (p,q) required-distinct

record B:
  (p,q) safe-to-merge

resolver:
  none
~~~

Expected:

~~~text
CONFLICT
~~~

Q2:

~~~text
METRIC-A:
  source=10
  reduced=8
  strict reduction passes

METRIC-B:
  source=10
  reduced=10
  strict reduction fails

both admissible
resolver:
  none
~~~

Expected:

~~~text
UNDERDETERMINED
~~~

Q3:

~~~text
forward compression otherwise established

sidecars:
  Aggregation
  Transformation
  Measurement
  Comparison
  Classification
  Tracking
  Lineage
  Reconstruction
  Audit
~~~

Expected:

~~~text
forward compression:
  established from compression contract

neighboring sidecars:
  not promoted into compression criteria
~~~

Frozen run precedence:

~~~text
OUT_OF_SCOPE
>
CONFLICTING
>
UNDERDETERMINED
>
BLOCKED
>
ESTABLISHED / PARTIAL / NOT_ESTABLISHED
~~~

Expected run terminal:

~~~text
COMPRESSION_TASK_CONFLICTING
~~~

Lower-level Q2/Q3 states remain visible.

Deterministic ledger/rerun identifiers remain present.

## 5. Protocol-level reconstruction

The retrace must also regenerate:

~~~text
COMPRESSION_PROTOCOL_CONFORMANCE:
  COMPRESSION_PROTOCOL_CONFORMANT

PROTOCOL_DEFECT_EXPOSED:
  no

PROTOCOL_REVISION_REQUIRED:
  no

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 6. Reconstruction-ledger rule

After this precommit is frozen:

1. construct a dedicated retrace reconstruction ledger from P0 + P1;
2. commit that ledger before any formal comparison against P2;
3. then compare the committed ledger against P2;
4. record every claim-relevant mismatch;
5. do not repair the ledger after comparison.

Allowed comparison labels:

~~~text
EXACT_MATCH
SEMANTIC_EQUIVALENT_MATCH
CLAIM_RELEVANT_MISMATCH
NONCLAIM_RELEVANT_WORDING_DIFFERENCE
~~~

No mismatch may be hidden by relabeling.

## 7. Frozen scoring — 56 checks

### A. Artifact and anti-post-hoc integrity — 10

~~~text
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
~~~

### B. R1 versioned purpose/map semantics — 10

~~~text
B1 TASK-v1 retained
B2 PURPOSE-v1 selected
B3 MAP-v1 selected
B4 two collision fibers reconstructed
B5 both fibers reconstructed as purpose-safe
B6 strict reduction 12 -> 8 reconstructed
B7 v2 purpose/map retroactive substitution prohibited
B8 rule/version provenance retained
B9 task terminal reconstructed as ESTABLISHED
B10 R1 comparison-target claim reproduced
~~~

### C. R2 kernel / declared-class losslessness — 10

~~~text
C1 kernel equations reconstructed
C2 ker(C)=span{(-1,-1,1)}
C3 nontrivial kernel retained
C4 global injectivity not established
C5 declared class A retained
C6 C restricted to A injective
C7 outside-A collision witness retained
C8 strict per-record reduction 3 -> 2 retained
C9 class-local -> global promotion prohibited
C10 R2 comparison-target claim reproduced
~~~

### D. R3 package accounting — 8

~~~text
D1 source cost reconstructed as 12
D2 main-output cost reconstructed as 4
D3 required-sidecar cost reconstructed as 8
D4 reduced package cost reconstructed as 12
D5 main shrinkage retained
D6 strict total reduction not established
D7 sidecar not omitted / task terminal NOT_ESTABLISHED
D8 R3 comparison-target claim reproduced
~~~

### E. R4 end-to-end chain — 8

~~~text
E1 stage 1 local established
E2 stage 2 local established
E3 original P0 retained through chain
E4 x1/x2 destructive end-to-end collision reconstructed
E5 x3/x4 destructive end-to-end collision reconstructed
E6 end-to-end original-purpose NOT_ESTABLISHED
E7 local-stage successes retained
E8 R4 comparison-target claim reproduced
~~~

### F. R5 integrated terminal / sidecar / rerun boundary — 8

~~~text
F1 Q1 purpose conflict reconstructed
F2 Q2 metric underdetermination reconstructed
F3 Q3 forward compression remains established
F4 neighboring sidecars not promoted
F5 frozen terminal precedence reproduced
F6 lower-level Q2/Q3 states retained
F7 deterministic ledger/rerun identifiers retained
F8 R5 comparison-target claim reproduced
~~~

### G. Final retrace verdict — 2

~~~text
G1 claim-relevant mismatch count recorded exactly
G2 deterministic same-project retrace classification
   follows the frozen comparison result
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  56

PASS_THRESHOLD:
  56/56

PARTIAL_PASS_ALLOWED:
  no
~~~

## 8. Allowed counter changes on 56/56 PASS

~~~text
REPRODUCIBILITY_CASES:
  0 -> 1

SAME_PROJECT_DETERMINISTIC_RETRACE:
  established_once

CLAIM_RELEVANT_MISMATCHES:
  must equal 0 for PASS

POST_COMPARISON_CORRECTIONS:
  must equal 0 for PASS
~~~

Do not alter:

~~~text
DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  5

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  5

BASELINE_COMPRESSION_CASES:
  2

NO_GAIN_COMPRESSION_CASES:
  2
~~~

## 9. Interpretation lock

~~~text
SAME_PROJECT_DETERMINISTIC_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
RETRACE_PASS != METHOD_SUPERIORITY
~~~

## 10. Next

If 56/56 PASS with zero claim-relevant mismatches and zero post-comparison corrections, proceed to CPR-AUD-001 frozen-axis internal-standardization audit.
