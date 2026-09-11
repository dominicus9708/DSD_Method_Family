# CMP-AUD-001 — DSD Comparison Maturity Audit Precommit

Status: **PRECOMMITTED BEFORE MATURITY SCORING**  
Date: **2026-09-11**  
Audit ID: `DSD-AUDIT-20260911-COMPARISON-001`  
Audit method: **DSD Audit / DSD 감사**  
Audited method: **DSD Comparison / DSD 비교론**  
Audited Comparison protocol: **v0.1**  
Record class: **audit_meta_record / first_maturity_audit**

## 1. Audit question / 감사 질문

Determine the maximum maturity claim supported by the current DSD Comparison corpus after the executable Protocol v0.1, positive/negative/boundary constructed challenges, two honest `NO_GAIN` comparisons including a strongest-reasonable baseline, one deterministic same-project retrace, and three successful external applications across materially different comparison domains.

This audit must keep method/protocol evidence maturity separate from:

```text
method survival
method merger/absorption/deletion
independent validation
independent replication
practical superiority
universal external generality
```

The audit does not create Comparison direct evidence and does not increment constructed-pilot, external-application, or reproducibility counts.

## 2. Frozen evidence inventory / 동결 증거 목록

### Protocol and pre-protocol pressure

```text
PROTOCOL_v0.1.md
  creation commit: a1700d960e0b41dfe32bf85b6334448d9104100d

PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
  preserved without refinement: 11
  preserved with non-breaking refinement: 5
  boundary collapse found: 0
  fundamental interface failure: 0
```

The Step-1 task-interface draft and Boundary Amendment 001 remain historical planning artifacts and are not rewritten by this audit.

### Constructed direct challenges

```text
CMP-CH-001 positive relation separation
  40/40 PASS

CMP-CH-002 negative/failure terminal distinction
  48/48 PASS
  RESOLVED != UNDERDETERMINED != BLOCKED

CMP-CH-003 direct neighboring-method boundary separation
  48/48 PASS
  Analysis / Classification / Transformation / Audit / Provenance-Lineage handoffs preserved

CMP-CH-004 competent baseline
  50/50 PASS / NO_GAIN

CMP-CH-005 strongest-reasonable baseline
  60/60 PASS / NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level
```

### Reproducibility/retrace evidence

```text
CMP-CH-006
  deterministic same-project retrace of CMP-APP-001
  48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

### External applications

```text
CMP-APP-001
  external authority: Unicode Standard Annex #15
  domain: text representation / Unicode normalization
  42/42 PASS
  criterion structure: binary identity vs canonical/compatibility normalization

CMP-APP-002
  external authority: RFC 9110 — HTTP Semantics
  domain: protocol validator / ETag comparison semantics
  48/48 PASS
  criterion structure: strong vs weak entity-tag comparison and context-selected criterion

CMP-APP-003
  external authority: JCGM 200:2012 VIM3 entry 2.47
  domain: physical metrology / measurement-result compatibility
  52/52 PASS
  criterion structure: value difference, standard uncertainty, chosen multiplier, correlation sufficiency
```

### Frozen counts before audit scoring

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
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

## 3. Maturity axes / 성숙도 축

The audit freezes fifteen axes. The first twelve parallel the established project maturity framework; M13 is Comparison-specific and M15 explicitly freezes the registry-separation rule.

```text
M1  dedicated executable protocol
M2  positive/negative terminal discrimination
M3  neighboring-method boundary discrimination
M4  NO_GAIN preservation
M5  reproducibility/retraceability
M6  external application origin
M7  strongest-reasonable-baseline comparison
M8  external source fidelity and criterion/bridge discipline
M9  established-level evidence breadth
M10 independent/practical-performance evidence
M11 protocol pressure / unresolved core defect
M12 maximum-supported-claim discipline
M13 comparison coverage / criterion / equivalence-closure discipline
M14 historical / anti-post-hoc preservation
M15 method-survival / merger-separation discipline
```

Allowed axis results:

```text
PASS
CONDITIONAL_PASS
INSUFFICIENT
UNRESOLVED_BUT_BOUNDED
PRESENT_NONFATAL
FAIL
```

## 4. Frozen axis criteria / 축별 기준

### M1
`PASS` requires a frozen executable Comparison protocol with explicit subject/claim/scope locks, map-family and element coverage, map properties and reverse/inverse policy, criterion and bridge provenance, output-level closure, terminal status, conformance, gain, limits, handoffs, and reproducibility data.

### M2
`PASS` requires direct evidence that Comparison distinguishes successful/resolved results from genuine non-success closure states without collapsing:

```text
COMPARISON_RESOLVED
COMPARISON_UNDERDETERMINED
COMPARISON_BLOCKED
```

It must also distinguish justified `NONCORRESPONDENCE` from unresolved failure-to-find.

### M3
`PASS` requires direct evidence that Comparison does not silently absorb neighboring Analysis, Classification, Transformation, Audit, or Provenance/Lineage operations and preserves explicit handoffs where required.

### M4
`PASS` requires at least one competent baseline comparison where `NO_GAIN` remains a valid result rather than being converted to superiority or method failure. Multiple preserved `NO_GAIN` cases strengthen but do not alter the criterion.

### M5
`PASS` requires independent replication.  
`CONDITIONAL_PASS` is available when deterministic same-project retrace succeeds while evaluator independence or blinding is absent.

### M6
`PASS` requires at least one application whose comparison criterion or correspondence legitimacy comes from a stable external authority rather than only a project-invented rule fixture.

### M7
`PASS` requires a precommitted competent strongest-reasonable comparator that is not intentionally impoverished and whose matching result is preserved even when DSD does not outperform it.

### M8
`PASS` requires external source facts, project fixture assumptions, criterion/bridge provenance, DSD relation labels, and Comparison verdicts to remain explicitly separated. External terminology may not be silently upgraded to DSD `STRICT_EQUIVALENT`, identity, causality, or broader domain conformance.

### M9
`PASS` requires external evidence broader than a single domain and broader than one comparison structure. Multiple external applications do not pass M9 merely by count: the audit must verify materially different authorities and materially different comparison mechanisms.

At minimum, the current corpus must show that Unicode normalization, HTTP validator comparison, and VIM metrological compatibility are not merely renamed instances of one project-authored relation rule.

### M10
`PASS` requires genuine independent evaluator validation and/or materially measured practical performance sufficient for the maturity claim.  
`UNRESOLVED_BUT_BOUNDED` is available when these remain absent but are explicitly bounded and not claimed.

### M11
`PASS` means the executable Protocol v0.1 has no identified material unresolved core defect and no post-freeze evidence requires reopening. Historical pre-protocol refinements may remain visible without lowering the result when they were incorporated prospectively before protocol freeze.  
`PRESENT_NONFATAL` means a material historical pressure event remains but does not require reopening.  
`FAIL` means a core protocol defect requires reopening before maturity consideration.

### M12
`PASS` requires the final maturity statement to remain within the established evidence and preserve unavailable claims.

### M13
`PASS` requires repeated preservation of Comparison-specific coverage, criterion, and closure discipline, including all applicable distinctions below:

```text
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different verdict
MISSING_CLAIM_REQUIRED_INFORMATION != FABRICATED_CLOSURE
```

The corpus must preserve `UNDERDETERMINED` or `BLOCKED` when required closure information is missing rather than silently supplying a map, bridge, inverse, transformation, correlation assumption, or stronger identity claim.

### M14
`PASS` requires historical planning refinements, `NO_GAIN`, scope limits, same-project retrace limits, and all earlier evidence states to remain visible and unrewritten. Absence of a failed post-protocol challenge does not itself fail this axis; the criterion is anti-post-hoc preservation of the history that actually exists.

### M15
`PASS` requires the audit to keep method maturity separate from method-registry survival/merger/deletion. A PASS or FAIL case, `NO_GAIN`, external success, or retrace success must not by itself force Comparison to survive, merge, be absorbed, or be deleted. The audit may assess current operational separability but may not turn maturity scoring into a permanent ontology decision for the 22-method registry.

## 5. Promotion decision rule / 승격 판정 규칙

Allowed maturity decisions:

```text
PROMOTE_ESTABLISHED
CLASSIFY_DEVELOPING
REOPEN_PROTOCOL_BEFORE_MATURITY
INSUFFICIENT_BASIS_FOR_CLASSIFICATION
```

`PROMOTE_ESTABLISHED` is prohibited when:

```text
M9 = INSUFFICIENT or FAIL
OR
M11 = FAIL
OR
M15 = FAIL
```

M10 is not an absolute prerequisite for established **method/protocol evidence maturity**. However, if M10 is not `PASS`, the final audit must preserve all of the following as unavailable:

```text
independent evaluator validation
independent replication
broad inter-rater agreement
measured practical superiority
measured efficiency advantage
measured defect-reduction advantage
```

Likewise, promotion does not imply universal cross-domain validity or permanent irreducibility of Comparison within every future method-family reorganization.

Promotion is not automatic when prohibition gates are clear. The complete frozen corpus must still justify the selected maturity label.

## 6. Precommitted audit checks / 사전 고정 검사

1. Use only evidence frozen before `CMP-AUD-001` scoring.
2. Do not increment Comparison direct-pilot count from the audit.
3. Do not increment external-application or reproducibility counts from the audit.
4. Keep the Step-1 task-interface draft and Boundary Amendment 001 historically visible.
5. Keep `CMP-CH-004` and `CMP-CH-005` visible as `NO_GAIN` results.
6. Do not call `CMP-CH-006` independent replication.
7. Record independent Comparison validation as unestablished unless genuinely independent evidence exists before scoring; none exists in the frozen inventory.
8. Evaluate M9 from the actual three external applications rather than constructed challenge volume.
9. Verify that Unicode normalization, HTTP ETag comparison, and VIM metrological compatibility are materially different domains/criterion structures rather than renamed copies.
10. Preserve Unicode binary/canonical/compatibility criterion provenance and its explicit scope exclusions.
11. Preserve HTTP strong/weak comparison scope and do not upgrade an ETag match to representation identity or whole-request outcome.
12. Preserve VIM uncertainty/correlation scope and do not upgrade compatibility to physical identity, calibration validity, or causal diagnosis.
13. Evaluate source/criterion/bridge discipline across all three external applications.
14. M5 may not exceed `CONDITIONAL_PASS` without independent replication.
15. M10 may not be `PASS` without independent/practical evidence in the frozen inventory.
16. M11 must distinguish pre-protocol refinement pressure from an unresolved Protocol-v0.1 core defect.
17. No Protocol-v0.1 revision is recommended unless a core defect is found.
18. No shared-core reopen is recommended unless required by evidence.
19. M13 must explicitly evaluate map-family coverage, element coverage, direction/inverse, encoding/bridge, criterion provenance, first-branch closure, aggregate separation, and unresolved-information handling.
20. `NO_GAIN` must not be interpreted as method failure or absorption proof.
21. External PASS count must not be interpreted as superiority.
22. Case PASS/FAIL must not decide method survival, merger, absorption, or deletion.
23. If established maturity is selected, explicitly bound it away from independent validation, superiority, universal generality, and permanent method-registry survival.
24. If developing/proposed maturity is retained, identify the exact insufficient axis rather than relying on caution by default.
25. Final maturity classification and current evidence status are recorded separately.
26. Next evidence priority is derived from the weakest remaining axis.
27. Audit execution score is separated from maturity-axis results.
28. The audit is recorded as an Audit meta-record, not direct Comparison validation.

```text
PRECOMMITTED_REQUIRED_CHECKS: 28
```

Any unsupported criterion remains failed or unresolved. No post-hoc rescue, criterion weakening, or criterion strengthening is permitted under this Audit ID.
