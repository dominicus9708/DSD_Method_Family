# CMP-APP-001 Precommit / DSD 비교론 Unicode Normalization External Application 사전동결

Status: **PRECOMMITTED — execution not yet performed at commit time**  
Date: **2026-09-11**  
Method: **DSD Comparison / DSD 비교론**  
Protocol: **v0.1**  
Protocol commit: `a1700d960e0b41dfe32bf85b6334448d9104100d`

## 1. Evidence identity

```text
CASE_ID: CMP-APP-001
CASE_CLASS: external_application
CASE_ORIGIN: public_external_standard
METHOD_VERSION_OR_PROTOCOL: Comparison Protocol v0.1
EVIDENCE_SCOPE_CLASS: method_specific
EXTERNAL_DOMAIN: Unicode text normalization / character-sequence equivalence
BASELINE: none
METHOD_GAIN: NOT_ASSESSED
```

Purpose: test Comparison Protocol v0.1 against a stable public standard whose own rules distinguish binary identity, canonical equivalence, compatibility equivalence, and normalized-form comparison.

## 2. External source lock

Primary source:

```text
Unicode Standard Annex #15: Unicode Normalization Forms
Version: Unicode 17.0.0
Revision: 57
Date: 2025-07-30
Publisher: Unicode Consortium
Stable document: yes
Canonical URL: https://www.unicode.org/reports/tr15/
Version URL: https://www.unicode.org/reports/tr15/tr15-57.html
```

Supporting normative context:

```text
The Unicode Standard 17.0.0, Chapter 3, Section 3.11 Normalization Forms
https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/
```

Frozen source facts used by this application:

```text
S1 canonical equivalence is stronger than mere compatibility equivalence.
S2 NFC/NFD preserve canonical equivalence and give equivalent strings the same normalized form.
S3 NFKC/NFKD also fold compatibility-equivalent strings to the same normalized form.
S4 binary comparison of normalized strings can be used to determine the corresponding equivalence.
S5 UAX #15 lists Ç <-> C + COMBINING CEDILLA as canonical-equivalence example.
S6 UAX #15 lists q + COMBINING DOT ABOVE + COMBINING DOT BELOW
   <-> q + COMBINING DOT BELOW + COMBINING DOT ABOVE as canonical-equivalence example.
S7 UAX #15 lists 가 <-> ᄀ + ᅡ as canonical-equivalence example.
S8 UAX #15 lists ① -> 1 as compatibility-equivalence example.
```

No Unicode confusability, locale collation, grapheme-cluster equality, identifier-security rule, rendering-engine behavior, or language-semantic equality is imported.

## 3. Frozen comparison discipline

For each subcase the comparison criterion is frozen independently.

```text
BINARY_IDENTITY:
  exact code-point sequence identity only.

CANONICAL_EQUIVALENCE_VIA_NFC:
  compare NFC-normalized sequences;
  equal normalized result -> canonical-equivalence correspondence.

COMPATIBILITY_EQUIVALENCE_VIA_NFKC:
  compare NFKC-normalized sequences;
  equal normalized result -> compatibility-equivalence correspondence.
```

DSD relation-label policy for this external application:

```text
If raw sequences are not literally identical but equivalence is established only through the externally supplied normalization mapping,
  -> ENCODED_CORRESPONDENCE.

If the frozen criterion is exact binary identity and raw sequences differ,
  -> NONCORRESPONDENCE under that binary-identity criterion.

If the frozen criterion is canonical equivalence and the pair is only compatibility-equivalent,
  -> NONCORRESPONDENCE under the canonical-equivalence criterion.
```

This does not claim that `NONCORRESPONDENCE` under one criterion means no relationship exists under every stronger/weaker/different criterion.

## 4. Frozen candidate set

### U1 — canonical equivalence, precomposed versus combining sequence

```text
LEFT:  Ç  U+00C7
RIGHT: C U+0043 + COMBINING CEDILLA U+0327
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
SOURCE BASIS: UAX #15 canonical-equivalence example
EXPECTED:
  raw binary identity: no
  normalized canonical comparison: equal
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
```

### U2 — same pair under exact binary identity

```text
LEFT:  Ç  U+00C7
RIGHT: C U+0043 + COMBINING CEDILLA U+0327
CRITERION: BINARY_IDENTITY
EXPECTED:
  exact code-point sequence identity: no
  CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen binary criterion
  TERMINAL: COMPARISON_RESOLVED
```

### U3 — compatibility-only pair under canonical criterion

```text
LEFT:  ① U+2460 CIRCLED DIGIT ONE
RIGHT: 1 U+0031 DIGIT ONE
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
SOURCE BASIS: UAX #15 compatibility-equivalence example
EXPECTED:
  compatibility relation exists in source
  canonical equivalence under NFC criterion: no
  CORRESPONDENCE_CLASS: NONCORRESPONDENCE under frozen canonical criterion
  TERMINAL: COMPARISON_RESOLVED
```

### U4 — same pair under compatibility criterion

```text
LEFT:  ① U+2460 CIRCLED DIGIT ONE
RIGHT: 1 U+0031 DIGIT ONE
CRITERION: COMPATIBILITY_EQUIVALENCE_VIA_NFKC
EXPECTED:
  normalized compatibility comparison: equal
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
```

### U5 — Hangul syllable versus conjoining jamo

```text
LEFT:  가 U+AC00
RIGHT: ᄀ U+1100 + ᅡ U+1161
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
SOURCE BASIS: UAX #15 canonical-equivalence example
EXPECTED:
  raw binary identity: no
  normalized canonical comparison: equal
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
```

### U6 — combining-mark ordering canonical equivalence

```text
LEFT:  q + COMBINING DOT ABOVE + COMBINING DOT BELOW
RIGHT: q + COMBINING DOT BELOW + COMBINING DOT ABOVE
CRITERION: CANONICAL_EQUIVALENCE_VIA_NFC
SOURCE BASIS: UAX #15 canonical-equivalence example
EXPECTED:
  raw binary identity: no
  canonical ordering/normalization establishes equivalence
  CORRESPONDENCE_CLASS: ENCODED_CORRESPONDENCE
  TERMINAL: COMPARISON_RESOLVED
```

## 5. Frozen cross-case claims

The application must preserve all of the following:

```text
RAW_BINARY_INEQUALITY != CANONICAL_NONCORRESPONDENCE
CANONICAL_EQUIVALENCE != COMPATIBILITY_EQUIVALENCE
NFC_EQUIVALENCE_RESULT != NFKC_EQUIVALENCE_RESULT_IN_GENERAL
SAME_PAIR + DIFFERENT_CRITERION -> possibly different comparison verdict
NORMALIZATION_BRIDGE_DEPENDENCE != DIRECT_LITERAL_IDENTITY
VISUAL_SIMILARITY is outside this task
```

In particular:

```text
U1 and U2 use the same pair but different criteria.
U3 and U4 use the same pair but different criteria.
```

The protocol must therefore preserve comparison-criterion provenance rather than treating relation class as intrinsic to the pair alone.

## 6. Output and closure policy

```text
CLAIMED_OUTPUT_LEVEL: CORRESPONDENCE_CLASSIFICATION
MAP_OR_BRIDGE_FAMILY: externally supplied Unicode normalization mapping appropriate to frozen criterion
MAP_FAMILY_COVERAGE: sufficient relative to the specific criterion and pair, not a claim about every Unicode relation
COMPARISON_ELEMENT_COVERAGE: exact frozen code-point sequences + normalized result under selected form
FIRST_BRANCH_POINT: not claimed
LINEAGE_IDENTITY: not claimed
AGGREGATE_READOUT: not used
```

Expected admissible resolved set:

```text
ALL SIX SUBCASES: COMPARISON_RESOLVED
ALL SIX: protocol conformance expected CONFORMANT
```

Relation outputs:

```text
U1 ENCODED_CORRESPONDENCE
U2 NONCORRESPONDENCE under binary criterion
U3 NONCORRESPONDENCE under canonical criterion
U4 ENCODED_CORRESPONDENCE
U5 ENCODED_CORRESPONDENCE
U6 ENCODED_CORRESPONDENCE
```

## 7. Method-gain policy

No fair independent comparison baseline is supplied in `CMP-APP-001`.

Therefore:

```text
COMPARISON_METHOD_GAIN_STATUS: NOT_ASSESSED
```

External-source agreement or protocol conformance must not be converted into `GAIN_ESTABLISHED`.

## 8. Precommitted scoring

Total required checks: **42**.

```text
A. source / precommit integrity: 8
B. candidate verdicts and terminals: 12
C. criterion / provenance discipline: 10
D. closure / protocol ledgers: 6
E. external-scope discipline: 6
```

Detailed checks:

```text
A1 Protocol commit fixed
A2 UAX #15 version/revision/date fixed
A3 candidate set U1-U6 fixed
A4 criteria fixed per case
A5 relation-label policy fixed
A6 score fixed before execution
A7 no post-hoc criterion substitution
A8 no unlisted Unicode relation imported

B1-B6 exact U1-U6 correspondence class
B7-B12 exact U1-U6 terminal COMPARISON_RESOLVED

C1 U1 raw inequality retained
C2 U1 canonical equivalence retained
C3 U2 same pair changes result under binary criterion without contradiction
C4 U3 compatibility-only relationship not upgraded to canonical equivalence
C5 U4 compatibility equivalence established only under NFKC criterion
C6 U5 Hangul canonical equivalence retained
C7 U6 combining-order canonical equivalence retained
C8 criterion provenance retained for every case
C9 normalization-dependent cases remain ENCODED rather than DIRECT literal correspondence
C10 no visual-similarity or semantic-language claim imported

D1 all six DSD runs CONFORMANT
D2 all six resolved without underdetermined/blocked fabrication
D3 no first-branch claim fabricated
D4 no lineage claim fabricated
D5 method gain remains NOT_ASSESSED
D6 Protocol revision not required if no contradiction appears

E1 external application recorded separately from constructed direct pilots
E2 external domain count increments by one only
E3 no practical superiority claim
E4 no independent-validation/reproducibility claim
E5 no maturity claim
E6 no method survival/merger/absorption/deletion conclusion
```

Decision:

```text
42/42 -> APPLICATION_VERDICT: PASS
otherwise -> APPLICATION_VERDICT: FAIL
```

## 9. Evidence-count lock

Before execution:

```text
DIRECT_COMPARISON_PILOTS: 5
NO_GAIN_COMPARISON_CASES: 2
BASELINE_COMPARISON_CASES: 2
STRONGEST_REASONABLE_BASELINE_COMPARISON: established_at_constructed_evidence_level
EXTERNAL_COMPARISON_APPLICATIONS: 0
EXTERNAL_COMPARISON_DOMAINS: 0
EXTERNAL_COMPARISON_APPLICATION_PASSES: 0
REPRODUCIBILITY_CASES: 0
COMPARISON_METHOD_MATURITY_CLASSIFICATION: proposed
```

A 42/42 PASS may add exactly:

```text
EXTERNAL_COMPARISON_APPLICATIONS: +1
EXTERNAL_COMPARISON_DOMAINS: +1
EXTERNAL_COMPARISON_APPLICATION_PASSES: +1
```

It does not increment `DIRECT_COMPARISON_PILOTS` and does not establish method gain, reproducibility, independent validation, maturity, or permanent registry status.
