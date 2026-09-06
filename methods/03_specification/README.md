# 03. DSD Specification / DSD 명세론

Status: **developing** — dedicated protocol v0.1 established; direct pilots `SPEC-CH-001` through `SPEC-CH-005` completed with limitations; initial internal constructed challenge sequence complete.

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
  NO_GAIN: 3/3
  OPERATIONAL_GAIN: 3/3
  UNDERSPECIFIED: 2/2
  RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS

SPEC-CH-005  reproducibility / independent retrace
  PRECOMMIT: dda33b2028c9e5fb0f7b3bef938a8b834219f787
  REFERENCE_KEY_HASH_MATCH: yes
  TRACE_A_FINAL_STATUS_MATCHES: 8/8
  TRACE_B_FINAL_STATUS_MATCHES: 8/8
  TRACE_A_B_DIAGNOSTIC_AGREEMENT: 8/8
  TRACE_A_B_ATOMIZATION_BOUNDARY_MATCHES: 32/32
  ORDER_SENSITIVITY_ERRORS: 0
  RESULT: SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
  INDEPENDENT_EVALUATOR_VALIDATION: not established
```

`SPEC-CH-005` supports procedural retraceability and order stability on the locked finite packet only. Both traces were performed in the same project session by the same assistant/model family, so the word `independent` in the challenge title does not imply that an independent reviewer or separately initialized evaluator has validated the method.

All five records are pilot-level direct evidence only. They do not make Specification a mature method.

## Evidence sequence / 증거 순서

```text
SPEC-CH-001  completed
SPEC-CH-002  completed
SPEC-CH-003  completed
SPEC-CH-004  completed
SPEC-CH-005  completed with independence limitation

INTERNAL_CONSTRUCTED_CHALLENGE_SEQUENCE: completed
NEXT_REQUIRED_EVIDENCE: external_or_independently_generated_application_case
```

A real-world or independently generated requirement corpus remains necessary before any later maturity promotion. A genuinely independent retrace/review and a competent external baseline comparison should be added where feasible.