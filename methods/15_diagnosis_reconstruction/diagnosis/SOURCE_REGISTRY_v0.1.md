# DSD Diagnosis — Source / Registry Recovery v0.1

Status: **SOURCE / REGISTRY RECOVERY COMPLETE — PRE-TASK-INTERFACE**  
Date: **2026-09-29**  
Method: **Diagnosis / DSD 진단론**  
Legacy path ID: `15A`  
Higher field: **VI. Inverse Inference & Reconstruction / 역추론·복원**

This document recovers the source constraints and current method-registry boundary for Diagnosis before any Task Interface is frozen.

It is not a Diagnosis protocol and does not itself authorize a protocol freeze.

## 1. Current registry identity

Current repository definition:

~~~text
Task:
  infer which current hidden states, failure modes, causes,
  or structural conditions remain compatible with present observations

Typical outputs:
  admissible current-state or cause set
  evidence-to-candidate compatibility table
  discriminating observations still required
  unresolved/non-identifiable diagnosis classes
  explicit separation of diagnosis from causal certainty

Boundary:
  diagnosis concerns present hidden structure or cause hypotheses;
  it does not automatically reconstruct a unique past history
~~~

Current Notion method root:

~~~text
DSD 진단론
Notion page:
  3d281f51-e7fa-813b-9188-cc45a52b3a6d
~~~

Current GitHub path:

~~~text
methods/15_diagnosis_reconstruction/diagnosis/
~~~

## 2. Source hierarchy used for recovery

### S1 — Formation Axiom System

Source:

~~~text
DSD_Formation_Axiom_System_EN(5).pdf
~~~

Relevant source constraints:

- undefined assignment is not a value and cannot be silently treated as zero;
- defined zero, undefined assignment, channel absence, and admitted zero contribution remain formally distinct;
- strict descriptive equivalence concerns the full candidate-level formation structure;
- equality of composite outputs is weaker than strict formation equivalence;
- staged comparison / first branching locates the earliest structural comparison obstruction when no compatible full comparison tuple survives.

Diagnosis consequence:

~~~text
an observation or derived readout that matches numerically
does not erase predecessor typed-status differences

and

one failed candidate comparison is not by itself proof
that every current-state candidate is excluded
~~~

### S2 — Property Axiom System

Source:

~~~text
DSD_Property_Axiom_System_EN(3).pdf
~~~

Property status family recovered from Definition 3.3:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Defined property records retain:

~~~text
property kind
complete ordered typed input
assigned value
~~~

The Property layer also preserves that an extension-level property assignment is not automatically a Formation assignment or operational-channel identity coordinate.

Diagnosis consequence:

~~~text
candidate compatibility must preserve claim-relevant status
and typed-input distinctions

absence / inapplicability / undefinedness
must not be converted into observed negative values
~~~

### S3 — Channel-Indexed Static Aggregation

Source:

~~~text
DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf
Section 11
~~~

Recovered constraints:

~~~text
support-retaining channel data
  !=
final aggregate alone

aggregate equality
  !=
source/support reconstruction

property aggregate may lose:
  selected support
  property kind
  typed input coordinates
  cross-property correlations

negative property statuses omitted from the defined-record carrier
must be retained separately when downstream work requires them
~~~

Exact reconstruction requires injectivity on the selected admissible class.

Combined coordinate recovery may additionally require a cross-coordinate reconstruction condition.

Diagnosis consequence:

~~~text
EQUAL_AGGREGATE != EQUAL_CURRENT_STATE

NONINJECTIVE_READOUT
  may leave multiple diagnostic candidates admissible

REQUIRED_SUPPORT_OR_STATUS_SIDECAR
  must remain available when the diagnostic claim depends on it
~~~

### S4 — Structural Reorganization Dynamics

Source:

~~~text
DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf
Sections 13-16
~~~

Recovered residual discipline:

~~~text
a residual is relative to:
  a declared target/reference relation
  a compatible carrier
  a declared residual map/discrepancy

no universal scalar subtraction exists across arbitrary typed components
~~~

Recovered transition discipline:

~~~text
a hybrid transition may be a typed relation
  J_k : X_k^- => X_k^+

the relation-valued form permits branching
or underdetermined transitions

a deterministic jump map is only a special case
~~~

Recovered descriptive-accessibility discipline:

~~~text
Pi_O : X -> X_O
need not be:
  linear
  orthogonal
  injective
  surjective

Pi_O(U)=Pi_O(V)
does not generally imply
U=V
~~~

A reduced readout need not be a complete classifier.

No converse reconstruction follows from a projection/readout without injectivity or another reconstruction condition.

Diagnosis consequence:

~~~text
RESIDUAL_MATCH != UNIQUE_CURRENT_STATE

PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY

REDUCED_READOUT != COMPLETE_DIAGNOSTIC_CLASSIFIER

TRANSITION_COMPATIBILITY != UNIQUE_PREDECESSOR_OR_CAUSE
~~~

### S5 — Measurement method handoff

Project-internal predecessor:

~~~text
methods/11_measurement/PROTOCOL_v0.1.md
blob:
  bc24a5e72adaf4a1b1e64203bd14b3e781810331
~~~

Measurement freezes alternatives, required distinctions, resolution, candidate readouts, decision rules, information-loss records, and temporal/regime scope.

The Measurement protocol explicitly preserves:

~~~text
AVAILABLE_MEASUREMENT != OBSERVED_RESULT
DISCRIMINATION_SUFFICIENCY != DIAGNOSIS
DISCRIMINATION_SUFFICIENCY != CAUSAL_PROOF
DYNAMIC_SUPPORT_AVAILABILITY != CAUSAL_SUFFICIENCY
~~~

Diagnosis consequence:

~~~text
Measurement may provide a typed discrimination/evidence handoff,
but Diagnosis must perform its own candidate-compatibility inference.

A measurement plan being sufficient does not select the diagnosed candidate.
~~~

### S6 — Diagnosis / Reconstruction registry boundary

Diagnosis registry:

~~~text
current hidden state
failure mode
cause hypothesis
current structural condition
compatible with present observations
~~~

Reconstruction registry:

~~~text
prior
omitted
damaged
compressed
otherwise hidden structures
and histories
compatible with evidence
~~~

Recovered registry boundary:

~~~text
DIAGNOSIS:
  primarily current hidden-state / current-condition inference

RECONSTRUCTION:
  primarily prior / omitted-structure / history inference

DIAGNOSIS_RESULT
  !=
UNIQUE_PAST_HISTORY

RECONSTRUCTION_RESULT
  !=
CURRENT_CAUSE_CERTAINTY
~~~

Both lanes must preserve multiplicity under insufficient evidence or non-injective forward structure.

## 3. Source-derived Diagnosis constraints

The following are recovered constraints rather than new Diagnosis theorems.

~~~text
DR-01
  preserve claim-relevant Formation / Property typed statuses

DR-02
  preserve support and typed-input sidecars when the diagnostic claim depends on them

DR-03
  equal aggregate / projection / reduced readout does not imply equal current state

DR-04
  residual evidence requires an explicit target/reference and compatible carrier

DR-05
  transition relations may be branching or underdetermined;
  do not assume deterministic uniqueness

DR-06
  injectivity / reconstruction scope must be tracked when a readout is used
  to eliminate or uniquely identify candidates

DR-07
  Measurement discrimination records are typed handoffs,
  not automatic Diagnosis results

DR-08
  dynamic distinguishability availability is not causal proof

DR-09
  Diagnosis does not automatically reconstruct a unique past history

DR-10
  if several candidates remain compatible, multiplicity remains visible
  unless additional frozen evidence eliminates candidates
~~~

## 4. Working atomic task — not yet frozen

The current working formulation is:

~~~text
Given:
  a declared current-state / failure-mode / cause-hypothesis candidate class,
  present observation/evidence records,
  typed applicability/status/provenance,
  explicit evidence-to-candidate compatibility or forward-model bridges,
  and any claim-relevant resolution / temporal / support / residual constraints,

determine:
  which candidates remain compatible,
  which are excluded,
  which cannot yet be evaluated,
  which distinctions remain unresolved,
  and which additional observations would discriminate remaining candidates.
~~~

This formulation is **prospective methodological construction**, not a theorem supplied by the predecessor papers.

It remains open to boundary attack before protocol freeze.

## 5. Candidate information classes for the future Task Interface

Not yet frozen:

~~~text
DIAGNOSIS_TASK_ID
TASK_VERSION

DIAGNOSIS_QUESTION
CANDIDATE_CLASS_ID
CANDIDATE_IDENTITIES

OBSERVATION_SET
OBSERVATION_PROVENANCE
OBSERVATION_STATUS

EVIDENCE_TO_CANDIDATE_BRIDGE_ID
BRIDGE_VERSION
BRIDGE_SCOPE

PROPERTY_STATUS_HANDOFF
FORMATION_STATUS_HANDOFF
MEASUREMENT_HANDOFF

SUPPORT_RETENTION_HANDOFF
AGGREGATION_OR_COMPRESSION_LOSS_HANDOFF

RESIDUAL_TARGET_ID
RESIDUAL_CARRIER
RESIDUAL_RULE

TEMPORAL_SCOPE
ACTIVE_REGIME
TRANSITION_CONSTRAINTS
DYNAMIC_SUPPORT_HANDOFF

IDENTIFIABILITY_SCOPE
INJECTIVITY_OR_COLLISION_RECORD

CAUSE_CLAIM_SCOPE
CAUSAL_BRIDGE_IF_ANY

MAXIMUM_SUPPORTED_CLAIM
~~~

These are recovery candidates only.

They do not yet constitute a required task record.

## 6. Prospective guards to pressure before freezing

Not yet protocol rules:

~~~text
OBSERVATION_COMPATIBLE != TRUE_STATE_ESTABLISHED

SINGLE_REMAINING_DECLARED_CANDIDATE
  !=
GLOBAL_UNIQUE_DIAGNOSIS

NO_ADMISSIBLE_DECLARED_CANDIDATE
  !=
NO_REAL_STATE_EXISTS

DIAGNOSTIC_COMPATIBILITY
  !=
CAUSAL_PROOF

CORRELATION_OR_RESIDUAL_MATCH
  !=
CAUSE_ESTABLISHED

MEASUREMENT_SUFFICIENCY
  !=
DIAGNOSIS

EQUAL_READOUT
  !=
EQUAL_HIDDEN_STATE

NONINJECTIVE_FORWARD_MAP
  !=
LICENSE_TO_SELECT_ONE_PREIMAGE

MISSING_REQUIRED_EVIDENCE
  !=
NEGATIVE_EVIDENCE

CURRENT_STATE_DIAGNOSIS
  !=
PAST_HISTORY_RECONSTRUCTION

CANDIDATE_RANKING
  !=
CANDIDATE_ELIMINATION

PROBABILITY
  !=
COMPATIBILITY
~~~

Each must be tested by pre-protocol boundary counterexamples before adoption.

## 7. Open interface questions

The following are intentionally unresolved:

~~~text
Q1
  Can current hidden-state diagnosis and cause-hypothesis diagnosis
  share one core protocol while keeping causal claims separately gated?

Q2
  What exact terminal distinguishes:
    multiple admissible candidates
    underdetermined bridge semantics
    missing required evidence
    zero admissible candidates
    candidate class out of scope?

Q3
  Is an exhaustive candidate class ever required,
  or may every result remain explicitly candidate-class-bounded?

Q4
  When one candidate remains,
  what additional completeness / injectivity assumptions are required
  before using a uniqueness label?

Q5
  How should conflicting observations be represented:
    conflicting evidence
    bridge conflict
    model mismatch
    candidate exclusion
    unresolved provenance?

Q6
  How should probabilistic / Bayesian diagnosis enter?
  The recovered DSD sources do not themselves supply priors,
  likelihoods, posterior semantics, or decision losses.

Q7
  Candidate ranking and best-next-measurement selection may overlap
  Optimization or Measurement.
  Which records remain Diagnosis outputs and which are handoffs?

Q8
  How should dynamic transition relations constrain present-state candidates
  without silently performing past-history Reconstruction?
~~~

## 8. Boundary with neighboring methods

Working non-substitution map:

~~~text
MEASUREMENT:
  asks whether observations/readouts can distinguish alternatives

DIAGNOSIS:
  asks which current candidates remain compatible with evidence

RECONSTRUCTION:
  asks which prior/omitted structures or histories remain compatible

PREDICTION:
  asks what future outcomes follow from supplied state/model assumptions

SIMULATION:
  executes supplied dynamic/model evolution

AUDIT:
  evaluates rule/evidence/process conformance

COMPARISON:
  evaluates declared relations between supplied objects

CLASSIFICATION:
  assigns objects to declared classes under frozen class semantics
~~~

These boundaries are registry-level working distinctions only.

Direct boundary validation has not yet been executed for Diagnosis.

## 9. Current evidence state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

DEDICATED_DIAGNOSIS_PROTOCOL:
  not established

TASK_INTERFACE_DRAFT:
  not established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

DIRECT_DIAGNOSIS_PILOTS_ATTEMPTED:
  0

BASELINE_DIAGNOSIS_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_DIAGNOSIS_APPLICATIONS:
  0

INDEPENDENT_DIAGNOSIS_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

DIAGNOSIS_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_DIAGNOSIS_EVIDENCE_STATUS:
  source_and_registry_recovery_complete

PROTOCOL_REVISION_REQUIRED:
  not applicable

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 10. Next

Create the Diagnosis planning/worklog lane and draft Task Interface v0.1 from this recovered registry.

The Task Interface draft must remain historical once boundary attack begins.
