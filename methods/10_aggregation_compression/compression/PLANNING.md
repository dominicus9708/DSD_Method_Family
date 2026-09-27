# DSD Compression Planning / DSD 압축론 기획

Status: **source/registry recovery complete / Task Interface v0.1 draft established / pre-protocol boundary attack next**
Date opened: **2026-09-27**
Legacy path ID: 10B
Path: methods/10_aggregation_compression/compression/
Higher field: **V. Reduction & Representation / 축약·표현**

## Purpose / 목적

Develop DSD Compression as the atomic method for reducing representation size, resolution, or retained coordinate detail relative to an explicitly declared downstream purpose while preserving every distinction that the task says must remain distinguishable.

Compression quality is not identified with smaller output.

The core question is:

~~~text
which source distinctions may collapse
which source distinctions must not collapse
what side information must remain
what reconstruction claims survive the reduction
at what declared resolution the claim is evaluated
~~~

## Source-derived scope lock

The current source basis does not contain a dedicated Compression Protocol.

Instead, Compression is reconstructed prospectively from constraints already present across the Property, Static Aggregation, and Dynamics layers.

### Property Axiom System

Section 9 exhibits a finite-summary collision.

Two property-finite models can have the same simple summary while remaining strictly non-isomorphic because cross-property correlations among typed input locations were forgotten.

The source warns that richer summaries can fail similarly unless a separate reconstruction theorem proves injectivity on the selected model class.

Therefore:

~~~text
SUMMARY_EQUALITY != STRICT_PROPERTY_EQUIVALENCE
SMALLER_SUMMARY != SUFFICIENT_CLASSIFIER
FORGOTTEN_CORRELATION != IRRELEVANT_CORRELATION
~~~

### Channel-Indexed Static Aggregation

Section 11 separates reduced aggregate values from support-retaining data.

Channel summation discards decomposition unless the summation map is injective on the chosen admissible data class.

Typed-property aggregation can lose selected support, property kind, typed input coordinates, cross-property correlations, and negative-status distinctions not carried into the defined-record set.

Combined reconstruction requires injectivity in both coordinates plus any required cross-coordinate reconstruction condition.

Therefore:

~~~text
REDUCED_OUTPUT != SUPPORT_RETAINING_DESCRIPTOR
AGGREGATE_EQUALITY != SOURCE_EQUALITY
FIXED_CLASS_INJECTIVITY != UNQUALIFIED_RECONSTRUCTION
~~~

### Structural Reorganization Dynamics

Section 15 defines a descriptive projection as an arbitrary declared map from admissible structural states to retained states and does not assume injectivity.

Equality after projection defines a coarser descriptive equivalence; distinct source states with equal projection are latent structural distinctions relative to that projection.

No converse reconstruction is available without injectivity or another reconstruction condition.

Section 16 treats reduced readouts as declared maps evaluated after the component-resolved state is specified and states that a readout need not be a complete classifier.

Therefore:

~~~text
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
LATENT_DISTINCTION = SOURCE_DIFFERENCE_ERASED_BY_DECLARED_PROJECTION
REDUCED_READOUT != COMPLETE_CLASSIFIER
NO_CONVERSE_RECONSTRUCTION_WITHOUT_EXTRA_CONDITION
~~~

## Compression method boundary

Compression may use aggregation, projection, coarse-graining, quantization, coordinate removal, summary statistics, support sidecars, status sidecars, and resolution thresholds as implementation mechanisms.

These mechanisms do not define the method.

Compression is identified by the task contract:

~~~text
declared downstream purpose
+
declared source representation
+
declared reduced representation
+
declared retained distinctions
+
declared acceptable collisions
+
declared reconstruction requirements
+
declared resolution/scope
~~~

## Initial compression validity idea

For a frozen source class X_task, reduction map C, and required-distinction relation D_req:

~~~text
for every (x,y) in D_req:
  C(x) != C(y)
~~~

Equivalently, every collision fiber of C must stay inside an equivalence class the task has declared safe to merge.

This is a prospective method-interface formulation, not a theorem claimed by the source papers.

The pre-protocol boundary attack must test whether it is sufficient or over-restrictive.

## Project sequencing

~~~text
source and registry recovery
-> Task Interface v0.1 draft
-> pre-protocol boundary attack
-> Boundary Amendment if required
-> executable Protocol
-> positive / negative / boundary challenges
-> competent baseline
-> strongest-reasonable baseline
-> deterministic same-project retrace
-> frozen-axis internal-standardization audit
-> external validation later
~~~

## Current sequence

1. ✅ Registry recovery.
2. ✅ Source recovery — Property §9, Static Aggregation §11, Dynamics §§15–16.
3. ✅ Task Interface v0.1 draft established prospectively.
4. ⏸ Pre-protocol boundary attack.
5. ⏸ Boundary Amendment if required.
6. ⏸ Executable Compression Protocol.
7. ⏸ Positive / negative / boundary challenges.
8. ⏸ Competent and strongest-reasonable baselines.
9. ⏸ Deterministic same-project retrace.
10. ⏸ Frozen-axis internal-standardization audit.
11. ⏸ External applications / independent validation.

## Initial counters

~~~text
TASK_INTERFACE_DRAFT: v0.1 established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 0
BOUNDARY_AMENDMENT: not established
DEDICATED_COMPRESSION_PROTOCOL: not established
DIRECT_COMPRESSION_PILOTS_ATTEMPTED: 0
SUCCESSFUL_DIRECT_COMPRESSION_PILOTS: 0
BASELINE_COMPRESSION_CASES: 0
NO_GAIN_COMPRESSION_CASES: 0
REPRODUCIBILITY_CASES: 0
EXTERNAL_COMPRESSION_APPLICATIONS: 0
INDEPENDENT_COMPRESSION_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
COMPRESSION_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_COMPRESSION_EVIDENCE_STATUS: source_and_interface_recovery
PROTOCOL_REVISION_REQUIRED: not applicable
SHARED_CORE_REOPEN_REQUIRED: no
~~~

## Next

Run the pre-protocol Compression boundary attack against the Task Interface v0.1 draft before freezing an executable protocol.
