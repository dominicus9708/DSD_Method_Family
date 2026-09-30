# DSD Reconstruction — Source / Registry Recovery v0.1

Status: **SOURCE / REGISTRY RECOVERY COMPLETE — PRE-TASK-INTERFACE**  
Date: **2026-10-01**  
Method: **Reconstruction / DSD 복원론**  
Legacy path ID: `15B`  
Higher field: **VI. Inverse Inference & Reconstruction / 역추론·복원**

This document recovers the source constraints and current method-registry boundary for Reconstruction before any Task Interface is frozen.

It is not a Reconstruction protocol and does not itself authorize a protocol freeze.

## 1. Current registry identity

Current repository definition:

~~~text
Task:
  infer which prior, omitted, damaged, compressed,
  or otherwise hidden structures and histories
  remain compatible with available evidence

Typical outputs:
  admissible reconstruction set
  multiple-history or multiple-support collision witnesses
  provenance / lineage requirements
  conditions for unique reconstruction
  explicit unrecoverable-information record

Boundary:
  when the forward map is non-injective or evidence is incomplete,
  multiple admissible reconstructions remain visible unless
  additional evidence eliminates them
~~~

Current Notion method root:

~~~text
DSD 복원론
Notion page:
  3d281f51-e7fa-8101-b6fb-e87911dcbb6a
~~~

Current GitHub path:

~~~text
methods/15_diagnosis_reconstruction/reconstruction/
~~~

## 2. Source hierarchy used for recovery

### S1 — Formation Axiom System

Source:

~~~text
DSD_Formation_Axiom_System_EN(5).pdf
~~~

Recovered constraints:

- the seven stages encode formation/dependency order rather than a temporal history of physical events;
- a candidate channel is admitted exactly when its formation-trace set is nonempty;
- formation traces are compatible witness histories used to characterize admission and are not automatically historical event trajectories;
- undefined assignment, defined zero, channel absence, and admitted zero contribution remain distinct;
- strict formation equivalence compares the full candidate-level formation structure;
- equality of composite outputs is strictly weaker than strict formation equivalence;
- nested stage-comparison sets locate a first branching obstruction without selecting one arbitrary failed comparison map as the whole explanation.

Reconstruction consequence:

~~~text
FORMATION_WITNESS_HISTORY
  !=
ACTUAL_TEMPORAL_HISTORY

STAGE_DEPENDENCY_ORDER
  !=
PHYSICAL_TIME_ORDER

EQUAL_COMPOSITE_OUTPUT
  !=
EQUAL_FORMATION_SOURCE

one surviving or failed formation witness
  !=
global historical uniqueness
~~~

A Formation trace may be an admissible reconstruction-side source only at the structural-witness level explicitly licensed by the Formation theory.

### S2 — Property Axiom System

Source:

~~~text
DSD_Property_Axiom_System_EN(3).pdf
~~~

Recovered Property status family:

~~~text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_VALUE
~~~

Defined records retain:

~~~text
property kind
complete ordered typed input
assigned value
~~~

The explicit completion / primitive-reduction inverse law uniquely recomputes the derived Property coordinates from a complete primitive core.

That result is definitional recompletion, not evidence-based recovery of an unknown historical state.

Reconstruction consequence:

~~~text
MISSING_OR_UNDEFINED_PROPERTY
  !=
ZERO_PROPERTY

COMPLETE_TYPED_INPUT
  must remain attached when claim-relevant

DEFINITIONAL_RECOMPLETION_FROM_SUPPLIED_PRIMITIVE_CORE
  !=
EVIDENCE_BASED_HISTORICAL_RECONSTRUCTION
~~~

### S3 — Channel-Indexed Static Aggregation

Source:

~~~text
DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf
Sections 11-14
~~~

Recovered constraints:

~~~text
aggregate equality
  !=
support equality

aggregate equality
  !=
source decomposition equality

combined static descriptor equality
  !=
formation support reconstruction

combined static descriptor equality
  !=
typed property support reconstruction
~~~

The source identifies:

~~~text
support-retaining data
exact kernel criteria
injectivity conditions
cross-coordinate reconstruction requirements
~~~

as the structures needed to state what aggregation discards and when reconstruction is possible.

Reconstruction consequence:

~~~text
EQUAL_AGGREGATE
  !=
UNIQUE_SOURCE_RECONSTRUCTION

NONINJECTIVE_FORWARD_OR_AGGREGATION_MAP
  =>
retain multiple compatible preimages when they exist

INJECTIVITY_ON_DECLARED_CLASS
  may support class-bounded uniqueness

COORDINATEWISE_RECOVERY
  does not automatically establish joint / relational recovery
~~~

### S4 — Structural Reorganization Dynamics

Source:

~~~text
DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf
Sections 4, 14, 16
~~~

Recovered lineage and transition constraints:

~~~text
channel-lineage and component-lineage
  are explicit relation data

direct long-interval lineage
  need not be uniquely reconstructed from one intermediate slice

lineage-connected succession
  is distinct from literal equality of time slices

branching and merging
  are not excluded

unique successor / bijection / cardinality conservation
  require separate conditions
~~~

Recovered transition constraint:

~~~text
J_k : X_k^- => X_k^+

may be relation-valued

deterministic jump map
  is only a special case
~~~

Recovered readout constraint:

~~~text
reduced readout
  need not be a complete classifier

projection/readout equality
  need not imply underlying state equality

no converse reconstruction
  follows without injectivity or another reconstruction condition
~~~

Reconstruction consequence:

~~~text
TRANSITION_COMPATIBILITY
  !=
UNIQUE_PREDECESSOR_HISTORY

LINEAGE_COMPATIBILITY
  !=
COMPLETE_HISTORY_RECONSTRUCTION

PROJECTED_EQUALITY
  !=
SOURCE_STATE_EQUALITY

BRANCHING_OR_MERGING
  must remain visible unless separately excluded
~~~

### S5 — Tracking / DSD 추적론

Project-internal predecessor:

~~~text
methods/09_provenance_lineage/provenance/PROTOCOL_v0.1.md
blob:
  72e9cc8576ae87e088bdf2f8ebb3d7016c2894c1
~~~

Tracking records evidence-bounded typed trace relations and explicitly preserves:

~~~text
MISSING_TRACE_LINK != LICENSE_TO_RECONSTRUCT
RECONSTRUCTED_LINK != ESTABLISHED_TRACE_LINK
TRACE_OF_AGGREGATE != RECONSTRUCTION_OF_SUPPORT
~~~

A Reconstruction handoff is retained in a reconstructed/inferred-link sidecar and does not become an established trace relation without separate evidence.

Reconstruction consequence:

~~~text
TRACKING_GAP
  may define a reconstruction target

but

RECONSTRUCTED_CANDIDATE_LINK
  !=
ESTABLISHED_TRACE_LINK
~~~

Tracking provenance can constrain candidate histories, but Reconstruction may not rewrite inferred links as observed trace facts.

### S6 — Lineage / DSD 계보론

Project-internal predecessor:

~~~text
methods/09_provenance_lineage/lineage/PROTOCOL_v0.1.md
blob:
  0ef686f3987b590e67e07b9ee5e4861c31e6e1ef
~~~

Lineage determines evidence-bounded predecessor/successor identity across change and explicitly preserves:

~~~text
TRACKING_TRACE != LINEAGE_DECISION
RECONSTRUCTION_CANDIDATE != ESTABLISHED_LINEAGE
TRANSFORMATION_MAPPING != SUCCESSOR_IDENTITY
AGGREGATE_READOUT != LINEAGE_IDENTITY
~~~

Reconstruction consequence:

~~~text
a candidate hidden or past relation
  may remain admissible as a reconstruction hypothesis

but

candidate reconstruction
  cannot be promoted to established lineage identity
  unless the Lineage interface separately licenses that claim
~~~

### S7 — Compression / DSD 압축론

Project-internal predecessor:

~~~text
methods/10_aggregation_compression/compression/PROTOCOL_v0.1.md
blob:
  4d67d800e107229f91c16cf5b0235928124482b2
~~~

Compression explicitly separates:

~~~text
PURPOSE_SAFE_COLLISION
  !=
RECONSTRUCTION_SAFE_COLLISION

LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY

COORDINATEWISE_RECONSTRUCTION
  !=
RELATIONAL_OR_FULL_SOURCE_RECONSTRUCTION

RECONSTRUCTION_CANDIDATE
  !=
COMPRESSION_LOSSLESSNESS

TRACKING_PROVENANCE
  !=
SOURCE_RECONSTRUCTION
~~~

Compression also freezes reconstruction scope and the availability of required cross-coordinate / relational conditions.

Reconstruction consequence:

~~~text
the reconstruction target class and reconstruction scope
must be explicit

compression-side losslessness is inherited only
at the exact frozen class/scope it establishes

required unavailable sidecar / relation
  !=
evidence that the source is impossible to reconstruct

known destructive information loss
  !=
mere interface unavailability
~~~

### S8 — Aggregation / DSD 집계론

Project-internal predecessor:

~~~text
methods/10_aggregation_compression/aggregation/PROTOCOL_v0.1.md
blob:
  5ac926aa40594126b42dac99762ff33fe87450f1
~~~

Aggregation outputs explicit collision/injectivity and reconstruction-scope sidecars when claimed.

The method boundary remains:

~~~text
AGGREGATION
  executes a declared many-to-one or summary operation

RECONSTRUCTION
  reasons backward over admissible source candidates

AGGREGATION_RESULT
  !=
RECONSTRUCTION_RESULT
~~~

Reconstruction may consume the frozen aggregate map, support sidecars, collision witnesses, and injectivity records without treating the forward aggregation operation itself as a reconstruction.

### S9 — Diagnosis / DSD 진단론 boundary

Project-internal predecessor:

~~~text
methods/15_diagnosis_reconstruction/diagnosis/PROTOCOL_v0.1.md
blob:
  7bf9ab2dbb2ae990b2b0a0c09209ec28aa0f1129
~~~

Registry boundary:

~~~text
DIAGNOSIS:
  current hidden state
  failure mode
  cause hypothesis
  current structural condition

RECONSTRUCTION:
  prior
  omitted
  damaged
  compressed
  otherwise hidden structures
  and histories
~~~

Required separation:

~~~text
CURRENT_STATE_DIAGNOSIS
  !=
PAST_HISTORY_RECONSTRUCTION

DIAGNOSIS_COMPATIBILITY
  !=
HISTORICAL_TRUTH

RECONSTRUCTION_RESULT
  !=
CURRENT_CAUSE_CERTAINTY
~~~

### S10 — DSD interface / shared-core discipline

Current interface profile:

~~~text
methodology/DSD_INTERFACE_PROFILE.md
blob:
  3d5550826e7e39822c07873352e300f7958103a9
~~~

Recovered rule:

~~~text
a reconstruction claim requires
a theorem or explicit condition appropriate
to the selected admissible data class
~~~

The current shared core also requires:

~~~text
SC-01  preserve claim-relevant DSD status/type distinctions
SC-02  lock source/interface/version semantics
SC-03  make claim-relevant mappings explicit
SC-04  avoid optional-interface overconstraint
SC-05  respect information-loss and reconstruction limits
SC-06  separate regular evolution, transition, and lineage
SC-07  separate evidence applicability from case origin
SC-08  preserve failure / NO_GAIN / precommit integrity
SC-09  separate evidence/audit status from object/model status
SC-10  separate external-domain standards from DSD-internal success
~~~

These are constraints on Reconstruction construction, not direct validation of Reconstruction as a method.

## 3. Source-derived Reconstruction constraints

The following are recovered constraints rather than new Reconstruction theorems.

~~~text
RR-01
  preserve claim-relevant Formation / Property typed statuses

RR-02
  preserve source identity, typed input, support, provenance,
  lineage, and sidecar data when the reconstruction claim depends on them

RR-03
  equal aggregate / projection / readout does not imply equal source

RR-04
  a uniqueness claim must name its admissible reconstruction class and scope

RR-05
  injectivity established only on a declared class
  does not become global injectivity

RR-06
  coordinatewise recoverability does not imply
  relational / joint / full-source recoverability

RR-07
  transition and lineage relations may branch or merge;
  deterministic uniqueness is not assumed

RR-08
  a reconstructed trace link is not an established Tracking relation

RR-09
  a reconstructed predecessor/successor candidate is not
  an established Lineage identity

RR-10
  Formation witness history / stage order does not automatically become
  actual temporal history

RR-11
  definitional recompletion from a fully supplied primitive core
  is distinct from evidence-based reconstruction of missing history

RR-12
  unavailable required reconstruction information
  must remain distinct from demonstrated destructive information loss

RR-13
  present-state Diagnosis and past/omitted Reconstruction remain separate tasks

RR-14
  if several source candidates remain compatible,
  multiplicity remains visible unless additional frozen evidence excludes them

RR-15
  no-admissible-candidate inside one declared reconstruction class
  does not by itself prove that no real prior source/history existed
~~~

## 4. Working atomic task — not yet frozen

The current working formulation is:

~~~text
Given:
  a declared reconstruction question,
  a declared prior / omitted / damaged / compressed source class,
  available present evidence,
  frozen forward / aggregation / compression / transition maps where relevant,
  typed status / support / provenance records,
  Tracking and Lineage handoffs where supplied,
  declared information-loss / collision / injectivity records,
  and claim-relevant temporal / regime / resolution / relational scope,

determine:
  which source structures or histories remain admissible,
  which are excluded,
  which cannot yet be evaluated,
  which information is provably unrecoverable under the frozen interface,
  whether uniqueness holds within the declared class and scope,
  and what additional evidence or sidecars would discriminate remaining candidates.
~~~

This formulation is **prospective methodological construction**, not a theorem supplied by the predecessor papers.

It remains open to direct boundary attack before protocol freeze.

## 5. Candidate information classes for the future Task Interface

Not yet frozen:

~~~text
RECONSTRUCTION_TASK_ID
TASK_VERSION
RECONSTRUCTION_QUESTION
RECONSTRUCTION_TARGET_KIND

SOURCE_CLASS_ID
SOURCE_CLASS_VERSION
SOURCE_CLASS_COMPLETENESS_CLAIM

AVAILABLE_EVIDENCE_SET
EVIDENCE_PROVENANCE
EVIDENCE_STATUS
EVIDENCE_TIME_OR_REGIME

FORWARD_MAP_ID
FORWARD_MAP_VERSION
FORWARD_MAP_SCOPE

AGGREGATION_HANDOFF
COMPRESSION_HANDOFF
COLLISION_OR_FIBER_RECORD
KERNEL_RECORD_IF_LINEAR
INJECTIVITY_SCOPE

SUPPORT_RETENTION_SIDECAR
PROPERTY_STATUS_SIDECAR
FORMATION_STATUS_SIDECAR

TRACKING_HANDOFF
LINEAGE_HANDOFF
TRANSITION_RELATION_HANDOFF

TEMPORAL_SCOPE
HISTORY_SCOPE
REGIME_SCOPE
RESOLUTION_SCOPE

RECONSTRUCTION_SCOPE_CLASS
CROSS_COORDINATE_OR_RELATIONAL_CONDITION

CANDIDATE_RECONSTRUCTION_SET
EXCLUSION_RECORD
BLOCKED_OR_UNAVAILABLE_RECORD
UNRECOVERABLE_INFORMATION_RECORD

UNIQUENESS_SCOPE
ADDITIONAL_EVIDENCE_HANDOFF
MAXIMUM_SUPPORTED_CLAIM
~~~

These are recovery candidates only.

They do not yet constitute a required task record.

## 6. Prospective guards to pressure before freezing

Not yet protocol rules:

~~~text
EQUAL_OUTPUT
  !=
EQUAL_SOURCE

FORMATION_WITNESS_HISTORY
  !=
ACTUAL_TEMPORAL_HISTORY

STAGE_DEPENDENCY_ORDER
  !=
PHYSICAL_TIME_ORDER

LOSSLESS_ON_DECLARED_CLASS
  !=
GLOBAL_INJECTIVITY

COORDINATEWISE_RECOVERY
  !=
RELATIONAL_OR_FULL_SOURCE_RECOVERY

TRANSITION_COMPATIBILITY
  !=
UNIQUE_PREDECESSOR_HISTORY

RECONSTRUCTION_CANDIDATE
  !=
ESTABLISHED_TRACE_LINK

RECONSTRUCTION_CANDIDATE
  !=
ESTABLISHED_LINEAGE

DEFINITIONAL_RECOMPLETION
  !=
EVIDENCE_BASED_RECONSTRUCTION

MISSING_REQUIRED_RECONSTRUCTION_INFORMATION
  !=
NEGATIVE_EVIDENCE

UNAVAILABLE_REQUIRED_INTERFACE
  !=
DEMONSTRATED_UNRECOVERABILITY

SINGLE_REMAINING_DECLARED_RECONSTRUCTION
  !=
GLOBAL_HISTORICAL_TRUTH

NO_ADMISSIBLE_DECLARED_RECONSTRUCTION
  !=
NO_REAL_PAST_STATE_OR_HISTORY

CURRENT_STATE_DIAGNOSIS
  !=
PAST_OR_OMITTED_RECONSTRUCTION
~~~

## 7. Initial neighboring-method pressure map

The first Task Interface / boundary phase should directly pressure at least:

~~~text
Tracking
  observed / supported trace
  vs inferred missing-link reconstruction

Lineage
  established successor identity
  vs candidate predecessor/successor reconstruction

Diagnosis
  current hidden state
  vs prior / omitted / damaged / historical structure

Aggregation
  forward summary
  vs inverse admissible-source inference

Compression
  purpose-bounded reduction / losslessness scope
  vs actual source reconstruction

Transformation
  declared source-target map
  vs inference of an unobserved source

Measurement
  evidence discrimination
  vs source/history reconstruction

Comparison
  similarity / difference
  vs reconstruction compatibility

Audit
  conformance verdict
  vs reconstruction result
~~~

Additional neighboring pairs may be added during boundary attack if the Task Interface exposes further collision risk.

## 8. Current recovery state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  not established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

DEDICATED_RECONSTRUCTION_PROTOCOL:
  not established

RECONSTRUCTION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_RECONSTRUCTION_EVIDENCE_STATUS:
  source_and_registry_recovery_complete

EXTERNAL_RECONSTRUCTION_APPLICATIONS:
  0

INDEPENDENT_RECONSTRUCTION_VALIDATION:
  not established

PROTOCOL_REVISION_REQUIRED:
  not applicable before protocol

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## 9. Next

Create the Reconstruction planning/worklog lane and draft Task Interface v0.1 from this recovery artifact.

Do not freeze a Reconstruction protocol before direct boundary attack.
