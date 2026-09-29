# DSD Diagnosis / DSD 진단론

Status: **source/registry recovery complete / Task Interface v0.1 draft established / pre-protocol boundary attack next**
Legacy path ID: `15A`
Higher field: **VI. Inverse Inference & Reconstruction / 역추론·복원**

Task: infer which current hidden states, failure modes, causes, or structural conditions remain compatible with present observations.

Primary DSD sources: Formation/Property status distinctions, measurement records, support-retaining descriptors, dynamic residuals and transition constraints.

Typical outputs:
- admissible current-state or cause set;
- evidence-to-candidate compatibility table;
- discriminating observations still required;
- unresolved/non-identifiable diagnosis classes;
- explicit separation of diagnosis from causal certainty.

Boundary: diagnosis concerns present hidden structure or cause hypotheses; it does not automatically reconstruct a unique past history.


## Development files

- [`SOURCE_REGISTRY_v0.1.md`](SOURCE_REGISTRY_v0.1.md)
- [`PLANNING.md`](PLANNING.md)
- [`WORKLOG.md`](WORKLOG.md)
- [`TASK_INTERFACE_v0.1-draft.md`](TASK_INTERFACE_v0.1-draft.md)

## Source / registry recovery

~~~text
SOURCE_REGISTRY_COMMIT:
  63ccc25d5bc8ddadadabfe698852d846e5671f15

SOURCE_REGISTRY_BLOB:
  1152759be5b56462156c83ecd3c508c73f1755f7

PLANNING_COMMIT:
  c320b49ad51d100cb1e42f939d4925d7a985558f

PLANNING_BLOB:
  138eba629cba3807a4a0e163e70c9383a58f49b9

WORKLOG_COMMIT:
  bbf71f71e06b2db2f265e58d0cacc42a1b66bc04

WORKLOG_BLOB:
  653659e0fbe72ec7418602ee091198bbf9e03f52

TASK_INTERFACE_COMMIT:
  e2c636eb0751878423a35d6848f7ef5a8fe81cc3

TASK_INTERFACE_BLOB:
  8cc12899c9b3f7a5f78d0e1893c5aa3a3824d444
~~~

Recovered source constraints come from Formation, Property, Channel-Indexed Static Aggregation, Structural Reorganization Dynamics, Measurement Protocol v0.1, and the existing Diagnosis/Reconstruction registry boundary.

Source-derived constraints are kept separate from prospective Diagnosis method construction.

## Current interface guards

~~~text
OBSERVATION_COMPATIBLE != TRUE_STATE_ESTABLISHED
SINGLE_REMAINING_DECLARED_CANDIDATE != GLOBAL_UNIQUE_DIAGNOSIS
NO_ADMISSIBLE_DECLARED_CANDIDATE != NO_REAL_STATE_EXISTS
DIAGNOSTIC_COMPATIBILITY != CAUSAL_PROOF
MEASUREMENT_SUFFICIENCY != DIAGNOSIS
EQUAL_READOUT != EQUAL_HIDDEN_STATE
NONINJECTIVE_FORWARD_MAP != LICENSE_TO_SELECT_ONE_PREIMAGE
MISSING_REQUIRED_EVIDENCE != NEGATIVE_EVIDENCE
CURRENT_STATE_DIAGNOSIS != PAST_HISTORY_RECONSTRUCTION
MULTIPLE_COMPATIBLE != TASK_UNDERDETERMINED
~~~

## Current evidence state

~~~text
SOURCE_REGISTRY_RECOVERY:
  complete

TASK_INTERFACE_DRAFT:
  v0.1 established

PRE_PROTOCOL_BOUNDARY_ATTACKS:
  0

BOUNDARY_AMENDMENT:
  not established

DEDICATED_DIAGNOSIS_PROTOCOL:
  not established

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
  source_and_interface_recovery

SHARED_CORE_REOPEN_REQUIRED:
  no
~~~

## Next

Treat Task Interface v0.1 as historical once the next step begins.

Execute a serious pre-protocol boundary attack before any Diagnosis Protocol freeze.
