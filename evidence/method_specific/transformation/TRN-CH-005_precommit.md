# TRN-CH-005 Precommit / DSD Transformation Strongest-Reasonable-Baseline Challenge

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-17**  
Method: **DSD Transformation / DSD 변환론**  
Protocol: **Transformation Protocol v0.1**  
Protocol commit at freeze: `b5e292ff89b1a2529a9f1fde98ad13d9af692e90`  
Protocol blob at freeze: `f78393c188c513acb30a10f1b180d598138cea61`

## 1. Case identity

```text
CASE_ID: TRN-CH-005
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_APPLICATION: no
BASELINE: B1_STRONG_TRANSFORMATION_LEDGER_ENGINE
```

Purpose: pressure DSD Transformation with a materially richer non-DSD baseline while giving both systems exactly the same claim-relevant source/target/map/version/domain/carrier/status/chain/stochastic/enrichment/reconstruction records.

A fair `NO_GAIN` is explicitly admissible. `NO_GAIN` is not method failure and does not establish merger, absorption, deletion, or permanent redundancy.

No external corpus, public standard, scientific dataset, legal record, historical source, or independent evaluator is used.

## 2. Strong baseline capability freeze

`B1_STRONG_TRANSFORMATION_LEDGER_ENGINE` is competent to:

```text
1 preserve source, target, map, schema, and version identities;
2 track every intermediate stage in composed transformation chains;
3 preserve intermediate collision/loss even when endpoint values later match;
4 apply version-scoped migration maps without retroactive reinterpretation;
5 execute supplied stochastic/choice policy with seed/support records;
6 distinguish target enrichment/default/addition from source-derived values;
7 separate claim-scoped reconstruction from full-source invertibility;
8 preserve missing/undefined/zero/out-of-scope distinctions where supplied;
9 retain terminal state, conformance, loss, reconstruction, and reversibility ledgers;
10 retain enough records for deterministic retrace of every frozen decision.
```

B1 need not use DSD terminology internally. Its outputs are mapped one-to-one to the frozen Transformation statuses for scoring. B1 may not be weakened after this precommit.

## 3. Frozen task family

Five stronger constructed subcases are frozen:

```text
R1 composed chain with irreversible intermediate merge followed by external re-enrichment
R2 schema-version / temporal migration with identical raw code but version-dependent meaning
R3 stochastic target choice with frozen policy and seed
R4 target enrichment provenance separated from source-derived transformation
R5 claim-scoped preservation/reconstruction despite full-source noninvertibility
```

## 4. R1 — composed chain / intermediate loss / endpoint coincidence

Source record:

```text
S1: x=2, y=3
SOURCE_SCHEMA: S1-v1
```

Stage A map:

```text
M1-A-v1: (x,y) -> z=x+y
TARGET_STAGE_A: A1-v1
```

Stage A therefore has a many-to-one merge over the declared integer-pair domain.

Stage B enrichment:

```text
E1: EXTERNAL_ENRICHMENT supplies x_ext=2
M1-B-v1: (z,x_ext) -> target(x'=x_ext, y'=z-x_ext)
```

For this fixture the endpoint is numerically `(2,3)`, matching the source values.

Frozen expected output for DSD and B1:

```text
STAGE_A_RELATION: MANY_TO_ONE_MERGE
STAGE_A_INJECTIVITY: noninjective on declared source domain
STAGE_A_INFORMATION_LOSS: x/y distinction lost in z alone
STAGE_B_x': TARGET_ADDED / EXTERNAL_ENRICHMENT-derived, not source-preserved
ENDPOINT_NUMERIC_MATCH: yes for fixture
INTERMEDIATE_LOSS_CLEARED_BY_ENDPOINT_MATCH: no
REVERSIBILITY_FROM_SOURCE_DERIVED_CHAIN_ALONE: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
TERMINAL -> TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
CONFORMANCE -> CONFORMANT
```

Preserved distinction:

```text
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
EXTERNAL_REENRICHMENT != SOURCE_INFORMATION_RECOVERY
```

## 5. R2 — schema-version / temporal migration

Two source records use the same raw code under different frozen schema versions:

```text
S2-t0 / schema V1: code=1 means READY
S2-t1 / schema V2: code=1 means HOLD
TEMPORAL_ORDER: t0 < t1
```

Version-scoped maps:

```text
M2-V1: V1 code=1 -> target state=READY
M2-V2: V2 code=1 -> target state=HOLD
TARGET_SCHEMA: U-v1
```

Frozen expected output for DSD and B1:

```text
S2-t0 -> state=READY / PRESERVED_UNDER_DECLARED_EQUIVALENCE
S2-t1 -> state=HOLD  / PRESERVED_UNDER_DECLARED_EQUIVALENCE
MAP_VERSION_SCOPE: preserved
VERSIONLESS_CODE_EQUIVALENCE: prohibited
RETROACTIVE_REINTERPRETATION: no
TERMINAL(t0) -> TRANSFORMATION_COMPLETED_PRESERVING
TERMINAL(t1) -> TRANSFORMATION_COMPLETED_PRESERVING
CONFORMANCE -> CONFORMANT
```

Preserved distinction:

```text
SAME_RAW_CODE != SAME_SEMANTICS_ACROSS_SCHEMA_VERSIONS
LATER_SCHEMA_MEANING != EARLIER_SCHEMA_MEANING
```

## 6. R3 — stochastic/choice semantics

Source:

```text
S3: record_id=K9, mode=A
```

Frozen transformation policy:

```text
P3-v1:
  preserve record_id and mode exactly
  add target route by Bernoulli choice over {R1,R2}
  P(R1)=0.5, P(R2)=0.5
  seed=17
  frozen realization under this fixture: R2
```

Target route has provenance:

```text
TARGET_ADDITION_ROLE: OTHER_EXPLICIT_ADDITION
ADDITION_PROVENANCE: P3-v1 stochastic choice
```

Frozen expected output for DSD and B1:

```text
record_id -> PRESERVED_EXACT
mode      -> PRESERVED_EXACT
route=R2  -> TARGET_ADDED_NOT_SOURCE_DERIVED
ALLOWED_OUTPUT_SUPPORT -> {R1,R2}
SEED_OR_REPLAY_RECORD -> 17
DETERMINISM_CLAIM -> stochastic, not deterministic
ONE_REALIZATION_DEFINES_FULL_MAP -> no
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
CONFORMANCE -> CONFORMANT
```

Preserved distinction:

```text
REALIZED_OUTPUT != FULL_STOCHASTIC_TRANSFORMATION_SEMANTICS
TARGET_ADDITION != SOURCE_DERIVABILITY
```

## 7. R4 — target enrichment provenance

Source:

```text
S4: id=7, temperature_c=20
```

Map and enrichment:

```text
M4-v1:
  id -> id exact
  temperature_c -> temperature_k using K=C+273.15

E4:
  target quality_label="verified"
  provenance=EXTERNAL_ENRICHMENT
```

Frozen expected output for DSD and B1:

```text
id -> PRESERVED_EXACT
temperature -> PRESERVED_UNDER_DECLARED_EQUIVALENCE
quality_label -> TARGET_ADDED_NOT_SOURCE_DERIVED / EXTERNAL_ENRICHMENT
QUALITY_LABEL_SOURCE_DERIVED: no
CLAIM_RELEVANT_INFORMATION_LOSS: none
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
CONFORMANCE -> CONFORMANT
```

Preserved distinction:

```text
TARGET_VALUE_EXISTENCE != SOURCE_DERIVABILITY
TARGET_ENRICHMENT != SOURCE_PRESERVATION
```

## 8. R5 — claim-scoped preservation and full-source noninvertibility

Source records range over:

```text
S5: payload in integers, nonce in arbitrary identifiers
```

Frozen fixture record:

```text
payload=42
nonce=N918
```

Map:

```text
M5-v1: (payload,nonce) -> target(payload)
```

Frozen scope:

```text
CLAIM_RELEVANT_CARRIERS: {payload}
NONCLAIM_CARRIER: nonce
TARGET_RESOLUTION: payload-preserving projection
FULL_SOURCE_INVERSE_CLAIM_SCOPE: full source record
CLAIM_SCOPED_RECONSTRUCTION_SCOPE: payload only
```

Frozen expected output for DSD and B1:

```text
payload -> PRESERVED_EXACT
nonce -> OUT_OF_SCOPE_FOR_TRANSFORMATION at claim resolution
CLAIM_SCOPED_RECONSTRUCTION(payload): exact
FULL_SOURCE_INJECTIVITY: no
FULL_SOURCE_REVERSIBILITY: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
GLOBAL_BIJECTIVITY_CLAIM: not made
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING at declared target resolution
CONFORMANCE -> CONFORMANT
```

Preserved distinction:

```text
LOSSLESS_RELATIVE_TO_DECLARED_CARRIERS != BIJECTIVE_ON_FULL_SOURCE_SPACE
CLAIM_SCOPED_RECONSTRUCTION != FULL_SOURCE_INVERSE
```

## 9. Frozen gain criteria

```text
G1 CHAIN_AND_INTERMEDIATE_LOSS_GAIN
  established only if DSD preserves intermediate loss / re-enrichment provenance more correctly than B1.

G2 VERSIONED_MIGRATION_GAIN
  established only if DSD preserves schema/time-specific map semantics more correctly than B1.

G3 STOCHASTIC_POLICY_GAIN
  established only if DSD preserves support/seed/realization/non-determinism more correctly than B1.

G4 TARGET_ENRICHMENT_PROVENANCE_GAIN
  established only if DSD separates target-added values from source-derived values more correctly than B1.

G5 CLAIM_SCOPED_RECONSTRUCTION_REVERSIBILITY_GAIN
  established only if DSD preserves claim-scoped reconstruction versus full-source invertibility more correctly than B1.

G6 TERMINAL_AND_GUARD_DISCIPLINE_GAIN
  established only if DSD assigns terminal/conformance/loss semantics more correctly than B1.

G7 TRACEABILITY_GAIN
  established only if DSD preserves a claim-relevant derivation/provenance trace that B1 cannot reconstruct from the same inputs.
```

Decision rule:

```text
If DSD is incorrect or NONCONFORMANT -> challenge FAIL.
If one or more G1-G7 are established against a correct B1 -> GAIN_ESTABLISHED.
If DSD and B1 are both correct and B1 matches all seven dimensions -> NO_GAIN.
Otherwise -> challenge FAIL or unresolved according to the frozen scoring record.
```

Implementation speed, elegance, terminology, pedagogical value, external practical benefit, and independent-evaluator performance are not scored.

## 10. Frozen scoring

```text
A. immutable/fairness discipline        8
B. DSD execution                       18
C. B1 execution                        18
D. comparative gain                     9
E. scope/protocol pressure              7
TOTAL                                  60
```

Detailed lock:

```text
A1 protocol commit/blob frozen
A2 five stronger subcases frozen
A3 B1 identity/capabilities frozen
A4 same claim-relevant inputs frozen
A5 gain criteria G1-G7 frozen
A6 scoring frozen
A7 B1 may not be weakened post-hoc
A8 no source/target/map/version/policy/scope revision after execution begins

B1-B5 exact terminals R1-R5
B6 R1 intermediate many-to-one loss preserved
B7 R1 endpoint coincidence does not erase loss
B8 R2 version-specific mappings preserved
B9 R2 no retroactive/versionless semantic collapse
B10 R3 support/seed/realization records preserved
B11 R3 one realization not generalized to deterministic map
B12 R4 target enrichment provenance preserved
B13 R4 source derivability not inferred from target existence
B14 R5 claim-scoped payload preservation retained
B15 R5 full-source noninvertibility retained
B16 claim-scoped reconstruction != full inverse
B17 all relevant carrier/status/addition/loss ledgers retained
B18 all five DSD executions CONFORMANT

C1-C5 exact terminals R1-R5
C6 R1 intermediate loss retained
C7 R1 enrichment not relabeled source recovery
C8 R2 version/time scopes retained
C9 R2 same code not treated as same semantics across versions
C10 R3 policy/support/seed retained
C11 R3 no deterministic overclaim
C12 R4 target enrichment provenance retained
C13 R4 source derivability not invented
C14 R5 claim/full-source scopes separated
C15 R5 noninvertibility retained
C16 all terminal/conformance states match
C17 provenance trace sufficient for all subcases
C18 full result set deterministically retraceable from frozen B1 record

D1-D7 G1-G7 each NOT_ESTABLISHED if B1 matches
D8 final method gain = NO_GAIN when D1-D7 all hold
D9 NO_GAIN not interpreted as failure/merger/absorption/deletion evidence

E1 protocol revision not required if no contradiction appears
E2 strongest-reasonable-baseline status may be established only at constructed-evidence level
E3 no external applicability claim
E4 no reproducibility claim
E5 no independent validation/practical-superiority claim
E6 no maturity-promotion claim
E7 no permanent survival/nonmerger/redundancy conclusion
```

Decision:

```text
60/60 -> CHALLENGE_VERDICT: PASS
otherwise -> CHALLENGE_VERDICT: FAIL
```

If a challenge-design defect appears, preserve this Case ID as failed and use a new Case ID for any corrected rerun.

## 11. Evidence-count lock

Before execution:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 4
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 4
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
METHOD_BOUNDARY_TRANSFORMATION_CASES: 1
BASELINE_TRANSFORMATION_CASES: 1
NO_GAIN_TRANSFORMATION_CASES: 1
STRONGEST_REASONABLE_BASELINE_TRANSFORMATION: not established
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
```

A 60/60 PASS with final `NO_GAIN` may add exactly:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: +1
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: +1
BASELINE_TRANSFORMATION_CASES: +1
NO_GAIN_TRANSFORMATION_CASES: +1
STRONGEST_REASONABLE_BASELINE_TRANSFORMATION: established_at_constructed_evidence_level
```

It does not establish reproducibility, external applicability, independent validation, practical superiority, maturity, method survival, non-merger, or permanent independence.

## 12. Next if passed

Proceed to deterministic same-project retrace using frozen Transformation artifacts. External validation remains deferred until the internal-standardization sequence is complete.