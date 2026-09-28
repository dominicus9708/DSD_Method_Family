# CPR-CH-005 — Strongest-Reasonable Non-DSD Compression Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-29**  
Challenge ID: `CPR-CH-005`  
Method: **Compression / DSD 압축론**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparator identities

~~~text
COMPRESSION_PROTOCOL_VERSION:
  v0.1

COMPRESSION_PROTOCOL_COMMIT:
  b1efa06e4c715e08ce2558a608c7f09aa22172bd

COMPRESSION_PROTOCOL_BLOB:
  4d67d800e107229f91c16cf5b0235928124482b2

PREVIOUS_COMPETENT_BASELINE:
  CPR-CH-004
  B0_GENERIC_TYPED_COMPRESSION_EVALUATOR
  64/64 PASS / NO_GAIN
~~~

No Compression Protocol revision is allowed in response to this baseline result.

## 2. Strong baseline identity

~~~text
BASELINE_ID:
  B1_STRONG_COMPRESSION_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_compression_engine

BASELINE_USES_DSD_AXIOMS:
  no

BASELINE_USES_DSD_METHOD_LABELS_INTERNALLY:
  no

BASELINE_RECEIVES_EQUAL_INFORMATION:
  yes
~~~

B1 is materially stronger than B0.

B1 may use ordinary:

~~~text
versioned purpose/map/metric registries
typed source and sidecar schemas
automatic purpose-relation consistency validation
finite fiber and collision enumeration
symbolic kernel/rank analysis for supplied linear maps
declared-class injectivity checks
dependency-aware required-sidecar closure
automatic package-cost accounting
alternative metric/schema management
resolution and threshold branch management
multi-purpose composition engines
multi-stage compression-chain composition
end-to-end obligation propagation
reconstruction-prerequisite closure
deterministic terminal-precedence engines
bounded-claim generation
neighbor-sidecar non-substitution rules
deterministic evaluation ledgers
full rerun manifests
~~~

B1 may derive consequences algorithmically from the same supplied records.

B1 may not receive hidden factual input unavailable to Compression.

B1 may not be weakened after precommit.

## 3. Strong baseline operation

B1 performs:

~~~text
B1-1 freeze task/version, source schema, purpose-registry version,
     map-registry version, accounting metric, resolution, sidecar scope,
     reconstruction scope, chain scope, and maximum claim

B1-2 bind every purpose/map/metric rule to explicit version and
     applicability; prohibit retroactive rule substitution

B1-3 automatically validate must-distinguish versus safe-to-merge relations,
     including multi-purpose conjunction/priority/alternative semantics

B1-4 retain supplied typed status, support, provenance, and unavailable/
     undefined distinctions before any reduction

B1-5 execute only the frozen deterministic map or deterministic composed chain

B1-6 enumerate finite collision fibers and independently score purpose,
     status, support, provenance, and reconstruction consequences

B1-7 when the supplied map is linear, compute exact kernel/rank information
     where decidable and test injectivity only on the frozen declared class

B1-8 compute required-sidecar dependency closure before package accounting;
     unavailable required sidecars block dependent claims

B1-9 compute source and reduced-package costs under the same frozen metric,
     including every required sidecar inside the frozen accounting scope

B1-10 preserve multiple admissible metrics/resolutions/schemas and emit
      unresolved/underdetermined state when outcomes differ without resolver

B1-11 keep forward compression and inverse/reconstruction claims separate;
      compute prerequisite closure for requested inverse claims

B1-12 for multi-stage chains, propagate original source-level purpose
      obligations through the full chain and separately retain local-stage results

B1-13 preserve conflict, outside-scope, unresolved, blocked, evaluable failure,
      established, and multi-obligation partial outcomes separately

B1-14 apply frozen terminal precedence without erasing lower-level states

B1-15 keep Aggregation / Transformation / Measurement / Comparison /
      Classification / Tracking / Lineage / Reconstruction / Audit records
      non-authoritative unless a supplied compression rule explicitly promotes them

B1-16 emit only a bounded maximum claim; prohibit unsupported source identity,
      universal purpose safety, global injectivity, reconstruction success,
      lineage identity, audit success, or external-validity promotion

B1-17 emit a deterministic evaluation ledger with rule/version/purpose/map/
      metric/sidecar/collision/reconstruction/chain identifiers

B1-18 emit a full rerun manifest sufficient to replay the frozen constructed task
~~~

## 4. Equal-information and fairness rule

Compression and B1 receive exactly the same claim-relevant records.

~~~text
EQUAL_INFORMATION_REQUIRED:
  yes

HIDDEN_FAVORABLE_INPUT_ALLOWED:
  no

BASELINE_WEAKENING_ALLOWED:
  no

POST_HOC_RULE_CHANGE_ALLOWED:
  no
~~~

B1 is not required to derive DSD ontology.

It receives the same already-frozen source, purpose, map, metric, status, sidecar, resolution, reconstruction, and chain semantics exposed to the Compression task.

Extra computational competence is allowed.

Extra hidden factual information is not.

## 5. Strong subcase R1 — versioned purpose/map registry and non-retroactivity

Frozen task versions:

~~~text
TASK-v1
TASK-v2
~~~

Purpose registry:

~~~text
PURPOSE-v1:
  valid for TASK-v1
  preserve group + status
  detail may merge

PURPOSE-v2:
  valid for TASK-v2
  preserve group + status + detail
~~~

Map registry:

~~~text
MAP-v1:
  valid for TASK-v1
  C(group,detail,status)=(group,status)

MAP-v2:
  valid for TASK-v2
  identity map
~~~

Frozen TASK-v1 source:

~~~text
x1=(A,a1,NONZERO)
x2=(A,a2,NONZERO)
x3=(B,b1,ZERO)
x4=(B,b2,ZERO)
~~~

Accounting:

~~~text
FIELD_UNIT_COUNT-v1
source cost=12
MAP-v1 reduced cost=8
strict reduction required
~~~

Expected both systems:

~~~text
TASK-v1 uses PURPOSE-v1 + MAP-v1
TASK-v1 terminal established
MAP-v1 collisions (x1,x2) and (x3,x4) are purpose-safe
strict reduction 12 -> 8 established

PURPOSE-v2 retroactive substitution into TASK-v1:
  prohibited

MAP-v2 retroactive substitution into TASK-v1:
  prohibited

rule/version provenance:
  retained
~~~

## 6. Strong subcase R2 — exact linear fiber/kernel and declared-class losslessness

Frozen linear map:

~~~text
C:
  R^3 -> R^2

C(x,y,z):
  (x+z, y+z)

matrix:
  [1 0 1]
  [0 1 1]
~~~

Exact kernel:

~~~text
ker(C):
  span{(-1,-1,1)}
~~~

Declared source class:

~~~text
A:
  {(x,y,0) : x,y in R}
~~~

On A:

~~~text
C(x,y,0):
  (x,y)
~~~

Purpose:

~~~text
preserve x and y on A
z is fixed to zero on A
~~~

Accounting:

~~~text
source fields per record:
  3

reduced fields per record:
  2

strict size reduction:
  required
~~~

Expected both:

~~~text
kernel:
  span{(-1,-1,1)}

GLOBAL_INJECTIVITY:
  not established

LOSSLESS_ON_DECLARED_CLASS:
  established on A

outside-A collision witness:
  (0,0,0)
  (-1,-1,1)
  both map to (0,0)

strict per-record reduction:
  3 -> 2

global promotion:
  prohibited
~~~

## 7. Strong subcase R3 — required-sidecar dependency closure and total package accounting

Frozen source:

~~~text
4 records
3 fields each

SOURCE_COST:
  12 PACKAGE_FIELD_UNIT-v1
~~~

Main compression output:

~~~text
4 records
1 field each

MAIN_OUTPUT_COST:
  4
~~~

Frozen purpose requires preservation of two additional source fields through a sidecar.

Required sidecar:

~~~text
4 records
2 fields each

REQUIRED_SIDECAR_COST:
  8
~~~

Accounting scope:

~~~text
output_plus_required_sidecars
~~~

Therefore:

~~~text
REDUCED_PACKAGE_COST:
  4 + 8 = 12

REDUCTION_REQUIREMENT:
  strict
~~~

Expected both:

~~~text
required-sidecar dependency:
  satisfied

main output shrinkage:
  yes

total package reduction:
  no

REDUCTION_STATUS:
  not established

TASK_TERMINAL:
  not established

no sidecar omission:
  allowed
~~~

Required guard:

~~~text
MAIN_OUTPUT_SHRINKAGE != TOTAL_REPRESENTATION_REDUCTION
~~~

## 8. Strong subcase R4 — local-stage success versus end-to-end chain failure

Frozen source:

~~~text
x1=(A,a,0)
x2=(A,b,1)
x3=(B,c,0)
x4=(B,d,1)
~~~

Original source-level purpose P0:

~~~text
preserve group
preserve status
detail may merge
~~~

Stage 1:

~~~text
C1(group,detail,status)
  =
(group,status)

local purpose:
  P0

cost:
  12 -> 8

expected:
  local compression established
~~~

Stage 2:

~~~text
C2(group,status)
  =
group

local stage-2 purpose P2:
  preserve group only

cost:
  8 -> 4

expected:
  local stage-2 compression established
~~~

Full chain:

~~~text
C2 o C1:
  (group,detail,status)
  ->
  group
~~~

Original P0 requires status distinction.

Thus:

~~~text
x1 and x2:
  required-distinct under P0
  but collide after full chain

x3 and x4:
  required-distinct under P0
  but collide after full chain
~~~

Expected both systems:

~~~text
stage 1 local result:
  established

stage 2 local result:
  established

end-to-end original-purpose result:
  not established

COMPOSITION_END_TO_END:
  not established

original P0 obligations:
  retained

local successes:
  retained

chain failure:
  does not erase local-stage results
~~~

Required guard:

~~~text
LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS
~~~

## 9. Strong subcase R5 — integrated alternative metric / conflict / sidecar / rerun pressure

Frozen obligations:

~~~text
Q1:
  same PURPOSE-RULE-v7 contains two equally applicable records

  record A:
    pair (p,q) must remain distinct

  record B:
    pair (p,q) explicitly safe-to-merge

  resolver:
    none

Q2:
  two admissible accounting metrics

  METRIC-A:
    source cost=10
    reduced package cost=8
    strict reduction passes

  METRIC-B:
    source cost=10
    reduced package cost=10
    strict reduction fails

  metric resolver:
    none

Q3:
  forward compression otherwise established

  neighboring sidecars present:
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

Frozen terminal precedence:

~~~text
OUTSIDE_SCOPE
>
CONFLICT
>
UNRESOLVED
>
BLOCKED
>
COMPLETE/PARTIAL/NOT_ESTABLISHED
~~~

Expected both:

~~~text
Q1:
  conflict

Q2:
  unresolved / underdetermined

Q3:
  forward compression remains established only from the supplied
  compression contract;
  neighboring sidecars do not substitute as compression criteria

run terminal:
  conflict

lower-level Q2 and Q3:
  retained

deterministic evaluation ledger:
  emitted

rerun manifest:
  emitted
~~~

## 10. Frozen gain axes

~~~text
G1 VERSIONED_PURPOSE_MAP_AND_NONRETROACTIVITY_GAIN

G2 EXACT_FIBER_KERNEL_AND_DECLARED_CLASS_GAIN

G3 PACKAGE_ACCOUNTING_AND_SIDECAR_DEPENDENCY_GAIN

G4 END_TO_END_CHAIN_AND_PURPOSE_PROPAGATION_GAIN

G5 CONFLICT_UNDERDETERMINATION_AND_SIDECAR_BOUNDARY_GAIN

G6 BOUNDED_MAXIMUM_CLAIM_GAIN

G7 DETERMINISTIC_LEDGER_AND_RERUN_MANIFEST_GAIN
~~~

Allowed per-axis result:

~~~text
DSD_ADVANTAGE_ESTABLISHED
BASELINE_MATCH
BASELINE_ADVANTAGE
UNRESOLVED
~~~

Overall rule:

~~~text
if Compression is protocol-nonconformant or wrong:
  FAIL

if one or more frozen axes establish a real DSD advantage
against the still-fair B1:
  COMPRESSION_METHOD_GAIN_ESTABLISHED

if all seven axes are BASELINE_MATCH:
  COMPRESSION_METHOD_GAIN_NO_GAIN

if a baseline advantage appears:
  preserve BASELINE_ADVANTAGE
  and do not relabel it as DSD gain

otherwise:
  COMPRESSION_METHOD_GAIN_UNDERDETERMINED
~~~

## 11. Frozen scoring — 82 checks

### A. Immutable fairness — 10

~~~text
A1 Compression protocol identity frozen
A2 B1 identity and capabilities frozen
A3 R1-R5 frozen before execution
A4 equal-information rule frozen
A5 Compression hidden favorable inputs = 0
A6 B1 claim-relevant withheld inputs = 0
A7 B1 not weakened after precommit
A8 output/gain mapping frozen
A9 scoring frozen
A10 external application/evaluator not counted
~~~

### B. R1 versioned purpose/map registry — 12

~~~text
B1 Compression selects PURPOSE-v1 for TASK-v1
B2 B1 selects same PURPOSE-v1
B3 Compression selects MAP-v1 for TASK-v1
B4 B1 selects same MAP-v1
B5 Compression records two purpose-safe collision fibers
B6 B1 records same two fibers as purpose-safe
B7 Compression strict reduction 12 -> 8 established
B8 B1 strict reduction 12 -> 8 established
B9 Compression prohibits v2 retroactive substitution
B10 B1 prohibits v2 retroactive substitution
B11 Compression rule/version provenance retained
B12 B1 rule/version provenance retained
~~~

### C. R2 exact kernel / declared class — 14

~~~text
C1 Compression exact kernel relation recognized
C2 B1 exact kernel relation recognized
C3 Compression ker(C)=span{(-1,-1,1)}
C4 B1 same kernel
C5 Compression global injectivity not established
C6 B1 global injectivity not established
C7 Compression declared class A frozen
C8 B1 declared class A frozen
C9 Compression C|_A injective
C10 B1 C|_A injective
C11 Compression outside-A collision witness retained
C12 B1 same collision witness retained
C13 both establish strict per-record reduction 3 -> 2
C14 neither promotes class-local losslessness globally
~~~

### D. R3 package accounting / sidecar dependency — 12

~~~text
D1 Compression source cost=12
D2 B1 source cost=12
D3 Compression main-output cost=4
D4 B1 main-output cost=4
D5 Compression required-sidecar cost=8
D6 B1 required-sidecar cost=8
D7 Compression reduced package cost=12
D8 B1 reduced package cost=12
D9 Compression strict reduction NOT_ESTABLISHED
D10 B1 strict reduction NOT_ESTABLISHED
D11 neither drops required sidecar to manufacture compression
D12 corresponding task terminals match
~~~

### E. R4 end-to-end chain validation — 12

~~~text
E1 Compression stage 1 established
E2 B1 stage 1 established
E3 Compression stage 2 established
E4 B1 stage 2 established
E5 Compression original P0 retained through chain evaluation
E6 B1 original P0 retained
E7 Compression detects x1/x2 end-to-end destructive collision
E8 B1 detects same collision
E9 Compression detects x3/x4 end-to-end destructive collision
E10 B1 detects same collision
E11 both keep local-stage successes while end-to-end claim fails
E12 both preserve LOCAL_STAGE_PASS != END_TO_END_COMPRESSION_PASS
~~~

### F. R5 integrated conflict / unresolved / sidecar pressure — 14

~~~text
F1 Compression Q1 conflict
F2 B1 Q1 conflict
F3 Compression Q2 underdetermined
F4 B1 Q2 unresolved
F5 Compression Q3 forward result retained
F6 B1 Q3 forward result retained
F7 Compression neighboring sidecars not promoted
F8 B1 neighboring sidecars not promoted
F9 Compression terminal conflict by frozen precedence
F10 B1 terminal conflict by frozen precedence
F11 lower-level Q2/Q3 retained by Compression
F12 lower-level Q2/Q3 retained by B1
F13 Compression deterministic ledger/rerun identifiers retained
F14 B1 deterministic ledger/rerun manifest emitted
~~~

### G. Comparative conclusion — 8

~~~text
G1 all five strong subcases scored from frozen evidence only
G2 seven gain axes scored from frozen outputs only
G3 terminology differences not counted as gain
G4 B1 extra unused competence not counted as baseline advantage
G5 DSD advantage recorded only if claim-relevant
G6 baseline advantage preserved if claim-relevant
G7 NO_GAIN preserved if all seven axes BASELINE_MATCH
G8 strongest-reasonable status limited to constructed-evidence level
   and no merger/deletion/absorption/permanent-redundancy conclusion inferred
~~~

~~~text
TOTAL_REQUIRED_CHECKS:
  82

PASS_THRESHOLD:
  82/82

PARTIAL_PASS_ALLOWED:
  no
~~~

Any mismatch remains visible.

## 12. Allowed counter changes on 82/82 PASS

~~~text
DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  4 -> 5

BASELINE_COMPRESSION_CASES:
  1 -> 2
~~~

If all seven gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_COMPRESSION_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_COMPRESSION:
  established_at_constructed_evidence_level
~~~

Unchanged:

~~~text
POSITIVE_COMPRESSION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_COMPRESSION_CASES:
  1

METHOD_BOUNDARY_COMPRESSION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  9

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPRESSION_APPLICATIONS:
  0

INDEPENDENT_COMPRESSION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established
~~~

## 13. Interpretation lock

~~~text
STRONGEST_REASONABLE_BASELINE_AT_CONSTRUCTED_EVIDENCE_LEVEL
  !=
UNIVERSALLY_STRONGEST_POSSIBLE_BASELINE

NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_DELETION_PROOF
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
NO_GAIN != PERMANENT_REDUNDANCY
~~~

A strongest-reasonable NO_GAIN result would mean only that a materially strong non-DSD compression engine matched the claim-relevant outputs on this frozen constructed workload under equal-information access.

## 14. Next

If the frozen strong workload completes without unresolved comparator weakness, proceed to deterministic same-project retrace as CPR-CH-006.
