# 03. DSD Specification / DSD 명세론

Status: **developing** — dedicated protocol v0.1 established; method-specific direct evidence accumulation is next.

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

## Next evidence stage / 다음 증거 단계

The first direct-evidence sequence is planned as:

```text
SPEC-CH-001  basic well-formed / malformed specification discrimination
SPEC-CH-002  contradiction and underspecification challenge
SPEC-CH-003  optional-layer and bridge boundary challenge
SPEC-CH-004  NO_GAIN specification challenge
SPEC-CH-005  reproducibility / independent retrace challenge
```

Protocol existence alone is not counted as direct validation.
