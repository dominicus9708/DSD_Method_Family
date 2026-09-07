# SPEC-MEAS-002 — OSHA Direct Baseline vs DSD Native Handoff Result

Date: 2026-09-08
Precommit commit: `7de2ffba9e26bb1870519a95cf171c9614a65063`
Direct-route freeze: `e410b7142c3713cc886823eed7e7e16a3a0b568d`
DSD-side prior handoff evidence: `SPEC-LINK-001_specification-to-audit-handoff.md`
DSD-side source record: `SPEC-APP-003_OSHA_EAP_core_guidance.md`
Status: COMPLETED_WITH_INDETERMINATE_PRIMARY_VERDICT

## 1. Result in one line

Both the direct official OSHA -> DSD Audit route and the OSHA -> DSD Specification -> DSD Audit route produced the same six locked audit findings with zero optional-guidance false positives, zero site-specific-openness false failures, and zero fabricated site facts. The DSD route removed source-to-audit re-extraction at the receiving boundary but required a prior 24-atom Specification artifact. Because the precommitted verdict rules did not define precedence between `TIE_WITH_DSD_TRACEABILITY_ADVANTAGE` and `TIE_WITH_DSD_OVERHEAD`, both predicates are satisfied and the only anti-post-hoc-valid primary verdict is `INDETERMINATE`.

## 2. Primary axes

```text
ROUTE_O_AUDIT_FINDING_MATCHES: 6/6
ROUTE_D_AUDIT_FINDING_MATCHES: 6/6

ROUTE_O_FALSE_POSITIVE_ON_OPTIONAL_GUIDANCE: 0
ROUTE_D_FALSE_POSITIVE_ON_OPTIONAL_GUIDANCE: 0

ROUTE_O_FALSE_FAILURE_FROM_SITE_SPECIFIC_OPENNESS: 0
ROUTE_D_FALSE_FAILURE_FROM_SITE_SPECIFIC_OPENNESS: 0

ROUTE_O_NORMATIVE_FORCE_PRESERVATION: pass
ROUTE_D_NORMATIVE_FORCE_PRESERVATION: pass

ROUTE_O_SOURCE_OR_NORM_REFERENCE_PRESERVATION: pass
ROUTE_D_SOURCE_OR_NORM_REFERENCE_PRESERVATION: pass

ROUTE_O_FABRICATED_SITE_SPECIFIC_FACTS: 0
ROUTE_D_FABRICATED_SITE_SPECIFIC_FACTS: 0
```

No accuracy/error advantage was demonstrated for either route on the six probes.

## 3. Burden proxies

### ROUTE_O — direct OSHA -> DSD Audit

```text
INTERMEDIATE_SPECIFICATION_ARTIFACT_REQUIRED: no
SOURCE_TO_AUDIT_REEXTRACTION_REQUIRED: yes
HIDDEN_RETRANSLATION_REQUIRED: no
ADDITIONAL_DSD_LAYER_OR_BRIDGE_REQUIRED: no
PROBE_FINDINGS: 6
```

The receiving Audit performs its own source-to-criterion extraction from the official OSHA corpus.

### ROUTE_D — OSHA -> DSD Specification -> DSD Audit

From `SPEC-APP-003` and `SPEC-LINK-001`:

```text
INTERMEDIATE_SPECIFICATION_ARTIFACT_REQUIRED: yes
DERIVATIVE_REQUIREMENT_ATOMS: 24
SOURCE_TO_AUDIT_REEXTRACTION_REQUIRED: no
HIDDEN_RETRANSLATION_REQUIRED: no
ADDITIONAL_DSD_BRIDGE_REQUIRED_FOR_SPEC_TO_AUDIT: no
PROBE_FINDINGS: 6
```

The receiving Audit can consume the existing typed criterion carrier directly.

## 4. Structural handoff observation

A genuine structural difference exists:

```text
ROUTE_O:
  external source remains available
  receiving audit must extract criterion semantics at audit time

ROUTE_D:
  criterion semantics already carried in DSD-native fields
  receiving audit does not rebuild the requirement model
```

This supports the narrow structural statement:

```text
DSD_NATIVE_CRITERION_CARRIER_REDUCES_RECEIVING_BOUNDARY_REEXTRACTION: yes_on_this_case
```

But the DSD carrier was not free. It required a prior 24-atom Specification artifact, and this benchmark did not measure human time, review effort, or repeated reuse.

Therefore the following stronger statements remain unsupported:

```text
DSD_NATIVE_HANDOFF_SAVES_TIME: not established
DSD_NATIVE_HANDOFF_REDUCES_HUMAN_ERROR: not established
DSD_NATIVE_HANDOFF_REDUCES_TOTAL_SINGLE_USE_WORK: not established
DSD_NATIVE_HANDOFF_HAS_POSITIVE_PRACTICAL_BENEFIT: not established
```

## 5. Direct-baseline source-force check

The direct OSHA route remained a strong baseline rather than a checklist-only strawman.

For P5, OSHA's EAP guidance says an employer might consider auxiliary power, while the employee-alarm checklist separately asks an auxiliary-power question. The governing regulatory text does not make absence of a separately named auxiliary-power supply an automatic violation merely from that checklist phrasing; it requires operational alarm conditions and backup means when systems are out of service.

The direct route therefore cross-checked the checklist against the regulation and reached the same non-failure result as the DSD route.

This matters because the DSD route receives no artificial advantage from a deliberately weak baseline.

## 6. Precommitted verdict-rule collision

The precommit defined:

```text
TIE_WITH_DSD_TRACEABILITY_ADVANTAGE
  equal findings + clear structural carrier advantage,
  without claiming time/error benefit

TIE_WITH_DSD_OVERHEAD
  equal findings + added upstream DSD representation,
  without demonstrated downstream outcome advantage
```

Observed result:

```text
EQUAL_FINDINGS: yes
CLEAR_STRUCTURAL_CARRIER_ADVANTAGE: yes
ADDED_UPSTREAM_DSD_REPRESENTATION: yes
DEMONSTRATED_DOWNSTREAM_OUTCOME_ADVANTAGE: no
```

Therefore both verdict predicates are true.

The precommit did not define a precedence relation or mutual-exclusion rule between them.

Choosing either one after observing the result would require a post-result verdict-rule addition, which was explicitly prohibited.

Hence:

```text
PRIMARY_COMPARATIVE_VERDICT: INDETERMINATE
INDETERMINACY_CAUSE: PRECOMMITTED_VERDICT_CATEGORY_OVERLAP
POST_RESULT_VERDICT_RULE_CHANGE: no
```

This is a benchmark-design limitation, not a DSD Specification hard failure.

## 7. Guardrail interpretation

```text
SOURCE_FIDELITY: preserved on both routes
EXTERNAL_STANDARD_BOUNDARY: preserved on both routes
SITE_SPECIFIC_OPENNESS: preserved on both routes
DETAIL_PROPORTIONALITY:
  direct route = lower upstream representation
  DSD route = higher upstream representation but explicit reusable carrier
```

No scalar guardrail winner is assigned because the benchmark did not precommit how to trade upfront representation against receiving-boundary re-extraction.

## 8. Evidence interpretation

```text
CASE_LEVEL_HANDOFF_STRUCTURE_DIFFERENCE: established
CASE_LEVEL_ACCURACY_DIFFERENCE: none demonstrated
CASE_LEVEL_ERROR_DIFFERENCE: none demonstrated
CASE_LEVEL_TIME_SAVING: not measured
CASE_LEVEL_TOTAL_WORK_REDUCTION: not established
MEASURED_POSITIVE_PRACTICAL_BENEFIT: not established
PRIMARY_COMPARATIVE_VERDICT: INDETERMINATE
```

The result adds evidence for **structural integration utility** but not for practical superiority.

## 9. Required correction for future practical benchmarks

Future paired handoff benchmarks must make verdict classes mutually exclusive before execution.

At minimum, precommit an explicit priority such as:

```text
1. accuracy / hard-error difference
2. actually measured workload or time difference
3. structural handoff difference
4. representation overhead
```

or define a multidimensional result without forcing a single scalar winner.

This correction applies prospectively only. `SPEC-MEAS-002` remains `INDETERMINATE` and is not rescored.

## 10. Final record

```text
BENCHMARK_ID: SPEC-MEAS-002
CASE: OSHA EAP
ROUTE_O: OSHA official corpus -> DSD Audit
ROUTE_D: OSHA official corpus -> DSD Specification -> DSD Audit

ROUTE_O_FINDINGS: 6/6
ROUTE_D_FINDINGS: 6/6

ROUTE_O_SOURCE_REEXTRACTION_AT_AUDIT: yes
ROUTE_D_SOURCE_REEXTRACTION_AT_AUDIT: no
ROUTE_D_UPSTREAM_SPECIFICATION_ATOMS: 24

PRIMARY_COMPARATIVE_VERDICT: INDETERMINATE
INDETERMINACY_CAUSE: PRECOMMITTED_VERDICT_CATEGORY_OVERLAP
MEASURED_POSITIVE_PRACTICAL_BENEFIT: not established
PROTOCOL_V1_0_REVISION_REQUIRED: no
METHOD_EVIDENCE_STATUS_CHANGE: no
```
