# TRN-CH-005 Result / DSD Transformation Strongest-Reasonable-Baseline Challenge

Status: **EXECUTED — 60/60 PASS / NO_GAIN**  
Date: **2026-09-17**  
Method: **DSD Transformation / DSD 변환론**  
Protocol: **Transformation Protocol v0.1**  
Protocol commit: `b5e292ff89b1a2529a9f1fde98ad13d9af692e90`  
Protocol blob: `f78393c188c513acb30a10f1b180d598138cea61`  
Precommit commit: `c344e983c7b24a74ee7d1a9f1e36dfd14794dc64`  
Precommit blob: `67147ab9f486d268a3ba34396d8ad3a9fcf50502`

## 1. Evidence identity

```text
CASE_ID: TRN-CH-005
CASE_CLASS: strongest_reasonable_baseline_comparison
CASE_ORIGIN: constructed_same_project
EVIDENCE_SCOPE_CLASS: method_specific
BASELINE: B1_STRONG_TRANSFORMATION_LEDGER_ENGINE
RESULT: PASS
TRANSFORMATION_METHOD_GAIN_STATUS: NO_GAIN
EXTERNAL_APPLICATION: no
```

The immutable precommit was read before execution. No source, target, map, schema/version, policy, carrier scope, enrichment record, reconstruction scope, baseline capability, gain criterion, or scoring item was changed after execution began.

## 2. R1 — composed chain / intermediate loss / endpoint coincidence

DSD execution:

```text
SOURCE: (x=2,y=3)
STAGE_A: z=x+y=5
STAGE_A_RELATION: MANY_TO_ONE_MERGE
STAGE_A_INJECTIVITY: noninjective on declared integer-pair domain
STAGE_A_INFORMATION_LOSS: x/y distinction unavailable from z alone

STAGE_B:
  x_ext=2 from EXTERNAL_ENRICHMENT
  x'=x_ext=2
  y'=z-x_ext=3

ENDPOINT_NUMERIC_MATCH_WITH_SOURCE: yes for frozen fixture
x' SOURCE_PRESERVATION_STATUS: TARGET_ADDED_NOT_SOURCE_DERIVED
INTERMEDIATE_LOSS_CLEARED_BY_ENDPOINT_MATCH: no
REVERSIBILITY_FROM_SOURCE_DERIVED_CHAIN_ALONE: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 execution from the same records:

```text
Stage A merge/noninjectivity retained
Stage B external x provenance retained
Endpoint equality retained as numeric coincidence only
No source-information recovery credited to external enrichment
Full source-derived chain remains noninvertible
TERMINAL -> TRANSFORMATION_COMPLETED_WITH_DECLARED_LOSS
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
EXTERNAL_REENRICHMENT != SOURCE_INFORMATION_RECOVERY
SAME_ENDPOINT_VALUES != SAME_PROVENANCE
```

No gain is established on R1.

## 3. R2 — schema-version / temporal migration

DSD execution:

```text
S2-t0 / V1 code=1 -> M2-V1 -> state=READY
  preservation -> PRESERVED_UNDER_DECLARED_EQUIVALENCE
  terminal -> TRANSFORMATION_COMPLETED_PRESERVING

S2-t1 / V2 code=1 -> M2-V2 -> state=HOLD
  preservation -> PRESERVED_UNDER_DECLARED_EQUIVALENCE
  terminal -> TRANSFORMATION_COMPLETED_PRESERVING

MAP_VERSION_SCOPE: preserved
TEMPORAL_SCOPE: t0<t1 preserved
VERSIONLESS_CODE_EQUIVALENCE: not asserted
RETROACTIVE_REINTERPRETATION: no
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 execution:

```text
V1 and V2 source semantics retained separately
M2-V1 and M2-V2 applied only in their frozen version scopes
same raw code did not collapse semantic distinction
no later-schema back-projection
both records -> TRANSFORMATION_COMPLETED_PRESERVING
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
SAME_RAW_CODE != SAME_SEMANTICS_ACROSS_SCHEMA_VERSIONS
LATER_SCHEMA_MEANING != EARLIER_SCHEMA_MEANING
```

No gain is established on R2.

## 4. R3 — stochastic/choice semantics

DSD execution:

```text
record_id=K9 -> PRESERVED_EXACT
mode=A       -> PRESERVED_EXACT
route=R2     -> TARGET_ADDED_NOT_SOURCE_DERIVED
ADDITION_PROVENANCE -> OTHER_EXPLICIT_ADDITION / P3-v1 stochastic choice
ALLOWED_OUTPUT_SUPPORT -> {R1,R2}
P(R1)=0.5
P(R2)=0.5
SEED_OR_REPLAY_RECORD -> 17
REALIZED_OUTPUT -> R2
DETERMINISM_CLAIM -> stochastic, not deterministic
ONE_REALIZATION_DEFINES_FULL_MAP -> no
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 execution:

```text
source carriers preserved
route retained as target addition with P3-v1 provenance
support/distribution/seed/realization all retained
one realization not generalized into a deterministic map
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
REALIZED_OUTPUT != FULL_STOCHASTIC_TRANSFORMATION_SEMANTICS
TARGET_ADDITION != SOURCE_DERIVABILITY
```

No gain is established on R3.

## 5. R4 — target enrichment provenance

DSD execution:

```text
id=7 -> PRESERVED_EXACT
temperature_c=20 -> temperature_k=293.15
  -> PRESERVED_UNDER_DECLARED_EQUIVALENCE
quality_label="verified"
  -> TARGET_ADDED_NOT_SOURCE_DERIVED
  -> EXTERNAL_ENRICHMENT
QUALITY_LABEL_SOURCE_DERIVED: no
CLAIM_RELEVANT_INFORMATION_LOSS: none
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_PRESERVING
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 execution:

```text
id exact preservation retained
temperature equivalence retained
quality label retained as externally enriched target-only value
no source derivability invented from target existence
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
TARGET_VALUE_EXISTENCE != SOURCE_DERIVABILITY
TARGET_ENRICHMENT != SOURCE_PRESERVATION
```

No gain is established on R4.

## 6. R5 — claim-scoped preservation and full-source noninvertibility

DSD execution:

```text
SOURCE_FIXTURE: payload=42, nonce=N918
MAP: (payload,nonce) -> target(payload)
CLAIM_RELEVANT_CARRIERS: {payload}
nonce -> OUT_OF_SCOPE_FOR_TRANSFORMATION at declared claim resolution
payload -> PRESERVED_EXACT
CLAIM_SCOPED_RECONSTRUCTION(payload): exact
FULL_SOURCE_INJECTIVITY: no
FULL_SOURCE_REVERSIBILITY: NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
GLOBAL_BIJECTIVITY_CLAIM: not made
TERMINAL_TRANSFORMATION_STATUS: TRANSFORMATION_COMPLETED_PRESERVING at declared target resolution
TRANSFORMATION_PROTOCOL_CONFORMANCE: CONFORMANT
```

B1 execution:

```text
payload claim scope retained
nonce kept outside the declared target resolution rather than silently treated as preserved
exact payload reconstruction retained
full-source many-to-one collision retained
no full-source inverse or global bijection claimed
TERMINAL -> TRANSFORMATION_COMPLETED_PRESERVING
TRACE_SUFFICIENT -> yes
```

Both preserve:

```text
LOSSLESS_RELATIVE_TO_DECLARED_CARRIERS != BIJECTIVE_ON_FULL_SOURCE_SPACE
CLAIM_SCOPED_RECONSTRUCTION != FULL_SOURCE_INVERSE
```

No gain is established on R5.

## 7. DSD versus B1 task-level comparison

```text
SUBCASE  DSD MAIN RESULT                                      B1 MAIN RESULT
R1       COMPLETED_WITH_DECLARED_LOSS / noninvertible          same
R2-t0    COMPLETED_PRESERVING / READY                          same
R2-t1    COMPLETED_PRESERVING / HOLD                           same
R3       COMPLETED_PRESERVING / stochastic route addition      same
R4       COMPLETED_PRESERVING / external enrichment            same
R5       COMPLETED_PRESERVING at claim resolution              same
         full-source noninvertibility preserved                same
```

B1 retained enough chain-stage, version/time, stochastic-policy, enrichment, carrier-scope, reconstruction, reversibility, terminal, and provenance records to deterministically reconstruct every frozen decision.

## 8. Gain evaluation

```text
G1 CHAIN_AND_INTERMEDIATE_LOSS_GAIN: NOT_ESTABLISHED
G2 VERSIONED_MIGRATION_GAIN: NOT_ESTABLISHED
G3 STOCHASTIC_POLICY_GAIN: NOT_ESTABLISHED
G4 TARGET_ENRICHMENT_PROVENANCE_GAIN: NOT_ESTABLISHED
G5 CLAIM_SCOPED_RECONSTRUCTION_REVERSIBILITY_GAIN: NOT_ESTABLISHED
G6 TERMINAL_AND_GUARD_DISCIPLINE_GAIN: NOT_ESTABLISHED
G7 TRACEABILITY_GAIN: NOT_ESTABLISHED
```

Therefore:

```text
TRANSFORMATION_METHOD_GAIN_STATUS: NO_GAIN
STRONGEST_REASONABLE_BASELINE_TRANSFORMATION:
  established_at_constructed_evidence_level
```

This is a successful strongest-reasonable-baseline comparison at constructed-evidence level. It is not a DSD superiority result.

## 9. Precommitted scoring

```text
A. IMMUTABLE_FAIRNESS_DISCIPLINE:      8/8 PASS
B. DSD_EXECUTION:                     18/18 PASS
C. B1_EXECUTION:                      18/18 PASS
D. COMPARATIVE_GAIN:                   9/9 PASS
E. SCOPE_PROTOCOL_PRESSURE:             7/7 PASS
TOTAL:                                 60/60 PASS
```

```text
CHALLENGE_VERDICT: PASS
TRANSFORMATION_METHOD_GAIN_STATUS: NO_GAIN
PROTOCOL_DEFECT_EXPOSED: no
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

No scoring item was removed, weakened, or reinterpreted after execution.

## 10. Counter update

```text
DIRECT_TRANSFORMATION_PILOTS_ATTEMPTED: 5
SUCCESSFUL_DIRECT_TRANSFORMATION_PILOTS: 5
SUCCESSFUL_POSITIVE_TRANSFORMATION_CASES: 1
NEGATIVE_OR_FAILURE_TRANSFORMATION_CASES: 1
METHOD_BOUNDARY_TRANSFORMATION_CASES: 1
BASELINE_TRANSFORMATION_CASES: 2
NO_GAIN_TRANSFORMATION_CASES: 2
STRONGEST_REASONABLE_BASELINE_TRANSFORMATION: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 0
EXTERNAL_TRANSFORMATION_APPLICATIONS: 0
INDEPENDENT_TRANSFORMATION_VALIDATION: not established
TRANSFORMATION_INTERNAL_STANDARDIZATION_STATUS: developing
CURRENT_TRANSFORMATION_EVIDENCE_STATUS: validation_in_progress
```

## 11. Scope and registry discipline

This result establishes only strongest-reasonable-baseline coverage at the constructed-evidence level.

It does not establish:

```text
reproducibility
external applicability
independent validation
practical superiority
maturity promotion
permanent method independence
```

And:

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_MERGER_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
BASELINE_MATCH != PERMANENT_METHOD_REDUNDANCY
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
```

## 12. Next

Precommit and execute deterministic same-project retrace from frozen Transformation artifacts. A successful retrace may increment only `REPRODUCIBILITY_CASES`; it does not establish independent replication or external validity. External validation remains deferred until the internal-standardization sequence is complete.