# CMP-AUD-001 — DSD Comparison Maturity Audit

Status: **COMPLETED — established method/protocol evidence maturity supported with explicit unresolved independent/practical limitations**  
Date: **2026-09-11**  
Audit ID: `DSD-AUDIT-20260911-COMPARISON-001`  
Audit method: **DSD Audit / DSD 감사**  
Audited method: **DSD Comparison / DSD 비교론**  
Audited Comparison protocol: **v0.1**  
Precommit: `CMP-AUD-001_precommit.md`  
Precommit commit: `69315746b3ed5367aa56e087b96b8ea878a59376`

## 1. Maturity decision / 성숙도 판정

The frozen Comparison corpus supports promotion of **DSD Comparison method/protocol evidence maturity** from `proposed` to `established` under the current DSD method-family evidence framework.

The decision is not based on raw PASS count. It is based on the combined architecture:

```text
frozen executable Protocol v0.1
positive direct correspondence/equivalence separation
negative/failure terminal discrimination
neighboring-method boundary separation
two honest NO_GAIN baseline comparisons
strongest-reasonable-baseline comparison
deterministic same-project retrace
three materially different external domains
external criterion / bridge / source-scope discipline
comparison-specific map/coverage/closure discipline
no identified post-freeze core protocol defect requiring reopen
```

Audit result:

```text
AUDIT_STATUS: COMPLETED
AUDIT_EXECUTION_VERDICT: PASS
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
COMPARISON_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
EXTERNAL_APPLICATION_INCREMENT_FROM_AUDIT: 0
REPRODUCIBILITY_INCREMENT_FROM_AUDIT: 0
```

The established label is deliberately limited to **method/protocol evidence maturity within this project framework**. It does not establish:

```text
INDEPENDENT_COMPARISON_VALIDATION
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
  commit a1700d960e0b41dfe32bf85b6334448d9104100d

PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
  preserved without refinement: 11
  preserved with non-breaking refinement: 5
  collapse: 0
  fundamental interface failure: 0
```

The Step-1 task-interface draft and Boundary Amendment 001 remain preserved as historical planning artifacts.

### Constructed direct evidence

```text
CMP-CH-001  positive relation separation       40/40 PASS
CMP-CH-002  negative/failure terminals         48/48 PASS
CMP-CH-003  neighboring-method boundary        48/48 PASS
CMP-CH-004  competent baseline                 50/50 PASS / NO_GAIN
CMP-CH-005  strongest-reasonable baseline      60/60 PASS / NO_GAIN
```

### Reproducibility

```text
CMP-CH-006
  deterministic same-project retrace
  48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

### External applications

```text
CMP-APP-001
  Unicode Standard Annex #15
  text representation / Unicode normalization
  42/42 PASS

CMP-APP-002
  RFC 9110 — HTTP Semantics
  protocol validator / ETag comparison semantics
  48/48 PASS

CMP-APP-003
  JCGM 200:2012 VIM3 entry 2.47
  physical metrology / measurement-result compatibility
  52/52 PASS
```

Frozen counts remain:

```text
DIRECT_COMPARISON_PILOTS: 5
POSITIVE_COMPARISON_CASES: 1
NEGATIVE_OR_FAILURE_COMPARISON_CASES: 1
BOUNDARY_COMPARISON_CASES: 1
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_COMPARISON_APPLICATIONS: 3
EXTERNAL_COMPARISON_DOMAINS: 3
EXTERNAL_COMPARISON_APPLICATION_PASSES: 3
INDEPENDENT_REPLICATION: not established
INDEPENDENT_COMPARISON_VALIDATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
```

## 3. Maturity-axis scoring / 성숙도 축 판정

```text
M1  dedicated executable protocol                          PASS
M2  positive/negative terminal discrimination              PASS
M3  neighboring-method boundary discrimination             PASS
M4  NO_GAIN preservation                                   PASS
M5  reproducibility/retraceability                          CONDITIONAL_PASS
M6  external application origin                            PASS
M7  strongest-reasonable-baseline comparison               PASS
M8  external source fidelity and criterion/bridge discipline PASS
M9  established-level evidence breadth                     PASS
M10 independent/practical-performance evidence             UNRESOLVED_BUT_BOUNDED
M11 protocol pressure / unresolved core defect             PASS
M12 maximum-supported-claim discipline                     PASS
M13 comparison coverage / criterion / equivalence closure  PASS
M14 historical / anti-post-hoc preservation                PASS
M15 method-survival / merger-separation discipline         PASS
```

### M1 — PASS

`PROTOCOL_v0.1.md` is executable and freezes the subject set, requested output, target resolution, comparison scope, map/correspondence family, map-family coverage, element coverage, map properties, reverse/inverse policy, feature/relation/Property/status rules, criterion, bridge/transformation provenance, first-branch policy, aggregate policy, lineage gate, terminal status, conformance, gain, and reproducibility record.

Its C1-C20 operation sequence is sufficient to execute the evidence corpus without a post-freeze protocol rewrite.

### M2 — PASS

The direct corpus demonstrates both positive correspondence and genuine non-success closure states.

`CMP-CH-001` separates:

```text
STRICT_EQUIVALENT
DIRECT_CORRESPONDENCE
ENCODED_CORRESPONDENCE
NONCORRESPONDENCE
```

`CMP-CH-002` separately demonstrates:

```text
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
COMPARISON_RESOLVED + NONCORRESPONDENCE
```

In particular:

```text
non-exhaustive one-map failure
!= resolved global noncorrespondence
```

while exhaustive all-map failure under the frozen family supports resolved `NONCORRESPONDENCE`.

### M3 — PASS

`CMP-CH-003` directly pressures five neighboring operations:

```text
internal decomposition      -> ANALYSIS_REQUIRED
taxonomy assignment         -> CLASSIFICATION_REQUIRED
unsupplied conversion       -> TRANSFORMATION_REQUIRED
procedural conformance      -> AUDIT_REQUIRED
historical identity/lineage -> PROVENANCE_LINEAGE_REQUIRED
```

Comparison preserved legitimate visible comparison results where possible and did not absorb the neighboring verdicts. A missing prerequisite transformation correctly produced `COMPARISON_BLOCKED` rather than a fabricated map.

This supports current operational boundary separation. It does not permanently settle every future registry-merger question; that remains separated under M15.

### M4 — PASS

`CMP-CH-004` and `CMP-CH-005` both preserve `NO_GAIN` against competent baselines.

The baselines received the same claim-relevant semantics rather than being intentionally weakened. Their matching outputs were not converted into DSD superiority, method failure, or absorption evidence.

```text
NO_GAIN != METHOD_FAILURE
NO_GAIN != METHOD_ABSORPTION_PROOF
```

### M5 — CONDITIONAL_PASS

`CMP-CH-006` successfully retraces the immutable Unicode application chain.

```text
REPRODUCIBILITY_LEVEL: deterministic_same_project
RETRACE_VERDICT: PASS
INDEPENDENT_REPLICATION: not established
BLINDED_REPRODUCTION: not established
```

The retrace reproduced candidate identity, criterion provenance, relation class, terminal status, conformance, and scope exclusions. Because it remains same-project and non-independent, M5 cannot be `PASS` under the frozen criterion.

### M6 — PASS

The external corpus uses three stable external authorities to supply comparison semantics rather than replacing them with project-invented equivalence rules:

```text
Unicode Consortium / UAX #15
IETF / RFC Editor / RFC 9110
JCGM-BIPM / VIM3 2.47
```

### M7 — PASS

`CMP-CH-005` is a precommitted strongest-reasonable-baseline comparison. `B1_STRONG_TYPED_COMPARISON_ENGINE` received the same claim-relevant information and matched DSD on:

```text
first-branch closure
directional map / inverse discipline
partial-vs-global element coverage
bridge and representation provenance
dynamic-trajectory vs lineage separation
status/relation trace
terminal and retraceability records
```

The preserved result is:

```text
STRONGEST_REASONABLE_BASELINE_COMPARISON:
  established_at_constructed_evidence_level
COMPARISON_METHOD_GAIN_STATUS: NO_GAIN
```

### M8 — PASS

External source facts, project fixture assumptions, criterion provenance, DSD relation labels, and broader identity claims remain separated across all three external cases.

`CMP-APP-001` preserves binary identity, canonical equivalence, and compatibility equivalence as different criteria. Normalization-dependent correspondence is not relabelled direct literal identity.

`CMP-APP-002` preserves RFC strong/weak comparison and context provenance. An ETag match is not upgraded to representation identity or to the whole request-precondition result.

`CMP-APP-003` preserves VIM uncertainty and correlation dependence. Metrological compatibility is not upgraded to strict structural equivalence, physical-object identity, calibration correctness, traceability validity, or causal diagnosis.

No later case retroactively broadens an earlier source authority.

### M9 — PASS

The three external applications are materially different in both domain and comparison mechanism:

```text
1. Unicode normalization
   representation transformation / normalized-form equivalence

2. HTTP ETag comparison
   direct validator-field comparison with strong/weak criterion selected by context

3. VIM metrological compatibility
   quantitative difference compared with uncertainty-dependent threshold and correlation sufficiency
```

This is not merely three renamed fixtures using one comparison operator. The Unicode application requires externally defined normalization relations; the HTTP application supplies two direct comparison functions without normalization; the VIM application introduces quantitative uncertainty, a chosen multiplier, strict threshold semantics, and a correctly underdetermined correlation-dependent case.

Therefore external breadth is no longer a maturity-blocking insufficiency under the frozen framework.

This does not establish universal cross-domain validity.

### M10 — UNRESOLVED_BUT_BOUNDED

The independent/practical axis remains open.

```text
INDEPENDENT_COMPARISON_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
BROAD_INTER_RATER_AGREEMENT: not established
MEASURED_PRACTICAL_SUPERIORITY: not established
MEASURED_EFFICIENCY_ADVANTAGE: not established
MEASURED_DEFECT_REDUCTION_ADVANTAGE: not established
```

No independent evaluator submission exists in the frozen Comparison inventory. This unresolved axis does not prohibit established **method/protocol evidence maturity** under the precommitted rule, but it sharply limits what `established` may mean.

### M11 — PASS

The 16 boundary attacks occurred before executable Protocol v0.1 was frozen. Five required non-breaking refinements, which were prospectively recorded in Boundary Amendment 001 and incorporated into the first executable protocol.

After Protocol v0.1 freeze, none of the positive, negative, method-boundary, competent-baseline, strongest-baseline, retrace, or three external cases exposed a core contradiction requiring the protocol to reopen.

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The pre-protocol refinement history remains visible, but it is not an unresolved post-freeze protocol defect. Therefore the frozen M11 criterion supports `PASS`, not `PRESENT_NONFATAL` or `FAIL`.

### M12 — PASS

The maturity claim remains explicitly bounded:

```text
ESTABLISHED_METHOD_PROTOCOL_EVIDENCE_MATURITY
!= INDEPENDENT_VALIDATION
!= INDEPENDENT_REPLICATION
!= PRACTICAL_SUPERIORITY
!= UNIVERSAL_EXTERNAL_GENERALITY
!= PERMANENT_METHOD_REGISTRY_SURVIVAL
```

No stronger claim is made.

### M13 — PASS

The corpus repeatedly preserves Comparison-specific coverage, criterion, and closure discipline.

`CMP-CH-002` demonstrates:

```text
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
PARTIAL_ELEMENT_COVERAGE != STRICT_EQUIVALENCE
FORWARD_MAP_SUCCESS != VERIFIED_INVERSE_PRESERVATION
MISSING_REQUIRED_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
```

`CMP-CH-004` and `CMP-CH-005` preserve:

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
later reconvergence != erasure of earlier justified branch
trajectory equivalence != lineage identity
```

The external applications add independent criterion pressure:

```text
same Unicode pair + different criterion -> different justified result
same ETag pair + strong/weak criterion -> different justified result
same measurement pair + different multiplier -> different justified result
unknown claim-relevant correlation -> UNDERDETERMINED, not assumed uncorrelated
```

Required information is therefore preserved as `UNDERDETERMINED` or `BLOCKED` rather than filled by a hidden map, bridge, inverse, transformation, correlation assumption, or identity claim.

### M14 — PASS

The historical record remains visible and unrewritten:

```text
Step-1 task-interface draft
Boundary Amendment 001
11 attacks needing no refinement
5 attacks needing non-breaking refinement
CMP-CH-004 NO_GAIN
CMP-CH-005 NO_GAIN
CMP-CH-006 same-project/non-independent limitation
CMP-APP-001 scope limits
CMP-APP-002 scope limits
CMP-APP-003 uncertainty/correlation and identity-scope limits
```

Comparison currently has no failed post-protocol challenge analogous to the preserved Design/Synthesis failed challenge designs. The audit does not invent one. M14 tests preservation of the actual history, not the presence of a failure for its own sake.

### M15 — PASS

The current corpus supports operational separability of Comparison from Analysis, Classification, Transformation, Audit, Provenance/Lineage, and Aggregation under the current protocol, but the audit does not turn case outcomes into an irreversible registry decision.

```text
CASE_PASS != METHOD_SURVIVAL_PROOF
CASE_FAIL != METHOD_DELETION_PROOF
NO_GAIN != METHOD_ABSORPTION_PROOF
EXTERNAL_PASS != PERMANENT_INDEPENDENCE_PROOF
RETRACE_PASS != METHOD_IRREDUCIBILITY_PROOF
```

Promotion to established protocol-evidence maturity therefore does not freeze the 22-method registry or prohibit future structural reclassification.

## 4. Promotion decision / 승격 결정

The frozen prohibition gates are:

```text
M9 = PASS
M11 = PASS
M15 = PASS
```

`PROMOTE_ESTABLISHED` is therefore not prohibited.

The complete frozen corpus provides:

```text
an executable stable protocol
positive correspondence/equivalence separation
resolved-vs-underdetermined-vs-blocked terminal discrimination
neighboring-method operational separation
two preserved NO_GAIN competent-baseline results
one strongest-reasonable-baseline comparison
deterministic same-project retraceability
three successful and materially different external-domain applications
explicit source / criterion / bridge / scope limits
map-family / element-coverage / direction / first-branch / aggregate closure discipline
no identified post-freeze core defect requiring protocol reopen
```

Under the frozen DSD method-family maturity framework, this is sufficient for established **method/protocol evidence maturity**.

```text
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 5. Maximum supported claim / 현재 최대 지지 주장

The maximum supported statement is:

> DSD Comparison Protocol v0.1 has established method/protocol evidence maturity within the current DSD method-family framework. Its corpus includes direct positive, negative/failure, neighboring-method-boundary, honest NO_GAIN, strongest-reasonable-baseline, deterministic same-project retrace, and three materially different external-application records while preserving map-family and element coverage, direction/inverse requirements, criterion and bridge provenance, first-branch closure, aggregate-versus-structure separation, and unresolved-information discipline. Independent validation, independent replication, broad inter-rater agreement, measured practical superiority, universal external generality, and permanent method-registry survival are not established or implied.

## 6. Precommitted audit-check score / 사전 고정 감사 점수

All 28 frozen audit-execution checks are satisfied.

```text
PRECOMMITTED_REQUIRED_CHECKS: 28
PASSED: 28
FAILED: 0
AUDIT_EXECUTION_VERDICT: PASS
```

The 28/28 score means the audit followed its own frozen rules. It does **not** mean every maturity axis is `PASS`.

```text
M5  = CONDITIONAL_PASS
M10 = UNRESOLVED_BUT_BOUNDED
```

## 7. Status separation / 상태 분리

```text
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress

INDEPENDENT_COMPARISON_VALIDATION: not established
INDEPENDENT_REPLICATION: not established
MEASURED_PRACTICAL_SUPERIORITY: not established

COMPARISON_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
EXTERNAL_APPLICATION_INCREMENT_FROM_AUDIT: 0
REPRODUCIBILITY_INCREMENT_FROM_AUDIT: 0
AUDIT_META_RECORD_CREATED: yes
```

The maturity label and ongoing validation status are intentionally separate ledgers.

## 8. Next evidence priority / 다음 증거 우선순위

The weakest remaining axes are M5 and M10, both limited by evaluator independence.

Therefore the highest-value next step is not another same-project external application. It is preparation of independent-evaluator infrastructure:

```text
CMP-IEP-001
-> separate evaluator task packet
-> blinded or key-separated reference record
-> immutable submission before reveal/scoring
-> precommitted scoring
-> independent-evidence Audit record
```

Packet preparation is infrastructure, not validation. A successful eligible external submission may improve M5/M10 in a later audit; disagreement is also valid evidence and must be preserved.

No Protocol v0.1 revision is justified merely because independent validation remains open.

## 9. Stable conclusion / 안정 판정

```text
AUDIT_ID: DSD-AUDIT-20260911-COMPARISON-001
AUDIT_STATUS: COMPLETED
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 28/28
FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
M5_REPRODUCIBILITY: CONDITIONAL_PASS
M9_EXTERNAL_BREADTH: PASS
M10_INDEPENDENT_PRACTICAL: UNRESOLVED_BUT_BOUNDED
M11_PROTOCOL_PRESSURE: PASS
M13_COMPARISON_DISCIPLINE: PASS
M15_REGISTRY_SEPARATION: PASS
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
INDEPENDENT_COMPARISON_VALIDATION: not established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
COMPARISON_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
```
