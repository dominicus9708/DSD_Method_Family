# 03. DSD Specification / DSD 명세론

Status: **developing** — dedicated protocol v0.1 established; direct pilots `SPEC-CH-001` through `SPEC-CH-004` completed with limitations.

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

### SPEC-CH-001 — completed

```text
WELL_FORMED_CASES_ACCEPTED: 2/2
MALFORMED_CASES_DETECTED: 6/6
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
RESULT: SPECIFICATION_DISCRIMINATION_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-002 — completed

```text
PRECOMMIT_COMMIT: 848a01b160ecfe4fcbdb8e69d6501e40555d782d
CONTRADICTION_CASES_CORRECTLY_CLASSIFIED: 3/3
UNDERSPECIFICATION_CASES_CORRECTLY_CLASSIFIED: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
CROSS_CLASS_ERRORS: 0
RESULT: SPECIFICATION_CONTRADICTION_UNDERSPECIFICATION_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-003 — completed

```text
PRECOMMIT_COMMIT: d2cc07121043546be8e2450d8af288491b837e76
OPTIONAL_LAYER_OVERCONSTRAINT_CASES_CORRECT: 3/3
REQUIRED_BRIDGE_FAILURE_CASES_CORRECT: 3/3
EXACT_DIAGNOSTIC_FAMILY_MATCHES: 8/8
CROSS_CLASS_ERRORS: 0
RESULT: SPECIFICATION_OPTIONAL_LAYER_BRIDGE_BOUNDARY_PILOT_PASS_WITH_LIMITATIONS
```

### SPEC-CH-004 — completed

`NO_GAIN Specification Challenge`

```text
PRECOMMIT_COMMIT: 4d55d00af7fa376d370415a48b82de6883ba6fc8
NO_GAIN_CASES_CORRECTLY_PRESERVED: 3/3
OPERATIONAL_GAIN_CASES_CORRECTLY_DISTINGUISHED: 3/3
UNDERSPECIFIED_CASES_CORRECTLY_DISTINGUISHED: 2/2
EXACT_EXPECTED_FINAL_STATUS_FAMILY: 8/8
FALSE_NO_GAIN_ON_INCOMPLETE_SOURCE: 0
FALSE_GAIN_FROM_COSMETIC_RELABELING_OR_REORDERING: 0
INVENTED_SOURCE_FACTS: 0
RESULT: SPECIFICATION_NO_GAIN_PILOT_PASS_WITH_LIMITATIONS
```

The fourth pilot shows that Protocol v0.1 does not count use of DSD itself as benefit. A competent already-complete non-DSD specification can legitimately receive `SPEC_NO_GAIN`, while actual operational gains and true underspecification remain separate outcomes.

All four records are pilot-level direct evidence only. They do not make Specification a mature method.

## Evidence sequence / 증거 순서

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination — completed
SPEC-CH-002  contradiction and underspecification challenge — completed
SPEC-CH-003  optional-layer and bridge boundary challenge — completed
SPEC-CH-004  NO_GAIN specification challenge — completed
SPEC-CH-005  reproducibility / independent retrace challenge — next
```

A real-world or independently generated requirement corpus remains necessary before any later maturity promotion.