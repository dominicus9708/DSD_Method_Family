# Standard-Theory Comparator Policy / 표준이론 비교 기준

Policy date: 2026-09-07
Status: active research policy

## 1. Purpose

This policy controls which external theories may be used as **premises, comparators, or validation references** in DSD method-family research.

The purpose is to reduce comparison-theory contamination: DSD should not inherit an external theory's disputed primitive identifications merely because that theory already packages several domains together.

## 2. Primary comparator class

The preferred external basis is an independently established standard theory in the domain actually under study.

Examples include:

```text
standard nonrelativistic quantum mechanics,
special relativity,
general relativity,
classical mechanics,
electromagnetism,
thermodynamics,
statistical mechanics,
standard particle theory / quantum field theory when the task genuinely requires it,
continuum mechanics,
standard mathematical structures used by those theories.
```

Use the minimum external theory needed for the declared task.

## 3. Non-primary comparator class

Speculative, competing, or not-yet-standard unification frameworks are not used as premises for establishing DSD structure or for validating DSD gravity-principle claims.

This includes alternative quantum-gravity or gravity-unification programs unless a future task explicitly treats one of them as a **research object** rather than as a source of assumed truth.

Historical DSD records that previously used semiclassical or other interface literature as comparison material are preserved. They are not silently deleted, but they are not treated as the primary foundation of the current QM/relativity/gravity line.

## 4. Research-object quarantine rule

A non-primary theory may later be analyzed only under a quarantine-style record:

```text
TARGET_THEORY:
TARGET_STATUS: research object only
PRIMITIVES_LOCKED_FROM_TARGET_SOURCE:
ASSUMPTIONS_NOT_TRANSFERRED_TO_DSD:
STANDARD_THEORY_BASELINE:
DSD_ANALYSIS_OUTPUT:
NO_VALIDATION_TRANSFER:
```

A result about such a target cannot be used to establish a DSD law unless the relevant claim is independently reproduced from standard theory, experiment, mathematics, or another admissible evidence class.

## 5. Predefinition-contamination firewall

Before comparing DSD with any external theory:

1. lock the external theory's primitive carriers, relations, and laws from that theory itself;
2. lock the DSD carriers, layers, statuses, and bridges independently;
3. do not create a shared vocabulary map yet;
4. only after both sides are fixed, declare explicit comparison maps;
5. reject any inference based solely on a shared word, symbol, index count, or similar role name.

The operating pattern is

```text
source A locked independently
source B locked independently
-> typed comparison interface
-> preserved / differing / unresolved structure
```

not

```text
shared word
-> presumed shared primitive
-> retroactive interpretation of both theories.
```

## 6. Typed-dimension firewall

At minimum, keep distinct:

```text
DSD channel / term count or DSD-specific rank,
Hilbert-space dimension,
spacetime-manifold dimension,
representation-vector dimension,
number of observables or probes,
number of effective degrees of freedom.
```

Equal numerical cardinality is not a physical identification.
A physically meaningful mapping requires an explicit bridge with declared domain, codomain, assumptions, and validation standard.

## 7. Gravity-principle application

For the active DSD gravity-principle line:

- use standard relativity for geometric, causal, proper-time, weak-field, and classical gravitational benchmarks;
- use standard quantum mechanics for state, measurement, probability, distinguishability, tensor-product, and reconstruction questions;
- use other standard theories only when the source or material sector genuinely requires them;
- do not infer a quantum-gravity bridge from the coexistence of quantum and relativistic descriptions;
- any quantum-to-gravity or gravity-to-quantum constitutive map remains an explicit additional bridge until independently derived or validated.

## 8. Method-family impact

This policy refines the existing SC-02 / SC-03 / SC-10 disciplines:

```text
SC-02  source/interface/version lock
SC-03  explicit bridge discipline
SC-10  external-standard/domain-validation separation
```

It does not create a new DSD axiom or new independent DSD method.

## 9. Current operational verdict

```text
PRIMARY_RESEARCH_BASE:
  standard theory only, chosen minimally by domain

NONPRIMARY_UNIFICATION_THEORY_AS_PREMISE:
  disallowed for current gravity/QM/relativity line

NONPRIMARY_THEORY_AS_FUTURE_RESEARCH_OBJECT:
  allowed only with quarantine and no validation transfer

HISTORICAL_RECORDS:
  preserved, not promoted to present foundation
```
