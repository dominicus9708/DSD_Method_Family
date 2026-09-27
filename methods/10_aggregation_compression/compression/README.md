# DSD Compression / DSD 압축론

Status: **source/registry recovery complete / Task Interface v0.1 draft established / pre-protocol boundary attack next**
Legacy path ID: `10B`
Higher field: **V. Reduction & Representation / 축약·표현**

## Internal-standardization files

- [`PLANNING.md`](PLANNING.md)
- [`WORKLOG.md`](WORKLOG.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)

## Atomic task

Reduce representation size, resolution, or retained coordinate detail relative to a declared downstream purpose while preserving every distinction and sidecar that the frozen purpose requires to remain available.

Compression quality is not identified with smaller output.

## Recovered DSD source basis

### Property Axiom System §9

A finite property summary can collide across strictly non-isomorphic property structures because cross-property correlations among typed inputs are forgotten.

~~~text
SUMMARY_EQUALITY != STRICT_PROPERTY_EQUIVALENCE
~~~

### Channel-Indexed Static Aggregation §11

Reduced aggregation can discard support decomposition and typed-property distinctions.

Exact reconstruction requires injectivity on the declared class plus any required cross-coordinate reconstruction conditions.

~~~text
REDUCED_OUTPUT != SUPPORT_RETAINING_DESCRIPTOR
AGGREGATE_EQUALITY != SOURCE_EQUALITY
~~~

### Structural Reorganization Dynamics §§15–16

A descriptive projection may be non-injective.

Equal projected states define a coarser descriptive equivalence; erased source differences are latent distinctions relative to that projection.

A reduced readout need not be a complete classifier.

~~~text
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
REDUCED_READOUT != COMPLETE_CLASSIFIER
NO_CONVERSE_RECONSTRUCTION_WITHOUT_EXTRA_CONDITION
~~~

## Prospective Compression interface

The draft freezes:

~~~text
downstream purpose
source class and source representation
compression map
reduced output type
required distinctions
acceptable collision relation
status/support/provenance sidecars
resolution/threshold when relevant
reconstruction scope and prerequisites
static/dynamic scope
maximum-supported claim
~~~

For a simple required-distinction relation:

~~~text
(x,y) required to remain distinguishable
  =>
C(x) != C(y)
~~~

This is a prospective method-interface rule derived from the recovered source constraints, not a theorem attributed to the predecessor papers.

## Core boundaries

~~~text
SMALLER_REPRESENTATION != BETTER_REPRESENTATION
COMPRESSION_RATIO != COMPRESSION_VALIDITY

SUMMARY_EQUALITY != STRICT_STRUCTURE_EQUIVALENCE
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY

LOSSY != FAILURE_BY_DEFAULT
PURPOSE_SAFE_COLLISION != UNIVERSALLY_SAFE_COLLISION

LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY

DEFINED_ZERO != ABSENCE
UNDEFINED != ZERO

REDUCED_READOUT != COMPLETE_CLASSIFIER

COMPRESSION != AGGREGATION
COMPRESSION != TRANSFORMATION
COMPRESSION != RECONSTRUCTION
COMPRESSION != CLASSIFICATION
~~~

## Current counters

~~~text
TASK_INTERFACE_DRAFT:
  v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

BOUNDARY_AMENDMENT:
  not established

DEDICATED_COMPRESSION_PROTOCOL:
  not established

DIRECT_COMPRESSION_PILOTS_ATTEMPTED:
  0

SUCCESSFUL_DIRECT_COMPRESSION_PILOTS:
  0

BASELINE_COMPRESSION_CASES:
  0

NO_GAIN_COMPRESSION_CASES:
  0

REPRODUCIBILITY_CASES:
  0

EXTERNAL_COMPRESSION_APPLICATIONS:
  0

INDEPENDENT_COMPRESSION_VALIDATION:
  not established

INDEPENDENT_REPLICATION:
  not established

COMPRESSION_INTERNAL_STANDARDIZATION_STATUS:
  developing

CURRENT_COMPRESSION_EVIDENCE_STATUS:
  source_and_interface_recovery

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## Next

Run the pre-protocol boundary attack against Task Interface v0.1 before freezing an executable Compression Protocol.
