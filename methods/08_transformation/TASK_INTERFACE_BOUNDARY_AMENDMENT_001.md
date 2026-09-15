# DSD Transformation Task Interface Boundary Amendment 001

Status: **ESTABLISHED PROSPECTIVELY**  
Date: **2026-09-16**

This amendment incorporates the eight non-breaking refinements forced by the 18 pre-protocol boundary attacks. The historical `TASK_INTERFACE_v0.1-draft.md` is preserved unchanged.

## A1. Map identity, version, domain, codomain, applicability

Every Transformation task must explicitly freeze:

```text
TRANSFORMATION_MAP_OR_RULE_ID_AND_VERSION
SOURCE_SCHEMA_ID_AND_VERSION
TARGET_SCHEMA_ID_AND_VERSION
DECLARED_DOMAIN
DECLARED_CODOMAIN
APPLICABILITY_CONDITION
OUTSIDE_DOMAIN_POLICY
```

A partial transformation may not be silently totalized.

## A2. Carrier correspondence and preservation taxonomy

The task must record source-to-target carrier relations rather than only endpoint values.

Allowed claim-relevant carrier relations include:

```text
ONE_TO_ONE
MANY_TO_ONE_MERGE
ONE_TO_MANY_SPLIT
OMITTED
TARGET_ADDED
NO_APPLICABLE_COUNTERPART
UNRESOLVED
```

Preservation status must distinguish at least:

```text
PRESERVED_EXACT
PRESERVED_UNDER_DECLARED_EQUIVALENCE
MERGED_IN_TARGET
SPLIT_IN_TARGET
OMITTED_BY_TRANSFORMATION
TARGET_ADDED_NOT_SOURCE_DERIVED
UNRESOLVED_PRESERVATION
INAPPLICABLE_AT_TARGET
OUT_OF_SCOPE_FOR_TRANSFORMATION
```

## A3. Target additions, defaults, and enrichment

Any target value not derivable from the declared source through the frozen transformation rule must carry explicit provenance:

```text
DEFAULT_VALUE
EXTERNAL_ENRICHMENT
DESIGN_OR_SYNTHESIS_HANDOFF
MANUAL_SUPPLY
OTHER_EXPLICIT_ADDITION
```

```text
TARGET_VALUE_EXISTENCE != SOURCE_DERIVABILITY
TARGET_DEFAULT != SOURCE_DERIVED_VALUE
```

## A4. Information loss, collision, injectivity, reconstruction

When transformation merges or omits claim-relevant source states, the run must record:

```text
COLLISION_OR_MERGE_SCOPE
INJECTIVITY_STATUS
INFORMATION_LOSS_DESCRIPTION
RECONSTRUCTION_AVAILABILITY
RECONSTRUCTION_SCOPE
```

Equal target outputs cannot prove equal source states without a justified injectivity/reconstruction claim.

## A5. Reversibility scope

Reversibility claims are scope-bound.

```text
REVERSIBLE_ON_DECLARED_DOMAIN
LEFT_INVERTIBLE_ON_DECLARED_DOMAIN
RIGHT_INVERTIBLE_ON_DECLARED_CODOMAIN
NONINVERTIBLE_DUE_TO_COLLISION_OR_LOSS
INVERSE_UNAVAILABLE
REVERSIBILITY_UNDETERMINED
NOT_ASSESSED
```

A finite sample round-trip cannot establish global invertibility.

## A6. Transformation-chain provenance

For a composed chain:

```text
T = T_n o ... o T_2 o T_1
```

record each stage identity/version, stage input/output schema, intermediate loss, additions, and applicable inverse claim.

```text
CHAIN_ENDPOINT_MATCH != LOSSLESS_INTERMEDIATE_CHAIN
```

Later reintroduction of information from defaults or auxiliary sources does not retroactively erase an earlier loss.

## A7. Stochastic or nondeterministic transformation policy

If output is nondeterministic, freeze enough semantics to make the run auditable:

```text
RANDOM_OR_CHOICE_POLICY_ID_AND_VERSION
DISTRIBUTION_OR_SELECTION_RULE
SEED_OR_REPLAY_RECORD if applicable
ALLOWED_OUTPUT_SET_OR_SUPPORT
DETERMINISM_CLAIM
```

One realized target is not equivalent to the transformation's full output semantics.

## A8. Temporal and schema-version migration scope

If transformation semantics vary by time, regime, or schema version, freeze the relevant scope explicitly.

```text
SAME_SOURCE_TOKEN != SAME_TARGET_MEANING_ACROSS_VERSIONS
MAP_VALID_FOR_v1 != MAP_VALID_FOR_v2
```

A version transition must not be hidden inside a nominally unchanged transformation ID.

## Amendment effect

These refinements do not change Transformation's core task identity. They make its claim boundaries explicit.

```text
SOURCE + EXPLICIT TRANSFORMATION RULE
-> TARGET REPRESENTATION
+ PRESERVATION / LOSS / ADDITION / REVERSIBILITY TRACE
```

The next binding artifact is `PROTOCOL_v0.1.md`.
