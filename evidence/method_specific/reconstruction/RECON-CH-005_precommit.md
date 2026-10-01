# RECON-CH-005 — Strongest-Reasonable Non-DSD Reconstruction Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-10-01**  
Challenge ID: `RECON-CH-005`  
Method: **Reconstruction / DSD 복원론**  
Protocol: **Reconstruction Protocol v0.1**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparator identities

~~~text
RECONSTRUCTION_PROTOCOL_VERSION:
  v0.1

RECONSTRUCTION_PROTOCOL_COMMIT:
  2d4cdcab4b646a9d75f96dcc2ef301722eb612ad

RECONSTRUCTION_PROTOCOL_BLOB:
  1f009e81b9992fbdec75abbd9551e9d06f0a170e

PREVIOUS_COMPETENT_BASELINE:
  RECON-CH-004
  B0_GENERIC_TYPED_INVERSE_RECONSTRUCTION_EVALUATOR
  64/64 PASS / NO_GAIN
~~~

No Reconstruction Protocol revision is allowed in response to this baseline result.

## 2. Strong baseline identity

~~~text
BASELINE_ID:
  B1_STRONG_INVERSE_RECONSTRUCTION_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_inverse_reconstruction_engine

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
versioned task / source-class / evidence / bridge registries
typed evidence and sidecar schemas
automatic evidence-set consistency validation

finite or symbolic constraint solving
exact affine-preimage computation
kernel / null-space / rank analysis
declared-class injectivity and uniqueness analysis

dependency-aware required-interface closure
explicit interface-closure registries
identifiability / nonidentifiability certificates

relation-valued temporal graph reasoning
backward reachability
branch / merge history enumeration
direct-versus-composed relation comparison

explicit Bayesian inverse inference when priors and likelihoods are supplied
symbolic or exact posterior normalization when decidable

blocked / conflicting / unresolved / outside-scope states
deterministic terminal precedence
bounded maximum-claim generation

Tracking / Lineage / Diagnosis / Measurement / Aggregation /
Compression / Transformation / Prediction / Simulation /
Optimization / Audit sidecar separation

deterministic evaluation ledgers
full rerun manifests
~~~

B1 may derive consequences algorithmically from the same supplied records.

B1 may not receive hidden factual input unavailable to Reconstruction.

B1 may not be weakened after precommit.

## 3. Strong baseline operation

B1 performs:

~~~text
B1-1 freeze task/version, primary claim, target kind,
     source/history class, class mode, completeness status,
     evidence registry, bridge registry, inference mode,
     temporal/history scope, and maximum-supported claim

B1-2 bind every class/evidence/bridge/interface/history record
     to explicit version, identity, scope, and precedence;
     prohibit retroactive substitution

B1-3 preserve typed evidence status, provenance, support,
     undefined/zero distinctions, and unavailable-interface states

B1-4 validate evidence-set coherence before candidate exclusion

B1-5 evaluate deterministic compatibility by exact finite or
     symbolic constraint solving where decidable

B1-6 compute exact preimages, affine fibers, kernels, and rank
     for supplied linear maps where decidable

B1-7 evaluate injectivity/uniqueness only on the supplied
     class and scope unless a broader proof is supplied

B1-8 compute dependency closure for required support/status/
     provenance/relational/readout/history interfaces

B1-9 evaluate interface-bounded identifiability or nonidentifiability
     only when the frozen interface is explicitly complete for the claim

B1-10 execute relation-valued backward reachability and history
      composition without imposing unique predecessors on branch/merge graphs

B1-11 retain direct long-interval history relations independently
      from composed short-interval relations

B1-12 execute explicit Bayesian inverse inference only when
      priors, likelihoods, normalization domain, and semantics are supplied

B1-13 keep posterior ranking, compatibility, unique recovery,
      Tracking relation, Lineage identity, and historical truth separate

B1-14 preserve conflict, outside-scope, unresolved, blocked,
      evaluable failure, established, and multi-obligation partial states

B1-15 apply frozen terminal precedence without erasing lower-level states

B1-16 keep neighboring/source-layer sidecars non-authoritative
      unless an explicit Reconstruction rule promotes them

B1-17 emit deterministic candidate/interface/history ledgers
      and a bounded maximum-supported claim

B1-18 emit a full rerun manifest sufficient to replay the frozen task
~~~

## 4. Equal-information and fairness rule

Reconstruction and B1 receive exactly the same claim-relevant records.

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

B1 is not required to reconstruct DSD ontology or terminology.

It receives the same already-frozen task/class/evidence/bridge/interface/history/status/support records exposed to Reconstruction.

Extra computational competence is allowed.

Extra hidden factual information is not.

## 5. Strong subcase R1 — versioned registries and non-retroactivity

Frozen task versions:

~~~text
TASK-v1
TASK-v2
~~~

Source-class registries:

~~~text
CLASS-v1:
  {h1,h2,h3}

CLASS-v2:
  {h1,h2,h3,h4}
~~~

Evidence registry:

~~~text
EVIDENCE-v1:
  y=0
  status=DEFINED_ZERO
  support=S1

EVIDENCE-v2:
  y=1
  status=DEFINED_NONZERO
  support=S2
~~~

Bridge registry:

~~~text
BRIDGE-v1:
  valid for TASK-v1

  h1:
    y=0 / DEFINED_ZERO / S1

  h2:
    y=0 / DEFINED_ZERO / S1

  h3:
    y=0 / APPLICABLE_BUT_UNDEFINED / S2

BRIDGE-v2:
  valid for TASK-v2
  separate definition
~~~

Expected both:

~~~text
TASK-v1 uses:
  CLASS-v1
  EVIDENCE-v1
  BRIDGE-v1

compatible:
  {h1,h2}

excluded:
  {h3}

set outcome:
  multiple compatible

task terminal:
  established / complete

retroactive substitution of v2 into TASK-v1:
  prohibited

registry/version provenance:
  retained
~~~

## 6. Strong subcase R2 — exact affine preimage / kernel / declared-class uniqueness

Frozen forward map:

~~~text
F:
  R^3 -> R^2

F(x,y,z):
  (x+z, y+z)

matrix:
  [1 0 1]
  [0 1 1]
~~~

Exact kernel:

~~~text
ker(F):
  span{(-1,-1,1)}
~~~

Observed readout:

~~~text
y_obs:
  (2,3)
~~~

Global affine preimage:

~~~text
F^{-1}(2,3):
  {(2-t, 3-t, t) : t in R}
~~~

Declared reconstruction class:

~~~text
A:
  {(x,y,0) : x,y in R}
~~~

On A:

~~~text
F(x,y,0):
  (x,y)
~~~

Expected both:

~~~text
GLOBAL_INJECTIVITY:
  not established

GLOBAL_PREIMAGE:
  infinite affine fiber

DECLARED_CLASS_PREIMAGE:
  {(2,3,0)}

UNIQUE_WITHIN_DECLARED_CLASS:
  established

outside-A alternative:
  (1,2,1)

GLOBAL_UNIQUE_RECONSTRUCTION:
  not established
~~~

Required guards:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_HISTORICAL_OR_SOURCE_TRUTH
CLASS_LOCAL_INJECTIVITY != GLOBAL_INJECTIVITY
~~~

## 7. Strong subcase R3 — required-interface dependency closure

Frozen candidates:

~~~text
s1:
  main_readout=0
  status=DEFINED_ZERO
  support=S1

s2:
  main_readout=0
  status=APPLICABLE_BUT_UNDEFINED
  support=S1
~~~

Frozen claim:

~~~text
recover which source candidate generated the retained readout
~~~

Available:

~~~text
main_readout:
  0

support:
  S1
~~~

Required:

~~~text
typed source-status sidecar
~~~

Availability:

~~~text
typed source-status sidecar:
  unavailable
~~~

Expected both:

~~~text
main readout:
  non-discriminating

support:
  non-discriminating

required-interface dependency closure:
  status sidecar required

candidate discrimination:
  blocked

task terminal:
  BLOCKED

no coercion:
  unavailable status != defined zero

no loss promotion:
  unavailable interface != established destructive information loss
~~~

## 8. Strong subcase R4 — explicit probabilistic inverse inference without truth promotion

Frozen prior-history hypotheses:

~~~text
p1
p2
~~~

Frozen probabilistic interface:

~~~text
prior:
  P(p1)=1/2
  P(p2)=1/2

observation:
  e

likelihood:
  P(e|p1)=3/4
  P(e|p2)=1/4

normalization domain:
  {p1,p2}

posterior semantics:
  Bayes rule

ranking rule:
  descending posterior probability
~~~

Exact evidence probability:

~~~text
P(e):
  (1/2)(3/4) + (1/2)(1/4)
  =
  1/2
~~~

Expected posterior:

~~~text
P(p1|e):
  3/4

P(p2|e):
  1/4

posterior ranking:
  p1 > p2
~~~

Expected both:

~~~text
probabilistic interface:
  fully supplied

posterior:
  exactly (3/4,1/4)

ranking:
  p1 > p2

unique reconstructed history:
  not established merely from ranking

global historical truth:
  not established

Lineage identity:
  not established
~~~

Required guards:

~~~text
MOST_PROBABLE_HISTORY != ONLY_COMPATIBLE_HISTORY
POSTERIOR_RANKING != HISTORICAL_TRUTH
PROBABILITY != ESTABLISHED_LINEAGE
~~~

## 9. Strong subcase R5 — temporal relation algebra / branch-merge / sidecar pressure

Frozen short-interval history relations:

~~~text
H_01:
  (a0,a1)
  (b0,a1)

H_12:
  (a1,c2)
  (a1,d2)
~~~

Thus branch and merge are both present.

Composed relation:

~~~text
H_12 o H_01:
  (a0,c2)
  (a0,d2)
  (b0,c2)
  (b0,d2)
~~~

Frozen direct long-interval relation:

~~~text
H_02:
  (a0,c2)
  (a0,d2)
  (b0,c2)
  (b0,d2)
  (e0,c2)
~~~

The extra direct pair `(e0,c2)` is independently supplied long-interval information.

Current observed endpoint:

~~~text
c2
~~~

Expected backward-compatible prior set from the direct relation:

~~~text
{a0,b0,e0}
~~~

Neighbor/source sidecars supplied:

~~~text
Tracking continuity for a subset
Lineage relation for a subset
Diagnosis current-state record
Aggregation equality record
Compression collision record
Measurement discrimination plan
Transformation map
Prediction output
Simulation trajectory
Optimization ranking
Audit pass
Formation witness-history
~~~

Expected both:

~~~text
branch/merge:
  preserved

composed H_02 candidates:
  {a0,b0}

direct H_02 candidates:
  {a0,b0,e0}

direct long-interval record:
  not replaced by composition

reconstructed prior candidate set for endpoint c2:
  {a0,b0,e0}

unique predecessor:
  not established

Tracking subset:
  not promoted to universal trace identity

Lineage subset:
  not promoted to universal lineage identity

Formation witness-history:
  not promoted to actual temporal history

other neighboring sidecars:
  not promoted into reconstruction criteria without explicit rule

deterministic history ledger:
  emitted

rerun manifest:
  emitted
~~~

## 10. Frozen gain axes

~~~text
G1 VERSIONED_REGISTRY_AND_NONRETROACTIVITY_GAIN

G2 EXACT_AFFINE_PREIMAGE_KERNEL_AND_DECLARED_CLASS_GAIN

G3 REQUIRED_INTERFACE_DEPENDENCY_CLOSURE_GAIN

G4 EXPLICIT_PROBABILISTIC_INVERSE_INFERENCE_AND_SCOPE_GAIN

G5 TEMPORAL_RELATION_ALGEBRA_BRANCH_MERGE_AND_HANDOFF_GAIN

G6 BOUNDED_MAXIMUM_CLAIM_AND_TERMINAL_GAIN

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
if Reconstruction is protocol-nonconformant or wrong:
  FAIL

if one or more frozen axes establish a real DSD advantage
against the still-fair B1:
  RECONSTRUCTION_GAIN_SHOWN

if all seven axes are BASELINE_MATCH:
  RECONSTRUCTION_NO_GAIN

if a baseline advantage appears:
  preserve BASELINE_ADVANTAGE
  and do not relabel it as DSD gain

otherwise:
  RECONSTRUCTION_GAIN_UNDERDETERMINED
~~~

## 11. Frozen scoring — 82 checks

### A. Immutable fairness — 10

~~~text
A1 Reconstruction protocol identity frozen
A2 B1 identity and capabilities frozen
A3 R1-R5 frozen before execution
A4 equal-information rule frozen
A5 Reconstruction hidden favorable inputs = 0
A6 B1 claim-relevant withheld inputs = 0
A7 B1 not weakened after precommit
A8 output/gain mapping frozen
A9 scoring frozen
A10 external application/evaluator not counted
~~~

### B. R1 versioned registries — 12

~~~text
B1 Reconstruction selects CLASS-v1 for TASK-v1
B2 B1 selects same class registry
B3 Reconstruction selects EVIDENCE-v1
B4 B1 selects same evidence registry
B5 Reconstruction selects BRIDGE-v1
B6 B1 selects same bridge
B7 Reconstruction compatible set={h1,h2}
B8 B1 compatible set={h1,h2}
B9 Reconstruction excludes h3
B10 B1 excludes h3
B11 both prohibit retroactive v2 substitution
B12 both retain registry/version provenance
~~~

### C. R2 exact preimage / declared class — 14

~~~text
C1 Reconstruction exact kernel relation recognized
C2 B1 exact kernel relation recognized
C3 Reconstruction ker(F)=span{(-1,-1,1)}
C4 B1 same kernel
C5 Reconstruction global affine preimage recognized
C6 B1 same affine preimage
C7 Reconstruction global injectivity not established
C8 B1 global injectivity not established
C9 Reconstruction declared class A frozen
C10 B1 declared class A frozen
C11 Reconstruction declared-class preimage={(2,3,0)}
C12 B1 same declared-class preimage
C13 both establish declared-class uniqueness
C14 neither promotes declared-class uniqueness globally
~~~

### D. R3 required-interface dependency closure — 12

~~~text
D1 Reconstruction main readout non-discriminating
D2 B1 same
D3 Reconstruction support non-discriminating
D4 B1 same
D5 Reconstruction identifies typed-status sidecar as required
D6 B1 identifies same dependency
D7 Reconstruction records sidecar unavailable
D8 B1 records sidecar unavailable
D9 Reconstruction task BLOCKED
D10 B1 task BLOCKED
D11 neither coerces unavailable status to zero
D12 neither promotes unavailability to destructive-loss proof
~~~

### E. R4 explicit probabilistic inverse inference — 12

~~~text
E1 Reconstruction prior=(1/2,1/2)
E2 B1 same prior
E3 Reconstruction likelihood=(3/4,1/4)
E4 B1 same likelihood
E5 Reconstruction evidence probability=1/2
E6 B1 evidence probability=1/2
E7 Reconstruction posterior=(3/4,1/4)
E8 B1 same posterior
E9 Reconstruction ranking p1>p2
E10 B1 same ranking
E11 neither promotes ranking to unique/global historical truth
E12 neither promotes probability to established Lineage identity
~~~

### F. R5 temporal relation algebra / handoff pressure — 14

~~~text
F1 Reconstruction computes composed H_02 candidate relations correctly
F2 B1 computes same composition
F3 Reconstruction preserves branch relation
F4 B1 preserves branch relation
F5 Reconstruction preserves merge relation
F6 B1 preserves merge relation
F7 Reconstruction retains direct H_02 independently
F8 B1 retains direct H_02 independently
F9 Reconstruction retains extra direct predecessor e0 for c2
F10 B1 retains e0
F11 Reconstruction returns prior set {a0,b0,e0}
F12 B1 returns same prior set
F13 both preserve Tracking/Lineage/Formation and neighboring sidecars as non-substituting without explicit rule
F14 both emit deterministic history ledger and rerun manifest
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
DIRECT_RECONSTRUCTION_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_RECONSTRUCTION_PILOTS:
  4 -> 5

BASELINE_RECONSTRUCTION_CASES:
  1 -> 2
~~~

If all seven gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_RECONSTRUCTION_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_RECONSTRUCTION:
  established_at_constructed_evidence_level
~~~

Unchanged:

~~~text
POSITIVE_RECONSTRUCTION_CASES:
  1

NEGATIVE_OR_UNRESOLVED_RECONSTRUCTION_CASES:
  1

METHOD_BOUNDARY_RECONSTRUCTION_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  11

UNRECOVERABILITY_RECONSTRUCTION_CASES:
  2

REPRODUCIBILITY_CASES:
  0

EXTERNAL_RECONSTRUCTION_APPLICATIONS:
  0

INDEPENDENT_RECONSTRUCTION_VALIDATION:
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

A strongest-reasonable NO_GAIN result would mean only that a materially strong non-DSD inverse-reconstruction engine matched the claim-relevant Reconstruction outputs on this frozen constructed workload under equal-information access.

## 14. Next

If the frozen strong workload completes without unresolved comparator weakness, proceed to deterministic same-project retrace as RECON-CH-006.
