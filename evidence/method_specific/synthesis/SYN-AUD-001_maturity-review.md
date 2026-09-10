# SYN-AUD-001 — DSD Synthesis Maturity Audit

Status: **COMPLETED — established method/protocol evidence maturity supported with explicit unresolved independent/practical limitations**  
Date: **2026-09-10**  
Audit ID: `DSD-AUDIT-20260910-SYNTHESIS-001`  
Audit method: **DSD Audit / DSD 감사**  
Audited method: **DSD Synthesis / DSD 합성론**  
Audited Synthesis protocol: **v0.1**  
Precommit: `SYN-AUD-001_precommit.md`  
Precommit commit: `ba966b5f12c5df89355ea557e7a1ff997e9f866f`

## 1. Maturity decision / 성숙도 판정

The frozen Synthesis corpus supports promotion of **DSD Synthesis method/protocol evidence maturity** from `proposed` to `established` under the current DSD method-family evidence framework.

The decision is not based on raw PASS count.
It is based on the combined architecture:

```text
frozen executable Protocol v0.1
positive direct case
negative/failure terminal discrimination
executable neighboring-method boundary case
preserved failed challenge design
multiple honest NO_GAIN cases
strongest-reasonable-baseline comparison
deterministic same-project retrace
three materially different external domains
source/bridge scope discipline
composition-basis / coverage / equivalence discipline
no identified core protocol defect requiring reopen
```

Audit result:

```text
AUDIT_STATUS: COMPLETED
AUDIT_EXECUTION_VERDICT: PASS
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
SYNTHESIS_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
EXTERNAL_APPLICATION_INCREMENT_FROM_AUDIT: 0
REPRODUCIBILITY_INCREMENT_FROM_AUDIT: 0
```

The established label is deliberately limited to **method/protocol evidence maturity within this project framework**.
It does not establish:

```text
INDEPENDENT_SYNTHESIS_VALIDATION
INDEPENDENT_REPLICATION
BROAD_INTER_RATER_AGREEMENT
MEASURED_PRACTICAL_SUPERIORITY
MEASURED_EFFICIENCY_ADVANTAGE
MEASURED_DEFECT_REDUCTION_ADVANTAGE
UNIVERSAL_EXTERNAL_GENERALITY
PERMANENT_METHOD_REGISTRY_SURVIVAL
PERMANENT_IRREDUCIBILITY_OR_NONMERGER
```

## 2. Frozen corpus used / 사용한 동결 증거

### Protocol and planning pressure

```text
PROTOCOL_v0.1
  commit 8787b242cb6648c47396151dbac3aadc19e3d184

PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
  preserved without refinement: 11
  preserved with non-breaking refinement: 5
  collapse: 0
  fundamental interface failure: 0
```

### Direct constructed evidence

```text
SYN-CH-001  positive                            28/28 PASS
SYN-CH-002  terminal-failure distinction       36/36 PASS
SYN-CH-003  neighboring-method boundary        46/46 PASS
SYN-CH-004  baseline challenge design          33/35 FAIL
            FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
SYN-CH-005  corrected competent baseline       37/37 PASS / NO_GAIN
SYN-CH-006  strongest-reasonable baseline      52/52 PASS / NO_GAIN
```

### Reproducibility

```text
SYN-CH-007
  deterministic same-project retrace
  48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

### External applications

```text
SYN-APP-001
  RFC 3986 / STD 66
  Internet identifier syntax / URI generic syntax
  40/40 PASS

SYN-APP-002
  BIPM SI Brochure 9th ed. v4.01 (2026)
  physical metrology / SI unit composition
  46/46 PASS

SYN-APP-003
  USB Type-C Release 2.0 frozen mechanical subset
  physical connector assembly / USB Type-C mating interface
  44/44 PASS
```

Frozen counts remain:

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

## 3. Maturity-axis scoring / 성숙도 축 판정

```text
M1  dedicated executable protocol                       PASS
M2  positive/negative terminal discrimination           PASS
M3  neighboring-method boundary discrimination          PASS
M4  NO_GAIN preservation                                PASS
M5  reproducibility/retraceability                       CONDITIONAL_PASS
M6  external application origin                         PASS
M7  strongest-reasonable-baseline comparison            PASS
M8  external source fidelity and bridge discipline      PASS
M9  established-level evidence breadth                  PASS
M10 independent/practical-performance evidence          UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect          PRESENT_NONFATAL
M12 maximum-supported-claim discipline                  PASS
M13 composition-basis / coverage / equivalence discipline PASS
M14 historical failure / anti-post-hoc preservation     PASS
M15 method-survival / merger-separation discipline      PASS
```

### M1 — PASS

`PROTOCOL_v0.1.md` is an executable parts-to-whole protocol with explicit locks for:

```text
task and output level
component identities/status source
composition rule/source
arity/order/multiplicity
composition-law profile
grouping/parenthesization
candidate basis and coverage
equivalence/canonicalization
interface/prerequisite conditions
Property lift/redeclaration
support/relation/status/decomposition/information loss
formation effect
partial residual obligations
static vs temporal process scope
neighboring-method handoffs
terminal status
protocol conformance
method gain
reproducibility data
```

No direct evidence required a core Protocol-v0.1 rewrite.

### M2 — PASS

The corpus spans the current Synthesis terminal outcomes.

`SYN-CH-001` demonstrates an admissible synthesis family.
`SYN-CH-002` directly separates:

```text
exhaustive all rejected
-> SYNTHESIS_INFEASIBLE

non-exhaustive coverage insufficient for requested closure
-> SYNTHESIS_UNDERDETERMINED

claim-required composition rule unavailable
-> SYNTHESIS_BLOCKED
```

Thus non-success states are not collapsed into one generic failure label.

### M3 — PASS

`SYN-CH-003` directly pressures the neighboring operations:

```text
missing architecture invention -> DESIGN_REQUIRED
representation conversion     -> TRANSFORMATION_REQUIRED
scalar/readout construction    -> AGGREGATION_REQUIRED
objective-based choice         -> OPTIMIZATION_REQUIRED
```

The Synthesis family remains a Synthesis result while downstream method operations remain handoffs.
No downstream verdict is silently absorbed into the Synthesis terminal ledger.

This establishes current **operational boundary separation** under Protocol v0.1.
It does not permanently settle every future registry-merger question; that is handled separately by M15.

### M4 — PASS

`SYN-CH-005` and `SYN-CH-006` both preserve `NO_GAIN` against competent baselines.

In `SYN-CH-006`, `B1_TYPED_COMPOSITION_GRAPH_CHECKER` received the same typed composition information and matched DSD on:

```text
status/Property lift
failure staging
grouping equivalence
relation retention
formation effect
raw/canonical closure
retraceability
```

The fact that DSD did not outperform the baseline was not converted into either superiority or method failure.

### M5 — CONDITIONAL_PASS

`SYN-CH-007` successfully retraces the immutable RFC application chain:

```text
REPRODUCIBILITY_LEVEL: deterministic_same_project
RETRACE_VERDICT: PASS
INDEPENDENT_REPLICATION: not established
BLINDED_REPRODUCTION: not established
```

This is meaningful reproducibility evidence but remains same-project and non-independent.
Therefore M5 cannot be `PASS` under the frozen criterion.

### M6 — PASS

Three external applications use external authorities for composition/interface legitimacy rather than treating Formation Clause VII or project notation as universal domain composition rules.

The source families are:

```text
RFC Editor / RFC 3986
BIPM / SI Brochure
USB-IF / Type-C specification subset
```

### M7 — PASS

`SYN-CH-006` is a precommitted strongest-reasonable-baseline comparison.
The baseline was deliberately equipped with the same claim-relevant semantic information rather than weakened to manufacture gain.
The resulting `NO_GAIN` was preserved.

```text
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
```

### M8 — PASS

External source facts, project candidate fixtures, and DSD verdicts remain separated across all three external applications.

`SYN-APP-001` remains limited to RFC-3986 **generic URI syntax** and does not claim scheme-specific validity, dereference success, or security.

`SYN-APP-002` remains limited to SI **unit-expression composition** and does not claim measurement validity, calibration, uncertainty, traceability, or physical realization.

`SYN-APP-003` remains explicitly version-scoped to the frozen **USB Type-C Release-2.0 mechanical subset** and does not claim current-release conformance, USB-IF certification, USB PD negotiation success, or complete electrical interoperability.

No later case retroactively broadens an earlier external authority.

### M9 — PASS

External breadth is materially wider than one domain and wider than one symbolic-composition family.

```text
1. URI generic syntax
   discrete grammar/component composition

2. SI unit composition
   algebraic products-of-powers, scale propagation, and coherence status

3. USB Type-C physical mating
   physical plug/receptacle role, insertion orientation, cable-end direction, and mechanical-vs-functional-role boundary
```

The third application is especially important for M9 because it is not merely another textual or symbolic grammar.
It pressures actual physical-interface compatibility and orientation while keeping functional electrical role establishment outside the mechanical claim.

Therefore the frozen M9 requirement is satisfied.
This does not establish universal cross-domain validity.

### M10 — UNRESOLVED_BUT_BOUNDED

The following remain unavailable:

```text
INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
BROAD_INTER_RATER_AGREEMENT: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
MEASURED_EFFICIENCY_ADVANTAGE: not established
MEASURED_DEFECT_REDUCTION_ADVANTAGE: not established
```

No independent evaluator packet/submission has yet been counted for Synthesis.
The axis is bounded rather than hidden.

Under the frozen project maturity rule, this does not prohibit established **method/protocol evidence maturity**, but it prevents the established label from being interpreted as independent validation or practical superiority.

### M11 — PRESENT_NONFATAL

`SYN-CH-004` is the principal historical pressure event.
Its frozen fixture omitted a readiness record required for one candidate and the first result attempted an invalid post-hoc exception.
The postexecution audit rejected that rescue and preserved the challenge as **33/35 FAIL / CHALLENGE_DESIGN_DEFECT**.

The prospective correction `SYN-CH-005` used a new Case ID and new precommit.
The defect therefore pressured evidence discipline but did not expose a core Synthesis Protocol-v0.1 contradiction.

No later baseline, retrace, or external application required Protocol v0.1 reopening.

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

### M12 — PASS

The final claim is explicitly bounded:

```text
ESTABLISHED_METHOD_PROTOCOL_EVIDENCE_MATURITY
!= INDEPENDENT_VALIDATION
!= PRACTICAL_SUPERIORITY
!= UNIVERSAL_EXTERNAL_GENERALITY
!= PERMANENT_METHOD_REGISTRY_SURVIVAL
```

No stronger claim is made.

### M13 — PASS

The corpus repeatedly preserves Synthesis-specific composition discipline.

`SYN-CH-002` demonstrates:

```text
non_exhaustive failure-to-find
!= global infeasibility
```

`SYN-CH-006` demonstrates:

```text
syntax-tree difference
!= material target difference
```

when supplied associativity and canonicalization justify equivalence, while preserving distinct targets when identity/Property status differs.

The same challenge also demonstrates:

```text
component Property
!= defined whole Property without explicit lift
```

The Protocol additionally locks algebraic laws, composition coverage, partial residual obligations, and static-versus-temporal process scope.
External applications preserve candidate-fixture exhaustiveness only within their frozen finite sets.

### M14 — PASS

Historical evidence remains visible rather than cleaned up after the fact:

```text
SYN-CH-004 33/35 FAIL / challenge-design defect
SYN-CH-005 NO_GAIN
SYN-CH-006 NO_GAIN
SYN-CH-007 same-project/non-independent limitation
SYN-APP-001 generic-RFC scope limit
SYN-APP-002 measurement-validity scope limit
SYN-APP-003 Release-2.0 mechanical/version scope limit
```

The maturity audit does not rewrite any of these records.

### M15 — PASS

The current evidence supports operational separability of Synthesis from Design, Transformation, Aggregation, and Optimization under the current protocol, but the audit does not turn case outcomes into an irreversible registry decision.

The following remain separate propositions:

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
EXTERNAL_PASS != PERMANENT_INDEPENDENCE_PROOF
RETRACE_PASS != METHOD_IRREDUCIBILITY_PROOF
```

Therefore promotion to established protocol-evidence maturity does not mean the 22-method registry is permanently frozen or that future structural analysis can never motivate reclassification.

## 4. Promotion decision / 승격 결정

The frozen prohibition gates are:

```text
M9 = PASS
M11 = PRESENT_NONFATAL, not FAIL
M15 = PASS
```

`PROMOTE_ESTABLISHED` is therefore not prohibited.

The complete frozen corpus provides:

```text
an executable stable protocol
all current terminal-status distinctions under direct pressure
neighboring-method operational separation
preserved NO_GAIN against competent baselines
one strongest-reasonable-baseline comparison
a preserved failed challenge design with anti-post-hoc handling
deterministic same-project retraceability
three successful and materially different external-domain applications
explicit external source/bridge limits
composition basis/coverage/equivalence discipline
no identified core defect requiring protocol reopen
```

Under the frozen DSD method-family maturity framework, this is sufficient for established **method/protocol evidence maturity**.

```text
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

## 5. Maximum supported claim / 현재 최대 지지 주장

The maximum supported statement is:

> DSD Synthesis Protocol v0.1 has established method/protocol evidence maturity within the current DSD method-family framework. Its corpus includes direct positive, negative/failure, neighboring-method-boundary, preserved failed-challenge, honest NO_GAIN, strongest-reasonable-baseline, deterministic same-project retrace, and three materially different external-application records while preserving source scope, composition coverage, target equivalence, Property-lift, and process-boundary discipline. Independent validation, independent replication, broad inter-rater agreement, measured practical superiority, universal external generality, and permanent method-registry survival are not established or implied.

## 6. Precommitted audit-check score / 사전 고정 감사 점수

All 28 frozen audit-execution checks are satisfied.

```text
PRECOMMITTED_REQUIRED_CHECKS: 28
PASSED: 28
FAILED: 0
AUDIT_EXECUTION_VERDICT: PASS
```

The 28/28 score means the audit followed its own frozen rules.
It does **not** mean every maturity axis is `PASS`.

```text
M5  = CONDITIONAL_PASS
M10 = UNRESOLVED_BUT_BOUNDED
M11 = PRESENT_NONFATAL
```

remain explicitly non-PASS.

## 7. Status separation / 상태 분리

```text
METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress

INDEPENDENT_SYNTHESIS_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established

SYNTHESIS_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
EXTERNAL_APPLICATION_INCREMENT_FROM_AUDIT: 0
REPRODUCIBILITY_INCREMENT_FROM_AUDIT: 0
AUDIT_META_RECORD_CREATED: yes
```

Maturity classification and ongoing validation remain separate ledgers.

## 8. Next evidence priority / 다음 증거 우선순위

After this audit, the weakest evidence axis is the shared independence limitation represented by M5/M10.
Another same-project constructed or external application would add breadth but would not resolve that bottleneck.

The highest-value next step is therefore independent-evaluator infrastructure for Synthesis, prepared without counting it as validation:

```text
SYN-IEP-001
-> clean reviewer packet
-> frozen task/source bundle
-> blind or cleanroom submission template
-> hidden reference answer / commitment
-> eligibility criteria
-> immutable evaluator submission before answer reveal
-> independent-evidence scoring only after a genuinely separate submission exists
```

A future independent disagreement is valid evidence and must be preserved rather than treated as protocol failure automatically.

No Protocol-v0.1 revision is justified merely because independent validation remains open.

## 9. Stable audit conclusion / 안정 판정

```text
AUDIT_ID: DSD-AUDIT-20260910-SYNTHESIS-001
AUDIT_STATUS: COMPLETED
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 28/28
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
M5_REPRODUCIBILITY: CONDITIONAL_PASS
M9_EXTERNAL_BREADTH: PASS
M10_INDEPENDENT_PRACTICAL: UNRESOLVED_BUT_BOUNDED
M11_PROTOCOL_PRESSURE: PRESENT_NONFATAL
M15_METHOD_SURVIVAL_SEPARATION: PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
INDEPENDENT_SYNTHESIS_VALIDATION: not established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
SYNTHESIS_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
```
