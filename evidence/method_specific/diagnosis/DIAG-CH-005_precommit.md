# DIAG-CH-005 — Strongest-Reasonable Non-DSD Diagnosis Baseline Precommit

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-30**  
Challenge ID: `DIAG-CH-005`  
Method: **Diagnosis / DSD 진단론**  
Protocol: **Diagnosis Protocol v0.1**  
Case class: `strongest_reasonable_baseline_constructed`  
Case origin: `constructed_same_project`  
Evidence scope: `method_specific`  
External application: `no`

## 1. Frozen comparator identities

~~~text
DIAGNOSIS_PROTOCOL_VERSION:
  v0.1

DIAGNOSIS_PROTOCOL_COMMIT:
  2d6eb83301860f044cba9a67a87c3a937335823b

DIAGNOSIS_PROTOCOL_BLOB:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129

PREVIOUS_COMPETENT_BASELINE:
  DIAG-CH-004
  B0_GENERIC_TYPED_DIAGNOSIS_EVALUATOR
  64/64 PASS / NO_GAIN
~~~

No Diagnosis Protocol revision is allowed in response to this baseline result.

## 2. Strong baseline identity

~~~text
BASELINE_ID:
  B1_STRONG_DIAGNOSTIC_INFERENCE_ENGINE

BASELINE_CLASS:
  strongest_reasonable_non_DSD_constructed_diagnostic_inference_engine

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
versioned task / candidate / evidence / bridge registries
typed evidence and sidecar schemas
automatic evidence-set consistency validation
constraint-propagation candidate elimination
finite relation enumeration
exact symbolic or linear-algebraic preimage analysis where decidable
kernel/rank analysis for supplied linear forward maps
declared-class injectivity and uniqueness checks
dependency-aware required-interface closure
alternative threshold / resolution / schema branch management
relation-valued transition reasoning
explicit Bayesian inference when priors and likelihoods are supplied
explicit model-bounded cause tables/graphs when supplied
deterministic terminal-precedence engines
bounded maximum-claim generation
neighbor-sidecar non-substitution rules
deterministic evaluation ledgers
full rerun manifests
~~~

B1 may derive consequences algorithmically from the same supplied records.

B1 may not receive hidden factual input unavailable to Diagnosis.

B1 may not be weakened after precommit.

## 3. Strong baseline operation

B1 performs:

~~~text
B1-1 freeze task/version, primary claim, candidate registry,
     evidence registry, bridge registry, inference mode,
     resolution/time/regime, and maximum-supported claim

B1-2 bind every candidate/evidence/bridge rule to explicit version,
     identity, scope, and precedence; prohibit retroactive substitution

B1-3 preserve typed evidence status, provenance, support,
     undefined/zero distinctions, and unavailable-interface states

B1-4 validate evidence-set coherence before interpreting
     broad candidate elimination

B1-5 evaluate deterministic pair relations by exact finite or
     symbolic constraint propagation where decidable

B1-6 compute exact preimages/kernel/rank information for supplied
     linear maps where decidable; distinguish global from declared-class uniqueness

B1-7 compute dependency closure for required status/support/readout/
     transition/cause/probabilistic interfaces before claim evaluation

B1-8 retain multiple admissible thresholds/resolutions/schema interpretations
     and emit unresolved state when outcomes differ without a resolver

B1-9 execute relation-valued transition constraints without selecting
     a unique predecessor/history unless supplied evidence warrants it

B1-10 execute explicit Bayesian posterior/ranking calculations only
      when frozen priors, likelihoods, normalization domain, and ranking
      semantics are supplied

B1-11 keep compatibility, probability, causal identification,
      current-state inference, and past-history reconstruction separate

B1-12 preserve conflict, outside-scope, unresolved, blocked,
      evaluable failure, established, and multi-obligation partial states

B1-13 apply frozen task-terminal precedence without erasing
      lower-level states

B1-14 keep Measurement / Reconstruction / Classification / Comparison /
      Prediction / Simulation / Optimization / Audit / Tracking / Lineage
      sidecars non-authoritative unless an explicit Diagnosis rule promotes them

B1-15 emit only bounded claims; prohibit unsupported global uniqueness,
      unrestricted causal proof, ontological impossibility, or external validity

B1-16 emit deterministic candidate/evidence/bridge ledgers

B1-17 emit a deterministic terminal/maximum-claim ledger

B1-18 emit a full rerun manifest sufficient to replay the frozen task
~~~

## 4. Equal-information and fairness rule

Diagnosis and B1 receive exactly the same claim-relevant records.

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

It receives the same already-frozen task/candidate/evidence/bridge/status/support/residual/transition/cause/probabilistic records exposed to Diagnosis.

Extra computational competence is allowed.

Extra hidden factual information is not.

## 5. Strong subcase R1 — versioned registries and non-retroactivity

Frozen task versions:

~~~text
TASK-v1
TASK-v2
~~~

Candidate registry:

~~~text
CANDIDATES-v1:
  {h1,h2,h3}

CANDIDATES-v2:
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
  CANDIDATES-v1
  EVIDENCE-v1
  BRIDGE-v1

compatible:
  {h1,h2}

excluded:
  {h3}

task terminal:
  established / complete

retroactive substitution of v2 into TASK-v1:
  prohibited

registry/version provenance:
  retained
~~~

## 6. Strong subcase R2 — exact linear preimage and declared-class uniqueness

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

Declared candidate class:

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

DECLARED_CLASS_PREIMAGE:
  {(2,3,0)}

UNIQUE_WITHIN_DECLARED_CLASS:
  established

outside-A alternatives:
  exist along kernel direction

example:
  (2,3,0)
  and
  (1,2,1)

both map to:
  (2,3)

GLOBAL_UNIQUE_DIAGNOSIS:
  not established
~~~

Required guard:

~~~text
UNIQUE_WITHIN_DECLARED_CLASS != GLOBAL_UNIQUE_DIAGNOSIS
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
identify whether current candidate is s1 or s2
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
Property-status sidecar
~~~

Availability:

~~~text
Property-status sidecar:
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
~~~

Required guard:

~~~text
UNAVAILABLE_REQUIRED_INTERFACE != EVALUABLE_INCOMPATIBILITY
~~~

## 8. Strong subcase R4 — explicit probabilistic inference without truth promotion

Frozen candidate hypotheses:

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

candidate truth:
  not established merely from ranking

unrestricted causal proof:
  not established
~~~

Required guards:

~~~text
MOST_PROBABLE != ONLY_COMPATIBLE
POSTERIOR_RANKING != GLOBAL_TRUTH
PROBABILITY != CAUSAL_PROOF
~~~

## 9. Strong subcase R5 — integrated conflict / threshold ambiguity / sidecar / rerun pressure

Frozen obligations:

~~~text
Q1:
  same EVIDENCE-RULE-v7 contains two equally applicable records

  record A:
    sensor S at t0 = 0

  record B:
    sensor S at t0 = 1

  exact single-valued schema
  resolver:
    none

Q2:
  two admissible thresholds for candidate q

  THRESHOLD-A:
    residual <= 0.2
    candidate passes

  THRESHOLD-B:
    residual <= 0.1
    candidate fails

  threshold resolver:
    none

Q3:
  deterministic compatibility otherwise established

  neighboring sidecars present:
    Measurement
    Reconstruction
    Classification
    Comparison
    Prediction
    Simulation
    Optimization
    Audit
    Tracking
    Lineage
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
  Diagnosis result remains established only from the supplied
  Diagnosis contract;
  neighboring sidecars do not substitute as Diagnosis criteria

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
G1 VERSIONED_REGISTRY_AND_NONRETROACTIVITY_GAIN

G2 EXACT_PREIMAGE_KERNEL_AND_DECLARED_CLASS_GAIN

G3 REQUIRED_INTERFACE_DEPENDENCY_CLOSURE_GAIN

G4 EXPLICIT_PROBABILISTIC_INFERENCE_AND_SCOPE_GAIN

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
if Diagnosis is protocol-nonconformant or wrong:
  FAIL

if one or more frozen axes establish a real DSD advantage
against the still-fair B1:
  DIAGNOSIS_METHOD_GAIN_ESTABLISHED

if all seven axes are BASELINE_MATCH:
  DIAGNOSIS_METHOD_GAIN_NO_GAIN

if a baseline advantage appears:
  preserve BASELINE_ADVANTAGE
  and do not relabel it as DSD gain

otherwise:
  DIAGNOSIS_METHOD_GAIN_UNDERDETERMINED
~~~

## 11. Frozen scoring — 82 checks

### A. Immutable fairness — 10

~~~text
A1 Diagnosis protocol identity frozen
A2 B1 identity and capabilities frozen
A3 R1-R5 frozen before execution
A4 equal-information rule frozen
A5 Diagnosis hidden favorable inputs = 0
A6 B1 claim-relevant withheld inputs = 0
A7 B1 not weakened after precommit
A8 output/gain mapping frozen
A9 scoring frozen
A10 external application/evaluator not counted
~~~

### B. R1 versioned registries — 12

~~~text
B1 Diagnosis selects CANDIDATES-v1 for TASK-v1
B2 B1 selects same candidate registry
B3 Diagnosis selects EVIDENCE-v1
B4 B1 selects same evidence registry
B5 Diagnosis selects BRIDGE-v1
B6 B1 selects same bridge
B7 Diagnosis compatible set={h1,h2}
B8 B1 compatible set={h1,h2}
B9 Diagnosis excludes h3
B10 B1 excludes h3
B11 both prohibit retroactive v2 substitution
B12 both retain registry/version provenance
~~~

### C. R2 exact preimage / declared class — 14

~~~text
C1 Diagnosis exact kernel relation recognized
C2 B1 exact kernel relation recognized
C3 Diagnosis ker(F)=span{(-1,-1,1)}
C4 B1 same kernel
C5 Diagnosis global injectivity not established
C6 B1 global injectivity not established
C7 Diagnosis declared class A frozen
C8 B1 declared class A frozen
C9 Diagnosis declared-class preimage={(2,3,0)}
C10 B1 same declared-class preimage
C11 Diagnosis outside-A alternative retained
C12 B1 same alternative retained
C13 both establish declared-class uniqueness
C14 neither promotes declared-class uniqueness globally
~~~

### D. R3 required-interface dependency closure — 12

~~~text
D1 Diagnosis main readout non-discriminating
D2 B1 same
D3 Diagnosis support non-discriminating
D4 B1 same
D5 Diagnosis identifies status sidecar as required
D6 B1 identifies same dependency
D7 Diagnosis records sidecar unavailable
D8 B1 records sidecar unavailable
D9 Diagnosis task BLOCKED
D10 B1 task BLOCKED
D11 neither coerces unavailable status to zero
D12 corresponding task terminals match
~~~

### E. R4 explicit probabilistic inference — 12

~~~text
E1 Diagnosis prior=(1/2,1/2)
E2 B1 same prior
E3 Diagnosis likelihood=(3/4,1/4)
E4 B1 same likelihood
E5 Diagnosis evidence probability=1/2
E6 B1 evidence probability=1/2
E7 Diagnosis posterior=(3/4,1/4)
E8 B1 same posterior
E9 Diagnosis ranking p1>p2
E10 B1 same ranking
E11 neither promotes ranking to truth
E12 neither promotes probability to causal proof
~~~

### F. R5 integrated conflict / unresolved / sidecar pressure — 14

~~~text
F1 Diagnosis Q1 evidence conflict
F2 B1 Q1 conflict
F3 Diagnosis Q2 underdetermined
F4 B1 Q2 unresolved
F5 Diagnosis Q3 substantive result retained
F6 B1 Q3 substantive result retained
F7 Diagnosis neighboring sidecars not promoted
F8 B1 neighboring sidecars not promoted
F9 Diagnosis terminal conflict by frozen precedence
F10 B1 terminal conflict by frozen precedence
F11 lower-level Q2/Q3 retained by Diagnosis
F12 lower-level Q2/Q3 retained by B1
F13 Diagnosis deterministic ledger/rerun identifiers retained
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
DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  4 -> 5

SUCCESSFUL_DIRECT_DIAGNOSIS_PILOTS:
  4 -> 5

BASELINE_DIAGNOSIS_CASES:
  1 -> 2
~~~

If all seven gain axes are `BASELINE_MATCH`:

~~~text
NO_GAIN_DIAGNOSIS_CASES:
  1 -> 2

STRONGEST_REASONABLE_BASELINE_DIAGNOSIS:
  established_at_constructed_evidence_level
~~~

Unchanged:

~~~text
POSITIVE_DIAGNOSIS_CASES:
  1

NEGATIVE_OR_UNRESOLVED_DIAGNOSIS_CASES:
  1

METHOD_BOUNDARY_DIAGNOSIS_CASES:
  1

METHOD_FAMILY_BOUNDARY_PAIRS_TESTED:
  10

REPRODUCIBILITY_CASES:
  0

EXTERNAL_DIAGNOSIS_APPLICATIONS:
  0

INDEPENDENT_DIAGNOSIS_VALIDATION:
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

A strongest-reasonable NO_GAIN result would mean only that a materially strong non-DSD diagnostic inference engine matched the claim-relevant Diagnosis outputs on this frozen constructed workload under equal-information access.

## 14. Next

If the frozen strong workload completes without unresolved comparator weakness, proceed to deterministic same-project retrace as DIAG-CH-006.
