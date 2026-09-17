# INT-RTR-001 Precommit / DSD Interpretation Deterministic Same-Project Retrace

Status: **PRECOMMITTED BEFORE RETRACE EXECUTION**  
Date: **2026-09-17**  
Method: **DSD Interpretation / DSD 해석론**

## 1. Retrace identity

```text
CASE_ID: INT-RTR-001
CASE_CLASS: deterministic_same_project_retrace
CASE_ORIGIN: same_project_frozen_artifact_retrace
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
INDEPENDENT_REPLICATION: no
SELECTED_PRIOR_CASE: INT-CH-006
```

Purpose: determine whether the frozen Interpretation protocol and frozen `INT-CH-006` task records are sufficient to reconstruct the prior result deterministically without changing protocol, task, source, witness/version, transformation, reconstruction handoff, context, bridge, reading policy, claim-strength rule, or verdict semantics.

A pass establishes only same-project deterministic retraceability for the selected frozen case. It does not establish independent replication, external validity, domain correctness, or practical superiority.

## 2. Immutable artifact lock

```text
INTERPRETATION_PROTOCOL_VERSION: v0.1
PROTOCOL_COMMIT: 40110a8a779f0ac6ff93ede6414544b8ec548fdf
PROTOCOL_BLOB: dc3c3a46ba170b3b7565a59a7113c473fb02b463

SOURCE_PRECOMMIT_CASE: INT-CH-006
SOURCE_PRECOMMIT_COMMIT: fca5d6a9a8c4c3ca8a890ad1c028225868e3fa84
SOURCE_PRECOMMIT_BLOB: da1b2218acccd15063326382f92faa561f6b4edf

FROZEN_REFERENCE_RESULT: INT-CH-006 strongest-reasonable-baseline result
REFERENCE_RESULT_COMMIT: cc7a12c9c3098813701841cab20dd7a630c2f5ff
REFERENCE_RESULT_BLOB: 819af91ccf79f46cec18e82ca4b7a0196bd4dcb3
```

The reference result is locked for post-reconstruction comparison only. The retrace record must reconstruct the required result fields from the frozen protocol + source precommit task record, then compare the reconstructed record with the frozen result artifact.

## 3. Frozen retrace inputs

The retrace may use only the following claim-relevant records already frozen for `INT-CH-006`:

```text
R1 witness/version conflict records
R2 normalization/transformation mapping records
R3 reconstruction-handoff records
R4 time-indexed context records
R5 claim-strength / obligation records
candidate-reading sets
ambiguity/conflict policy
witness precedence policy
transformation precedence policy
context temporal scope
bridge records
claim-strength rules
baseline B1 capability record
G1-G7 gain criteria
precommitted scoring and terminal rules
Interpretation Protocol v0.1 validity/operation semantics
```

No external corpus, new bridge, new witness priority, new context, new normalization rule, new reconstruction candidate, or new domain assumption may be introduced.

## 4. Frozen reconstruction targets

The retrace must independently reconstruct, from the locked protocol/task records, the following target fields before comparison to the reference result:

```text
R1 terminal status and witness-precedence/harmonization disposition
R2 support status of R2A/R2B/R2C, claim-strength, terminal status
R3 support status of R3A/R3B/R3C/R3D, observed/reconstructed provenance distinction, terminal status
R4 support status of R4A/R4B/R4C, temporal-context disposition, terminal status
R5 support status of R5A/R5B/R5C/R5D, claim-strength disposition, terminal status
all five Protocol-v0.1 conformance statuses
B1 matched/not-matched disposition for R1-R5
G1-G7 comparative gain statuses
final INTERPRETATION_METHOD_GAIN_STATUS
STRONGEST_REASONABLE_BASELINE_INTERPRETATION status
protocol/shared-core pressure disposition
```

## 5. Expected deterministic semantics locked by the source task

The source precommit already fixes the task semantics. The retrace therefore must obtain:

```text
R1 -> witness-conditioned plurality / INTERPRETATION_RESOLVED_MULTI
R2 -> two mapping-conditioned readings / INTERPRETATION_RESOLVED_MULTI
R3 -> two reconstruction-conditioned candidates, no observed-source promotion / INTERPRETATION_RESOLVED_MULTI
R4 -> t0 HAZARD + t1 ALL_CLEAR, no semantic identity from wording / INTERPRETATION_RESOLVED_MULTI
R5 -> obligation supported, factual/causal/predictive upgrades unsupported / INTERPRETATION_RESOLVED_SINGLE
```

This expected structure comes from the frozen task record and is not a post-hoc modification.

## 6. Determinism criteria

A retrace is deterministic only if all of the following hold:

```text
D1 identical protocol version/commit/blob is used
D2 identical source-precommit commit/blob is used
D3 no claim-relevant input is added, removed, or reinterpreted
D4 no hidden precedence/harmonization is introduced
D5 no transformation mapping is silently selected or discarded
D6 reconstruction handoff remains distinct from observed source
D7 time-indexed contexts remain scoped to their frozen times
D8 obligation remains distinct from occurrence/prediction/causation
D9 reconstructed support/terminal fields equal the frozen reference result fields
D10 reconstructed comparative-gain fields equal the frozen reference result fields
D11 protocol/shared-core pressure disposition equals the frozen reference result
D12 no reference-result field is copied as an unexplained substitute for reconstruction
```

## 7. Frozen scoring

```text
A. artifact identity and freeze discipline       10
B. DSD result reconstruction                    20
C. B1/gain reconstruction                       12
D. exact reference-result correspondence        12
E. scope and reproducibility discipline          6
TOTAL                                           60
```

Detailed check lock:

```text
A1 protocol commit fixed
A2 protocol blob fixed
A3 source-precommit commit fixed
A4 source-precommit blob fixed
A5 reference-result commit fixed
A6 reference-result blob fixed
A7 selected prior case fixed to INT-CH-006
A8 no external material
A9 independent replication explicitly false
A10 no post-freeze claim-relevant modification

B1 R1 terminal exact
B2 R1 no hidden precedence/harmonization
B3 R2 R2A support exact
B4 R2 R2B support exact
B5 R2 R2C support exact
B6 R2 terminal exact
B7 R3 R3A/R3B support exact
B8 R3 R3C/R3D support exact
B9 R3 observed/reconstructed provenance exact
B10 R3 terminal exact
B11 R4 R4A/R4B support exact
B12 R4 R4C support exact
B13 R4 temporal-scope disposition exact
B14 R4 terminal exact
B15 R5 R5A support/claim-strength exact
B16 R5 R5B support exact
B17 R5 R5C support exact
B18 R5 R5D support exact
B19 R5 terminal exact
B20 all five protocol-conformance statuses exact

C1-C5 B1 task-level result matches for R1-R5
C6 G1 exact
C7 G2 exact
C8 G3 exact
C9 G4 exact
C10 G5 exact
C11 G6 exact
C12 G7 + final NO_GAIN/strongest-baseline status exact

D1 R1 reconstructed record corresponds to reference
D2 R2 reconstructed record corresponds to reference
D3 R3 reconstructed record corresponds to reference
D4 R4 reconstructed record corresponds to reference
D5 R5 reconstructed record corresponds to reference
D6 conformance ledger corresponds
D7 task-level DSD/B1 comparison corresponds
D8 G1-G7 gain ledger corresponds
D9 final NO_GAIN corresponds
D10 strongest-reasonable-baseline status corresponds
D11 PROTOCOL_REVISION_REQUIRED corresponds
D12 SHARED_CORE_REOPEN_REQUIRED corresponds

E1 RETRACE_STATUS explicitly recorded
E2 same-project retrace not called independent replication
E3 no external-applicability claim
E4 no maturity promotion from retrace alone
E5 REPRODUCIBILITY_CASES may increment by exactly +1 only on 60/60 PASS
E6 external validation remains deferred
```

Decision:

```text
60/60 -> RETRACE_VERDICT: PASS
otherwise -> RETRACE_VERDICT: FAIL
```

Any failure is preserved. The retrace may not be repaired in place by changing the frozen source task or protocol.

## 8. Counter lock

Before retrace:

```text
DIRECT_INTERPRETATION_PILOTS_ATTEMPTED: 6
SUCCESSFUL_DIRECT_INTERPRETATION_PILOTS: 5
BASELINE_INTERPRETATION_CASES: 2
NO_GAIN_INTERPRETATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_INTERPRETATION: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 0
EXTERNAL_INTERPRETATION_APPLICATIONS: 0
INDEPENDENT_INTERPRETATION_VALIDATION: not established
INTERPRETATION_METHOD_MATURITY_CLASSIFICATION: developing
```

A 60/60 PASS may change only:

```text
REPRODUCIBILITY_CASES: 0 -> 1
```

It does not increment direct pilots, baseline cases, NO_GAIN cases, external applications, or independent validation.

## 9. Next if passed

Proceed to the frozen-axis internal maturity/standardization audit. External validation remains deferred until the internal standardization sequence is complete.
