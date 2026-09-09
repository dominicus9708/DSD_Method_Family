# DSD Design Planning / DSD 설계론 기획

Status: **Protocol v0.1 / maturity: established / independent validation open**

Date opened: **2026-09-08**

## Purpose / 목적

Develop DSD Design as an independent method that constructs and filters target structures from declared goals and constraints while preserving the 22-method boundary discipline.

Shared-core evidence and neighboring-method results may be referenced, but direct Design validation is accumulated separately.

## Protocol and interface

- Current executable protocol: [`PROTOCOL_v0.1.md`](PROTOCOL_v0.1.md)
- Design assumes no universal candidate generator.
- Candidate coverage remains `exhaustive / non_exhaustive / unknown`.
- `DESIGN_INFEASIBLE` requires exhaustive coverage or an impossibility argument.
- Material distinctness is judged at `TARGET_RESOLUTION`.
- Soft preferences are not silently promoted into hard constraints.
- External authority and neighboring-method verdicts remain separately identifiable.

## Three independent Design ledgers

```text
TERMINAL_DESIGN_STATUS:
  DESIGN_ADMISSIBLE
  DESIGN_INFEASIBLE
  DESIGN_UNDERDETERMINED
  DESIGN_BLOCKED

DESIGN_PROTOCOL_CONFORMANCE:
  CONFORMANT
  NONCONFORMANT
  UNDETERMINED

DESIGN_METHOD_GAIN_STATUS:
  GAIN_ESTABLISHED
  NO_GAIN
  NOT_ASSESSED
```

Maturity is evaluated separately by DSD Audit.

## Development sequence / 개발 순서

1. ✅ Design-specific task interface and minimum valid output.
2. ✅ Boundary counterexamples and non-breaking refinements.
3. ✅ `PROTOCOL_v0.1.md`.
4. ✅ Positive pilot `DES-CH-001` — 11/11 PASS.
5. ✅ Negative/failure pilot `DES-CH-002` — 20/20 PASS.
6. ✅ Boundary stage — failed `DES-CH-003` preserved; corrected `DES-CH-004` 23/23 PASS.
7. ✅ NO_GAIN pilot `DES-CH-005` — 25/25 PASS.
8. ✅ Broader strongest-reasonable-baseline comparison `DES-CH-006` — 54/54 PASS / NO_GAIN.
9. ✅ First external-standard application `DES-APP-001` — W3C WCAG 2.2 subset, 36/36 PASS.
10. ✅ Dedicated reproducibility/retrace `DES-CH-007` — 44/44 PASS at deterministic same-project level.
11. ✅ First DSD Audit maturity review `DES-AUD-001` — historical developing classification; established promotion withheld at that time.
12. ✅ Second external application `DES-APP-002` — NIST SP 800-63B-4 AAL2 route-form grammar, 38/38 PASS.
13. ✅ First blinded independent-evaluator packet `DES-IEP-001` prepared; public packet/template + hidden reference commitment frozen, but no external submission yet.
14. **Pending external action:** obtain a genuinely separate evaluator submission under `DES-IEP-001` and score it only after immutable submission freeze and reference-key reveal.
15. ✅ Additional physical breadth: `DES-APP-003` — U.S. Access Board 2010 ADA Standards §405 selected ramp-run application, 38/38 PASS.
16. ✅ Revision maturity audit `DES-AUD-002` — 26/26 audit checks PASS; M9 external breadth PASS; method/protocol maturity promoted to `established` with M5/M10 limitations preserved.
17. **Next:** complete the independent-evaluator track; later re-audit only after genuinely new independent/practical evidence or a new protocol pressure event.

## Evidence milestones / 증거 이정표

### Positive and non-success behavior

`DES-CH-001` preserved status distinctions and returned the complete admissible family.

`DES-CH-002` directly separated:

```text
DESIGN_INFEASIBLE
DESIGN_UNDERDETERMINED
DESIGN_BLOCKED
```

including the valid `DESIGN_BLOCKED + CONFORMANT` combination.

### Boundary behavior

`DES-CH-003` exposed a challenge-design defect and was preserved at 20/21 rather than repaired post hoc.
`DES-CH-004` prospectively corrected the candidate-resolution problem and passed the Design/Optimization boundary test.

### Method-gain behavior

`DES-CH-005` and `DES-CH-006` both produced valid `NO_GAIN` results against competent baselines.
No extra DSD bookkeeping was counted as gain by itself.

### External applications

```text
DES-APP-001
  W3C WCAG 2.2 subset
  web accessibility
  36/36 PASS

DES-APP-002
  NIST SP 800-63B-4 AAL2 route-form subset
  digital identity / authentication security
  source-supplied positive construction grammar
  38/38 PASS

DES-APP-003
  U.S. Access Board 2010 ADA Standards §405 selected ramp-run subset
  built environment / physical accessibility
  38/38 PASS
```

External evidence therefore now spans:

```text
3 applications / 3 materially different domains
```

The three cases preserve external authority and subset scope separately from DSD verdicts.
None is expanded into full-standard or engineering certification.

### Dedicated retrace

`DES-CH-007` reproduced the frozen `DES-APP-001` claim-relevant result exactly and passed 44/44 checks.

```text
RETRACE_RESULT: PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

This remains non-independent.

## Maturity audit lineage / 성숙도 감사 계보

### DES-AUD-001

At the first audit time:

```text
EXTERNAL_APPLICATIONS: 1
EXTERNAL_DOMAINS: 1
M9: INSUFFICIENT
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
```

That decision remains historical and unchanged.

### DES-AUD-002

The revision audit froze the expanded corpus and reused the same 14 maturity axes and inherited promotion logic before scoring.

```text
AUDIT_ID: DSD-AUDIT-20260909-DESIGN-002
PRECOMMITTED_REQUIRED_CHECKS: 26/26 PASS
AUDIT_EXECUTION_VERDICT: PASS

M1  PASS
M2  PASS
M3  PASS
M4  PASS
M5  CONDITIONAL_PASS
M6  PASS
M7  PASS
M8  PASS
M9  PASS
M10 UNRESOLVED_BUT_BOUNDED
M11 PRESENT_NONFATAL
M12 PASS
M13 PASS
M14 PASS

FINAL_MATURITY_DECISION: PROMOTE_ESTABLISHED
METHOD_MATURITY_CLASSIFICATION: established
PROMOTION_TO_ESTABLISHED: SUPPORTED
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The material change is M9: the external corpus is no longer one-domain/one-fixture evidence.
The NIST case additionally pressures candidate/construction provenance using source-supplied positive grammar.

The established label is limited to **method/protocol evidence maturity under the current DSD method-family framework**.
It does not establish:

```text
independent evaluator agreement
independent replication
broad inter-rater reproducibility
measured practical superiority
measured efficiency advantage
measured defect-reduction advantage
```

## Independent evaluator packet / 독립 평가자 패킷

`DES-IEP-001` remains prepared and frozen as infrastructure.

```text
REVIEWER_PACKET_COMMIT:
78b1fb45d0b2e40838517828d089942e7b55e7d8

SUBMISSION_TEMPLATE_COMMIT:
fe1eedca019b4283a21047d21fcac12dd672e328

REFERENCE_COMMITMENT_COMMIT:
8fe4ff64b3fc964746d7e8c11bd03d712c40fedd

REFERENCE_SHA256:
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

Current state:

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
```

The project assistant/session that created the packet cannot count as the independent evaluator.

## Evidence architecture status / 증거 구조 상태

```text
DEDICATED_PROTOCOL: established
POSITIVE_CASE: established
NEGATIVE_OR_FAILURE_CASE: established
BOUNDARY_CASE: established with one preserved failed predecessor test
NO_GAIN_CASE: established
STRONGEST_REASONABLE_BASELINE_COMPARISON: established at constructed level
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
REPRODUCIBILITY_RETRACE: deterministic_same_project
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: established
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

Current counts:

```text
DIRECT_CONSTRUCTED_PILOTS: 7
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
```

## Recording rule / 기록 규칙

Historical runs remain preserved under the protocol version used at execution time.
Prospective corrections do not rewrite earlier evidence.
`DES-AUD-001` and `DES-AUD-002` are time-indexed audit records and neither replaces the other.

The independent evaluator packet is append-only at the committed version.
A disagreement from a later reviewer is evidence and must not be repaired away.

## Next step / 다음 단계

The former M9 breadth blocker is now closed.
The highest-value unresolved evidence event is independent evaluation.

```text
1. select a genuinely separate evaluator
2. distribute the frozen clean reviewer packet + submission template + source material only
3. collect eligibility/contamination declarations
4. freeze the final evaluator submission with an immutable/timestamped identifier
5. reveal the private escrow nonce and canonical key
6. recompute and verify the SHA-256 commitment
7. score the frozen submission under the precommitted 24-check rule
8. preserve agreement or disagreement as a new Audit/evidence record
```
