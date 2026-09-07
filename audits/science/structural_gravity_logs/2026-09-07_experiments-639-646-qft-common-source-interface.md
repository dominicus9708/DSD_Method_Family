# DSD Gravity-Principle Research Log — Experiments 639–646

Date: 2026-09-07

Historical repository path: `structural_gravity_logs/` is retained for continuity.  The active conceptual name in this record is the **DSD gravity-principle research line**.

## Experiments 639–640 — external QFT source carrier and finite probe record

### Result

The QFT/relativity interface is not inserted into the DSD gravity line by identifying a quantum state, a local algebra, or a renormalized stress tensor directly with a DSD source scalar.

The minimum external source record is version-locked by

```text
background/spacetime,
QFT/local algebra or field model,
admissible state class,
renormalization prescription,
selected local or smeared source probes.
```

For a finite selected probe family `F=(f_1,...,f_m)`, define an external source descriptor schematically by

\[
S_{\mathcal F}(q)
=
(\langle T^{\rm ren},f_1\rangle_q,\ldots,
 \langle T^{\rm ren},f_m\rangle_q).
\]

This is external QFT representation data, not a Formation Stage-V assignment and not a Stage-VI channel by itself.

### Verdict

- direct `<T_mu nu>_ren = DSD source` identification: **REJECTED**
- finite probe descriptor as an explicit comparison carrier: **CONFIRMED AS AN INTERFACE CONSTRUCTION**
- physical sufficiency of any fixed finite probe family: **UNRESOLVED / MODEL-DEPENDENT**

---

## Experiments 641–642 — explicit DSD source bridge and comparison carrier

### Result

Introduce an application-level source bridge

\[
B_G:V_T\to V_G
\]

from the external source carrier to a declared DSD gravity-source carrier.  For fixed DSD structural context `sigma`, let

\[
R_G^\sigma:V_G\to X_G
\]

be the DSD gravity response.  Let an external comparator be

\[
H_{\rm ext}:V_T\to X_{\rm ext}.
\]

Because `X_G` and `X_ext` need not be the same type, comparison requires explicit maps

\[
J_G:X_G\to Z,
\qquad
J_{\rm ext}:X_{\rm ext}\to Z.
\]

The common interface is well typed only when the claim is made in a declared comparison carrier `Z`, with the target commuting condition

\[
\boxed{
J_G\circ R_G^\sigma\circ B_G
=
J_{\rm ext}\circ H_{\rm ext}
}
\]

on a declared admissible source class.

### Verdict

- same role/name implies same source or response type: **REJECTED**
- explicit source bridge plus explicit comparison maps: **CONFIRMED AS MINIMUM INTERFACE DATA**
- current DSD gravity response already equals semiclassical response: **UNRESOLVED / NOT ESTABLISHED**

---

## Experiments 643–644 — exact source-sufficiency theorem

### Result

For arbitrary maps

\[
B:A\to G,
\qquad
H:A\to Z,
\]

there exists

\[
F:B[A]\to Z
\]

with

\[
H=F\circ B
\]

if and only if `H` is constant on every fiber of `B`:

\[
\boxed{
B(x)=B(y)\Rightarrow H(x)=H(y)
\quad(x,y\in A).
}
\]

Hence a DSD source reduction is sufficient for a selected external response exactly when the external response does not distinguish states/source records that the bridge identifies.

For linear carriers and linear maps, this reduces to

\[
\boxed{
\ker B\subseteq\ker H.
}
\]

on the selected source space.

### Consequence

This lifts the earlier mass/distortion kernel audit to the full QFT-source -> DSD-source interface.

If the bridge erases a source distinction that the comparator still sees, **no downstream DSD response depending only on the reduced bridge output can repair the loss**.

### Verdict

- nonlinear set-level fiber criterion: **CONFIRMED**
- linear kernel-inclusion specialization: **CONFIRMED**
- downstream fitting can always compensate for upstream source erasure: **REJECTED**

---

## Experiment 645 — finite scalarization counterexample

### Setup

Use a synthetic finite selected source carrier

\[
V_T=\mathbb R^4,
\qquad
(\rho,j,p,\pi),
\]

where the coordinate labels stand only for density-like, flux-like, pressure/stress-like and anisotropy-like source sectors.

Take

\[
B_\rho(\rho,j,p,\pi)=\rho
\]

and a deliberately synthetic response

\[
H(\rho,j,p,\pi)
=(\rho+2p+\pi,\;j+\pi).
\]

Then

\[
d=(0,0,1,0)
\]

satisfies

\[
B_\rho(d)=0,
\qquad
H(d)=(2,0)\ne0.
\]

Thus the density-like scalar is not sufficient for this response.

A second bridge

\[
B_{\rho p}(\rho,j,p,\pi)=(\rho,p)
\]

also fails because `d'=(0,1,0,0)` lies in its kernel while the response changes.

On the 16-point binary cube, the reproducible script reports:

```text
rho-only bridge:        56 violating fiber pairs
(rho,pressure) bridge:  24 violating fiber pairs
full selected record:    0 violating fiber pairs
```

The witness is structural only; it does not claim that every toy vector is physically realized by a QFT state or that the four-coordinate record is physically complete.

### Verdict

- scalar density-like source is generically sufficient without a theorem: **REJECTED**
- partial source records can fail even after adding one stress sector: **CONFIRMED BY FINITE WITNESS**
- full four-coordinate toy record is physically sufficient: **NOT CLAIMED**

---

## Experiment 646 — source sufficiency is separate from causality/covariance

### Result

The source factorization theorem is static.  It does not identify

```text
QFT microcausality,
relativistic support propagation,
DSD c_info,
DSD axis principal speed,
DSD metric/evolution time.
```

A causal common-interface test still requires a supplied region/support map, time identification, evolution operator, DSD localization carrier and external response-support convention.

The dynamic radial line from Experiments 621–638 therefore remains intact as a separate downstream audit.  The QFT common-source interface is upstream: only after a physical source bridge survives the fiber/kernel test should it be connected to the causal time-dependent DSD radial model.

### Verdict

- source sufficiency implies causal compatibility: **REJECTED**
- QFT causality bound = DSD `c_info` by terminology: **REJECTED**
- upstream source bridge and downstream propagation audit should remain separated: **CONFIRMED**

---

## Combined consequence

The DSD gravity-principle line now has an explicit entry point for quantum/QFT matter data without importing semiclassical gravity as a DSD law:

```text
QFT local state/algebra
  -> fixed renormalized source prescription
  -> selected source descriptor S_F
  -> explicit DSD source bridge B_G
  -> fiber/kernel sufficiency audit
  -> DSD gravity response R_G
  -> independent dynamics / c_info audit
  -> optional common comparison with external semiclassical response.
```

This is a bridge architecture, not a derivation of quantum gravity and not a determination of the unresolved DSD gravity normalization.

## Reproducibility

Repository-root command:

```bash
python audits/science/2026-09-07_qft_dsd_gravity_common_interface.py --mode all
```

Main cross-audit record:

```text
audits/science/2026-09-07_phy-qft-016-018-dsd-gravity-common-interface.md
```

## Next audit target

Replace the synthetic comparator by one actual external semiclassical control family on a fixed background and fixed renormalization prescription.  Test the weakest source descriptor that preserves the selected external response.  Only a surviving bridge is eligible to enter the causal time-dependent DSD radial model.
