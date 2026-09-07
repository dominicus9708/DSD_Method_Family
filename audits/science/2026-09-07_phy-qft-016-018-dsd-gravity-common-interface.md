# PHY-QFT-016~018 — Minimum QFT / DSD Gravity Common-Interface Construction and Factorization Audit

Date: 2026-09-07

## Method-family record

```text
METHOD_ID_OR_LEGACY_PATH: 01 Analysis + 02 Audit + 06 Comparison + 10B Compression + 15B Reconstruction
METHOD_NAME: DSD method-family joint application
HIGHER_FIELD: I / II / V / VI
STATUS: active research audit
TASK: construct the smallest explicit common source/response interface between local QFT data and the DSD gravity-principle research line
INPUTS: local QFT state/algebra data, renormalized source data, explicit source reduction, DSD gravity source carrier, response maps
DSD_LAYERS_USED: Formation background + General Property when typed source records are used + optional Static Aggregation + Dynamics for propagation only
DOMAIN_BRIDGE: always explicit; no name-based identification
EXTERNAL_STANDARD: QFT in curved spacetime / renormalized stress-energy / semiclassical response
INFORMATION_LOSS_CHECK: source-map fibers and linear kernel inclusion
LINEAGE_OR_TRANSITION_CHECK: deferred until time-dependent source/response coupling is activated
REPRODUCIBILITY_RECORD: 2026-09-07_qft_dsd_gravity_common_interface.py
```

## 1. Scope and source lock

The previous synthesis ended with the safe chain

```text
local QFT state/algebra
    -> renormalized source data
    -> explicit DSD-gravity source bridge
    -> independent DSD gravity response
```

and rejected direct identifications such as

```text
<T_mu nu>_ren = DSD static aggregate
<T_mu nu>_ren = current scalar DSD gravity source
8*pi*G = a quantity already derived by the present DSD core
```

This stage does not reverse those verdicts.  It constructs the first explicit common interface on which such claims can be tested.

The external QFT source record must be version-locked by at least

```text
(spacetime/background,
 local algebra or field model,
 admissible state class,
 renormalization prescription,
 selected local/smeared stress-energy probes).
```

Changing any of these may change the source carrier or source map and is therefore not silently treated as the same interface.

## 2. Minimum finite renormalized-source carrier

Let `Q` denote an admissible family of external QFT records.  Instead of pretending that a pointwise renormalized stress tensor is automatically a finite DSD vector, choose a finite family of admissible test tensors or source probes

\[
\mathcal F=(f_1,\ldots,f_m).
\]

Where the renormalized stress-energy expectation is defined, form the finite external source descriptor

\[
S_{\mathcal F}:Q\to V_T,
\qquad
S_{\mathcal F}(q)
=
\bigl(
\langle T^{\rm ren},f_1\rangle_q,
\ldots,
\langle T^{\rm ren},f_m\rangle_q
\bigr).
\]

This is an **external QFT representation choice**.  It is not a DSD Formation assignment and does not create a Stage-VI operational channel.

The finite probe family can be enlarged, reduced, or changed.  Such a change changes the readout map and therefore changes its fibers.

## 3. Explicit DSD gravity source bridge

Supply a typed application bridge

\[
B_G:V_T\to V_G,
\]

where `V_G` is the selected DSD gravity-source carrier for the physical specialization being tested.

Examples of possible **carrier roles**, not automatic identifications, include

```text
coarse mass/source sector,
flux-like sector,
pressure/stress correction sector,
anisotropy/relational correction sector,
progression-driving source record.
```

The bridge may be injective, lossy, nonlinear, state-dependent, or undefined outside a selected admissible subset.  These possibilities must be recorded rather than inferred from names.

For a fixed DSD structural context `sigma`, let

\[
R_G^{\sigma}:V_G\to X_G
\]

be the supplied DSD gravity response map.  The current DSD gravity-principle program does not obtain `R_G^sigma` from the QFT labels themselves.

## 4. External comparator and common comparison carrier

Let

\[
H_{\rm ext}:V_T\to X_{\rm ext}
\]

be an external standard-theory response defined on the same selected source class.  In a semiclassical specialization this may be a chosen geometric/background response functional, but its exact mathematical form remains part of the external model.

Because `X_G` and `X_ext` need not be the same carrier, introduce explicit comparison maps

\[
J_G:X_G\to Z,
\qquad
J_{\rm ext}:X_{\rm ext}\to Z.
\]

The minimum interface commutes on an admissible source class `A subset V_T` when

\[
\boxed{
J_G\circ R_G^{\sigma}\circ B_G
=
J_{\rm ext}\circ H_{\rm ext}
\quad\text{on }A.
}
\]

This equation is the first point at which a quantitative DSD-gravity / external-QFT-gravity comparison is well typed.  Equality before the comparison maps are supplied is not assumed.

## 5. PHY-QFT-016 — Common-interface factorization theorem

Let

\[
B:A\to G,
\qquad
H:A\to Z.
\]

There exists a map

\[
F:B[A]\to Z
\]

such that

\[
H=F\circ B
\quad\text{on }A
\]

if and only if `H` is constant on every fiber of `B` restricted to `A`:

\[
\boxed{
B(x)=B(y)\Longrightarrow H(x)=H(y)
\qquad(x,y\in A).
}
\]

### Proof

If `H=F o B`, equal `B` values obviously give equal `H` values.

Conversely, if `H` is constant on each `B`-fiber, define

\[
F(g):=H(x)
\]

for any `x in A` satisfying `B(x)=g`.  Fiber constancy makes this definition independent of the chosen representative, hence well defined on `B[A]`.

### Linear specialization

If `A=V` is a vector space and both `B:V->G` and `H:V->Z` are linear, then a linear factorization through the image of `B` exists exactly when

\[
\boxed{
\ker B\subseteq\ker H.
}
\]

This is the same structural criterion already used in the DSD gravity source-descriptor audits, now lifted to the QFT-source / DSD-source interface.

## 6. PHY-QFT-017 — No-shortcut criterion for a reduced QFT source bridge

Fix the DSD structural context `sigma` and define the external comparison target

\[
H:=J_{\rm ext}\circ H_{\rm ext}.
\]

If there exist `x,y in A` with

\[
B_G(x)=B_G(y),
\qquad
H(x)\ne H(y),
\]

then **no DSD response depending only on `B_G(x)` can reproduce that external comparator on the full class `A`**.

The obstruction is not repaired by changing the downstream DSD response law: the distinguishing information has already been removed upstream by `B_G`.

Therefore the correct audit order is

```text
1. choose external source carrier,
2. choose DSD source bridge,
3. inspect bridge fibers,
4. test external response constancy on those fibers,
5. only then fit or derive a downstream DSD response.
```

This prevents a reduced source variable from being declared sufficient merely because one later response ansatz uses only that variable.

## 7. Finite scalarization counterexample

For a reproducible structural witness, use the finite selected source carrier

\[
V_T=\mathbb R^4
\]

with coordinates labelled

\[
(\rho,j,p,\pi).
\]

The labels are only finite stress-energy-sector placeholders: density-like, flux-like, pressure/stress-like, and anisotropy-like.  The witness does **not** claim that every point of this toy carrier is realized by a physical QFT state.

Take the scalar reduction

\[
B_\rho(\rho,j,p,\pi)=\rho
\]

and the synthetic comparator

\[
H(\rho,j,p,\pi)
=
(\rho+2p+\pi,\;j+\pi).
\]

Then the difference direction

\[
d=(0,0,1,0)
\]

satisfies

\[
B_\rho(d)=0,
\qquad
H(d)=(2,0)\ne0.
\]

Hence

\[
\ker B_\rho\not\subseteq\ker H,
\]

so the comparator cannot factor through the density scalar.

Likewise the partial bridge

\[
B_{\rho p}(\rho,j,p,\pi)=(\rho,p)
\]

fails because

\[
d'=(0,1,0,0)
\]

lies in `ker B_rhop` while `H(d')=(0,1)`.

The full selected four-coordinate record is injective on this carrier, so the finite test has no same-bridge / different-response collision there.

### Reproducible enumeration

On the 16-point binary cube `{0,1}^4`, the audit script finds

```text
rho-only bridge:        56 violating fiber pairs
(rho,pressure) bridge:  24 violating fiber pairs
full selected record:    0 violating fiber pairs
```

This is a finite structural audit, not evidence that the full four-coordinate descriptor is physically sufficient for semiclassical gravity.

## 8. What this proves and what it does not

### Confirmed

- A minimum QFT-to-DSD-gravity common interface can be written without changing the DSD core.
- Source sufficiency is exactly a **fiber-constancy** problem on the chosen admissible class.
- In a linear specialization it reduces to the **kernel-inclusion** test.
- A scalar or partial QFT source reduction cannot be assumed sufficient for a response that still distinguishes discarded sectors.
- The obstruction occurs upstream of the DSD gravity response law and therefore cannot be repaired by downstream curve fitting alone.

### Conditional

- A selected reduced source bridge may be sufficient on a restricted physical state/source family if the external comparator is constant on its fibers there.
- A finite probe family may be adequate for a declared comparison only after the relevant external response is shown to factor through that probe family.

### Unresolved / external-theory dependent

- Which renormalized QFT source records are physically realizable for the selected field theory and state class.
- Which finite or infinite stress-energy descriptor is sufficient for a chosen semiclassical response problem.
- The physical map from renormalized QFT source data to the present DSD gravity source sectors.
- Any value of the unresolved DSD gravity normalization parameter.

### Rejected

```text
same scalar energy-density-like readout
    => same complete gravitational response
```

as a generic inference without a factorization theorem on the chosen admissible family.

## 9. PHY-QFT-018 — Causality and covariance remain a separate bridge

The source-factorization theorem is static.  It does not identify QFT microcausality, external relativistic propagation, or DSD `c_info`.

A causal common-interface test requires additional supplied data:

```text
region/support map,
metric or causal relation,
time parameter identification,
source-to-response evolution operator,
DSD localization carrier,
DSD c_info convention,
external response support convention.
```

Only after these are supplied can one ask whether support propagation commutes across the interface.

Similarly, local covariance on the external QFT side and DSD map-specific covariance remain different mathematical conditions.  A common covariance claim requires explicit transport maps on both source and response carriers and a commuting diagram.

## 10. Relation to the current DSD gravity-principle line

This result does not replace the existing dynamic radial branch from Experiments 621–638.  That branch had already separated the static parameters from kinetic parameters and obtained the conditional causal-speed inequality

\[
\frac{c_A}{c_*}=\frac{\ell_A}{\sqrt{\nu_A}},
\]

with the corresponding `c_info` constraint when a causal comparison is supplied.

The new common-interface work is an **upstream source-typing branch**.  Once a real QFT source bridge passes the fiber test, it can be inserted as an input to a time-dependent DSD gravity model whose propagation sector is audited independently.

## 11. Core-paper impact

No amendment to the Formation Axiom System, Property Axiom System, Channel-Indexed Static Aggregation, or Structural Reorganization Dynamics core is indicated by this construction.

The result uses existing DSD discipline:

- explicit typed bridges,
- separation of optional physical specializations from the core,
- no reconstruction from a reduced readout without injectivity/sufficiency,
- independent dynamical propagation conditions.

## 12. Verdict

**PASS_WITH_BOUNDARY.**

The second-stage research line has moved from a verbal interface proposal to a mathematically testable common-interface criterion.  The first nontrivial result is negative but useful: a source reduction is acceptable only on state/source classes for which the target response is constant on its fibers.

## 13. Next target

Use an actual external semiclassical control family rather than the synthetic response:

```text
fixed background + fixed renormalization prescription
    -> selected admissible QFT source family
    -> finite smeared RSET descriptor
    -> candidate DSD gravity source bridge
    -> external linearized/semi-classical response comparator
    -> fiber/kernel sufficiency audit.
```

If that bridge survives, connect it to the causal time-dependent DSD radial model while keeping source sufficiency and propagation speed as separate audits.

## Reproducibility

Run from the repository root:

```bash
python audits/science/2026-09-07_qft_dsd_gravity_common_interface.py --mode all
```

The script uses only the Python standard library.
