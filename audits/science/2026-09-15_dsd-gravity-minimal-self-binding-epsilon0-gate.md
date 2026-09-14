# BH-RB-020 — Minimal self-binding quantum closure / epsilon0 derivation gate

**Date:** 2026-09-15  
**Status:** `PASS_WITH_BOUNDARY / FINITE_DENSITY_SELF_BINDING_SCALE_CONSTRUCTED / EPSILON0_DERIVABLE_FROM_MICRO_COEFFICIENTS_IN_TOY_CLOSURE / LOCAL_CAUSALITY_CONDITION_IDENTIFIED / GLOBAL_CAUSAL_COMPLETION_REQUIRED / BLACK_HOLE_CORE_EOS_AND_RADIUS_NOT_DERIVED`

## Scope

BH-RB-019 separated four closure classes and showed that a positive finite-density EOS intercept requires self-binding, a vacuum/phase offset, or an interaction-generated saturation scale; a mass/gap by itself is insufficient.

BH-RB-020 asks the narrower constructive question:

> Can a minimal interaction energy functional generate a finite saturation density and a positive \(\varepsilon_0\) without inserting a target black-hole radius, while remaining locally stable and causal at the saturation point?

The answer is **yes for a local effective closure**, but **no for a globally complete black-hole-core EOS**.

## DSD provenance boundary

Formation/Property/DSD-QM may type the successor formation, microscopic inputs, applicability, prerequisites, state/status, and lineage. They do not determine the numerical interaction coefficients used below.

The physical bridge remains explicit:

\[
F_{\rm core}
\to
\Pi_{\rm micro}
\to
(H\text{ or QFT action})
\to
\varepsilon(n)
\to
p(n)
\to
\langle T_{\mu\nu}\rangle.
\]

Therefore the coefficients \(m,A,B\) in the present control are **external microscopic/effective coefficients to be derived from a later Hamiltonian/QFT closure**, not new DSD constants.

## Standard thermodynamic comparator

For zero-temperature uniform matter with constituent density \(n\) and energy per constituent \(e(n)=\varepsilon(n)/n\), the pressure is

\[
\boxed{
p=n^2\frac{de}{dn}.
}
\]

The CompOSE reference manual uses the same saturation criterion: at the saturation density, pressure vanishes and the energy per baryon is minimal. Modern dense-matter reviews likewise describe nuclear saturation as arising from the competition of attractive and repulsive interactions.

These are external standard many-body comparators only; the successor core is not identified with nuclear matter.

## Minimal interaction-generated self-binding control

Take the local effective energy per constituent

\[
\boxed{
e(n)=mc^2-An+Bn^2,
\qquad A>0,\quad B>0.
}
\]

Interpretation at the control level:

- \(-An\): effective attractive contribution;
- \(+Bn^2\): higher-density repulsive/stiffening contribution;
- \(mc^2\): dilute rest-energy reference.

No physical black-hole radius is inserted.

The energy density is

\[
\varepsilon(n)=nmc^2-An^2+Bn^3.
\]

The pressure is

\[
\boxed{
p(n)=-An^2+2Bn^3.
}
\]

## Saturation density emerges from the interaction coefficients

The finite stationary point of the energy per constituent is

\[
\frac{de}{dn}=-A+2Bn=0,
\]

hence

\[
\boxed{
n_*=\frac{A}{2B}>0.
}
\]

Because

\[
\frac{d^2e}{dn^2}=2B>0,
\]

this is a strict local minimum.

At the same density,

\[
p(n_*)=0.
\]

Thus the model produces the standard self-bound saturation structure

\[
\boxed{
\text{finite-density energy minimum}
\Longleftrightarrow
p=0.
}
\]

## Derived positive EOS intercept

At the minimum,

\[
e_*=mc^2-\frac{A^2}{4B}.
\]

Therefore the zero-pressure energy density is not an independent parameter but

\[
\boxed{
\varepsilon_0
=\varepsilon(n_*)
=\frac{A}{2B}
\left(mc^2-\frac{A^2}{4B}\right).
}
\]

Define

\[
y:=\frac{A^2}{4Bmc^2}.
\]

Then

\[
e_*=mc^2(1-y).
\]

For

\[
0<y<1,
\]

the phase is bound relative to the dilute rest-energy reference while retaining positive energy per constituent.

This is the first restart-stage control in which \(\varepsilon_0\) is **calculated from microscopic/effective interaction coefficients rather than entered as a separate EOS offset**.

It is still not a physical black-hole-core prediction because \(m,A,B\) have not yet been derived from a successor-core Hamiltonian or QFT.

## Local causal-stability gate

For a barotropic zero-temperature closure,

\[
\frac{c_s^2}{c^2}=\frac{dp}{d\varepsilon}
=\frac{dp/dn}{d\varepsilon/dn}.
\]

Here

\[
\frac{dp}{dn}=-2An+6Bn^2,
\]

\[
\frac{d\varepsilon}{dn}=mc^2-2An+3Bn^2.
\]

At \(n=n_*\),

\[
\boxed{
\left.\frac{c_s^2}{c^2}\right|_*
=\frac{2y}{1-y}.
}
\]

Thermodynamic stability requires the result to be positive; relativistic causality requires it not to exceed unity. Therefore

\[
\boxed{
0<y\le\frac13.
}
\]

Equivalently, the local self-binding cannot be made arbitrarily strong in this toy closure while preserving a causal sound speed at saturation.

## Causal-density cap of the polynomial control

Requiring

\[
\frac{dp}{d\varepsilon}\le1
\]

for the same polynomial gives

\[
3Bn^2\le mc^2,
\]

or

\[
\boxed{
n\le n_{\rm causal}:=\sqrt{\frac{mc^2}{3B}}.
}
\]

The saturation point lies below this cap exactly when \(y\le1/3\).

However, at asymptotically high density,

\[
\frac{dp}{d\varepsilon}\to2,
\]

so the polynomial becomes superluminal.

Therefore

\[
\boxed{
\text{finite self-binding scale derived}
\neq
\text{globally causal high-density EOS derived}.
}
\]

This closure must be treated as a **near-saturation effective control** and replaced or completed by a relativistic many-body/QFT constitutive law before it can be used for the deepest trapped-core dynamics.

## Physical interpretation for the successor-core program

BH-RB-020 narrows the unknown from a free EOS intercept to microscopic coefficients:

\[
\boxed{
(m,A,B)
\longrightarrow
n_*
\longrightarrow
\varepsilon_0
\longrightarrow
\text{GR length scale candidate}.
}
\]

The BH-RB-017 length carrier may then be written

\[
L_0
=\frac{c^2}{\sqrt{G\varepsilon_0}},
\]

but \(L_0\) is still not the physical core radius. The actual \(R_{\min}\) requires coupling the derived constitutive law to the trapped, rotating, non-equilibrium GR dynamics audited in BH-RB-009 through BH-RB-016.

The important gain is that one no longer needs to choose \(\varepsilon_0\) after seeing the desired radius. If a successor-core Hamiltonian fixes \(m,A,B\), the saturation scale is downstream.

## Formation threshold remains separate

Nothing in this calculation identifies the saturation density with the density at which the successor formation first becomes admissible.

Keep

\[
\boxed{
n_{\rm form}\neq_{\rm automatically}n_*}
\]

and

\[
\boxed{
\varepsilon_{\rm form}\neq_{\rm automatically}\varepsilon_0^{\rm EOS}.
}
\]

A phase may first become dynamically accessible at one density and reach its self-bound zero-pressure state at another.

## Main result

A minimal attraction-plus-higher-order-repulsion closure is sufficient to construct, without radius fitting,

\[
\boxed{
n_*=\frac{A}{2B}}
\]

and

\[
\boxed{
\varepsilon_0
=\frac{A}{2B}
\left(mc^2-\frac{A^2}{4B}\right).
}
\]

Local causal saturation further imposes

\[
\boxed{
\frac{A^2}{4Bmc^2}\le\frac13.
}
\]

This is a genuine reduction of freedom relative to BH-RB-017/018/019, but it does not determine the physical coefficients or globally valid high-density dynamics.

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
FINITE\_DENSITY\_SELF\_BINDING\_SCALE\_CONSTRUCTED /
EPSILON0\_DERIVABLE\_FROM\_MICRO\_COEFFICIENTS\_IN\_TOY\_CLOSURE /
LOCAL\_CAUSALITY\_CONDITION\_IDENTIFIED /
GLOBAL\_CAUSAL\_COMPLETION\_REQUIRED /
BLACK\_HOLE\_CORE\_EOS\_AND\_RADIUS\_NOT\_DERIVED}
}
\]

The accompanying script reports **15/15 PASS**.

## Reproducibility

```powershell
python audits/science/2026-09-15_dsd_gravity_minimal_self_binding_epsilon0_gate.py --mode all
```

## External comparators

- Typel et al., *CompOSE reference manual*, European Physical Journal A **58**, 221 (2022). The saturation density is defined by zero pressure and minimum energy per baryon.
- Kumar et al., *Theoretical and experimental constraints for the equation of state of dense and hot matter*, Living Reviews in Relativity **27**, 3 (2024). Nuclear saturation is discussed as the result of the balance of attractive and repulsive interactions.
- Kojo, *QCD equations of state and speed of sound in neutron stars*, AAPPS Bulletin **31**, 11 (2021). Thermodynamic stability and causality are summarized by \(0\le c_s^2=\partial P/\partial\varepsilon\le1\) in units with \(c=1\).

## Next audit

BH-RB-021 should replace the local polynomial at high density by a causal completion and test whether a matched closure can simultaneously preserve:

1. the finite-density self-binding point \(n_*\),
2. \(\varepsilon_0>0\),
3. continuity of \(p\) and chemical potential,
4. \(0\le dp/d\varepsilon\le1\),
5. sufficient stress response for the trapped dynamic core branch,
6. no radius fitting.
