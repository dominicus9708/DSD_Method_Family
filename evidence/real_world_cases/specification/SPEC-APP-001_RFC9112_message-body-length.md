# SPEC-APP-001 — RFC 9112 §6.3 Message Body Length / 외부 명세 적용

Date: 2026-09-06
Evidence scope: `method_specific`
Case origin: `public_normative_standard`
Method directly tested: **DSD Specification / DSD 명세론**
Method protocol: **DSD Specification Protocol v0.1**
Precommit: [`SPEC-APP-001_RFC9112_message-body-length_precommit.md`](SPEC-APP-001_RFC9112_message-body-length_precommit.md)
Precommit commit: `9b91cecda9516fd7cd65c9eb181e80ab4fa45deb`

## 1. External source

Primary authoritative source:
- RFC 9112, *HTTP/1.1*, STD 99, June 2022, RFC Editor.
- Locked corpus: §6.3, core message-body-length precedence algorithm through numbered item 8.
- Canonical source: https://www.rfc-editor.org/rfc/rfc9112.html#section-6.3
- Status: https://www.rfc-editor.org/info/rfc9112

Current-source context retained from the precommit:
- RFC 9112 is updated by RFC 9931 (March 2026).
- RFC 9931 §8 adds separate HTTP CONNECT requirements; this run does not silently merge those additions into the locked §6.3 framing corpus.
- Verified RFC 9112 errata currently concern other sections, not the locked §6.3 precedence text.

RFC 9112 §1.1 defines BCP 14 requirement-keyword force only for the all-capital forms. Therefore the lowercase advisory word `ought` in §6.3 item 3 is not upgraded to `MUST` or `SHOULD` in this record.

## 2. Source / interpretation boundary

The RFC determines HTTP semantics and conformance requirements.

DSD Specification only re-expresses the locked clauses as typed requirement atoms and checks whether that representation preserves:
- source trigger conditions;
- actor scope;
- precedence;
- required action;
- BCP 14 force;
- source references.

No DSD-internal success is treated as proof that an HTTP implementation conforms to RFC 9112.

## 3. DSD layer lock

```text
FORMATION_LAYER: used as structural carrier background
PROPERTY_CORE: used for typed condition/action records
STATIC_AGGREGATION_LAYER: not used
DYNAMICS_LAYER: not used
REALIZED_AXIS_SPECIALIZATION: not supplied
EXTERNAL_DOMAIN: HTTP/1.1 message framing
EXTERNAL_STANDARD: RFC 9112 §6.3
DOMAIN_BRIDGE: explicit atom -> RFC clause mapping
```

No additional DSD layer was activated during scoring.

## 4. Requirement atomization

Protocol v0.1 does not have a dedicated precedence field. To preserve the RFC's ordered semantics without altering the protocol, each lower-priority atom explicitly depends on the non-activation of all higher-priority source ranks.

`P<n>` below is a recording aid in this application, not a new Protocol v0.1 atom field.

| Atom | Source unit | Typed activation summary | Required result/action | Precedence encoding |
|---|---|---|---|---|
| A01 | §6.3 item 1 | response to HEAD, or response status 1xx/204/304 | terminate after header section; no message body/trailer | P1 |
| A02 | item 2 | 2xx response to CONNECT; A01 inactive | tunnel begins; client ignores Content-Length/Transfer-Encoding | P2; depends on P1 inactive |
| A03 | item 3 | both Transfer-Encoding and Content-Length; P1–P2 inactive | Transfer-Encoding controls framing; forwarding intermediary removes Content-Length and processes Transfer-Encoding first | P3; P1–P2 inactive |
| A04 | item 4a | Transfer-Encoding present, final coding is chunked; P1–P3 inactive | determine length by decoding chunked data to completion | P4 branch |
| A05 | item 4b | response; Transfer-Encoding present; final coding not chunked; P1–P3 inactive | length is close-delimited | P4 branch |
| A06 | item 4c | request; Transfer-Encoding present; final coding not chunked; P1–P3 inactive | server returns 400 and closes connection | P4 branch |
| A07 | item 5 exception | no Transfer-Encoding; Content-Length syntactically invalid as a single value but recoverable as a valid identical-value list; P1–P4 inactive | process using the single identical value | P5 exception branch |
| A08 | item 5 request | no Transfer-Encoding; unrecoverable invalid Content-Length in request; P1–P4 inactive | server returns 400 and closes | P5 actor branch |
| A09 | item 5 proxy response | no Transfer-Encoding; unrecoverable invalid Content-Length in response received by proxy; P1–P4 inactive | proxy closes upstream connection, discards response, sends 502 downstream | P5 actor branch |
| A10 | item 5 UA response | no Transfer-Encoding; unrecoverable invalid Content-Length in response received by user agent; P1–P4 inactive | user agent closes upstream connection and discards response | P5 actor branch |
| A11 | item 6 | valid Content-Length, no Transfer-Encoding; P1–P5 inactive | Content-Length defines expected octets; premature close/timeout means incomplete and connection close | P6 |
| A12 | item 7 | request; none of P1–P6 applies | no message body | P7 |
| A13 | item 8 | response; none of P1–P7 applies | body length is close-delimited | P8 |

The table paraphrases the source. RFC 9112 remains the normative wording and authority.

## 5. Fidelity scoring

```text
SOURCE_UNIT_COVERAGE: 13/13
TRIGGER_OR_ACTOR_SCOPE_PRESERVATION: 13/13
PRECEDENCE_PRESERVATION: 13/13
BCP14_MUST_OBLIGATIONS_PRESERVED: 8/8
LOWERCASE_OUGHT_UPGRADED_TO_BCP14_REQUIREMENT: no
INVENTED_SOURCE_FACTS: 0
SILENTLY_DROPPED_SOURCE_ACTIONS: 0
WRONG_EXTERNAL_STANDARD_SUBSTITUTIONS: 0
SOURCE_FIDELITY_RESULT: pass
```

The eight BCP 14 `MUST` obligations counted here are the locked core obligations concerning:
1. CONNECT-response header ignoring;
2. intermediary handling when both framing fields are received and the message is forwarded;
3. request handling when non-final chunked framing makes length unreliable;
4. general unrecoverable invalid-Content-Length treatment subject to the source exception;
5. request-side unrecoverable invalid-Content-Length action;
6. proxy-side response action;
7. user-agent-side response action;
8. incomplete valid-Content-Length handling.

This count is only a fidelity check; it does not replace the source's own conformance language.

## 6. Gain / NO_GAIN comparison

Strongest reasonable baseline: **RFC 9112 §6.3 itself**.

The source already supplies:
- an explicit ordered precedence list;
- explicit request/response branches;
- explicit actor-specific error actions;
- explicit framing-field distinctions;
- directly locatable numbered source clauses;
- BCP 14 requirement keywords where normative force is intended.

Precommitted gain dimensions were scored as follows:

```text
DISTINCTION_GAIN: no demonstrated gain
TRACEABILITY_GAIN: no demonstrated gain
AMBIGUITY_REDUCTION_GAIN: no demonstrated gain
DOWNSTREAM_CHECKABILITY_GAIN: no demonstrated gain
```

Reasoning:
- atom IDs do not add a source distinction that the RFC lacked;
- the original section is already strongly traceable by numbered rule and section;
- the original source explicitly states its precedence relation;
- this application produced a structured table, not a new executable conformance checker.

Therefore:

```text
FINAL_SPEC_STATUS: no_gain
NO_GAIN_STATUS: true
COMPETITIVE_RESULT: BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK
RESULT: SPEC_NO_GAIN
```

`BASELINE_PREFERRED_FOR_THIS_LOCKED_TASK` means the RFC's original ordered presentation is more compact while already exposing the task-relevant operational structure. It is not a claim that DSD Specification is generally inferior.

## 7. Protocol pressure observed

```text
PROTOCOL_PRESSURE: present_nonfatal
PRESSURE_POINT: ordered precedence / priority
SOURCE_FIDELITY_LOST: no
SAME_RUN_PROTOCOL_CHANGE: no
```

Protocol v0.1 can preserve the precedence semantics by writing predecessor-exclusion conditions into `ACTIVATION_CONDITION` / `DEPENDENCIES`, so the run does not fail source fidelity.

However, the encoding is repetitive. A future protocol revision may consider an **optional explicit precedence/priority field** for ordered decision procedures.

This is only a refinement candidate. It was not added retroactively to v0.1 and did not rescore the run.

## 8. Shared-core activation

```text
SC-02 active: source/update/errata and protocol version lock
SC-03 active: explicit DSD-atom -> RFC-clause domain bridge
SC-04 active: Static/Dynamics/axis remain inactive
SC-07 active: method-specific evidence + public normative-standard origin
SC-08 active: strongest baseline, precommit, NO_GAIN and baseline-preferred preservation
SC-10 active: RFC remains the HTTP domain authority

SC-01 limited: typed message/actor/condition distinctions, not DSD object-status semantics
SC-05 inactive
SC-06 inactive
SC-09 inactive for the scored claim
```

No new shared-core rule is proposed.

## 9. External-origin requirement

This corpus was authored and standardized independently of DSD and existed before this application.

```text
EXTERNAL_OR_INDEPENDENTLY_GENERATED_CORPUS: yes
PUBLIC_AUTHORITATIVE_SOURCE: yes
SAME_PROJECT_CONSTRUCTED_BENCHMARK: no
```

Thus the case satisfies the project maturity checklist's **external-or-independently-generated application origin** requirement.

It does not satisfy independent evaluator validation because the DSD application and scoring were still performed by the same assistant/model family in the current project.

## 10. Reproducibility record

```text
METHOD_PROTOCOL: Specification Protocol v0.1
PRECOMMIT_COMMIT: 9b91cecda9516fd7cd65c9eb181e80ab4fa45deb
SOURCE: RFC 9112 §6.3 core precedence algorithm
SOURCE_VERSION: June 2022, current status checked 2026-09-06
SOURCE_UPDATE_CONTEXT: RFC 9931 noted separately
ERRATA_CONTEXT: verified RFC 9112 errata checked; none changes locked §6.3 precedence corpus
LOCKED_SOURCE_ATOMS: 13
SOURCE_FIDELITY_SCORING: 13 units + BCP14 obligation preservation
POST_REVEAL_CRITERION_CHANGE: no
POST_REVEAL_EXCEPTION_ADDITION: no
SOURCE_FACT_INVENTION: 0
```

## 11. Limits

- one external technical standard and one selected subsection;
- no implementation conformance tests;
- no external reviewer or independent model retrace;
- no measured time, defect-rate, comprehension, maintenance, or inter-rater improvement;
- source is already unusually structured, making it a strong baseline but not representative of all real-world requirement prose;
- external application supports method restraint and source fidelity on this corpus, not general utility.

## 12. Next step

The initial internal challenge sequence and the first external/independently generated application are now both present.

Next perform a **DSD Specification maturity audit** against the repository promotion checklist. Do not automatically promote the method merely because the checklist now has an external-origin case; the audit must separately evaluate evidence breadth, independence, baseline result, protocol pressure, and remaining limitations.
