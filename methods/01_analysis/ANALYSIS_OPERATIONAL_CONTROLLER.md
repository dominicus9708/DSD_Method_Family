# DSD Analysis Operational Controller / DSD 분석론 운영 제어기

Status: **temporary-branch canonical dry run; not on main**

Use this controller only when one declared Analysis target has material intermediate requirements, multiple sufficient routes, multiple representations, or claim-relevant reductions.

It receives an already-declared claim. It does not create or replace domain requirements.

## 1. Declared-claim lock and requirement relation

Record only claim-relevant axes.

```text
DECLARED_CLAIM_LOCK:
ACTIVE_REQUIREMENT_AXES:
INTERMEDIATE_REQUIREMENT:
RELATION_TO_DECLARED_CLAIM:
IMPLICATION_OR_PRESERVATION_BASIS:
```

Candidate axes include scope, quantifier, locality, uniformity, moment, norm, sign, support, aggregation, and precision.

Allowed relation vocabulary:

```text
REQUIRED_MATCH
PROVEN_STRONGER_SUFFICIENT
CONDITIONAL_STRONGER_SUFFICIENT
WEAKER_INSUFFICIENT
INCOMPARABLE
RELATION_UNDETERMINED
```

Do not force heterogeneous axes into one total order without an explicit implication or preservation rule.

## 2. Dependency/frontier representation

When several routes are material, distinguish:

```text
AND_PREREQUISITE
OR_SUFFICIENT_ROUTE
THEOREM_OR_DOMAIN_GATE
BRIDGE
SUPPORTING_LEMMA
ATTACK_METHOD
COMPUTATIONAL_CERTIFICATE
```

Preserve plural minimal dependency frontiers when more than one sufficient route remains.

This is a structural representation, not a scheduler. It does not decide which computation or project action must be run next.

## 3. Representation and information relation

Use claim-relevant relation labels:

```text
IDENTICAL
BIJECTIVE_EXACT
ISOMETRIC_OR_PARSEVAL_EQUIVALENT
FIXED_WEIGHT_EQUIVALENT
PROJECTION
CONTRACTION
COARSENING
ONE_WAY_BOUND
SIBLING_CONTRACTIONS
INDEPENDENT
UNKNOWN
```

Merge structural obligations only under established claim-relevant equivalence.

Equal outputs, a shared latent parent, or a one-way bound do not by themselves establish equivalence.

Record separately:

```text
CLAIM_STRENGTH_ESCALATION
REPRESENTATION_INFORMATION_LOSS
```

A route may simultaneously impose a stronger sufficient condition and discard source information.

## 4. Descriptive branch state

When useful:

```text
DIRECT_STRUCTURAL_OBLIGATION
SUPPORTING
OPTIONAL_STRONGER
DORMANT
FROZEN_UNDER_CURRENT_INPUTS
CLOSED
INVALIDATED_UNDER_SCOPE
```

For frozen branches record:

```text
FROZEN_REASON:
PRESERVED_RESULTS:
REOPEN_CONDITION:
```

`FROZEN_UNDER_CURRENT_INPUTS` does not mean false or impossible.
These states do not allocate resources or execution priority.

## 5. Method handoffs

If the primary operation becomes:

- authoring or organizing requirements -> **DSD Specification**;
- source-to-target representation mapping -> **DSD Transformation**;
- deciding what to evaluate or omit, or implementing reuse/cache -> **DSD Computation**;
- intentional representation reduction -> **DSD Compression**;
- live lifecycle/resource/monitoring orchestration -> **DSD Operation**;
- cross-target structural judgment -> **DSD Comparison**;
- criterion-based class assignment -> **DSD Classification**;
- source/context/interpretive-bridge reading -> **DSD Interpretation**.

## 6. Gain recording

Optional multi-label record:

```text
THEOREM_GAIN
STRUCTURAL_GAIN
COMPUTATIONAL_GAIN
REPRODUCIBILITY_GAIN
AUDIT_GAIN
NEGATIVE_NARROWING_GAIN
NO_DEMONSTRATED_GAIN
```

Gain labels do not alter the external-domain validity standard.

## 7. Safeguards

- No automatic branch deletion.
- No scalar total ordering without justification.
- No weaker condition is called sufficient without an argument.
- No stronger sufficient condition is called necessary without an argument.
- No representation merge follows from equal output or shared parenthood alone.
- No external-domain verdict is generated from DSD structural classification alone.
- No historical record is invalidated merely because it predates this controller.

## 8. Shared-core relation

This controller does not reopen SC-01 through SC-10.

- claim-requirement relation is adjacent to SC-04 but remains Analysis-specific at this stage;
- representation/information checks operationalize SC-03 and SC-05;
- gain and external-standard guards remain consistent with SC-08 and SC-10.

Independent receiving-method evidence is required before proposing a new shared-core obligation.
