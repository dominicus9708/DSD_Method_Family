# BH-RB-018 — Quantum microphysical scale / successor-core EOS provenance gate

**Date:** 2026-09-14  
**Status:** `PASS_WITH_BOUNDARY / QUANTUM_SCALE_PROVENANCE_IDENTIFIED / MICROSCOPIC_HAMILTONIAN_OR_FIELD_SCALE_REQUIRED / PLANCK_SCALE_NOT_AUTOMATICALLY_SELECTED / BLACK_HOLE_CORE_EOS_NOT_DERIVED`

## Scope

BH-RB-017 showed that a finite constitutive radius scale requires an independent dimensionful energy-density scale such as \(\varepsilon_0\), while causal stiffness alone does not choose it.

This audit asks the next narrower question:

> Can the active DSD Formation/Property/QM structure identify or derive the origin of \(\varepsilon_0\), and under what additional physical closure could a black-hole successor-core EOS become calculable rather than assumed?

The result is positive at the **provenance/closure level** but negative at the **unique numerical EOS level**.

## DSD boundary

The active DSD documents impose the following firewalls.

- Formation and Property layers can type formation identity, applicability, prerequisites, defined/undefined status, and lineage.
- Property names do not canonically determine physical coefficients or operators.
- When property data influence dynamics, an explicit constitutive dynamic bridge is required.
- The existing DSD-QM analysis keeps standard Hilbert/Born structures as explicit external quantum specialization rather than relabeling them as generic DSD consequences.

Therefore the admissible chain is

\[
\boxed{
F_{\rm core}
\to
\text{typed microphysical inputs}
\to
B_{\rm Qmicro}
\to
(H\text{ or action},\rho,\text{statistics/interactions})
\to
\langle T_{\mu\nu}\rangle
\to
\text{constitutive law / EOS}
\to
\varepsilon_0\text{ if it exists}
}
\]

and not

\[
\boxed{
\text{property label ``density''}
\not\Rightarrow
\varepsilon_0.
}
\]

## Dimensional no-free-scale gate

The dimensions of reduced Planck constant and light speed are

\[
[\hbar]=M L^2T^{-1},
\qquad
[c]=LT^{-1}.
\]

An energy density has dimension

\[
[\varepsilon]=M L^{-1}T^{-2}.
\]

Solving for a monomial \(\hbar^a c^b\) gives no solution.

Hence

\[
\boxed{
\hbar+c+\text{dimensionless couplings}
\not\Rightarrow
\text{an absolute energy-density scale}.
}
\]

A dimensionless coupling can change only a coefficient or functional dependence, not repair the missing dimension.

This means the current DSD-QM layer cannot manufacture a numerical \(\varepsilon_0\) merely by adding quantum notation.

## One microscopic mass scale is enough dimensionally, but not dynamically

If a physical mass scale \(m_*\) is independently supplied, dimensional analysis admits

\[
\boxed{
\varepsilon_m
\sim
C_m\frac{m_*^4c^5}{\hbar^3}
}
\]

with a dimensionless coefficient \(C_m\).

Equivalently, if a microscopic energy scale \(\Lambda\) is supplied,

\[
\boxed{
\varepsilon_\Lambda
\sim
C_\Lambda
\frac{\Lambda^4}{(\hbar c)^3}.
}
\]

But this is only a dimensional carrier.

The coefficient and even the validity of this form depend on the actual quantum state, statistics, interactions, vacuum contribution, chemical potentials, phase structure, and thermodynamic limit.

Therefore

\[
\boxed{
\text{mass/energy scale present}
\neq
\text{successor-core EOS derived}.
}
\]

The BH-RB-017 GR scale built from the mass-generated density obeys

\[
L_m
=
\frac{c^2}{\sqrt{G\varepsilon_m}}
\propto m_*^{-2}.
\]

Thus different microscopic scale assignments produce radically different macroscopic length scales; the microscopic carrier cannot be guessed after the desired radius is known.

## Vacuum/self-binding offset as an explicit standard comparator

The original MIT bag model introduced a Lorentz-invariant constant energy per unit volume \(B\) for the confining region (Chodos et al., 1974, Phys. Rev. D 9, 3471).

A conventional noninteracting quark-matter form is

\[
p=\frac13(\varepsilon-4B_{\rm eff}),
\]

so that

\[
\boxed{
\varepsilon_0=4B_{\rm eff}
}
\]

in that specific model.

This is useful only as a **mechanism comparator**:

\[
\text{microscopic/vacuum energy offset}
\to
\text{positive zero-pressure energy density}.
\]

It is not evidence that a black-hole successor core is quark matter, a bag, or governed by the MIT EOS.

## Formation-transition scale and EOS intercept must remain distinct

Define a candidate formation threshold

\[
\varepsilon_{\rm form}
:=
\inf\{\varepsilon>0:
F_{\rm core}\text{ satisfies the declared physical prerequisites}\}.
\]

Separately, when a self-bound EOS exists, define

\[
\varepsilon_0^{\rm EOS}
:=
\inf\{\varepsilon>0:
p(\varepsilon)=0\text{ on the stable successor branch}\}.
\]

Current DSD does not imply

\[
\boxed{
\varepsilon_{\rm form}=\varepsilon_0^{\rm EOS}.
}
\]

They may coincide only after an explicit quantum-statistical or field-theoretic derivation.

This distinction prevents a formation threshold from being silently renamed as the EOS offset.

## Planck-scale gate

With \(\hbar,c,G\), dimensional analysis admits

\[
\boxed{
\varepsilon_P
=
\frac{c^7}{\hbar G^2}
}
\]

and BH-RB-017 then gives

\[
\frac{c^2}{\sqrt{G\varepsilon_P}}
=
\sqrt{\frac{\hbar G}{c^3}}
=\ell_P.
\]

Using CODATA 2022 constants, the audit script obtains

\[
\varepsilon_P
\simeq
4.632946790734\times10^{113}\ {\rm J\,m^{-3}},
\]

\[
\ell_P
\simeq
1.616255023929\times10^{-35}\ {\rm m}.
\]

This is a dimensional identity, not a black-hole-core prediction.

The existence of the Planck combination does **not** prove

\[
\boxed{
\varepsilon_0=\varepsilon_P.
}
\]

Selecting the Planck density would require a physical argument that the successor phase is controlled by that quantum-gravitational scale. Standard QM + classical GR do not supply that selection rule merely from the constants being available.

## Why the next bridge must go beyond the current measurement-level DSD-QM layer

The current DSD-QM work has successfully analyzed state representation, measurement contexts, readout fibers, contextuality, locality, and related describability questions while preserving standard quantum mechanics as an external specialization.

A bulk EOS requires more:

\[
\boxed{
\text{many-body quantum statistical mechanics and, at sufficiently relativistic density, QFT-scale input}.
}
\]

The minimum physical closure must declare at least some of the following when applicable:

- microscopic degrees of freedom or field content;
- masses or dynamically generated gaps;
- interaction Hamiltonian/action and coupling parameters;
- statistics and conserved charges;
- chemical potentials/temperature or a non-equilibrium state rule;
- vacuum/condensate contribution;
- stress-energy operator and renormalization prescription when field theory is used;
- transport coefficients if the successor core remains non-equilibrium.

Formation/Property axioms can type and audit these inputs, but they do not replace their physical content.

## Candidate downstream quantum closure

A controlled successor-core specialization should therefore be written schematically as

\[
\mathcal Q_{\rm core}
=
(F_{\rm core},\Pi_{\rm micro},\mathcal H\text{ or field algebra},H_\lambda,\rho,\mathcal C_{\rm therm})
\]

with an explicit physical bridge

\[
B_{\rm Qmicro}:
\mathcal Q_{\rm core}
\longrightarrow
\bigl(\langle T_{\mu\nu}\rangle,\text{transport},\text{phase data}\bigr).
\]

Only after this bridge is specified may one test whether the output contains an intrinsic positive scale

\[
\varepsilon_*>0
\]

and whether that scale is

1. a phase-formation threshold,
2. a vacuum/self-binding offset,
3. a gap/confinement scale,
4. a zero-pressure EOS intercept,
5. or none of these.

## Consequence for the black-hole-only EOS idea

A distinct successor-core constitutive law remains an open and legitimate target, but the correct target is broader than a static one-parameter EOS.

The active dynamical branch may require

\[
T_{\mu\nu}
=
\mathcal C_{\mu\nu}
[\rho_Q,\varepsilon,s,J,\Omega,\sigma_{\mu\nu},\nabla\rho_Q,\ldots],
\]

with \(p=p(\varepsilon)\) appearing only as an equilibrium or coarse-grained specialization.

Thus the research question is now sharpened to

\[
\boxed{
\text{Does the minimal admissible quantum microphysical closure of }F_{\rm core}
\text{ generate a unique intrinsic energy-density scale and constitutive law?}
}
\]

If yes, BH-RB-017 converts that scale into a genuine candidate radius scale.

If no, \(\varepsilon_0\) remains an external free parameter and cannot be used as evidence for a derived black-hole-core radius.

## Main result

The combined Formation/Property/DSD-QM framework can do more than merely relabel an EOS parameter: it can enforce provenance, distinguish formation thresholds from EOS intercepts, retain the full typed microscopic input, and reject scale-free closures that cannot possibly determine an absolute radius.

But the current axioms and measurement-level quantum specialization do not yet determine a unique microscopic Hamiltonian, field content, vacuum scale, or \(\varepsilon_0\).

Therefore

\[
\boxed{
\text{DSD can make }\varepsilon_0\text{ an internal derivation target, but has not yet derived it.}
}
\]

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
QUANTUM\_SCALE\_PROVENANCE\_IDENTIFIED /
MICROSCOPIC\_HAMILTONIAN\_OR\_FIELD\_SCALE\_REQUIRED /
PLANCK\_SCALE\_NOT\_AUTOMATICALLY\_SELECTED /
BLACK\_HOLE\_CORE\_EOS\_NOT\_DERIVED}
}
\]

The accompanying script reports **13/13 PASS**.

## Reproducibility

```powershell
python audits/science/2026-09-14_dsd_gravity_quantum_microphysical_scale_gate.py --mode all
```

## External comparators

- Chodos, A., Jaffe, R. L., Johnson, K., Thorn, C. B., & Weisskopf, V. F., *New extended model of hadrons*, Physical Review D **9**, 3471 (1974), DOI: 10.1103/PhysRevD.9.3471.
- Zhang, C. & Mann, R. B., *Unified interacting quark matter and its astrophysical implications*, Physical Review D **103**, 063018 (2021), DOI: 10.1103/PhysRevD.103.063018.
- NIST/CODATA 2022 fundamental constants for \(G\), \(\hbar\), Planck mass and Planck length.

## Project-source continuity

- `DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf`: constitutive dynamic bridge is explicit additional structure; property labels do not canonically determine dynamic coefficients/operators.
- `DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf`: property-to-channel association and property bridges are explicit downstream data; the static layer contains no physical constitutive law.
- Notion `양자역학·상대론 — DSD 기술가능성 접점 분석`: standard quantum formalism is retained as external specialization and DSD is used to analyze describability/context structure rather than rename standard quantum laws.
