# SPEC-CH-004 Precommit — NO_GAIN Specification Challenge / 무이득 명세 도전 사전고정

Status: **precommitted_before_scoring**  
Date: 2026-09-06  
Evidence scope: `method_specific`  
Case origin: `constructed_benchmark`  
Method directly tested: **DSD Specification / DSD 명세론**  
Method protocol: **DSD Specification Protocol v0.1**

## 1. Locked question / 고정 질문

Can DSD Specification preserve `SPEC_NO_GAIN` as a legitimate result when a competent locked source specification already contains all claim-relevant structure, while still distinguishing that case from:

1. a source for which DSD re-expression adds an operationally testable benefit; and
2. a source that is genuinely underspecified and therefore cannot be rescued by re-expression?

The challenge does **not** ask whether DSD formatting is aesthetically clearer. Only operationally declared gain dimensions count.

## 2. Locked gain dimensions / 고정 이득 차원

A DSD re-expression counts as operational gain only when, relative to the locked source and downstream task, it adds at least one of the following **without inventing a new source fact**:

```text
G1 DISTINCTION_GAIN
  a claim-relevant distinction already present in the source becomes separately
  addressable/checkable rather than remaining merged or prose-dependent

G2 TRACEABILITY_GAIN
  a requirement can be retraced to its source/version/dependency through an
  explicit requirement atom or cross-reference that the baseline lacks

G3 AMBIGUITY_REDUCTION_GAIN
  an activation/dependency/allowed-alternative relation already recoverable from
  the source is made explicit enough to remove more than one admissible reading

G4 DOWNSTREAM_CHECKABILITY_GAIN
  the re-expression supplies an explicit violation/unresolved/check rule from
  information already present in the source, allowing the locked checker to act
  without prose inference
```

The following do **not** count as gain:

```text
COSMETIC_RELABELING
FIELD_REORDERING
DSD_TERMINOLOGY_SUBSTITUTION_WITHOUT_NEW_OPERATIONAL_CONTENT
DUPLICATING_AN_ALREADY_EXPLICIT_SOURCE_TABLE
ADDING_OPTIONAL_DSD_LAYERS_UNUSED_BY_THE_TASK
```

## 3. Locked NO_GAIN criterion / 고정 무이득 기준

Return `SPEC_NO_GAIN` only if all of the following hold:

```text
NG1 source specification is usable for the declared downstream task
NG2 all claim-relevant type/status/dependency/bridge/violation distinctions are already explicit
NG3 source/version traceability required by the task is already explicit
NG4 DSD re-expression adds none of G1-G4
NG5 no contradiction or underspecification is being hidden by the NO_GAIN label
```

`SPEC_NO_GAIN` is a valid non-failure outcome.

## 4. Locked benchmark / 고정 벤치마크

Synthetic benchmark family: `SpecificationGainToy-v4`  
Locked requirement family: `SG-SPEC-004-v1`

Core task: specify a two-carrier relay rule for a downstream checker.

Core semantics used when present in a source variant:

```text
source carrier: C_src
target carrier: C_dst
input type: scalar signal token
ACTIVE context controls evaluation
status distinction: defined_zero != applicable_but_undefined
cross-carrier transfer, when activated, uses B_sd : C_src -> C_dst
violation rule, when supplied: output outside [0,10] -> VIOLATED
unresolved rule: missing active value or missing required bridge selector -> UNRESOLVED_OR_UNDERSPECIFIED
```

Selected DSD layers for the benchmark:

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
EXTERNAL_DOMAIN: none
```

## 5. Locked cases / 고정 사례

### NG-01 — Already-complete atomic baseline

The baseline already contains requirement IDs, source references, typed carriers, activation conditions, status distinctions, explicit `B_sd`, dependency fields, violation/unresolved rules, and version traceability.

Expected:

```text
FINAL_SPEC_STATUS: no_gain
NO_GAIN_STATUS: true
GAIN_DIMENSIONS: none
```

### NG-02 — Complete non-DSD structured schema

The baseline uses different terminology but has a one-to-one operational field correspondence with every claim-relevant DSD Specification atom needed by the task.

Expected: `no_gain`.

### NG-03 — Reordered/relabelled duplicate

The baseline is already complete and checkable. The DSD output changes ordering and labels only.

Expected: `no_gain`.

### GN-01 — Prose distinctions become separately checkable

The source prose explicitly states both `defined_zero` and `applicable_but_undefined` as different cases, but they are embedded in one paragraph and the downstream checker cannot address them separately without prose parsing. DSD atomization creates separately addressable requirement/status records while preserving the same facts.

Expected:

```text
FINAL_SPEC_STATUS: usable
NO_GAIN_STATUS: false
GAIN_DIMENSIONS: DISTINCTION_GAIN, DOWNSTREAM_CHECKABILITY_GAIN
```

### GN-02 — Source/dependency traceability added from existing references

The source contains all required facts and citations, but requirement-to-source and requirement-to-dependency links are scattered and not recorded in a retraceable table. DSD atomization records explicit source references and dependency links using only already-present references.

Expected:

```text
FINAL_SPEC_STATUS: usable
NO_GAIN_STATUS: false
GAIN_DIMENSIONS: TRACEABILITY_GAIN
```

### GN-03 — Activation relation made explicit from source text

The source explicitly says in prose that the relay rule applies only in ACTIVE context, but the baseline requirement row omits an activation field. DSD re-expression records the already-stated ACTIVE condition in `ACTIVATION_CONDITION`, removing an otherwise admissible context-free reading.

Expected:

```text
FINAL_SPEC_STATUS: usable
NO_GAIN_STATUS: false
GAIN_DIMENSIONS: AMBIGUITY_REDUCTION_GAIN
```

### US-01 — Missing violation threshold

The source says only `output must be acceptable` and contains no threshold/range/category rule competent for the locked numeric checker.

Expected:

```text
FINAL_SPEC_STATUS: underspecified
NO_GAIN_STATUS: false
DIAGNOSTIC: SPEC_UNDERSPECIFIED / U1 MISSING_VIOLATION_RULE
```

The DSD re-expression may expose the missing rule, but it may not invent `[0,10]` for this source variant.

### US-02 — Multiple bridges without selector

The source allows both `B_direct` and `B_scaled` and gives no selector/profile rule, while the downstream result is bridge-sensitive.

Expected:

```text
FINAL_SPEC_STATUS: underspecified
NO_GAIN_STATUS: false
DIAGNOSTIC: SPEC_UNDERSPECIFIED / U2 BRIDGE_SELECTOR_MISSING
```

The DSD re-expression may expose the ambiguity, but it may not choose a bridge.

## 6. Precommitted scoring / 사전 고정 점수

```text
NO_GAIN_CASES: 3
GAIN_CASES: 3
UNDERSPECIFIED_CASES: 2
TOTAL_CASES: 8

PASS_REQUIREMENT:
  NO_GAIN correctly preserved: 3/3
  operational-gain cases correctly distinguished from NO_GAIN: 3/3
  underspecified cases correctly distinguished from NO_GAIN: 2/2
  exact expected final-status family: 8/8
  false NO_GAIN on incomplete source: 0
  false gain from cosmetic relabeling/reordering: 0
  invented source facts: 0
  post-reveal rule change: 0
```

## 7. Shared-core activation / 공통 코어 활성화

```text
SC-02 active: source/version lock
SC-03 active: bridge ambiguity case US-02
SC-04 active: unused optional layers remain inactive
SC-07 active: method-specific + constructed-benchmark evidence classification
SC-08 active: strongest competent baseline, NO_GAIN preservation, precommit

SC-01 active only where status distinction is scored in GN-01
SC-05 inactive for core claim
SC-06 inactive for core claim
SC-09 inactive for core claim
SC-10 inactive for core claim
```

## 8. Promotion restraint / 승격 절제

A PASS would support only the method-specific claim that Specification Protocol v0.1 can preserve a locked NO_GAIN outcome and distinguish it from operational gain and genuine underspecification on this constructed benchmark.

It would not establish:

- general superiority over requirements engineering;
- mature method status;
- real-world validity;
- independent blind reproducibility.

The scoring record must not modify this precommit after case evaluation begins.
