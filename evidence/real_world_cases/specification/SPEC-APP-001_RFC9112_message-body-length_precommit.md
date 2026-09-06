# SPEC-APP-001 Precommit — RFC 9112 §6.3 Message Body Length

Date: 2026-09-06
Evidence scope: `method_specific`
Case origin: `public_normative_standard`
Method directly tested: **DSD Specification / DSD 명세론**
Method protocol: **DSD Specification Protocol v0.1**

## 1. External source lock

Primary authoritative source:
- RFC 9112, *HTTP/1.1*, STD 99, June 2022, RFC Editor.
- Selected requirement corpus: **Section 6.3, Message Body Length — core precedence algorithm from the opening precedence statement through numbered item 8.**
- Canonical source: https://www.rfc-editor.org/rfc/rfc9112.html#section-6.3
- Status page: https://www.rfc-editor.org/info/rfc9112

Current-source context checked before scoring:
- RFC 9112 is updated by RFC 9931 (March 2026).
- RFC 9931 §8 adds separate HTTP CONNECT security requirements. This application does not treat those added requirements as replacements for the selected RFC 9112 §6.3 body-length precedence algorithm.
- The verified RFC 9112 errata currently concern §1.2 and Appendix C.3, not the selected §6.3 precedence text.

This source/update/errata status is part of the lock. If the authoritative source status changes before scoring, the change must be recorded rather than silently substituted.

## 2. Locked task

Re-express the selected external requirement corpus under Specification Protocol v0.1 without changing its HTTP semantics, requirement strength, precedence, actor scope, or error actions.

The task is not to prove RFC 9112 correct, improve HTTP, or replace IETF requirements engineering.

## 3. Locked baseline

Strongest baseline:

```text
RFC 9112 §6.3 itself
```

The RFC already provides an ordered normative decision procedure. DSD receives no gain credit merely for turning prose/list clauses into different field names.

## 4. Locked source units

The selected source is scored as 13 operational atoms so that source subbranches are not silently merged:

```text
A01  HEAD/1xx/204/304 response branch
A02  successful CONNECT response branch
A03  Transfer-Encoding + Content-Length conflict branch
A04  Transfer-Encoding present, final coding chunked
A05  response: Transfer-Encoding present, final coding not chunked
A06  request: Transfer-Encoding present, final coding not chunked
A07  invalid Content-Length but recoverable identical-list form
A08  unrecoverable invalid Content-Length in request
A09  unrecoverable invalid Content-Length in proxy-received response
A10  unrecoverable invalid Content-Length in user-agent-received response
A11  valid Content-Length without Transfer-Encoding
A12  request fallback when no prior branch applies
A13  response fallback when no prior branch applies
```

These IDs are project-local references only; RFC 9112 remains the external authority.

## 5. Locked DSD interfaces

```text
FORMATION_LAYER: used only as structural carrier background
PROPERTY_CORE: used for typed condition/action records where helpful
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
EXTERNAL_DOMAIN: HTTP/1.1 message framing
EXTERNAL_STANDARD: RFC 9112 §6.3
DOMAIN_BRIDGE: explicit mapping from each DSD requirement atom to its RFC source unit
```

No inactive DSD layer may be added to manufacture complexity or gain.

## 6. Precommitted fidelity criteria

A DSD re-expression passes source fidelity only if all of the following hold:

```text
SOURCE_UNIT_COVERAGE: 13/13
TRIGGER_OR_ACTOR_SCOPE_PRESERVATION: 13/13
PRECEDENCE_PRESERVATION: 13/13
NORMATIVE_STRENGTH_PRESERVATION: all applicable normative actions preserved
INVENTED_SOURCE_FACTS: 0
SILENTLY_DROPPED_SOURCE_ACTIONS: 0
WRONG_EXTERNAL_STANDARD_SUBSTITUTIONS: 0
```

`PRECEDENCE_PRESERVATION` means each atom is explicitly subordinated to all higher-priority applicable branches, whether represented by a dedicated precedence field or by explicit activation/dependency conditions. Mere row order without declared semantic force is insufficient.

## 7. Gain / NO_GAIN criteria

Only these precommitted operational gain dimensions count:

```text
DISTINCTION_GAIN
TRACEABILITY_GAIN
AMBIGUITY_REDUCTION_GAIN
DOWNSTREAM_CHECKABILITY_GAIN
```

No gain credit for:
- DSD terminology substitution;
- reordering the RFC list;
- copying already-explicit actor/condition/action information into a table;
- duplicating the existing precedence numbers;
- adding irrelevant DSD layers;
- treating DSD internal consistency as HTTP validity.

Allowed comparative outcomes:

```text
SPEC_NO_GAIN
  source baseline already exposes equivalent task-relevant operational structure

usable_with_operational_gain
  DSD adds at least one locked operational gain without losing source fidelity

usable_with_protocol_pressure
  source fidelity is preserved, but Protocol v0.1 needs a cumbersome encoding that exposes a schema improvement need

SPEC_UNDERSPECIFIED
  the DSD representation fails to state a source-required distinction/condition/action
```

Protocol-pressure observations do not count as DSD gain by themselves.

## 8. Protocol-pressure check

RFC 9112 §6.3 explicitly uses ordered precedence. Protocol v0.1 has `ACTIVATION_CONDITION` and `DEPENDENCIES` but no dedicated `PRECEDENCE_OR_PRIORITY` atom field.

Precommitted question:

```text
Can the precedence relation be preserved explicitly and retraceably with v0.1 as written?
```

If yes, the application may pass fidelity while separately recording a possible v0.2 convenience improvement.
If no, the result must preserve that failure rather than adding a field retroactively and rescoring the same run.

## 9. Evidence and maturity boundary

This corpus is externally authored and independently generated relative to DSD. It therefore satisfies the **origin** requirement for an external application case if the application is completed under this lock.

It does not establish:
- independent evaluator agreement;
- empirical engineering performance improvement;
- HTTP implementation conformance;
- correctness of RFC 9112 itself;
- mature DSD Specification validity by itself.

## 10. Scoring lock

```text
POST_REVEAL_CRITERION_CHANGE: prohibited for this run
POST_REVEAL_EXCEPTION_ADDITION: prohibited for this run
SOURCE_FACT_INVENTION: prohibited
BASELINE_DOWNGRADE: prohibited
NO_GAIN_RESCUE: prohibited
```

The result record must preserve a genuine `SPEC_NO_GAIN`, protocol pressure, or failure if observed.