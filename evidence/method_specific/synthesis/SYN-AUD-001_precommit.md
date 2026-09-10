# SYN-AUD-001 — DSD Synthesis Maturity Audit Precommit

Status: **PRECOMMITTED BEFORE MATURITY SCORING**  
Date: **2026-09-10**  
Audit ID: `DSD-AUDIT-20260910-SYNTHESIS-001`  
Audit method: **DSD Audit / DSD 감사**  
Audited method: **DSD Synthesis / DSD 합성론**  
Audited Synthesis protocol: **v0.1**  
Record class: **audit_meta_record / first_maturity_audit**

## 1. Audit question / 감사 질문

Determine the maximum maturity claim supported by the current DSD Synthesis corpus after the executable Protocol v0.1, constructed direct challenges, two honest `NO_GAIN` comparisons including a strongest-reasonable baseline, one deterministic same-project retrace, and three successful external applications across materially different domains.

This audit must keep method/protocol evidence maturity separate from:

```text
method survival
method merger/absorption/deletion
independent validation
independent replication
practical superiority
universal external generality
```

The audit does not create Synthesis direct evidence and does not increment constructed-pilot, external-application, or reproducibility counts.

## 2. Frozen evidence inventory / 동결 증거 목록

### Protocol and pre-protocol pressure

```text
PROTOCOL_v0.1.md
  creation commit: 8787b242cb6648c47396151dbac3aadc19e3d184

PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
  preserved without refinement: 11
  preserved with non-breaking refinement: 5
  boundary collapse found: 0
  fundamental interface failure: 0
```

### Constructed direct challenges

```text
SYN-CH-001 positive
  28/28 PASS

SYN-CH-002 negative/failure terminal distinction
  36/36 PASS
  INFEASIBLE != UNDERDETERMINED != BLOCKED

SYN-CH-003 direct method-boundary separation
  46/46 PASS
  Design / Transformation / Aggregation / Optimization handoffs preserved

SYN-CH-004 first NO_GAIN baseline attempt
  33/35 FAIL
  FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
  preserved without post-hoc rescue

SYN-CH-005 corrected prospective competent-baseline comparison
  37/37 PASS / NO_GAIN

SYN-CH-006 broader strongest-reasonable-baseline comparison
  52/52 PASS / NO_GAIN
  category established_at_constructed_evidence_level
```

### Reproducibility/retrace evidence

```text
SYN-CH-007
  deterministic same-project retrace of SYN-APP-001
  48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established
```

### External applications

```text
SYN-APP-001
  external authority: RFC 3986 / STD 66
  domain: Internet identifier syntax / URI generic syntax
  PASS 40/40

SYN-APP-002
  external authority: BIPM SI Brochure 9th ed. v4.01 (2026)
  DOI: 10.59161/AUEZ1291
  domain: physical metrology / SI unit composition
  PASS 46/46

SYN-APP-003
  frozen authority: USB Type-C Cable and Connector Specification Release 2.0 mechanical subset
  supporting authority: USB-IF Type-C overview
  domain: physical connector assembly / USB Type-C mating interface
  PASS 44/44
```

### Frozen counts before audit scoring

```text
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_POSITIVE_SYNTHESIS_CASES: 1
SUCCESSFUL_NEGATIVE_OR_FAILURE_SYNTHESIS_CASES: 1
SUCCESSFUL_BOUNDARY_SYNTHESIS_CASES_UNDER_PROTOCOL: 1
PRESERVED_FAILED_BASELINE_CHALLENGE_DESIGNS: 1
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
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

## 3. Maturity axes / 성숙도 축

The audit freezes fifteen axes.
The first fourteen intentionally parallel the Design maturity framework where applicable; M15 explicitly freezes the project rule that pass/fail counts do not decide method survival or merger.

```text
M1  dedicated executable protocol
M2  positive/negative terminal discrimination
M3  neighboring-method boundary discrimination
M4  NO_GAIN preservation
M5  reproducibility/retraceability
M6  external application origin
M7  strongest-reasonable-baseline comparison
M8  external source fidelity and bridge discipline
M9  established-level evidence breadth
M10 independent/practical-performance evidence
M11 protocol pressure / unresolved core defect
M12 maximum-supported-claim discipline
M13 composition-basis / coverage / equivalence discipline
M14 historical failure / anti-post-hoc preservation
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
`PASS` requires a frozen executable Synthesis protocol with explicit task/claim lock, supplied component identities, supplied composition rule/source, candidate basis and coverage, interface/prerequisite checks, property-lift discipline, relation/support/loss checks, formation effect, output level, terminal status, conformance, gain, limits, handoffs, and reproducibility data.

### M2
`PASS` requires protocol-level evidence spanning successful synthesis and genuine non-success terminal states without collapsing:

```text
SYNTHESIS_ADMISSIBLE
SYNTHESIS_INFEASIBLE
SYNTHESIS_UNDERDETERMINED
SYNTHESIS_BLOCKED
```

### M3
`PASS` requires direct evidence that Synthesis does not silently absorb neighboring Design, Transformation, Aggregation, or Optimization operations and preserves explicit handoffs.

### M4
`PASS` requires at least one competent baseline comparison where `NO_GAIN` remains a valid result rather than being converted to superiority. Preserved multiple `NO_GAIN` records strengthen but do not change the criterion.

### M5
`PASS` requires independent replication.
`CONDITIONAL_PASS` is available when a deterministic same-project retrace succeeds while reviewer independence or blinding is absent.

### M6
`PASS` requires at least one application whose composition/interface legitimacy comes from a stable external authority rather than only a project-invented rule fixture.

### M7
`PASS` requires a precommitted competent strongest-reasonable comparator that is not intentionally impoverished and whose matching result is preserved even when DSD does not outperform it.

### M8
`PASS` requires external source facts, project fixture assumptions, DSD bridge vocabulary, and Synthesis verdict to remain explicitly separated. No source rule may be upgraded beyond its authority scope.

### M9
`PASS` requires external evidence broader than a single domain and broader than one type of symbolic composition fixture.
Multiple external applications do not pass M9 merely by count: the audit must verify materially different domains and materially different composition/interface structures.

### M10
`PASS` requires genuine independent evaluator validation and/or materially measured practical performance sufficient for the maturity claim.
`UNRESOLVED_BUT_BOUNDED` is available when these remain absent but are explicitly bounded and not claimed.

### M11
`PASS` means no material protocol pressure remains.
`PRESENT_NONFATAL` means a historical challenge or fixture defect exists but the executable protocol did not require retrospective repair and no core defect remains open.
`FAIL` means a core protocol defect requires reopening before maturity consideration.

### M12
`PASS` requires the final maturity statement to remain within the established evidence and preserve unavailable claims.

### M13
`PASS` requires explicit composition-candidate basis and coverage discipline, including all applicable distinctions below:

```text
component admission != automatic composability
component-list completeness != composition-space exhaustiveness
non-exhaustive failure-to-find != global infeasibility
candidate syntax difference != material target distinctness
associativity/commutativity only when supplied
component Property != whole Property without explicit lift
static composition order != temporal assembly process
```

### M14
`PASS` requires failed challenges, `NO_GAIN`, scope limitations, version limits, and retrace limitations to remain historically visible and unrewritten.

### M15
`PASS` requires the audit to keep method maturity separate from method-registry survival/merger/deletion.
A PASS or FAIL case, a `NO_GAIN` result, external success, or retrace success must not by itself force Synthesis to survive, merge, be absorbed, or be deleted.
The audit may assess current operational separability, but it may not turn maturity scoring into a permanent ontology decision for the 22-method registry.

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

M10 is not an absolute prerequisite for established **method/protocol evidence maturity**.
However, if M10 is not `PASS`, the final audit must preserve all of the following as unavailable:

```text
independent evaluator validation
independent replication
broad inter-rater agreement
measured practical superiority
measured efficiency advantage
measured defect-reduction advantage
```

Likewise, promotion does not imply that Synthesis is permanently irreducible to every possible future method-family reorganization.

Promotion is not automatic when the prohibition gates are clear.
The complete frozen corpus must still justify the selected label.

## 6. Precommitted audit checks / 사전 고정 검사

1. Use only evidence frozen before `SYN-AUD-001` scoring.
2. Do not increment Synthesis direct-pilot count from the audit.
3. Do not increment external-application or reproducibility counts from the audit.
4. Keep `SYN-CH-004` visible as a failed precommitted challenge design.
5. Keep `SYN-CH-005` and `SYN-CH-006` visible as `NO_GAIN` results.
6. Do not call `SYN-CH-007` independent replication.
7. Record independent Synthesis validation as unestablished unless genuinely independent evidence exists before scoring; none exists in the frozen inventory.
8. Evaluate M9 from the actual three external applications rather than constructed challenge volume.
9. Verify that RFC URI syntax, SI unit composition, and USB Type-C physical mating are materially different domains/structures rather than renamed copies.
10. Preserve that `SYN-APP-001` is generic RFC syntax only, not scheme-specific validity.
11. Preserve that `SYN-APP-002` is SI unit-composition logic only, not measurement validity, calibration, uncertainty, or traceability.
12. Preserve that `SYN-APP-003` is the frozen Release-2.0 mechanical subset, not current Type-C certification or full electrical interoperability.
13. Evaluate source/bridge discipline across all three external applications.
14. M5 may not exceed `CONDITIONAL_PASS` without independent replication.
15. M10 may not be `PASS` without independent/practical evidence in the frozen inventory.
16. M11 must distinguish challenge-design defect from protocol-core failure.
17. No Protocol-v0.1 revision is recommended unless a core defect is found.
18. No shared-core reopen is recommended unless required by evidence.
19. M13 must explicitly evaluate composition coverage, equivalence/canonicalization, Property lift, and process-scope guards.
20. `NO_GAIN` must not be interpreted as method failure.
21. External PASS count must not be interpreted as superiority.
22. Case PASS/FAIL must not decide method survival, merger, absorption, or deletion.
23. If established maturity is selected, explicitly bound it away from independent validation, superiority, universal generality, and permanent method-registry survival.
24. If developing maturity is selected, identify the exact insufficient axis rather than relying on caution by default.
25. Final maturity classification and current evidence status are recorded separately.
26. Next evidence priority is derived from the weakest remaining axis.
27. Audit execution score must be separated from maturity-axis results.
28. The audit is recorded as an Audit meta-record, not direct Synthesis validation.

```text
PRECOMMITTED_REQUIRED_CHECKS: 28
```

Any unsupported criterion remains failed or unresolved.
No post-hoc rescue, criterion weakening, or criterion strengthening is permitted under this Audit ID.
