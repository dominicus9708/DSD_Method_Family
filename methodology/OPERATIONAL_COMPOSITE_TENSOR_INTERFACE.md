# Operational Composite and Tensor-Carrier Interface

Status: reusable DSD Method Family interface / comparator-aware  
Origin: QM Core Reconstruction 004H  
Scope: finite-dimensional operational specializations using local systems, composites, product preparations/effects, or local tomography

## 1. Purpose

This interface prevents four distinct claims from being silently identified:

```text
explicit declaration of a composite carrier,
independent local product availability,
local-product readout injectivity,
exact tensor-product carrier equality.
```

Generic DSD does not identify these claims.

## 2. Composite Rule Declaration — CRD

Whenever a DSD specialization uses a composite system, record at least:

```text
GLOBAL_CARRIER
LOCAL_EMBEDDINGS
LOCAL_READOUT_FAMILY
GLOBAL_READOUT_FAMILY
REDUCTION_MAPS
COMPOSITE_DYNAMICS
```

CRD is a declaration discipline. It does not impose a tensor-product composition law.

## 3. Independent Local Product Composition — ILPC

When independent subsystem operations are claimed, additionally declare:

```text
LOCAL_OPERATIONAL_CARRIERS
PRODUCT_PREPARATION_OPERATION
PRODUCT_EFFECT_OPERATION
LOCAL_RANDOMIZER_COMPATIBILITY
PRODUCT_PROBABILITY_FACTORIZATION
PRODUCT_UNIT_EFFECT / NORMALIZATION
LOCAL_TRANSFORMATION_PRODUCTS   if used
```

For normalized operational states, compatibility with independent classical randomization requires the product-preparation operation to be affine in each argument.

After ordered-carrier linearization this yields a bilinear map

\[
\beta:V_A\times V_B\to V_{AB}
\]

and therefore a unique linear map

\[
\widetilde\beta:V_A\otimes V_B\to V_{AB}.
\]

If local effect families span the local duals and product probabilities factorize, product effects separate tensor directions, so

\[
\ker\widetilde\beta=\{0\}.
\]

Hence

\[
\dim V_{AB}\ge \dim V_A\dim V_B.
\]

## 4. Local Descriptive Completeness — LDC

Let all declared local-product effects define the linear readout

\[
R_{AB}^{\rm loc}:V_{AB}\to Y_{AB}^{\rm loc}.
\]

LDC requires this map to be injective on the declared global carrier.

When the local effect families span `V_A^*` and `V_B^*`, the independent local-product readout span has dimension at most

\[
\dim V_A\dim V_B.
\]

Therefore LDC gives

\[
\dim V_{AB}\le \dim V_A\dim V_B.
\]

## 5. Conditional exact tensor theorem

Under the finite-dimensional ordered-carrier specialization, if both ILPC and LDC hold with spanning local effect families, then

\[
\dim V_A\dim V_B
\le
\dim V_{AB}
\le
\dim V_A\dim V_B.
\]

Thus

\[
\dim V_{AB}=\dim V_A\dim V_B
\]

and the injective product map is an isomorphism:

\[
\boxed{V_{AB}\cong V_A\otimes V_B.}
\]

If the product unit effect is declared, normalization transports to

\[
u_{AB}=u_A\otimes u_B
\]

under this identification. If local transformation products are also declared, their transported linear action has the tensor-product form.

## 6. Non-implications

```text
CRD != ILPC
CRD != LDC
LDC alone != full product availability
ILPC alone != local tomography
Formation Clause-VII finite channel summation != physical subsystem tensor product
multi-input Property data != tensor factorization
aggregate equality != composite-state reconstruction
```

A restricted global carrier may be completely separated by local-product readouts while omitting an otherwise independent product state.

Conversely, a global carrier may contain the full local product subspace plus additional relational directions invisible to all local-product readouts.

## 7. Provenance rule for QM Core 004H

For the current quantum-reconstruction challenge:

```text
CRD                 pre-existing DSD-wide declaration discipline
ORD/ORE linearity   Class B general operational result
LDC-QM              Class C target-specialization selector
ILPC-QM             provisional Class D comparator precursor
exact tensor carrier CONDITIONAL_DERIVATION from ILPC-QM + LDC-QM
```

ILPC-QM is not reclassified as Class B merely because the interface is operationally general. It was isolated during an exact quantum-comparator stage and requires independent non-QM validation before any provenance upgrade.

## 8. Audit rule

Before asserting tensor-product composition, record separately:

```text
PRODUCT_AVAILABILITY_ESTABLISHED:
PRODUCT_PROBABILITY_FACTORIZATION:
PRODUCT_MIXTURE_BILINEARITY:
LOCAL_PRODUCT_READOUT_INJECTIVE:
GLOBAL_RELATIONAL_KERNEL:
DIMENSION_LOWER_BOUND:
DIMENSION_UPPER_BOUND:
TENSOR_ISOMORPHISM_PROVED:
NORMALIZATION_PRODUCT_RULE:
LOCAL_TRANSFORMATION_PRODUCT_RULE:
PROVENANCE_CLASS:
```

Tensor notation by itself is not evidence that the physical composite satisfies this interface.
