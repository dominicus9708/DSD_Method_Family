# DSD Interpretation pre-protocol boundary attacks v0.1

Status: **18 attacks completed before Protocol v0.1 freeze**  
Date: **2026-09-14**

The attacks target the historical Task Interface v0.1 draft. They are not direct validation cases.

## Result summary

```text
BOUNDARY_ATTACKS_RUN: 18
PRESERVED_NO_REFINEMENT: 11
PRESERVED_WITH_NONBREAKING_REFINEMENT: 7
BOUNDARY_COLLAPSE_FOUND: 0
FUNDAMENTAL_INTERFACE_FAILURE: 0
```

## Attacks

### B1 — same title, different source version
Two source versions share a title but differ in a claim-relevant clause. Treating the title as identity would make the reading unstable.

Result: preserved with refinement.
Required: explicit source identity/version/witness lock and version-relative reading provenance.

### B2 — translation resolves an ambiguity not resolved in the source
A translation selects one of two grammatically possible source readings.

Result: preserved with refinement.
Required: translation/normalization mapping and loss/choice ledger; translation choice cannot be retroactively attributed to the source.

### B3 — commentary presented adjacent to source text
A later commentator's explanation is copied into the same document view as the primary text.

Result: preserved without refinement.
Existing `SOURCE_ROLE` distinction blocks commentary-as-source substitution.

### B4 — later reception used as original context
A later institution or commentator adopts a reading centuries after the source.

Result: preserved with refinement.
Required: explicit temporal-role separation between source context and later reception.

### B5 — missing contextual record
The requested reading depends on a contextual convention that is not supplied.

Result: preserved without refinement.
Correct result may be `UNDERDETERMINED` or `BLOCKED_BY_MISSING_SOURCE_OR_BRIDGE`, not invented context.

### B6 — two source-compatible readings
The source and supplied context support two mutually distinct readings at the declared resolution.

Result: preserved with refinement.
Required: alternative-reading relation and `INTERPRETATION_RESOLVED_MULTI` semantics; plurality is not failure.

### B7 — source silence treated as negation
The source does not state P; an interpreter outputs not-P.

Result: preserved without refinement.
`SOURCE_SILENCE != NEGATIVE_CLAIM` blocks the inference.

### B8 — conflict across source witnesses
Two supplied witnesses differ on a claim-relevant phrase and no precedence rule is supplied.

Result: preserved with refinement.
Required: witness-conflict ledger and no hidden harmonization/precedence.

### B9 — direct statement and contextual implication diverge
The source states X while a contextual record makes Y plausible.

Result: preserved without refinement.
Textual statement and contextual reading remain separate evidence roles.

### B10 — same wording under different actor/perspective scope
A pronoun, command, or duty changes referent depending on declared actor/perspective.

Result: preserved with refinement.
Required: actor/perspective scope lock and perspective-relative reading provenance.

### B11 — summary preserves output but loses clause order
An aggregate or summary yields the same summary value for two source structures whose ordering changes interpretation.

Result: preserved without refinement.
Summary/aggregate may be consumed only as a handoff and cannot replace source structure when the interpretation claim requires ordering.

### B12 — temporal sequence is interpretively material
A narrative or instruction changes meaning if events are reordered.

Result: preserved without refinement.
Dynamics may be activated conditionally; static interpretation must not invent temporal relations.

### B13 — Analysis boundary
A target is structurally decomposed into clauses, roles, and conditions, but no contextual bridge or reading claim is made.

Result: preserved without refinement.
This is Analysis output, not Interpretation merely because the object is text.

### B14 — Comparison boundary
Two readings are already supplied and the task asks only where they correspond/diverge.

Result: preserved without refinement.
That is Comparison unless Interpretation must first derive/evaluate readings from source/context.

### B15 — Provenance/Lineage boundary
The task asks which manuscript copied which witness and in what historical chain.

Result: preserved without refinement.
Origin/successor chain is Provenance/Lineage, not source meaning.

### B16 — Reconstruction boundary
A damaged phrase is missing and the task asks to infer the missing wording.

Result: preserved with refinement.
Required: explicit reconstruction handoff rule. Interpretation may consume a reconstruction record but may not silently create missing source text.

### B17 — Classification boundary
A passage is assigned to a genre/category using a supplied taxonomy and criteria.

Result: preserved without refinement.
Taxonomy assignment is Classification; genre membership is not automatically an interpretive conclusion.

### B18 — Audit boundary
A prior interpretation report is checked for source-role leakage, missing bridges, and unsupported claims.

Result: preserved without refinement.
That is Audit of Interpretation, not a new Interpretation run.

## Non-breaking refinement groups forced by the attacks

```text
R1 SOURCE_ID_VERSION_WITNESS_LOCK
R2 TRANSLATION_NORMALIZATION_MAPPING_AND_LOSS_LEDGER
R3 SOURCE_CONTEXT_VS_LATER_RECEPTION_TEMPORAL_ROLE
R4 MULTI_READING_RELATION_AND_RESOLVED_MULTI_SEMANTICS
R5 WITNESS_CONFLICT_AND_PRECEDENCE_POLICY
R6 ACTOR_PERSPECTIVE_SCOPE_AND_PROVENANCE
R7 RECONSTRUCTION_HANDOFF_AND_NO_SILENT_TEXT_COMPLETION
```

These refinements do not change the method's task identity. They make already implicit interpretation obligations executable and auditable.

## Boundary conclusion

No exact collapse with Analysis, Comparison, Classification, Provenance, Lineage, Reconstruction, or Audit was forced by the 18 attacks.

This result is pre-protocol infrastructure only. It is not permanent nonmerger evidence and does not decide method survival.