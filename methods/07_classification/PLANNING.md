# DSD Classification Planning / DSD 분류론 기획

Status: **development initiated / task-interface stage**  
Date opened: **2026-09-12**

## Purpose / 목적

Develop **DSD Classification / DSD 분류론** as an independent method under **Field I: Structural Description & Understanding**.

Classification receives one or more supplied subjects together with a declared classification scope, class schema or class-generation policy, class-relevant criteria, feature provenance, and any required DSD/domain bridge. It returns criterion-traceable class assignments, boundary or underdetermined cases, and class-relation structure without inferring mathematical or semantic properties from labels alone.

The method is distinct from:

- **DSD Analysis**: decomposes and structurally re-expresses one target;
- **DSD Comparison**: evaluates correspondence/divergence between supplied subjects under a comparison relation or map family;
- **DSD Interpretation**: forms source/context-dependent interpretive readings;
- **DSD Specification**: states requirements/status distinctions rather than assigning subjects to classes;
- **DSD Diagnosis**: infers candidate causes or latent states from observations.

Classification may consume outputs from these methods, but their verdicts are not silently converted into class membership.

## Core methodological rule / 핵심 방법 규칙

```text
CLASS_LABEL != CLASS_CRITERION
SUMMARY_COINCIDENCE != STRUCTURAL_CLASS_IDENTITY
PAIRWISE_SIMILARITY != EQUIVALENCE_CLASS_MEMBERSHIP
ORDERED_LABELS != PROVEN_PARTIAL_ORDER
CURRENT_CLASS_MATCH != TEMPORAL_LINEAGE_IDENTITY
MISSING_FEATURE != NEGATIVE_FEATURE
UNDEFINED != DEFINED_ZERO
OUT_OF_SCOPE != UNCLASSIFIED
BOUNDARY_CASE != CLASSIFICATION_FAILURE
MULTI_CLASS_MEMBERSHIP != CRITERION_CONFLICT
```

A classification claim is valid only relative to a declared task resolution, criterion set, class-schema semantics, and evidence/provenance basis.

## Development sequence / 개발 순서

1. ✅ Classification-specific Task Interface v0.1 draft.
2. ⬜ Pre-protocol boundary attacks covering label leakage, missing-data collapse, aggregate collision, overlapping classes, open-world classes, hierarchy/partial-order assumptions, temporal class change, and criterion conflict.
3. ⬜ Boundary Amendment 001 if the attacks expose missing interface obligations.
4. ⬜ Executable Classification Protocol v0.1.
5. ⬜ Positive direct challenge.
6. ⬜ Negative/failure-terminal challenge.
7. ⬜ Direct method-boundary challenge against Analysis / Comparison / Specification / Diagnosis.
8. ⬜ Competent-baseline `NO_GAIN` challenge.
9. ⬜ Strongest-reasonable-baseline comparison.
10. ⬜ First external application.
11. ⬜ Deterministic same-project retrace.
12. ⬜ Additional materially different external domains.
13. ⬜ Maturity audit under frozen axes.
14. ⬜ Independent-evaluator infrastructure only if the accumulated evidence warrants it.

## Evidence discipline / 증거 규율

- Task-interface and protocol construction are infrastructure, not direct method evidence.
- Constructed challenges, external applications, reproducibility evidence, and maturity audits remain separate evidence classes.
- A PASS, FAIL, `NO_GAIN`, boundary result, or underdetermined result does **not** decide method survival, merger, absorption, or deletion.
- Shared-core support does not directly validate Classification.
- External origin does not imply independent-evaluator validation.
- Same-project retrace does not imply independent replication.
- A classification baseline must receive the same frozen task, class schema, criterion source, and claim-relevant information as the DSD run.

## DSD layer use / DSD 층위 사용

Classification activates only the layers required by the task:

- **Formation** when channel/state admission, absence, undefinedness, or composition status is class-relevant;
- **General Property** when typed applicability, prerequisites, definedness, or property values are class-relevant;
- **Static Aggregation** only when aggregate descriptors are explicitly part of the criterion, with collision/information-loss checks;
- **Dynamics** when classification depends on time-indexed state, transition class, or lineage;
- **Optional specializations** only when explicitly required by the class criterion.

No unused DSD layer is activated merely to make the classification record more elaborate.

## Minimum Classification result / 최소 산출물

A valid run must record at least:

```text
CLASSIFICATION_TASK_ID
SUBJECT_SET
TASK_SCOPE
TARGET_RESOLUTION
CLASS_SCHEMA_OR_GENERATION_POLICY
CLASS_CRITERIA
CRITERION_SOURCE
FEATURE_BASIS_AND_PROVENANCE
DSD_LAYERS_USED
DOMAIN_BRIDGE_IF_ANY
CLASS_ASSIGNMENTS
MEMBERSHIP_STATUS
JUSTIFICATION_TRACE
BOUNDARY_OR_UNDERDETERMINED_CASES
MISSING_INFORMATION_RECORD
LIMITS
```

If a hierarchy, equivalence class, partial order, temporal class transition, aggregate criterion, or multi-label result is claimed, its additional obligations must be recorded explicitly.

## Current status / 현재 상태

```text
DEDICATED_CLASSIFICATION_PROTOCOL: not established
TASK_INTERFACE_DRAFT: v0.1 created
DIRECT_CLASSIFICATION_PILOTS: 0
EXTERNAL_CLASSIFICATION_APPLICATIONS: 0
REPRODUCIBILITY_CASES: 0
INDEPENDENT_CLASSIFICATION_VALIDATION: not established
CLASSIFICATION_METHOD_MATURITY_CLASSIFICATION: proposed/developing
CURRENT_CLASSIFICATION_EVIDENCE_STATUS: pre_validation
```

## Next / 다음

Run the pre-protocol boundary-attack stage against the Task Interface v0.1 draft. The attack stage must be allowed to return non-destructive amendments, blocking defects, or no amendment; it must not be used to predetermine that Classification survives or should be removed.