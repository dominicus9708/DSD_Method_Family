# 03. DSD Specification / DSD 명세론

Status: **developing** — dedicated protocol v0.1 established; direct pilots `SPEC-CH-001` through `SPEC-CH-005` completed with limitations; first external/independently generated corpus application `SPEC-APP-001` completed; maturity audit completed and `developing` retained.

Task: state explicitly what entities, statuses, inputs, prerequisites, outputs, transitions, and distinctions a system or study must preserve.

Primary DSD sources: Formation + General Property; Static Aggregation and Dynamics when output, reduction, or transition specifications matter.

Typical outputs:
- typed requirement/status tables;
- allowed and disallowed state distinctions;
- explicit bridge declarations;
- domain and undefinedness rules;
- aggregate/reconstruction obligations when reduction is specified;
- transition and lineage obligations;
- external-standard requirements for domain-level claims;
- explicit violation, unresolved, contradiction, and `NO_GAIN` conditions.

Boundary: DSD Specification organizes structural requirements; it does not replace domain-specific requirements engineering, standards, law, safety rules, clinical standards, scientific definitions, or other competent validation authorities.

## Dedicated protocol / 전용 프로토콜

- [`PROTOCOL.md`](PROTOCOL.md) — **DSD Specification Protocol v0.1**
  - locks target scope and requirement-source inventory;
  - atomizes requirements into typed records;
  - preserves claim-relevant status distinctions;
  - separates required dependencies from optional interfaces;
  - records explicit bridges, external standards, reduction/reconstruction, and transition/lineage obligations when activated;
  - distinguishes `SATISFIED / VIOLATED / UNRESOLVED_OR_UNDERSPECIFIED / NOT_APPLICABLE` where relevant;
  - defines method-specific contradiction, underspecification, overconstraint, wrong-standard, and `SPEC_NO_GAIN` outcomes;
  - makes completeness only relative to the locked requirement inventory unless a stronger external completeness basis is supplied.

## Direct method evidence / 개별 방법 직접 증거

Evidence lane: [`../../evidence/method_specific/specification/`](../../evidence/method_specific/specification/)

```text
SPEC-CH-001  well-formed / malformed discrimination
  RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS

SPEC-CH-002  contradiction / underspecification
  PRECOMMIT: 848a01b160ecfe4fcbdb8e69d6501e40555d782d
  RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS

SPEC-CH-003  optional-layer / bridge boundary
  PRECOMMIT: d2cc07121043546be8e2450d8af288491b837e76
  RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS

SPEC-CH-004  NO_GAIN specification
  PRECOMMIT: 4d55d00af7fa376d370415a48b82de6883ba6fc8
  RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS

SPEC-CH-005  reproducibility / independent retrace
  PRECOMMIT: dda33b2028c9e5fb0f7b3bef938a8b834219f787
  TRACE_A_B_FINAL_STATUS_AGREEMENT: 8/8
  TRACE_A_B_DIAGNOSTIC_AGREEMENT: 8/8
  TRACE_A_B_ATOMIZATION_BOUNDARY_MATCHES: 32/32
  ORDER_SENSITIVITY_ERRORS: 0
  RESULT: SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
  INDEPENDENT_EVALUATOR_VALIDATION: not established
```

The five internal records are pilot-level direct evidence. `SPEC-CH-005` establishes procedural retraceability on a locked finite packet, not independent reviewer validation.

## First external application / 첫 외부 적용

External evidence lane:
[`../../evidence/real_world_cases/specification/`](../../evidence/real_world_cases/specification/)

### SPEC-APP-001 — RFC 9112 §6.3 Message Body Length

```text
CASE_ORIGIN: public_normative_standard
SOURCE: RFC 9112 §6.3 core precedence algorithm
PRECOMMIT: 9b91cecda9516fd7cd65c9eb181e80ab4fa45deb
SOURCE_UNIT_COVERAGE: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
INVENTED_SOURCE_FACTS: 0
SOURCE_FIDELITY_RESULT: pass
FINAL_SPEC_STATUS: no_gain
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
PROTOCOL_PRESSURE: ordered precedence / priority, present_nonfatal
```

RFC 9112 already presents the selected requirements as a compact ordered normative procedure. Under the precommitted gain criteria, DSD atomization added no demonstrated distinction, traceability, ambiguity-reduction, or downstream-checkability gain, so `SPEC_NO_GAIN` was preserved rather than manufacturing a benefit claim.

Protocol v0.1 could preserve the RFC precedence using explicit predecessor exclusions in `ACTIVATION_CONDITION` / `DEPENDENCIES`, but this was repetitive. An optional explicit precedence/priority field is therefore a **future refinement candidate**, not a retroactive change to this run.

## Maturity audit / 성숙도 감사

Audit record:
[`../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md`](../../DSD_Audit/audits/methodology/2026-09-07_dsd-specification-maturity-audit.md)

```text
AUDIT_ID: DSD-AUDIT-20260907-METHODOLOGY-001
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_VERDICT_ON_CURRENT_DEVELOPING_STATUS: CONFIRMED
AUDIT_VERDICT_ON_PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
METHOD_STATUS_DECISION: RETAIN_DEVELOPING
ESTABLISHED_EVIDENCE_BREADTH: insufficient
EXTERNAL_CORPUS_COUNT: 1
EXTERNAL_DOMAIN_COUNT: 1
INDEPENDENT_EVALUATOR_VALIDATION: not_established
MEASURED_ENGINEERING_BENEFIT: not_established
```

The eight minimum evidence-component categories are present, but they are treated as an eligibility floor for promotion review rather than an automatic status upgrade. The principal blocker is evidence breadth: the external evidence remains one subsection of one technical standard in one domain. The external `NO_GAIN` result is preserved as valid evidence of fidelity and non-favoritism, not converted into either a failure or a gain claim.

## Evidence state / 증거 상태

```text
SPEC-CH-001  completed
SPEC-CH-002  completed
SPEC-CH-003  completed
SPEC-CH-004  completed
SPEC-CH-005  completed with independence limitation
SPEC-APP-001 external/independently generated corpus application  completed
SPECIFICATION_MATURITY_AUDIT  completed

INTERNAL_CONSTRUCTED_CHALLENGE_SEQUENCE: completed
EXTERNAL_OR_INDEPENDENTLY_GENERATED_APPLICATION_CASE: completed
INDEPENDENT_EVALUATOR_VALIDATION: not_established
METHOD_STATUS: developing
ESTABLISHED_STATUS: not_justified_on_current_evidence
NEXT_STEP: SPEC-APP-002_less_structured_external_corpus
```

Next development should add a less-structured external requirement corpus and at least one different external domain, followed by genuinely independent retrace/review where feasible. Any precedence/priority refinement belongs to a prospective Protocol v0.2 rather than retroactive rescoring of `SPEC-APP-001`.
