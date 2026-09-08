# DSD Design Protocol v0.1 / DSD 설계론 프로토콜 v0.1

Status: **initial executable protocol / validation pending**  
Date: **2026-09-08**  
Method: **DSD Design / DSD 설계론**  
Higher field: **III. Construction & Transformation / 구성·변환**

## 0. Protocol boundary / 프로토콜 경계

This protocol is the first executable DSD Design protocol.
It is derived from the pre-protocol task interface and its first boundary amendment:

```text
TASK_INTERFACE_v0.1-draft.md
+ TASK_INTERFACE_BOUNDARY_AMENDMENT_001.md
```

The eight planning-stage boundary counterexamples in `BOUNDARY_COUNTEREXAMPLES_v0.1-draft.md` found no method collapse with Specification, Synthesis, Transformation, or Optimization, but required two non-breaking safeguards:

```text
CONSTRAINT_SOURCE_OR_SPECIFICATION
AUXILIARY_METHODS_OR_HANDOFFS
```

Protocol establishment does **not** establish method maturity, external validity, engineering usefulness, or superiority over existing design methods.
Direct Design pilots begin only after this protocol is frozen for a case.

## 1. Method task / 방법 과제

DSD Design constructs or filters a target structure or admissible target family from a declared design task, hard constraints, and an explicit candidate/construction basis while preserving the DSD distinctions and external-domain boundaries that materially affect admissibility.

Compact form:

```text
DECLARED DESIGN TASK
+ CANDIDATE / CONSTRUCTION BASIS
+ SELECTED DSD INTERFACE
+ EXPLICIT DOMAIN BRIDGE / EXTERNAL STANDARD when required
-> CANDIDATE DESIGN FAMILY
-> STATUS-SENSITIVE ADMISSIBILITY EVALUATION
-> ADMISSIBLE TARGET / ADMISSIBLE FAMILY / JUSTIFIED NON-SUCCESS STATUS
```

Design does not supply a universal candidate generator and does not invent missing domain design knowledge.

Design is distinct from:

```text
Specification   -> declares requirements and admissibility constraints
Design          -> constructs or filters a target/design space under those constraints
Synthesis       -> validates or performs substantive parts-to-whole composition
Transformation  -> determines preservation/loss under a source-target map
Optimization    -> ranks/selects admissible alternatives under an objective
Audit           -> retraces the completed execution against scope, procedure, evidence, and rules
```

A workflow may invoke several of these methods, but their substantive verdicts remain separately identifiable.

## 2. Protocol run lock / 실행 잠금

Every v0.1 run must declare the following core fields before candidate evaluation begins, except fields explicitly marked conditional.

```text
DESIGN_TASK_ID:
PROTOCOL_VERSION: v0.1
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
GOALS:
HARD_CONSTRAINTS:
CONSTRAINT_SOURCE_OR_SPECIFICATION:
BASE_STRUCTURE_OR_PREDECESSOR:
TARGET_DSD_LAYER_SCOPE:
TARGET_RESOLUTION:
CANDIDATE_OR_CONSTRUCTION_BASIS:
CANDIDATE_GENERATION_RULE:
CANDIDATE_COVERAGE:
DSD_INTERFACE_PROFILE:
VALIDATION_OR_ACCEPTANCE_RULE:
```

Conditional task fields:

```text
SOFT_PREFERENCES:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
AUXILIARY_METHODS_OR_HANDOFFS:
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
```

Inactive conditional fields are recorded as `not_used` or omitted consistently; they are not filled with invented content.

### 2.1 Claim lock

The run must state what it is claiming.

Allowed `CLAIMED_OUTPUT_LEVEL` values are:

```text
DESIGN_SPACE
ADMISSIBLE_TARGET
UNIQUE_TARGET
PARTIAL_TARGET
```

- `DESIGN_SPACE`: return the admissible family within the declared candidate/construction coverage. Completeness beyond that coverage is not implied.
- `ADMISSIBLE_TARGET`: return at least one traceable admissible target without claiming optimality or uniqueness.
- `UNIQUE_TARGET`: claim that one target is determined at the declared scope and resolution.
- `PARTIAL_TARGET`: resolve only a declared subset of target coordinates/relations.

A stronger claim requires correspondingly stronger candidate coverage and determinacy evidence.

## 3. Constraint discipline / 제약 규율

### 3.1 Hard constraints

Hard constraints determine admissibility.
Their source must be traceable through `CONSTRAINT_SOURCE_OR_SPECIFICATION` when the source is external, upstream, or otherwise material to the claim.

Possible sources include:

- declared task owner;
- upstream DSD Specification record;
- theorem or proof obligation;
- physical or technical limit;
- domain standard or competent authority;
- explicit predecessor-state requirement.

### 3.2 Soft preferences

```text
SOFT_PREFERENCE != HARD_CONSTRAINT
```

A Design run must not silently promote a soft preference into a hard constraint after inspecting candidates in order to force determinacy.

If a task owner, Specification process, or competent domain authority changes the requirement, that is a new/upstream task revision and must be locked before the revised Design verdict is evaluated.

Preference-based ranking among already admissible candidates belongs to Optimization unless it has become a legitimate hard constraint upstream before the Design run.

## 4. Candidate/construction basis / 후보·구성 기반

DSD Design assumes no canonical universal candidate generator.
At least one reproducible basis must be supplied, such as:

- explicit candidate family;
- construction grammar;
- allowed parts plus constructors;
- parameterized target schema;
- theorem/domain rule generating a candidate family;
- externally generated candidate set;
- another explicit mechanism sufficient to reproduce the covered design family.

If no adequate basis exists, the run may validly end as `DESIGN_BLOCKED`; the protocol must not fabricate candidates to avoid that result.

### 4.1 Candidate coverage

Record exactly one:

```text
CANDIDATE_COVERAGE:
  exhaustive
  non_exhaustive
  unknown
```

`DESIGN_INFEASIBLE` is permitted only when:

1. the covered candidate/construction space is established as exhaustive for the claimed task and every candidate fails at least one required condition; or
2. an explicit impossibility argument establishes that no target can satisfy the hard constraints.

Failure to find a target in a non-exhaustive or unknown search is not global infeasibility.

## 5. DSD interface activation / DSD 인터페이스 활성화

The minimum-layer rule applies.
Do not activate a downstream DSD layer merely because it exists.

### 5.1 Formation

Use Formation when new structural admission, roles, assignments, operational channels, or formation-compatible target structure are material.

When a downstream design task inherits an already fixed Stage-VI formation background, lock that predecessor rather than silently redesign it.

Preserve claim-relevant distinctions including, as applicable:

```text
UNDEFINED_ASSIGNMENT
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
CHANNEL_ABSENCE
ADMITTED_CHANNEL_WITH_ZERO_COMPONENT_TERM
```

### 5.2 General Property

Activate only when typed properties, applicability, contextual prerequisites, or partial property assignments materially affect the target.

Preserve as applicable:

```text
UNDECLARED
PROFILE_UNAVAILABLE
INAPPLICABLE
PREREQUISITE_UNSATISFIED
APPLICABLE_BUT_UNDEFINED
DEFINED_ZERO
DEFINED_NONZERO_OR_OTHER_DEFINED_VALUE
```

A Property extension does not silently alter the inherited formation identity.

### 5.3 Static Aggregation

Activate only when candidate admissibility or evaluation depends on a declared analytic readout or aggregate.

Aggregate equality alone does not prove support, decomposition, source structure, or target identity equality.
A reconstruction claim requires an additional injectivity or reconstruction condition appropriate to the declared admissible class.

### 5.4 Dynamics

Activate only when trajectory, transition, propagation, regular-epoch, time-dependent, or lineage obligations materially affect the target.

A formation-level identity change is not represented as ordinary value evolution of one unchanged inherited channel.
If predecessor-successor identity is claimed across such a change, the lineage relation must be explicit.

### 5.5 Optional specialization

Activate geometry or another specialization only when supplied by the declared task or an explicit domain/specialization bridge.
No cross-layer bridge is inferred from names or intuition alone.

## 6. Auxiliary-method and handoff discipline / 보조 방법·인계 규율

When another DSD method materially supplies a verdict used by Design, record it under:

```text
AUXILIARY_METHODS_OR_HANDOFFS:
```

Examples:

```text
Specification -> locked requirement/status record -> Design
Synthesis -> composition-legitimacy verdict -> Design admissibility
Transformation -> preservation/loss verdict -> Design admissibility
Design admissible family -> Optimization
completed Design execution -> Audit
```

Boundary rule:

```text
Design may consume a neighboring-method result.
Design does not absorb the neighboring method's operation, validation standard, failure state, or direct evidence.
```

### Candidate generation versus Synthesis

Design may construct a symbolic candidate description from a licensed candidate basis.
If admissibility requires a substantive parts-to-whole composition claim, the Synthesis verdict remains separate.

### Candidate evaluation versus Transformation

Design may propose a target schema or regime.
If admissibility requires a claim about what a fixed source preserves or loses when mapped into that target, the Transformation verdict remains separate.

### Admissible family versus Optimization

Design may filter by hard constraints.
Ranking or choosing the best admissible candidate under an objective, cost, utility, preference, or trade-off function is Optimization.

## 7. Candidate record / 후보 레코드

Each candidate or symbolic candidate class that materially supports the final verdict must be retraceable.

Recommended record:

```text
CANDIDATE_ID:
CANDIDATE_SOURCE_OR_GENERATION_TRACE:
STRUCTURAL_DESCRIPTION_AT_TARGET_RESOLUTION:
REQUIRED_DSD_CHECKS:
CLAIM_RELEVANT_STATUS_RECORD:
DOMAIN_OR_EXTERNAL_CHECKS:
AUXILIARY_METHOD_RESULTS_IF_ANY:
ADMISSIBILITY_RESULT:
  admissible
  rejected
  unresolved
  blocked
REJECTION_OR_UNRESOLVED_BASIS:
```

A candidate is `admissible` only when every required check for the declared output level is established at the declared resolution.
Unknown, inapplicable, undefined, absent, and zero states are not automatically collapsed into one Boolean failure or success state.

## 8. Construction procedure v0.1 / 구성 절차

```text
D1  LOCK TASK AND CLAIM
D2  LOCK CONSTRAINT SOURCES
D3  LOCK CANDIDATE / CONSTRUCTION BASIS AND COVERAGE
D4  LOCK SELECTED DSD INTERFACES AND REQUIRED BRIDGES
D5  CONSTRUCT / ENUMERATE COVERED CANDIDATES
D6  RUN STATUS-SENSITIVE DSD ADMISSIBILITY CHECKS
D7  RUN DOMAIN / EXTERNAL / AUXILIARY-METHOD CHECKS WHEN ACTIVE
D8  CONSTRUCT ADMISSIBLE FAMILY
D9  CHECK CLAIMED OUTPUT LEVEL
D10 ASSIGN TERMINAL DESIGN STATUS
D11 RECORD PROTOCOL CONFORMANCE SEPARATELY
D12 RECORD METHOD-GAIN STATUS SEPARATELY
D13 RECORD LIMITS AND REPRODUCIBILITY DATA
```

### D1 — Lock task and claim

Freeze scope, goals, hard constraints, target resolution, and output level before candidate evaluation.

### D2 — Lock constraint sources

Record where claim-relevant hard constraints came from and preserve any upstream unresolved/open conditions.

### D3 — Lock candidate basis and coverage

Freeze the candidate generator, grammar, family, or other construction basis and the coverage claim.

### D4 — Lock interfaces and bridges

Activate only the DSD layers and external/domain bridges materially required by the task.

### D5 — Construct or enumerate candidates

Use only the declared candidate basis.
If stochastic or heuristic generation is used, record seeds, ordering, stopping conditions, or other information needed for the claimed level of retraceability.

### D6 — Run DSD admissibility checks

Preserve claim-relevant status distinctions rather than zero-padding or Boolean-collapsing them.

### D7 — Run external and auxiliary checks

Use external standards and neighboring-method verdicts only where explicitly activated.
Keep those validation authorities separate from DSD-internal structural checks.

### D8 — Construct admissible family

Construct the admissible subfamily from candidates whose required checks are established.
Rejected, unresolved, and blocked candidates remain traceable where they materially support the result.

### D9 — Check output level

- `DESIGN_SPACE`: return the covered admissible family with its coverage label.
- `ADMISSIBLE_TARGET`: return at least one admissible target. If several survive, any selection rule used by Design must have been locked before evaluation and must not claim optimality.
- `UNIQUE_TARGET`: uniqueness must follow from the declared task and adequate coverage/determinacy evidence; an arbitrary tie-breaker does not establish uniqueness.
- `PARTIAL_TARGET`: resolve only the declared partial target and list unresolved fields outside the claim.

### D10 — Assign terminal Design status

Use only the terminal ledger in Section 9.

### D11 — Record protocol conformance

Evaluate whether the run itself followed this protocol independently of whether the target was admissible.

### D12 — Record method gain

Only when a baseline comparison has actually been performed; otherwise use `NOT_ASSESSED`.

### D13 — Record limits and reproducibility

Preserve enough execution detail for later retrace at the declared resolution.

## 9. Terminal Design-status ledger / 종결 설계 상태

```text
DESIGN_ADMISSIBLE
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

### `DESIGN_ADMISSIBLE`

At least one target satisfies every required condition for the declared output level and resolution.

This does not imply optimality, uniqueness, external approval, empirical validation, safety certification, or practical superiority.

### `DESIGN_INFEASIBLE`

No target satisfies the hard constraints, and the no-target claim is supported by exhaustive coverage or an explicit impossibility argument.

### `DESIGN_UNDERDETERMINED`

Admissible possibilities remain, but the declared task does not support the stronger requested result.

Examples:

- `UNIQUE_TARGET` requested while several materially distinct admissible targets remain;
- required target coordinates remain unconstrained at the claimed resolution;
- a global no-target claim is requested from non-exhaustive/unknown coverage.

### `DESIGN_BLOCKED`

A required prerequisite for constructing or validating the declared Design result is unavailable.

Examples:

- no reproducible candidate/construction basis;
- missing predecessor-layer data;
- missing required domain bridge or external standard;
- missing prerequisite needed to perform a claim-required check.

A blocked result is a valid protocol outcome when the missing dependency is explicitly identified rather than silently fabricated.

## 10. Protocol-conformance ledger / 프로토콜 준수 장부

Target/design status and protocol-conformance status are different ledgers.

```text
DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED
```

Representative nonconformance conditions:

```text
POST_HOC_SOFT_TO_HARD_PROMOTION
UNDECLARED_CANDIDATE_BASIS_CHANGE
UNSUPPORTED_EXHAUSTIVENESS_CLAIM
INFEASIBLE_FROM_NONEXHAUSTIVE_FAILURE_TO_FIND
CLAIM_RELEVANT_STATUS_COLLAPSE
REQUIRED_BRIDGE_OMISSION
EXTERNAL_STANDARD_SUBSTITUTION
HIDDEN_OPTIMIZATION
NEIGHBORING_METHOD_VERDICT_ABSORPTION
UNRECORDED_TASK_REVISION
UNSUPPORTED_UNIQUENESS_CLAIM
```

A run may therefore be:

```text
DESIGN_BLOCKED + CONFORMANT
DESIGN_UNDERDETERMINED + CONFORMANT
DESIGN_ADMISSIBLE + NONCONFORMANT   # claimed target exists, but the recorded method execution violated protocol
```

The last combination must not be treated as valid direct evidence for protocol success.

## 11. Method-gain ledger / 방법 이득 장부

Method utility remains separate from target/design status and protocol conformance.

```text
DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

`GAIN_ESTABLISHED` requires a declared baseline and an explicit gain criterion.
`NO_GAIN` is a valid non-failure method result.
Without a baseline comparison, the required value is `NOT_ASSESSED`.

Possible gain dimensions include, only when actually measured or demonstrated:

- improved distinction preservation;
- improved rejection-reason traceability;
- improved cross-method handoff clarity;
- improved reproducibility/retraceability;
- reduced unsupported design closure.

The protocol does not assume that DSD must outperform a competent domain-native design procedure.

## 12. Standard execution output / 표준 실행 산출물

Every v0.1 run records at minimum:

```text
DESIGN_RESULT_ID:
DESIGN_TASK_ID:
PROTOCOL_VERSION: v0.1
TASK_SCOPE:
CLAIMED_OUTPUT_LEVEL:
GOALS:
HARD_CONSTRAINTS:
CONSTRAINT_SOURCE_OR_SPECIFICATION:
BASE_STRUCTURE_OR_PREDECESSOR:
TARGET_DSD_LAYER_SCOPE:
TARGET_RESOLUTION:
CANDIDATE_OR_CONSTRUCTION_BASIS:
CANDIDATE_GENERATION_RULE:
CANDIDATE_COVERAGE:
DSD_INTERFACE_PROFILE:
VALIDATION_OR_ACCEPTANCE_RULE:
CANDIDATES_ACTUALLY_EVALUATED_OR_SYMBOLIC_FAMILY:
CANDIDATE_STATUS_RECORD:
ADMISSIBLE_TARGETS_OR_ADMISSIBLE_FAMILY:
REJECTED_CANDIDATE_REASONS:
UNRESOLVED_FIELDS:
TERMINAL_DESIGN_STATUS:
TERMINAL_STATUS_BASIS:
DESIGN_PROTOCOL_CONFORMANCE:
DESIGN_METHOD_GAIN_STATUS:
LIMITS:
REPRODUCIBILITY_RECORD:
```

Conditional output fields:

```text
SOFT_PREFERENCES:
DOMAIN_BRIDGE:
EXTERNAL_STANDARD:
AUXILIARY_METHODS_OR_HANDOFFS:
NONOPTIMIZATION_SELECTION_RULE_IF_NEEDED:
TARGET_SELECTION_BASIS_IF_ONE_TARGET_RETURNED:
IMPOSSIBILITY_ARGUMENT_IF_USED:
BASELINE_IF_GAIN_ASSESSED:
GAIN_CRITERION_IF_ASSESSED:
```

## 13. Minimum output by terminal status / 상태별 최소 산출물

### 13.1 `DESIGN_ADMISSIBLE`

Must include:

- at least one reproducibly identified admissible target or admissible family;
- trace from claim-relevant target coordinates/relations to the constraints/rules that license them;
- unresolved fields outside the claimed scope/resolution;
- no implicit claim of optimality, uniqueness, or external validity.

### 13.2 `DESIGN_INFEASIBLE`

Must include:

- exhaustive-space justification or impossibility argument;
- violated condition classes;
- enough rejected-candidate or symbolic proof structure to retrace the no-target claim.

### 13.3 `DESIGN_UNDERDETERMINED`

Must include:

- the stronger requested output that could not be supported;
- at least one surviving alternative family, unresolved discriminator, or unconstrained field;
- what additional task input would be required to resolve the claim without silently invoking Optimization.

### 13.4 `DESIGN_BLOCKED`

Must include:

- the specific missing prerequisite, bridge, source datum, standard, or candidate basis;
- the downstream checks that cannot be performed because it is missing.

## 14. Core protocol checks / 핵심 프로토콜 검사

A conformant v0.1 execution checks, when applicable:

```text
P1  task and claim locked before evaluation
P2  hard-constraint provenance preserved
P3  no post-hoc soft-to-hard promotion
P4  candidate/construction basis explicit and reproducible at claimed level
P5  candidate coverage explicitly classified
P6  no infeasibility overclaim from non-exhaustive/unknown search
P7  only required DSD layers activated
P8  claim-relevant DSD statuses preserved
P9  required bridges explicit
P10 external standard remains external validation authority
P11 neighboring-method substantive verdicts remain separately identifiable
P12 no hidden optimization in Design
P13 uniqueness claim separately justified
P14 aggregate/reconstruction claims disciplined when Static Aggregation is active
P15 transition/lineage discipline preserved when Dynamics is active
P16 terminal Design status supported by recorded basis
P17 protocol conformance recorded separately from Design outcome
P18 method gain recorded only with an actual baseline comparison
P19 limits and unresolved fields preserved
P20 execution sufficiently retraceable at declared resolution
```

## 15. Reproducibility / 재현성

Record enough information for a later retrace:

```text
PROTOCOL_VERSION: v0.1
DESIGN_TASK_ID:
TASK_REVISION_OR_HASH:
CONSTRAINT_SOURCE_IDS_OR_VERSIONS:
CANDIDATE_BASIS_ID_OR_VERSION:
CANDIDATE_GENERATION_RULE_VERSION:
CANDIDATE_COVERAGE_BASIS:
DSD_INTERFACE_PROFILE_DATE:
ACTIVE_DSD_LAYERS:
DOMAIN_BRIDGE_VERSION_IF_ACTIVE:
EXTERNAL_STANDARD_VERSION_IF_ACTIVE:
AUXILIARY_METHOD_PROTOCOLS_AND_RESULT_IDS_IF_ACTIVE:
ORDERING_OR_RANDOM_SEED_IF_RELEVANT:
STOPPING_RULE_IF_RELEVANT:
MANUAL_JUDGMENT_POINTS:
OUTPUT_RECORD_ID:
```

Reproducibility at the recorded protocol level does not imply independent evaluator agreement or empirical correctness.

## 16. Case-ID and evidence convention / 사례 ID·증거 규칙

Protocol v0.1 fixes the Design evidence prefixes:

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
```

Every case additionally records:

```text
CASE_CLASS:
  positive
  negative_or_failure
  boundary
  no_gain
  baseline_comparison
  reproducibility
  external_application
  other_declared
```

A single case may satisfy more than one evidence category only when each claimed category is explicitly tested and separately reported.

Planning artifacts `DES-BND-DRAFT-*` remain pre-protocol records and are not retroactively promoted into direct v0.1 evidence.

## 17. Validation and scope / 검증·범위

Protocol-level success asks whether the run:

1. locks the task, constraints, candidate basis, coverage, DSD interfaces, and validation rule;
2. preserves hard/soft constraint provenance and prevents post-hoc determinacy forcing;
3. keeps absent, undefined, inapplicable, prerequisite-unsatisfied, zero, and other claim-relevant states distinct when the selected DSD interface requires them;
4. distinguishes covered candidate-space results from global completeness claims;
5. keeps Synthesis, Transformation, Optimization, Specification, Audit, and other substantive neighboring-method results separate when used;
6. assigns a terminal Design status only within the declared scope/resolution;
7. records protocol conformance and method gain on separate ledgers;
8. remains retraceable at the declared resolution.

It does not replace domain-specific engineering, architecture, mathematics, science, law, safety validation, artistic judgment, organizational design expertise, or other competent design authority.

## 18. v0.1 evidence state / v0.1 증거 상태

At protocol creation:

```text
DEDICATED_PROTOCOL: established at v0.1
DIRECT_CONSTRUCTED_PILOTS: 0
EXTERNAL_APPLICATIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
BASELINE_BENEFIT: not established
CURRENT_METHOD_EVIDENCE_STATUS: validation_pending
```

The next required step is the first **positive constructed Design challenge** under a protocol-frozen task record.
