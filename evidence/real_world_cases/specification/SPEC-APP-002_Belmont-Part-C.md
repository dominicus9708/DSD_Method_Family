# SPEC-APP-002 — Belmont Report Part C External Application

Date: 2026-09-07
Method directly tested: **DSD Specification / DSD 명세론**
Protocol: **Specification Protocol v0.2**
Precommit: [`SPEC-APP-002_Belmont-Part-C_precommit.md`](SPEC-APP-002_Belmont-Part-C_precommit.md)
Precommit commit: `2ad9b5820a959195b32e1d9560be6328a4905771`
Case origin: `public_normative_ethics_guideline`
External domain: human-subject research ethics

## 1. Source lock

Primary source:
- **The Belmont Report — Ethical Principles and Guidelines for the Protection of Human Subjects of Research**
- National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research
- report date: 1979-04-18
- authoritative host used for this run: HHS OHRP
- locked application corpus: **Part C. Applications**

Locked purpose/context evidence comes from the Report's summary and introductory ethical-principles section.

The source explicitly frames itself as an ethical principles/guidelines statement and analytical framework. It does not present itself as a mechanically complete administrative rulebook, and it acknowledges that difficult ethical problems are not always resolvable beyond dispute by the three principles alone.

### Baseline-B source-status correction

The precommit named HHS OHRP's Assurance Training summary as a secondary concise baseline. During source-status verification before scoring, the HHS page itself was found to mark that tutorial as **outdated and archived**, reflecting the pre-2018 Common Rule.

Therefore:

```text
BASELINE_A: Belmont Part C original prose — active primary baseline for this locked ethical-framework task
BASELINE_B: archived historical OHRP summary — retained only as a historical concise comparator
CURRENT_REGULATORY_COMPLIANCE_BASELINE: not claimed in this run
POST_HOC_REPLACEMENT_BASELINE_ADDED: no
```

This correction does not change the precommitted gain/guardrail criteria and does not import a new baseline after reveal.

## 2. Purpose / viewpoint lock result

```text
SOURCE_PRIMARY_PURPOSE_PRESERVED: yes
SOURCE_ANALYTICAL_FRAMEWORK_FUNCTION_PRESERVED: yes
SOURCE_TARGET_ACTORS_PRESERVED: yes
GLOBAL_PRIORITY_AMONG_THREE_PRINCIPLES_INVENTED: no
DSD_VIEW_DECLARED_DERIVATIVE: yes
DSD_ONTOLOGY_ATTRIBUTED_TO_BELMONT_AUTHORS: no
CURRENT_REGULATORY_FORCE_ATTRIBUTED_TO_BELMONT: no
```

The DSD output is treated as a **derivative structural map**, not as a replacement for the Report's ethical reasoning or as a claim about the authors' own ontology.

## 3. Locked source-unit coverage

All 22 precommitted units remained represented.

```text
SOURCE_UNIT_COVERAGE: 22/22
SILENTLY_DROPPED_SOURCE_UNITS: 0
```

Trace map:

| Unit | Preserved DSD record family |
|---|---|
| U01 | three application branches |
| U02 | autonomy / opportunity-to-choose requirement |
| U03 | information / comprehension / voluntariness structure |
| U04 | disclosure scope and sufficiency judgment |
| U05 | incomplete-disclosure constraints |
| U06 | comprehension presentation/context |
| U07 | adaptation and comprehension verification |
| U08 | diminished-capacity subject + protective third-party roles |
| U09 | voluntariness / coercion / undue-influence boundary |
| U10 | investigator / review committee / prospective-subject risk-benefit functions |
| U11 | risk / benefit conceptual distinctions |
| U12 | multiple harm/benefit domains and affected parties |
| U13 | subject-centered weighting with rights protection |
| U14 | systematic nonarbitrary assessment |
| U15 | presupposition / probability / magnitude / alternatives checks |
| U16 | nonnegotiable and heightened-risk considerations |
| U17 | justice -> fair selection requirement |
| U18 | individual vs social justice |
| U19 | class order and vulnerable-population conditionality |
| U20 | distributive injustice beyond local individual fairness |
| U21 | already-burdened populations + condition-related exception |
| U22 | anti-convenience / anti-manipulability protection |

## 4. DSD requirement map

The 22 source units were represented by 33 checkable derivative atoms. The atom count is not itself treated as a gain.

### Informed consent

```text
A01 Part C has three application branches
A02 capable subjects receive a meaningful opportunity to choose participation
A03 consent analysis preserves information / comprehension / voluntariness as distinct elements
A04 disclosure record includes research purpose/procedure, relevant risks/benefits, alternatives when applicable, questions, and withdrawal opportunity
A05 information sufficiency is not reduced to a mere fixed-item checklist; volunteer-context judgment remains
A06 incomplete disclosure requires necessity for the research purpose
A07 incomplete disclosure must not conceal more-than-minimal undisclosed subject risk
A08 incomplete disclosure requires an adequate debrief/dissemination plan when appropriate
A09 risk information is not withheld merely to secure cooperation; direct questions receive truthful answers
A10 comprehension depends on manner/context as well as content
A11 presentation is adapted to subject capacity and comprehension is ascertained
A12 diminished-capacity subjects retain choice to the extent possible and protective third-party permission may be required
A13 protective representatives should understand the subject's situation, act in the subject's interest, and retain protective withdrawal capacity where applicable
A14 valid participation is voluntary and requires freedom from coercion and undue influence
```

### Risk / benefit assessment

```text
A15 assessment gathers relevant data and considers alternative ways of obtaining the sought benefit when applicable
A16 investigator / review committee / prospective subject roles are kept distinct
A17 probability of harm, magnitude of harm, benefit, and probability of benefit are not silently collapsed
A18 psychological / physical / legal / social / economic harms and benefits, and multiple affected parties, remain in scope
A19 immediate subject risks and benefits normally receive special weight; non-subject interests do not erase subject-right protections
A20 assessment aims at systematic and nonarbitrary reasoning rather than false numerical precision
A21 research presuppositions, nature/probability/magnitude of risk, and risk-ascertainment method are made explicit as far as possible
A22 probability estimates are checked against known facts or available studies
A23 brutal or inhumane treatment is not treated as balanceable by benefit
A24 risks are reduced to what is necessary for the research objective; necessity of human-subject use and alternatives are considered
A25 significant risk of serious impairment activates heightened justification pressure
A26 involvement of vulnerable populations requires its own appropriateness justification
A27 relevant risks and benefits are represented in consent documents/processes
```

### Selection of subjects / justice

```text
A28 justice requires fair procedures and outcomes in subject selection
A29 individual fairness and social/distributive justice remain distinct
A30 class-level ordering or conditional eligibility is represented only where source-supported; no universal ranking is invented
A31 local individual fairness does not by itself establish distributive justice across institutions or society
A32 for risky nontherapeutic research, less-burdened classes are preferred before already-burdened classes unless the research is directly related to the latter's condition
A33 vulnerable groups are protected against selection merely for administrative convenience, availability, dependence, or manipulability
```

## 5. Local priority and open-judgment preservation

The source does contain local priority/weighting relations, but it does not declare one total order among Respect for Persons, Beneficence, and Justice.

Five source-supported local priority relations were explicitly preserved:

```text
P1 more serious risk -> stronger comprehension-assurance obligation
P2 immediate subject risks/benefits normally receive special weight
P3 serious-impairment risk -> heightened review insistence
P4 class ordering may prefer less vulnerable / more able-to-bear-burden classes under stated conditions
P5 already-burdened groups are not first-line risk bearers in nontherapeutic research unless condition relevance supplies the exception
```

```text
LOCAL_PRIORITY_RELATIONS_IDENTIFIED: 5
LOCAL_PRIORITY_RELATIONS_PRESERVED: 5/5
GLOBAL_PRIORITY_RELATIONS_INVENTED: 0
```

The following source-open judgment boundaries were deliberately **not** collapsed into deterministic rules:

```text
J1 exact boundary between justified persuasion and undue influence
J2 exact quantitative balancing of heterogeneous risks and benefits
J3 hard cases where ethical principles or claims conflict
J4 context-sensitive adequacy of information/comprehension protections
```

```text
UNRESOLVED_JUDGMENT_BOUNDARIES_IDENTIFIED: 4
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
FALSE_DETERMINISTIC_RESOLUTION: 0
```

### Protocol pressure discovered

Protocol v0.2 can preserve these boundaries using `UNRESOLVED_CONDITION` and limits, but it does not yet distinguish cleanly between:

```text
accidental underspecification
!= source-intentional open-textured ethical judgment
```

This is recorded as a **nonfatal protocol pressure**, not repaired during the same run.

```text
PROTOCOL_PRESSURE_STATUS: present_nonfatal
PRESSURE_POINT: intentional_normative_openness_vs_underspecification
RETROACTIVE_FIELD_ADDITION: no
```

## 6. Hard-failure audit

```text
SOURCE_FACT_INVENTION: 0
SILENT_REQUIRED_SOURCE_OMISSION: 0
NORMATIVE_FORCE_STRENGTHENING: 0
FALSE_GLOBAL_PRIORITY_INVENTION: 0
UNRESOLVED_ETHICAL_JUDGMENT_CONVERTED_TO_DETERMINISTIC_RULE: 0
REQUIRED_ACTOR_OR_SCOPE_COLLAPSE: 0
EXTERNAL_STANDARD_SUBSTITUTION: 0
DSD_DERIVATIVE_STRUCTURE_ATTRIBUTED_TO_SOURCE_AUTHOR: 0

HARD_FAILURE_COUNT: 0
```

## 7. Guardrail audit

### G1 — Source fidelity

Result: **inside**.

All 22 locked source units remained traceable. No current regulatory rule was imported into Belmont's historical text.

### G2 — Purpose and priority fidelity

Result: **inside**.

The output remains an ethical-framework derivative. No claim was made that the Report supplies a fully deterministic administrative algorithm or a total ordering among the three principles.

### G3 — Detail proportionality

Result: **pressure**.

The derivative expanded 22 source units into 33 atoms plus actor/condition/priority metadata. This increases reviewability but also increases representation burden.

The DSD map is therefore suitable as an appendix/checking layer, not as a replacement for the Belmont prose when ethical explanation and contextual reasoning are the primary task.

### G4 — Viewpoint separation

Result: **inside**.

The DSD structural view is explicitly labeled derivative; no DSD-added status/ontology is attributed to the Commission.

```text
SEMANTIC_CONTENT_PRESERVED: yes_on_locked_unit_inventory
SOURCE_PRIORITY_SEMANTICS_PRESERVED: yes
SOURCE_PRIORITY_PRESENTATION_PRESERVED: yes_in_derivative_map
SOURCE_PURPOSE_PRESERVED: yes
TARGET_USER_FUNCTION_PRESERVED: yes_if_used_as_derivative_checking_layer
DETAIL_INFLATION: present
REPRESENTATION_BURDEN: moderate
VIEWPOINT_CHANGE_DECLARED: yes
DSD_ADDED_STRUCTURE_DECLARED: yes
AUTHORIAL_INTENT_INFERRED_WITHOUT_BASIS: no
PURPOSE_DISTORTION: no
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
GUARDRAIL_REPAIR_IF_ANY: keep original Belmont prose as primary ethical-reading layer; use DSD map as derivative trace/check layer
```

## 8. Gain audit against baselines

### Against Baseline A — Belmont Part C original prose

The original prose is superior for conveying ethical rationale, tensions, examples, and the intended analytical framework.

The DSD derivative adds:

```text
DISTINCTION_GAIN: demonstrated for actor/condition/judgment-boundary separation
TRACEABILITY_GAIN: demonstrated through Uxx -> Axx mapping
AMBIGUITY_REDUCTION_GAIN: limited; structural location of ambiguity is clarified, substantive ethical ambiguity is intentionally preserved
DOWNSTREAM_CHECKABILITY_GAIN: demonstrated for checking whether a review record addressed the locked Part-C considerations
```

The DSD output does **not** demonstrate better ethical judgment than the Report.

### Against Baseline B — archived historical OHRP summary

The archived OHRP summary is more concise and already exposes the major Belmont principle-to-requirement relationships. Therefore no gain is counted merely for reproducing those high-level categories.

The DSD derivative still adds source-unit traceability and preserves several open judgment boundaries omitted by the concise summary, but this comparison is historical only because the baseline is explicitly archived/outdated for current compliance use.

## 9. Final scoring

```text
SOURCE_UNIT_COVERAGE: 22/22
SOURCE_PURPOSE_PRESERVATION: pass
ACTOR_SCOPE_PRESERVATION: pass_on_locked_units
LOCAL_PRIORITY_PRESERVATION: 5/5
GLOBAL_PRIORITY_INVENTION_COUNT: 0
UNRESOLVED_JUDGMENT_BOUNDARIES_PRESERVED: 4/4
INVENTED_SOURCE_FACTS: 0
SILENTLY_DROPPED_SOURCE_OBLIGATIONS: 0
NORMATIVE_FORCE_STRENGTHENINGS: 0
DSD_VIEWPOINT_OVERATTRIBUTIONS: 0

DISTINCTION_GAIN: demonstrated_relative_to_primary_prose_for_structural_checking
TRACEABILITY_GAIN: demonstrated
AMBIGUITY_REDUCTION_GAIN: limited_to_structural_localization
DOWNSTREAM_CHECKABILITY_GAIN: demonstrated_for_coverage/review-trace_task

DETAIL_INFLATION: present
REPRESENTATION_BURDEN: moderate
GUARDRAIL_VERDICT: GUARDRAIL_PRESSURE
FINAL_SPEC_STATUS: usable
COMPETITIVE_RESULT: MIXED_GAIN_WITH_GUARDRAIL_PRESSURE
```

## 10. Interpretation of the result

This run differs materially from `SPEC-APP-001`.

The RFC case already had a compact ordered normative procedure and therefore produced `SPEC_NO_GAIN`.

Belmont Part C is less mechanically structured and intentionally preserves ethical judgment space. Here DSD v0.2 produces a real **traceability/checkability gain** without being allowed to convert the source into a false deterministic algorithm.

The gain is task-specific:

```text
PRIMARY_ETHICAL_READING_AND_REASONING:
  Belmont original prose preferred

STRUCTURAL_COVERAGE / TRACE / REVIEW-CHECKING:
  DSD derivative provides additional operational value
```

Therefore the correct result is neither universal DSD superiority nor `NO_GAIN`.

## 11. Result

```text
RESULT:
SPECIFICATION_EXTERNAL_GUARDRAIL_APPLICATION_PASS_WITH_MIXED_GAIN

FINAL_SPEC_STATUS:
usable

GUARDRAIL_VERDICT:
GUARDRAIL_PRESSURE

COMPETITIVE_RESULT:
MIXED_GAIN_WITH_GUARDRAIL_PRESSURE

METHOD_STATUS_AFTER_CASE:
developing
```

## 12. Limits

- one historical ethics document and one locked Part-C corpus;
- structural scoring performed inside the same project/model environment;
- no independent IRB reviewer or research-ethics expert retrace;
- no claim that DSD determines whether a proposed study is ethically permissible;
- no claim that Belmont alone substitutes for current HHS regulation, IRB policy, law, or professional standards;
- no measured improvement in review time, inter-rater agreement, or real-world error detection;
- Baseline B was found to be archived/outdated and is retained only as a historical concise comparator;
- v0.2 now has one external application, but broad v0.2 maturity is not established.

## 13. Next step

Do not immediately promote the method.

Next evidence should test one of:
1. a third external corpus in a different document genre, ideally with operational prose and explicit audience function;
2. an independent blinded retrace of `SPEC-APP-002` by a different evaluator;
3. a prospective challenge separating **intentional normative openness** from accidental specification underspecification without weakening `SPEC_UNDERSPECIFIED` detection.
