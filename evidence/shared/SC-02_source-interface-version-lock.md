# SC-02 — Source / Interface / Version Lock / 소스·인터페이스·버전 잠금 검증

Status: **promoted_with_conditions**
Date: 2026-09-06
Evidence scope: `shared_method_family`
Case origin: `synthetic_constructed_benchmark`
DSD interface profile date: `2026-09-05`

## 1. Result / 결과

`Source / Interface / Version Lock` is promoted as a **conditional shared-core rule**.
A representative method from each of the eight higher-level fields was tested against three deliberately destabilizing perturbations:

- `S`: source substitution — a temporal/transition claim is sourced to Static Aggregation instead of Dynamics;
- `V`: semantic version drift — a synthetic incompatible snapshot changes whether assigned value `v` is part of operational-channel identity;
- `I`: optional-interface omission — the record omits whether Property Core is used.

```text
SOURCE_SUBSTITUTION_CHECKS: 8/8 detected
SEMANTIC_VERSION_DRIFT_CHECKS: 8/8 detected
INTERFACE_OMISSION_CHECKS: 8/8 detected
NEGATIVE_CONTROL: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
DIRECT_METHOD_VALIDATION: not claimed
```

Invariant meaning:

> A method result may depend not only on case data but also on the semantics supplied by a particular source, interface profile, and revision. Claim-relevant dependencies must therefore be locked or explicitly placed in a proven equivalence class before the result is interpreted or reproduced.

## 2. Locked source package / 잠근 소스 패키지

```text
Formation Axiom System — 2026.08.06
Property Axiom System — 2026.09.01
Channel-Indexed Static Aggregation — 2026.09.02
Structural Reorganization Dynamics — 2026.08.12 current supplied manuscript
```

The main benchmark uses Formation + Dynamics.
Property is activated only in the interface-omission perturbation.
Static Aggregation is used as an intentionally wrong source in the source-substitution perturbation.

## 3. Source basis / 소스 근거

### Formation Axiom System

Stage VI forms admitted operational channels with typed identity

```text
c = (p,a,lambda,v,rho)
```

and the assigned value `v` is part of channel identity.

### Property Axiom System

The Property system is parameterized by a fixed Stage-VI Formation background and does not alter inherited formation assignments, roles, or operational-channel identity.

### Channel-Indexed Static Aggregation

The Static Aggregation paper uses the same fixed predecessor interfaces but explicitly remains a static analytic construction. It does not introduce an evolution law.

### Structural Reorganization Dynamics

The Dynamics paper fixes the Stage-VI Formation background during regular dynamics and does not write one unchanged inherited channel as `c(t)=(...,v(t),...)` when `v` changes. Formation-level change is handled through transition/lineage machinery. Property, static analytic realization, and realized-axis geometry are optional interfaces rather than universal prerequisites.

## 4. Locked microcase / 고정 microcase

```text
t0:
  c0=(p,a,lambda,3,rho)

t1:
  c1=(p,a,lambda,4,rho)

formation transition J_0,1 supplied
(c0,c1) in Lambda_0,1

optional Property slice at t1:
  q(x)=0
  status=defined_zero
```

Under the locked current Formation/Dynamics interface:

- `c0 != c1`;
- succession may be asserted through the supplied lineage relation;
- `q(x)=defined_zero` is available only in an execution that actually supplies the Property Core.

## 5. Perturbations / 교란 연산

### S — Source substitution

Replace Dynamics with **Static Aggregation** as the source for a temporal/transition claim.
Static Aggregation can supply static analytic readouts but does not itself supply regular epochs, formation transitions, or lineage.

### V — Semantic version drift

Keep the source name but replace the current identity rule with a deliberately incompatible synthetic snapshot `V*`:

```text
current: assigned value v is part of channel identity
V*:      assigned value v is not part of channel identity
```

`V*` is **not** claimed to be an actual historical DSD revision. It is a counterexample used only to test whether an unlocked semantic revision can change a method result.

### I — Optional-interface omission

Delete the field

```text
PROPERTY_CORE: used / not used
```

from the execution record.
Then a formation-only execution and a property-extended execution become indistinguishable at the record level, even though the availability of the property-status claim differs.

## 6. Eight-field transfer test / 8개 상위 분야 교차 시험

| Field | Representative method | S: source substitution | V: version drift | I: interface omission | Result |
|---|---|---|---|---|---|
| I. Structural Description & Understanding | Analysis | temporal-transition analysis loses source support | one-channel value change vs two-channel succession changes | availability of property-status analysis becomes ambiguous | PASS: 3/3 detected |
| II. Criteria & Validation | Audit | transition claim has an invalid source trace | audit pass/fail for same-channel claim can reverse | interface obligations cannot be reconstructed | PASS: 3/3 detected |
| III. Construction & Transformation | Transformation | temporal source-target mapping cannot be justified as a transition from Static alone | identity-preserving map vs successor map changes | property-coordinate preservation obligation is ambiguous | PASS: 3/3 detected |
| IV. Evidence & Lineage | Lineage | lineage relation loses its dynamic source basis | whether a lineage edge is required changes | existence of a property-component lineage target is ambiguous | PASS: 3/3 detected |
| V. Reduction & Representation | Compression | preservation obligations for a temporal record are under-specified | whether `v` may be discarded without identity loss changes | need for property-status sidecar is ambiguous | PASS: 3/3 detected |
| VI. Inverse Inference & Reconstruction | Reconstruction | past transition/lineage reconstruction is reduced to an unsupported static source | admissible reconstruction changes between one-channel and successor-channel histories | whether property state belongs to the reconstruction target is ambiguous | PASS: 3/3 detected |
| VII. Computation & Selection | Computation | transition-aware evaluation branch loses source justification | whether a channel-identity computation key can be reused changes | whether a property branch must be evaluated is ambiguous | PASS: 3/3 detected |
| VIII. Dynamics & Action | Simulation | Static alone cannot justify a dynamic transition law | formation transition vs ordinary value evolution changes the model | whether the state includes a Property slice is ambiguous | PASS: 3/3 detected |

This is a shared-rule transfer test, not direct validation of the selected methods as complete methodologies.

## 7. Negative control / 음성 대조군

SC-02 does **not** require every DSD document and every downstream layer to be locked in every case.

A minimal lock is sufficient when:

1. an unused layer is explicitly recorded as `not used`;
2. a revision cannot affect any coordinate or claim actually used by the method; or
3. two revisions have been separately proved equivalent over the declared interface, in which case a documented `equivalence_class` or revision range may replace one exact revision.

Source identity and the equivalence rule must still be recorded.

Therefore the shared rule is not “snapshot everything”. It is:

> **Lock every source, interface branch, and revision whose semantics can affect the claimed result.**

## 8. Standard lock record / 표준 잠금 기록

```text
SOURCE_LOCK:
  DOCUMENT_OR_DATA_SOURCE:
  SOURCE_VERSION_OR_DATE:
  SOURCE_ID_OR_COMMIT_IF_AVAILABLE:

INTERFACE_LOCK:
  FORMATION_LAYER: used / not used
  PROPERTY_CORE: used / not used
  STATIC_AGGREGATION_LAYER: used / not used
  DYNAMICS_LAYER: used / not used
  OPTIONAL_SPECIALIZATION: supplied / not supplied

VERSION_EQUIVALENCE_RULE:
  exact_revision / explicit_equivalence_class / declared_range

LOCK_CHANGE_RECORD:
  none / explicit_revision_with_reason
```

## 9. Promotion test / 승격 시험

```text
SOURCE_SUPPORT: pass
SAME_SEMANTIC_MEANING_ACROSS_METHODS: pass
SOURCE_SUBSTITUTION_COUNTEREXAMPLE: pass
SEMANTIC_VERSION_DRIFT_COUNTEREXAMPLE: pass
OPTIONAL_INTERFACE_OMISSION_COUNTEREXAMPLE: pass
NON_TRANSFER_CASE_IDENTIFIED: pass
METHOD_TASK_REDEFINITION: none
DIRECT_VALIDATION_SEPARATION: pass
SHARED_CORE_PROMOTION_RESULT: promoted_with_conditions
```

## 10. Transfer conditions / 적용 조건

Apply SC-02 when:

- a method claim depends on definitions, identity rules, status rules, optional interfaces, representation choices, or domain/source semantics that can vary across sources or revisions;
- reproducibility, comparison, auditability, or historical traceability is claimed;
- a downstream method inherits an upstream interface whose revision materially affects the result.

A narrower equivalence-class lock may be used only when equivalence over the actually used interface has been established separately.

## 11. Evidence limits / 한계

- This is a synthetic cross-field transfer pilot.
- `V*` is an intentionally incompatible counterfactual interface, not an asserted historical DSD revision.
- One representative method per higher-level field was tested.
- It does not validate the overall correctness, performance, or usefulness of all 22 methods.
- No real event, judicial case, historical case, personal case, or empirical dataset is included.

## 12. Relation to SC-01 / SC-01과의 관계

SC-01 can preserve status and typed-domain distinctions only after the relevant interface has been identified. SC-02 therefore supplies the provenance/version condition needed to know **which distinctions the active interface actually requires**.

The two rules remain distinct:

```text
SC-01 = preserve claim-relevant distinctions
SC-02 = lock the semantics that determine which distinctions and rules are active
```

## 13. Next shared-core candidate / 다음 후보

`SC-03 — Explicit Bridge Discipline` should be tested separately.
