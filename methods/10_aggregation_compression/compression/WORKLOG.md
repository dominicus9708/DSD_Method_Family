# DSD Compression Worklog / DSD 압축론 작업 기록

Status: **active**
Opened: **2026-09-27**
Path: methods/10_aggregation_compression/compression/

## Step 1 — Internal-build front opened

Aggregation completed AGG-AUD-001 and was promoted to project-internal standard status.

The family-wide internal-build front therefore moved to Compression / DSD 압축론.

Existing state before this step:

~~~text
GitHub:
  compression/README.md only

Notion:
  canonical DSD 압축론 page exists
  short purpose / questions / boundary only

Dedicated PLANNING:
  absent

Dedicated WORKLOG:
  absent

Dedicated executable protocol:
  absent
~~~

## Step 2 — Source and registry recovery

Canonical method identity retained:

~~~text
Method:
  Compression / DSD 압축론

Higher field:
  V. Reduction & Representation / 축약·표현

Legacy path:
  methods/10_aggregation_compression/compression/

Independent method:
  yes

Legacy umbrella:
  10. DSD 집계·압축론
  compatibility/navigation only
~~~

Recovered source constraints:

~~~text
Property §9:
  finite summaries can collide while strict property structure differs;
  forgotten cross-property correlations matter.

Static Aggregation §11:
  reduced aggregates can lose support and decomposition;
  exact reconstruction requires injectivity on the declared class;
  combined reconstruction may require cross-coordinate conditions.

Dynamics §15:
  descriptive projection may be non-injective;
  equal projection defines coarser descriptive equivalence;
  source differences erased by projection are latent distinctions;
  converse reconstruction is unavailable without extra conditions.

Dynamics §16:
  reduced readout need not be a complete classifier.
~~~

Initial boundary lock:

~~~text
SMALLER_REPRESENTATION != BETTER_REPRESENTATION
REDUCED_OUTPUT != SOURCE_IDENTITY
SUMMARY_EQUALITY != STRICT_STRUCTURE_EQUIVALENCE
PROJECTED_EQUALITY != COMPLETE_STATE_EQUALITY
LOSSY_COLLISION != AUTOMATIC_FAILURE
LOSSLESS_ON_DECLARED_CLASS != GLOBAL_INJECTIVITY
PURPOSE_SAFE_COLLISION != UNIVERSALLY_SAFE_COLLISION
COMPRESSION != AGGREGATION
COMPRESSION != TRANSFORMATION
COMPRESSION != RECONSTRUCTION
~~~

## Step 3 — Task Interface v0.1 draft

Created:

~~~text
methods/10_aggregation_compression/compression/TASK_INTERFACE_v0.1-draft.md
~~~

The draft freezes purpose, source class, reduced representation, compression map, required distinctions, acceptable collisions, resolution, sidecar policy, reconstruction scope, and maximum-supported claim before evaluation.

Prospective compression condition:

~~~text
for every pair that the frozen purpose requires to remain distinguishable:
  their compressed outputs must remain distinguishable
~~~

This is a method-interface construction derived from the source constraints.

It is not attributed to the source papers as an existing theorem.

## Current counters

~~~text
TASK_INTERFACE_DRAFT: v0.1 established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 0
DEDICATED_COMPRESSION_PROTOCOL: not established
DIRECT_COMPRESSION_PILOTS_ATTEMPTED: 0
BASELINE_COMPRESSION_CASES: 0
REPRODUCIBILITY_CASES: 0
COMPRESSION_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_COMPRESSION_EVIDENCE_STATUS: source_and_interface_recovery
SHARED_CORE_REOPEN_REQUIRED: no
~~~

## Next

Run the pre-protocol boundary attack against the Compression Task Interface v0.1 draft.
