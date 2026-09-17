# TRN-CH-006 Precommit / DSD Transformation Deterministic Same-Project Retrace

Status: **PRECOMMITTED BEFORE EXECUTION**  
Date: **2026-09-17**  
Method: **DSD Transformation / DSD 변환론**  
Protocol: **Transformation Protocol v0.1**  
Protocol commit at freeze: `b5e292ff89b1a2529a9f1fde98ad13d9af692e90`  
Protocol blob at freeze: `f78393c188c513acb30a10f1b180d598138cea61`

## 1. Case identity

```text
CASE_ID: TRN-CH-006
CASE_CLASS: deterministic_same_project_retrace
CASE_ORIGIN: same_project_retrace_of_prior_constructed_challenge
EVIDENCE_SCOPE_CLASS: method_specific
RETRACE_TARGET: TRN-CH-005
EXTERNAL_APPLICATION: no
BASELINE: none for evidence increment
```

Purpose: test whether the claim-relevant DSD Transformation outputs of `TRN-CH-005` can be reconstructed deterministically from immutable project artifacts without modifying the protocol, source/target/map records, version/time scope, chain stages, stochastic policy, enrichment provenance, carrier scope, reconstruction scope, reversibility semantics, or terminal-status rules.

This is a same-project documentary retrace. It is **not blind, independent, or external replication**.

```text
SAME_PROJECT_RETRACE != INDEPENDENT_REPLICATION
DETERMINISTIC_MATCH != INDEPENDENT_VALIDATION
RETRACE_PASS != EXTERNAL_APPLICABILITY
```

## 2. Frozen artifact chain

```text
P0 Transformation Protocol v0.1
   commit: b5e292ff89b1a2529a9f1fde98ad13d9af692e90
   blob:   f78393c188c513acb30a10f1b180d598138cea61

P1 TRN-CH-005 precommit
   commit: c344e983c7b24a74ee7d1a9f1e36dfd14794dc64
   blob:   67147ab9f486d268a3ba34396d8ad3a9fcf50502

P2 TRN-CH-005 result comparison target
   commit: b05d24a861bfa2146e9522da968c29c6018468d3
   blob:   28bd10b14a5cb600a4a8e047852eea3f4a10dad3
```

Retrace derivation must use `P0 + P1` as the reconstruction basis. `P2` may be used only as the post-reconstruction immutable comparison target.

No live web lookup, external corpus, new map, new enrichment record, new stochastic policy, new carrier scope, or post-hoc reconstruction rule may be used to repair a mismatch.

## 3. Frozen retrace target

Five claim-relevant Transformation outputs from `TRN-CH-005` must be reconstructed:

```text
R1 composed chain with irreversible intermediate merge followed by external re-enrichment
R2 schema-version / temporal migration with identical raw code but version-dependent meaning
R3 stochastic target choice with frozen policy and seed
R4 target enrichment provenance separated from source-derived transformation
R5 claim-scoped preservation/reconstruction despite full-source noninvertibility
```

The retrace tests DSD Transformation output determinism. The prior B1 comparison remains historical baseline evidence and is not counted as a new baseline execution.

## 4. Frozen expected DSD reconstruction

### R1 — composed chain / intermediate loss

```text
STAGE_A: (x,y) -> z=x+y
STAGE_A_RELATION -> MANY_TO_ONE_MERGE
STAGE_A_INJECTIVITY -> noninjective on declared integer-pair domain
STAGE_A_INFORMATION_LOSS -> x/y distinction unavailable from z alone
STAGE_B x' -> TARGET_ADDED_NOT_SOURCE_DERIVED / EXTERNAL_ENRICHMENT
ENDPOINT_NUMERIC_MATCH_WITH_SOURCE -> yes for fixture
INTERMEDIATE_LOSS_CLEARED_BY_ENDPOINT_MATCH -> no
REVERSIBILITY_FROM_SOURCE_DERIVED_CHAIN_ALONE -> NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
TERMINAL -> TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
CONFORMANCE -> CONFORMANT
```

### R2 — schema-version / temporal migration

```text
S2-t0 / V1 code=1 -> READY / PRESERVED_UNDER_DECLARED_EQUIVALENCE
S2-t1 / V2 code=1 -> HOLD  / PRESERVED_UNDER_DECLARED_EQUIVALENCE
MAP_VERSION_SCOPE -> preserved
VERSIONLESS_CODE_EQUIVALENCE -> prohibited
RETROACTIVE_REINTERPRETATION -> no
TERMINAL(t0) -> TRANSFORMATION_COMPLETED_PRESERVING
TERMINAL(t1) -> TRANSFORMATION_COMPLETED_PRESERVING
CONFORMANCE -> CONFORMANT
```

### R3 — stochastic policy

```text
record_id -> PRESERVED_EXACT
mode -> PRESERVED_EXACT
route=R2 -> TARGET_ADDED_NOT_SOURCE_DERIVED
ALLOWED_OUTPUT_SUPPORT -> {R1,R2}
P(R1)=0.5; P(R2)=0.5
SEED_OR_REPLAY_RECORD -> 17
DETERMINISM_CLAIM -> stochastic
ONE_REALIZATION_DEFINES_FULL_MAP -> no
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
CONFORMANCE -> CONFORMANT
```

### R4 — target enrichment provenance

```text
id -> PRESERVED_EXACT
temperature_c -> temperature_k / PRESERVED_UNDER_DECLARED_EQUIVALENCE
quality_label="verified" -> TARGET_ADDED_NOT_SOURCE_DERIVED / EXTERNAL_ENRICHMENT
QUALITY_LABEL_SOURCE_DERIVED -> no
CLAIM_RELEVANT_INFORMATION_LOSS -> none
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
CONFORMANCE -> CONFORMANT
```

### R5 — claim-scoped preservation / full-source noninvertibility

```text
payload -> PRESERVED_EXACT
nonce -> OUT_OF_SCOPE_FOR_TRANSFORMATION at declared claim resolution
CLAIM_SCOPED_RECONSTRUCTION(payload) -> exact
FULL_SOURCE_INJECTIVITY -> no
FULL_SOURCE_REVERSIBILITY -> NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
GLOBAL_BIJECTIVITY_CLAIM -> not made
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING at declared target resolution
CONFORMANCE -> CONFORMANT
```

## 5. Frozen distinction ledger

```text
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
EXTERNAL_REENRICHMENT != SOURCE_INFORMATION_RECOVERY
SAME_ENDPOINT_VALUES != SAME_PROVENANCE

SAME_RAW_CODE != SAME_SEMANTICS_ACROSS_SCHEMA_VERSIONS
LATER_SCHEMA_MEANING != EARLIER_SCHEMA_MEANING

REALIZED_OUTPUT != FULL_STOCHASTIC_TRANSFORMATION_SEMANTICS
TARGET_ADDITION != SOURCE_DERIVABILITY

TARGET_VALUE_EXISTENCE != SOURCE_DERIVABILITY
TARGET_ENRICHMENT != SOURCE_PRESERVATION

LOSSLESS_RELATIVE_TO_DECLARED_CARRIERS != BIJECTIVE_ON_FULL_SOURCE_SPACE
CLAIM_SCOPED_RECONSTRUCTION != FULL_SOURCE_INVERSE
```

## 6. Frozen comparison policy

The retrace output is generated from `P0 + P1` first. Only after the reconstructed ledger is frozen may it be compared with P2.

Required comparison dimensions:

```text
D1 carrier-preservation outputs
D2 terminal transformation statuses
D3 information-loss / collision / injectivity records
D4 target-addition / enrichment provenance
D5 version/time scope
D6 stochastic policy/support/seed/realization
D7 reconstruction / reversibility scope
D8 protocol conformance and preserved distinctions
```

A mismatch may not be repaired by changing P0/P1 semantics.

## 7. Frozen scoring

```text
A. artifact lock / comparison discipline        10
B. five-subcase deterministic reconstruction    20
C. provenance / distinction reconstruction      12
D. exact post-reconstruction comparison          8
E. evidence-scope discipline                     6
TOTAL                                            56
```

Detailed check lock:

```text
A1 P0 commit/blob fixed
A2 P1 commit/blob fixed
A3 P2 commit/blob fixed only as comparison target
A4 derivation basis limited to P0+P1
A5 no live external lookup
A6 no source/target/map/version/policy/scope modification
A7 no P2 use before reconstruction freeze
A8 scoring fixed
A9 mismatch repair prohibited
A10 same-project/non-independent scope explicit

B1 R1 terminal exact reconstruction
B2 R1 intermediate merge/noninjectivity retained
B3 R1 endpoint equality does not erase loss
B4 R1 external enrichment not source recovery
B5 R2 t0 READY reconstruction
B6 R2 t1 HOLD reconstruction
B7 R2 version scopes retained
B8 R2 no retroactive semantic collapse
B9 R3 preserved source carriers
B10 R3 target route addition provenance retained
B11 R3 support/distribution/seed retained
B12 R3 no deterministic overclaim
B13 R4 source-derived conversions reconstructed
B14 R4 external quality-label provenance retained
B15 R5 payload claim-scope preservation retained
B16 R5 nonce out-of-scope status retained
B17 R5 exact claim-scoped reconstruction retained
B18 R5 full-source noninvertibility retained
B19 all required terminal statuses reconstructed
B20 all required conformance statuses CONFORMANT

C1 chain-stage provenance preserved
C2 intermediate loss provenance preserved
C3 version/time provenance preserved
C4 stochastic-policy provenance preserved
C5 target-enrichment provenance preserved
C6 claim-scope provenance preserved
C7-C12 frozen distinction-ledger groups preserved without collapse

D1 R1 claim-relevant output matches P2
D2 R2 claim-relevant output matches P2
D3 R3 claim-relevant output matches P2
D4 R4 claim-relevant output matches P2
D5 R5 claim-relevant output matches P2
D6 terminal-status match at all frozen scopes
D7 conformance match at all frozen scopes
D8 post-hoc corrections after comparison = 0

E1 reproducibility increment limited to same-project retrace
E2 no independent-replication claim
E3 no independent-validation claim
E4 no external-applicability claim
E5 no maturity promotion from retrace alone
E6 no method survival/merger/absorption/deletion conclusion
```

Decision:

```text
56/56 -> RETRACE_VERDICT: PASS
otherwise -> RETRACE_VERDICT: FAIL
```

## 8. Evidence-count lock

Before execution:

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 5
BASELINE_TRANSFORMATION_CASES: 2
NO_GAIN_TRANSFORMATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_TRANSFORMATION: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
INDEPENDENT_TRANSFORMATION_VALIDATION: not established
TRANSFORMATION_INTERNAL_STANDARDIZATION_STATUS: developing
```

A 56/56 PASS may add exactly:

```text
REPRODUCIBILITY_CASES: +1
```

It does not add direct pilots, baseline cases, NO_GAIN cases, external applications, independent replication, independent validation, or maturity promotion.

## 9. Next if passed

Proceed to a frozen-axis internal maturity / standardization audit. External validation remains deferred until that audit is complete.