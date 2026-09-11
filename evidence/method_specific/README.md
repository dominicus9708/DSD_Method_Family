# Method-Specific Evidence / 개별 방법 직접 증거

This folder records evidence that directly tests one of the **22 independent DSD methods**. Evidence does not transfer automatically between methods merely because methods share a higher-level field or common DSD source layers.

## Current inheritance policy / 현재 상속 정책

- Shared-rule lessons may be cross-referenced but do not automatically become another method's direct validation.
- Maturity/status audits do not themselves increase the audited method's direct-pilot count.
- Independent-evaluator packet preparation is infrastructure until an eligible external submission exists.
- Failed challenge designs remain historical evidence of test pressure but do not fill successful validation categories.
- A success or failure in one case does not by itself imply that a method must survive, merge, be absorbed, or be deleted. Method independence is assessed separately.
- `NO_GAIN` or baseline matching does not by itself prove redundancy or absorption.
- Same-project retrace does not establish independent replication.
- Established method/protocol evidence maturity does not permanently freeze the method registry.

## Method-specific evidence lanes / 개별 증거 경로

### `design/` — DSD Design / DSD 설계론

```text
PROTOCOL: v0.1 established
METHOD_MATURITY_CLASSIFICATION: established after DES-AUD-002
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
DIRECT_CONSTRUCTED_PILOTS: 7
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

### `synthesis/` — DSD Synthesis / DSD 합성론

```text
DEDICATED_SYNTHESIS_PROTOCOL: v0.1 established
DIRECT_SYNTHESIS_PILOTS_COMPLETED: 6
SUCCESSFUL_NO_GAIN_SYNTHESIS_CASES: 2
SUCCESSFUL_BASELINE_COMPARISON_PASSES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
REPRODUCIBILITY_CASES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_SYNTHESIS_APPLICATIONS: 3
EXTERNAL_SYNTHESIS_DOMAINS: 3
EXTERNAL_SYNTHESIS_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_SYNTHESIS_VALIDATION: not established
SYNTHESIS_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_SYNTHESIS_EVIDENCE_STATUS: validation_in_progress
```

### `comparison/` — DSD Comparison / DSD 비교론

Executable `PROTOCOL_v0.1.md` was established at commit `a1700d960e0b41dfe32bf85b6334448d9104100d` after 16 pre-protocol boundary attacks.

Current Comparison state after `CMP-AUD-001`:

```text
DEDICATED_COMPARISON_PROTOCOL: v0.1 established
PRE_PROTOCOL_BOUNDARY_ATTACKS: 16
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
COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

Comparison evidence:

```text
CMP-CH-001  40/40 PASS
CMP-CH-002  48/48 PASS
CMP-CH-003  48/48 PASS
CMP-CH-004  50/50 PASS / NO_GAIN
CMP-CH-005  60/60 PASS / NO_GAIN
  STRONGEST_REASONABLE_BASELINE_COMPARISON:
    established_at_constructed_evidence_level

CMP-CH-006
  RETRACE TARGET: CMP-APP-001
  48/48 PASS
  REPRODUCIBILITY_LEVEL: deterministic_same_project
  INDEPENDENT_REPLICATION: not established

CMP-APP-001
  SOURCE: Unicode Standard Annex #15, Unicode 17.0.0 Revision 57
  DOMAIN: text representation / normalization
  42/42 PASS

CMP-APP-002
  SOURCE: RFC 9110 HTTP Semantics
  DOMAIN: protocol validator comparison
  48/48 PASS

CMP-APP-003
  SOURCE: JCGM 200:2012 VIM3 entry 2.47
  DOMAIN: physical metrology / measurement-result compatibility
  52/52 PASS

CMP-AUD-001
  PRECOMMIT: 69315746b3ed5367aa56e087b96b8ea878a59376
  RESULT: afe4cc7d8a4efe2f7485768e0d9dc363010e34e2
  AUDIT EXECUTION: 28/28 PASS
  FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
  COMPARISON_METHOD_MATURITY_CLASSIFICATION: established
```

The three Comparison external domains are materially distinct at the current evidence level: Unicode normalization, HTTP strong/weak validator comparison, and uncertainty/correlation-dependent VIM metrological compatibility.

`CMP-AUD-001` records:

```text
M5  reproducibility: CONDITIONAL_PASS
M9  external breadth: PASS
M10 independent/practical: UNRESOLVED_BUT_BOUNDED
M11 protocol pressure: PASS
M13 Comparison-specific closure discipline: PASS
M15 registry separation: PASS
```

Comparison guards include:

```text
AGGREGATE_EQUALITY != STRUCTURAL_EQUIVALENCE
ONE_MAP_FAILURE != GLOBAL_NONCORRESPONDENCE
FIRST_OBSERVED_DIFFERENCE != FIRST_JUSTIFIED_BRANCH_POINT
PARTIAL_CORRESPONDENCE != GLOBAL_EQUIVALENCE
ENCODING_REQUIRED_CORRESPONDENCE != DIRECT_CORRESPONDENCE
FORWARD_MAP_SUCCESS != REVERSE_MAP_SUCCESS
MAP_FAMILY_COVERAGE != COMPARISON_ELEMENT_COVERAGE
MISSING_COMPARISON_BRIDGE != PROVEN_STRUCTURAL_DIFFERENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NO_GAIN != METHOD_ABSORPTION_PROOF
RETRACE_PASS != INDEPENDENT_REPLICATION
METROLOGICAL_COMPATIBILITY != STRICT_STRUCTURAL_EQUIVALENCE
UNKNOWN_CORRELATION != ASSUME_UNCORRELATED
```

The next high-value Comparison event is independent-evaluator infrastructure `CMP-IEP-001`. Preparation is infrastructure only and does not establish independent validation.

## Promotion expectation / 성숙도 승격 기준

A proposed/developing method should accumulate, at minimum, a dedicated method protocol; positive, negative/failure, boundary and `NO_GAIN` cases; reproducibility records; external or independently generated applications; and a strongest-reasonable-baseline comparison when applicable. These are evidence categories, not automatic promotion rules. Same-project retrace does not substitute for independent review, external-application count does not establish practical superiority or method survival, and an established maturity label does not imply independent validation or permanently freeze the method registry.
