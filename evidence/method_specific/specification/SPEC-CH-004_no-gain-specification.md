# SPEC-CH-004 — NO_GAIN Specification Challenge / 무이득 명세 도전

Status: **SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Case origin: `constructed_benchmark`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**  
Precommit: [`SPEC-CH-004_precommit.md`](SPEC-CH-004_precommit.md)  
Precommit commit: `4d55d00af7fa376d370415a48b82de6883ba6fc8`

## 1. Purpose / 목적

This challenge tests whether DSD Specification preserves `SPEC_NO_GAIN` as a legitimate non-failure result when a competent locked baseline already contains all task-relevant specification content.

It also tests the two adjacent boundaries:

```text
baseline already complete + DSD adds no operational content
-> SPEC_NO_GAIN

DSD re-expression makes already-present source semantics newly addressable,
traceable, less ambiguous, or directly checkable
-> usable + operational gain

source itself lacks a required fact/rule
-> SPEC_UNDERSPECIFIED
```

The case set, gain dimensions, NO_GAIN criterion, and scoring rule were committed before scoring. No post-reveal exception or gain criterion was introduced.

## 2. Locked benchmark / 고정 벤치마크

Synthetic benchmark family: `SpecificationGainToy-v4`  
Locked requirement family: `SG-SPEC-004-v1`

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
EXTERNAL_DOMAIN: none
```

The benchmark uses a two-carrier relay requirement and varies only the quality/completeness of the locked source representation.

## 3. Locked gain dimensions / 고정 이득 차원

Only the precommitted operational dimensions count:

```text
DISTINCTION_GAIN
TRACEABILITY_GAIN
AMBIGUITY_REDUCTION_GAIN
DOWNSTREAM_CHECKABILITY_GAIN
```

Cosmetic relabeling, field reordering, DSD terminology substitution, duplication of an already complete table, or activation of unused optional DSD layers do not count as gain.

## 4. Case scoring / 사례 판정

### NG-01 — Already-complete atomic baseline

The baseline already supplies:

```text
requirement IDs
source/version references
typed source and target carriers
ACTIVE activation condition
separate defined_zero / applicable_but_undefined statuses
explicit B_sd : C_src -> C_dst
dependencies
violation rule
unresolved rule
```

DSD re-expression preserves the same operational content and adds no precommitted gain dimension.

Observed:

```text
FINAL_SPEC_STATUS: no_gain
NO_GAIN_STATUS: true
GAIN_DIMENSIONS: none
```

Diagnostic match: exact.

### NG-02 — Complete non-DSD structured schema

The source uses non-DSD field names, but every task-relevant field has a one-to-one operational counterpart and is already independently checkable and traceable.

Changing labels to DSD terminology does not add a distinction, trace link, ambiguity reduction, or checker capability.

Observed: `no_gain`.

Diagnostic match: exact.

### NG-03 — Reordered/relabelled duplicate

The DSD record changes only field order and names relative to an already complete baseline.

Observed:

```text
FINAL_SPEC_STATUS: no_gain
FALSE_COSMETIC_GAIN: no
```

Diagnostic match: exact.

### GN-01 — Prose distinctions become separately checkable

The source already states that `defined_zero` and `applicable_but_undefined` are distinct cases, but both are embedded in prose. The DSD representation creates separately addressable status requirements and explicit downstream verdict conditions without inventing a source fact.

Observed:

```text
FINAL_SPEC_STATUS: usable
NO_GAIN_STATUS: false
GAIN_DIMENSIONS:
  DISTINCTION_GAIN
  DOWNSTREAM_CHECKABILITY_GAIN
```

Diagnostic match: exact.

### GN-02 — Requirement/source/dependency traceability added

All required facts and references already exist in the source, but links among requirement, source location, and dependency are scattered. The DSD atomization records those existing links explicitly.

Observed:

```text
FINAL_SPEC_STATUS: usable
NO_GAIN_STATUS: false
GAIN_DIMENSIONS:
  TRACEABILITY_GAIN
```

No new source fact was introduced.

Diagnostic match: exact.

### GN-03 — ACTIVE activation relation made explicit

The source prose states that the relay rule applies only in ACTIVE context, while the baseline requirement row lacks an activation field. The DSD record copies the already-present source condition into `ACTIVATION_CONDITION`.

This removes a context-free reading that the baseline row by itself leaves open.

Observed:

```text
FINAL_SPEC_STATUS: usable
NO_GAIN_STATUS: false
GAIN_DIMENSIONS:
  AMBIGUITY_REDUCTION_GAIN
```

Diagnostic match: exact.

### US-01 — Missing violation threshold

The source says only that output must be acceptable. It contains no numeric range, category rule, or competent threshold for the locked numeric checker.

The benchmark family uses `[0,10]` only in variants where that rule is explicitly supplied; it is not imported into this variant.

Observed:

```text
FINAL_SPEC_STATUS: underspecified
NO_GAIN_STATUS: false
DIAGNOSTIC: SPEC_UNDERSPECIFIED / U1 MISSING_VIOLATION_RULE
INVENTED_THRESHOLD: no
```

Diagnostic match: exact.

### US-02 — Multiple bridges without selector

The source permits both `B_direct` and `B_scaled`, the downstream result depends on the choice, and no selector/profile rule is supplied.

Observed:

```text
FINAL_SPEC_STATUS: underspecified
NO_GAIN_STATUS: false
DIAGNOSTIC: SPEC_UNDERSPECIFIED / U2 BRIDGE_SELECTOR_MISSING
INVENTED_SELECTOR: no
```

Diagnostic match: exact.

## 5. Score / 점수

```text
NO_GAIN_CASES_CORRECTLY_PRESERVED: 3/3
OPERATIONAL_GAIN_CASES_CORRECTLY_DISTINGUISHED: 3/3
UNDERSPECIFIED_CASES_CORRECTLY_DISTINGUISHED: 2/2
EXACT_EXPECTED_FINAL_STATUS_FAMILY: 8/8
FALSE_NO_GAIN_ON_INCOMPLETE_SOURCE: 0
FALSE_GAIN_FROM_COSMETIC_RELABELING_OR_REORDERING: 0
INVENTED_SOURCE_FACTS: 0
POST_REVEAL_RULE_CHANGE: no
POST_REVEAL_EXCEPTION_ADDED: no
NEGATIVE_CONTROL: pass
RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS
```

| Case | Expected | Observed | Match |
|---|---|---|---|
| NG-01 | no_gain | no_gain | yes |
| NG-02 | no_gain | no_gain | yes |
| NG-03 | no_gain | no_gain | yes |
| GN-01 | usable + distinction/checkability gain | exact | yes |
| GN-02 | usable + traceability gain | exact | yes |
| GN-03 | usable + ambiguity-reduction gain | exact | yes |
| US-01 | underspecified / U1 | exact | yes |
| US-02 | underspecified / U2 | exact | yes |

## 6. Main finding / 핵심 결과

The protocol did not treat DSD use itself as evidence of benefit.

```text
DSD applied
!= gain automatically exists
```

A competent non-DSD specification that already exposes the same typed requirements, distinctions, dependencies, mappings, verdict semantics, and traceability can legitimately receive:

```text
SPEC_NO_GAIN
```

Conversely, `NO_GAIN` was not used to hide an incomplete source. When a threshold or bridge selector was genuinely absent, the result remained `SPEC_UNDERSPECIFIED` rather than being rescued by reformatting.

The gain cases were also constrained: DSD received credit only when the re-expression changed a precommitted operational property of the record, not when it merely changed terminology or ordering.

## 7. Strong-baseline interpretation / 강한 기준선 해석

The strongest baseline in this constructed challenge is the already-complete non-DSD structured schema represented by NG-02.

Because NG-02 is operationally equivalent to the task-relevant DSD atomization, the proper result is `SPEC_NO_GAIN`, not a forced DSD advantage claim.

This directly exercises Specification's method-specific use of SC-08 baseline and NO_GAIN discipline.

## 8. Shared-core activation / 공통 코어 활성화

```text
SC-01 active: GN-01 status distinction
SC-02 active: locked source/version comparison
SC-03 active: US-02 bridge-selector boundary
SC-04 active: unused optional layers stay inactive
SC-07 active: evidence scope/case origin
SC-08 active: strongest competent baseline, precommit, NO_GAIN preservation

SC-05 inactive for core claim
SC-06 inactive for core claim
SC-09 inactive for core claim
SC-10 inactive for core claim
```

This record is not a new shared-core candidate. It directly tests how **Specification Protocol v0.1** turns the shared NO_GAIN/baseline discipline into a Specification-specific result.

## 9. Evidence status / 증거 상태

```text
METHOD: DSD Specification
METHOD_STATUS: developing
DIRECT_PILOT_RECORDS_COMPLETED: 4
  SPEC-CH-001
  SPEC-CH-002
  SPEC-CH-003
  SPEC-CH-004
MATURE_METHOD_STATUS: not_claimed
```

Four successful constructed pilots still do not establish mature direct validity. Independent retrace and external/independently generated requirement evidence remain outstanding.

## 10. Reproducibility / 재현성

```text
PROTOCOL_VERSION: Specification Protocol v0.1
PRECOMMIT_FILE: SPEC-CH-004_precommit.md
PRECOMMIT_COMMIT: 4d55d00af7fa376d370415a48b82de6883ba6fc8
BENCHMARK_FAMILY: SpecificationGainToy-v4
REQUIREMENT_FAMILY: SG-SPEC-004-v1
CASE_COUNT: 8
SCORING_RULE: exact final-status family + gain/no-gain/underspecification counts
MANUAL_JUDGMENT_POINTS:
  operational equivalence of already-complete baseline fields
  whether an explicit atom changes downstream addressability/checkability
  whether trace links are newly explicit but source-supported
  whether ambiguity reduction uses an already-present source condition
  whether a missing rule is genuinely absent rather than merely implicit
POST_REVEAL_RULE_CHANGE: no
```

No executable code is required for this finite declarative benchmark.

## 11. Limits / 한계

- constructed synthetic benchmark;
- same-session evaluation with separate precommit;
- not independent blind validation;
- the operational gain dimensions were designed within the current DSD method-family project;
- no external requirements-engineering benchmark is used here;
- no measured cost, time, defect-rate, comprehension, or inter-rater improvement is claimed;
- real-world usefulness remains unverified.

## 12. Next step / 다음 단계

Proceed to **SPEC-CH-005 — Reproducibility / Independent Retrace Challenge**.

The existing SPEC-CH-001 through SPEC-CH-004 records remain append-only.
