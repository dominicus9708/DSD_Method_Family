# DSD Interpretation Task Interface Boundary Amendment 001

Status: **established before Protocol v0.1 freeze**  
Date: **2026-09-14**

This amendment is additive. The historical `TASK_INTERFACE_v0.1-draft.md` remains unchanged.

## A1 — source identity/version/witness lock

Every claim-relevant source unit must record a stable source identifier plus version, edition, witness, revision, or equivalent discriminator when multiple materially different forms can exist.

```text
SAME_TITLE != SAME_SOURCE_VERSION
SAME_WORK_LABEL != SAME_WITNESS_CONTENT
```

Interpretive conclusions are version-relative unless a broader cross-version claim is separately established.

## A2 — translation/normalization mapping and loss ledger

Whenever translation, transliteration, normalization, modernization, tokenization, or equivalent preprocessing is claim-relevant, record:

```text
SOURCE_SPAN
TARGET_RENDERING
TRANSFORMATION_TYPE
CHOICE_OR_LOSS
REVERSIBILITY_STATUS
ALTERNATIVES_PRESERVED
```

A translation decision may support a translated-text reading but cannot be silently reclassified as the source's uniquely determined meaning.

## A3 — source context vs later reception

Context records must carry temporal/role provenance sufficient to distinguish:

```text
SOURCE_CONTEXT
CONTEMPORARY_CONTEXT
LATER_COMMENTARY
LATER_RECEPTION
CURRENT_INTERPRETIVE_CONTEXT
```

No later reception record is promoted to original source context without an explicit justified bridge.

## A4 — multi-reading relation and resolved-multi semantics

When multiple readings remain supported, the method records their relation rather than forcing a single winner.

```text
READING_RELATION:
  compatible
  mutually_exclusive
  partially_overlapping
  resolution_dependent
  unspecified
```

`INTERPRETATION_RESOLVED_MULTI` is a valid terminal when the evidence justifies multiple readings and the requested output does not require unsupported disambiguation.

## A5 — witness conflict and precedence policy

If supplied source witnesses conflict, record:

```text
WITNESS_CONFLICT: yes/no
PRECEDENCE_POLICY: supplied / absent / not_applicable
HARMONIZATION_ALLOWED: yes/no
```

No hidden majority rule, preferred-edition rule, or harmonization may be invented.

## A6 — actor/perspective scope

When interpretation depends on referent, role, viewpoint, audience, speaker, legal party, narrator, observer, or other perspective, freeze the relevant scope and propagate it into the reading provenance.

```text
SAME_WORDING + DIFFERENT_PERSPECTIVE
-> possibly different justified reading
```

## A7 — reconstruction handoff and no silent text completion

Missing, damaged, omitted, or unavailable source content remains missing unless a separately identified Reconstruction output is supplied.

Interpretation may consume:

```text
RECONSTRUCTION_HANDOFF_ID
RECONSTRUCTION_STATUS
RECONSTRUCTION_PROVENANCE
ALTERNATIVE_RECONSTRUCTIONS
```

but must preserve:

```text
RECONSTRUCTED_CONTENT != OBSERVED_SOURCE_CONTENT
INTERPRETATION_OF_RECONSTRUCTION != INTERPRETATION_OF_DIRECT_WITNESS
```

## Amendment effect

These seven refinements are binding for Protocol v0.1 and later runs unless prospectively superseded.

They do not add a new DSD foundational layer and do not count as direct Interpretation evidence.