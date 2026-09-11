# CMP-APP-001 Result / DSD 비교론 Unicode Normalization External Application 결과

Status: **EXECUTED — 42/42 PASS**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`  
Precommit commit: `e1a109b9e4515336b4ee22c4d8ff216d4fd21705`  
Precommit blob: `640f2b5e7cf9b990a07a2e3db542b114d655122f`

## 1. Evidence identity

```text
CASE_ID: CMP-APP-001
CASE_CLASS: external_application
CASE_ORIGIN: public_external_standard
EXTERNAL_DOMAIN: Unicode text normalization / character-sequence equivalence
SOURCE: Unicode Standard Annex #15, Unicode 17.0.0, Revision 57
BASELINE: none
METHOD_GAIN: NOT_ASSESSED
```

The immutable precommit was fetched by commit before execution. No candidate pair, criterion, source fact, relation-label rule, scoring item, or evidence-count rule was changed.

## 2. External-source result lock

UAX #15 defines canonical equivalence separately from compatibility equivalence and defines NFC/NFD versus NFKC/NFKD accordingly. Equivalent strings under the relevant normalization relation obtain identical normalized representations suitable for binary comparison.

The specific source examples used by the frozen task are:

```text
Ç <-> C + COMBINING CEDILLA
q + COMBINING DOT ABOVE + COMBINING DOT BELOW
  <-> q + COMBINING DOT BELOW + COMBINING DOT ABOVE
가 <-> ᄀ + ᅡ
① -> 1 as compatibility equivalence
```

No source relation beyond the precommit was imported.

## 3. U1 — canonical equivalence under NFC

```text
LEFT:  U+00C7 Ç
RIGHT: U+0043 C + U+0327 COMBINING CEDILLA
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC

RAW_BINARY_IDENTITY: no
NFC(LEFT):  U+00C7
NFC(RIGHT): U+00C7
NORMALIZED_COMPARISON: equal

CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

The raw code-point sequences remain distinct even though the externally supplied normalization relation closes canonical equivalence.

## 4. U2 — same pair under binary identity

```text
LEFT:  U+00C7
RIGHT: U+0043 U+0327
CRITERION: BINARY_IDENTITY

EXACT_CODE_POINT_SEQUENCE_IDENTITY: no

CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen binary criterion
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

This does not contradict U1 because U1 and U2 ask different externally frozen comparison questions.

## 5. U3 — compatibility-only pair under canonical criterion

```text
LEFT:  U+2460 ①
RIGHT: U+0031 1
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC

SOURCE_RELATION: compatibility equivalence
NFC(LEFT):  U+2460
NFC(RIGHT): U+0031
NORMALIZED_CANONICAL_COMPARISON: different

CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen canonical criterion
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

The weaker/alternative compatibility relation was not upgraded into canonical equivalence.

## 6. U4 — same pair under compatibility criterion

```text
LEFT:  U+2460 ①
RIGHT: U+0031 1
CRITERION: COMPATIBILITY_EQUIVALENCE_VIA_NFKC

NFKC(LEFT):  U+0031
NFKC(RIGHT): U+0031
NORMALIZED_COMPATIBILITY_COMPARISON: equal

CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

U3 and U4 therefore preserve the distinction between canonical and compatibility criteria for the same pair.

## 7. U5 — Hangul syllable versus conjoining jamo

```text
LEFT:  U+AC00 가
RIGHT: U+1100 ᄀ + U+1161 ᅡ
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC

RAW_BINARY_IDENTITY: no
NFC(LEFT):  U+AC00
NFC(RIGHT): U+AC00
NORMALIZED_CANONICAL_COMPARISON: equal

CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

## 8. U6 — combining-mark ordering

```text
LEFT:  q + COMBINING DOT ABOVE + COMBINING DOT BELOW
RIGHT: q + COMBINING DOT BELOW + COMBINING DOT ABOVE
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC

RAW_BINARY_IDENTITY: no
CANONICAL_ORDERING/NORMALIZATION: same normalized sequence
NORMALIZED_CANONICAL_COMPARISON: equal

CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
```

The comparison records equivalence under Unicode canonical ordering rather than pretending that the original code-point order was identical.

## 9. Cross-case comparison

```text
CASE  RAW/BASIS                         FROZEN CRITERION                    RESULT
U1    Ç vs C+cedilla                   canonical via NFC                  ENCODED_CORRESPONDENCE
U2    same pair                        binary identity                    NONCORRESPONDENCE
U3    ① vs 1                           canonical via NFC                  NONCORRESPONDENCE
U4    same pair                        compatibility via NFKC             ENCODED_CORRESPONDENCE
U5    가 vs ᄀ+ᅡ                       canonical via NFC                  ENCODED_CORRESPONDENCE
U6    reordered combining marks        canonical via NFC                  ENCODED_CORRESPONDENCE
```

The result preserves:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
```

`CORRESPONDENCE_CLASS` is therefore not treated as an intrinsic label of a pair independent of task criterion.

## 10. Three-ledger result

Across U1-U6:

```text
TERMINAL_COMPARISON_STATUS: COMPARISON_RESOLVED
COMPARISON_PROTOCOL_CONFORMANCE: CONFORMANT
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

No baseline was supplied, so external-source agreement was not converted into comparative method gain.

## 11. Precommitted scoring

```text
A. source / precommit integrity          8 / 8 PASS
B. candidate verdicts and terminals     12 / 12 PASS
C. criterion / provenance discipline    10 / 10 PASS
D. closure / protocol ledgers            6 / 6 PASS
E. external-scope discipline             6 / 6 PASS

PRECOMMITTED_REQUIRED_CHECKS:           42
PASSED:                                  42
FAILED:                                   0
APPLICATION_VERDICT:                   PASS
```

No item was deleted, weakened, or reclassified after execution.

## 12. Evidence increment

```text
DIRECT_COMPARISON_PILOTS: 5  # unchanged; constructed lane only
EXTERNAL_COMPARISON_APPLICATIONS: 1
EXTERNAL_COMPARISON_DOMAINS: 1
EXTERNAL_COMPARISON_APPLICATION_PASSES: 1
REPRODUCIBILITY_CASES: 0
```

Other state remains:

```text
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
INDEPENDENT_COMPARISON_VALIDATION: not established
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
CURRENT_COMPARISON_EVIDENCE_STATUS: validation_in_progress
```

## 13. Protocol pressure

```text
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
```

The external criterion dependence fit the existing Comparison requirement to freeze scope, map/bridge family, output level, and relation criterion before evaluation.

## 14. Limits

This application establishes only that Comparison Protocol v0.1 can preserve the selected Unicode normalization distinctions in one stable public-standard domain.

It does not establish:

```text
Unicode implementation conformance in general
locale-sensitive collation correctness
grapheme-cluster identity
visual confusability
identifier-security equivalence
language-semantic equality
practical superiority of DSD Comparison
independent replication
independent validation
method maturity
permanent method survival or irreducibility
```

## 15. Next

Run a deterministic same-project retrace of `CMP-APP-001` from the frozen protocol, precommit, external source lock, and result record. The retrace must reproduce all six criterion-specific relation classes, terminals, and scope exclusions without reopening the task.
