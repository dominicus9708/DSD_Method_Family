# 03. DSD Specification / DSD 명세론

Status: **developing** — dedicated protocol v0.1 established; direct pilots `SPEC-CH-001` through `SPEC-CH-005` completed with limitations; first external/independently generated corpus application `SPEC-APP-001` completed; maturity audit pending.

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

## Evidence state / 증거 상태

```text
SPEC-CH-001  completed
SPEC-CH-002  completed
SPEC-CH-003  completed
SPEC-CH-004  completed
SPEC-CH-005  completed with independence limitation
SPEC-APP-001 external/independently generated corpus application  completed

INTERNAL_CONSTRUCTED_CHALLENGE_SEQUENCE: completed
EXTERNAL_OR_INDEPENDENTLY_GENERATED_APPLICATION_CASE: completed
INDEPENDENT_EVALUATOR_VALIDATION: not_established
METHOD_STATUS: developing
MATURE_METHOD_STATUS: not_claimed
NEXT_STEP: specification_maturity_audit
```

The project checklist now has both the internal challenge sequence and one external-origin application. Maturity is **not** promoted automatically: a dedicated audit must still weigh evidence breadth, the independent-evaluator gap, the baseline-preferred external result, protocol pressure, and absence of measured real-world engineering benefit.
