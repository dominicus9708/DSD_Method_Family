# BH-RB-019 — Quantum closure branch / self-binding criterion gate

**Date:** 2026-09-15  
**Status:** `PASS_WITH_BOUNDARY / QUANTUM_CLOSURE_BRANCHES_SEPARATED / POSITIVE_EOS_INTERCEPT_REQUIRES_SELF_BINDING_OR_VACUUM_OFFSET / MASS_GAP_ALONE_INSUFFICIENT / SCALE_FREE_BRANCH_REJECTED_FOR_RADIUS_SELECTION / MICROPHYSICAL_CORE_EOS_NOT_YET_DERIVED`

## Scope

BH-RB-018 moved the constitutive scale \(\varepsilon_0\) from an assumed EOS parameter to an internal derivation target. The remaining question is not merely whether a microscopic scale exists, but whether that scale can produce a **positive zero-pressure self-bound state** that can serve as

\[
\varepsilon_0^{\rm EOS}>0.
\]

This audit separates four minimal quantum-closure branches:

1. mass/gap scale only;
2. vacuum/self-binding offset;
3. interaction-generated scale or finite-density saturation;
4. exactly scale-free closure.

The branches are tested for two logically distinct capabilities:

\[
\text{intrinsic scale generation}
\qquad\text{and}\qquad
\text{positive zero-pressure self-binding}.
\]

They are not equivalent.

## DSD provenance boundary

The active DSD structure permits formation identity, typed property/status, lineage, and explicit downstream quantum/physical bridges, but does not canonically map a property label to a physical Hamiltonian, coefficient, pressure law, or EOS.

Therefore the admissible chain remains

\[
F_{\rm core}
\to
\Pi_{\rm micro}
\to
B_{\rm Qmicro}
\to
(H\text{ or action},\rho,\text{statistics/interactions})
\to
\langle T_{\mu\nu}\rangle
\to
\text{constitutive law}
\to
\varepsilon_0^{\rm EOS}\text{ if it exists}.
\]

No branch below is promoted to a DSD theorem merely because it is representable in the Formation/Property/Dynamics interfaces.

---

## Branch D — exactly scale-free closure

Take the control EOS

\[
p=w\varepsilon,
\qquad 0<w\le1.
\]

Then

\[
p=0
\Longleftrightarrow
\varepsilon=0.
\]

Moreover the relation is preserved under a positive overall rescaling

\[
\varepsilon\mapsto \lambda\varepsilon,
\qquad
p\mapsto \lambda p.
\]

Hence the branch contains no preferred positive energy-density scale and cannot by itself choose a unique absolute radius through the BH-RB-017 relation.

Therefore

\[
\boxed{
\text{exactly scale-free closure}
\not\Rightarrow
\varepsilon_0^{\rm EOS}>0
}
\]

and this branch is rejected **as a unique radius-selection closure**, not as an inconsistent physical EOS in general.

---

## Branch A — mass/gap scale only

A supplied microscopic mass or gap \(m_*\) can carry an absolute scale. Dimensional analysis gives

\[
\varepsilon_m
\sim
C_m\frac{m_*^4c^5}{\hbar^3}.
\]

Thus the mass/gap branch passes the **scale-carrying** gate.

However a scale is not the same thing as self-binding.

For a free spin-1/2 degenerate Fermi gas at \(T=0\), with

\[
x=\frac{p_F}{m c},
\]

the pressure may be written

\[
P
=
\frac{m^4c^5}{24\pi^2\hbar^3}
\left[
 x(2x^2-3)\sqrt{1+x^2}
 +3\operatorname{arsinh}x
\right].
\]

The bracket is positive for every \(x>0\) and vanishes at \(x=0\). Therefore the free-gas comparator reaches zero pressure only when the Fermi momentum and number density vanish.

Hence

\[
\boxed{
\text{mass/gap scale present}
\not\Rightarrow
\text{positive finite-density zero-pressure state}
}
\]

and mass/gap alone is insufficient to identify \(\varepsilon_0^{\rm EOS}>0\).

This is an important narrowing of the successor-core search: a new mass eigenvalue, excitation gap, or quasiparticle gap can supply the missing dimensionful scale, but it does not automatically make the phase self-bound.

---

## Branch B — vacuum/self-binding offset

A vacuum or phase-energy offset can directly create a positive zero-pressure intercept.

The MIT bag model provides a standard mechanism comparator by introducing a constant energy per unit volume \(B\) for the confining region. In the conventional noninteracting quark-matter EOS,

\[
p=\frac13(\varepsilon-4B_{\rm eff}),
\]

so

\[
\boxed{
\varepsilon_0^{\rm EOS}=4B_{\rm eff}>0
}
\]

when \(B_{\rm eff}>0\).

This branch therefore demonstrates a concrete mechanism of the form

\[
\text{vacuum/phase energy difference}
\to
\text{positive zero-pressure energy density}.
\]

It is only a mechanism comparator. It does not imply that the black-hole successor core is quark matter, a bag, or governed by the MIT EOS.

Branch result:

\[
\boxed{
\text{vacuum/self-binding offset}
\Rightarrow
\text{positive-intercept-capable}
}
\]

provided the offset itself is derived from the declared microphysical closure rather than fitted to a desired radius.

---

## Branch C1 — interaction-generated scale by dimensional transmutation

An interaction can generate a physical dimensionful scale even when the classical or bare parameterization is written using a dimensionless coupling.

Use the generic one-loop asymptotically-free control

\[
\frac{d\alpha}{d\ln\mu}
=-b\alpha^2,
\qquad b>0.
\]

Its solution implies the RG-invariant combination

\[
\boxed{
\Lambda
=
\mu\exp\left[-\frac{1}{b\alpha(\mu)}\right].
}
\]

The accompanying script verifies that the same \(\Lambda\) is obtained after evolving \(\alpha\) between two renormalization scales.

This is the relevant correction to the purely dimensional statement of BH-RB-018:

\[
\boxed{
\text{dimensionless coupling alone with no scale data cannot create }\varepsilon_0,
}
\]

but

\[
\boxed{
\text{running interaction + renormalization boundary data}
\to
\text{RG-invariant generated scale}
}
\]

is possible.

QCD is the standard physical prototype of this dimensional-transmutation mechanism.

Once an energy scale \(\Lambda_E\) exists, it can feed a density scale

\[
\varepsilon_\Lambda
\sim
C_\Lambda
\frac{\Lambda_E^4}{(\hbar c)^3}.
\]

For the script's purely illustrative \(\Lambda_E=200\,\mathrm{MeV}\) and coefficient one,

\[
\varepsilon_\Lambda
\simeq
3.3363451\times10^{34}\ {\rm J\,m^{-3}}.
\]

This number is not a successor-core prediction.

Crucially, the same generated \(\Lambda\) can feed different phase functionals and different dimensionless coefficients. Therefore

\[
\boxed{
\text{dimensional transmutation}
\not\Rightarrow
\text{unique }\varepsilon_0^{\rm EOS}.
}
\]

It passes the scale-generation gate but not the complete EOS gate.

---

## Branch C2 — interaction-generated finite-density saturation

A second interaction route does not rely on a constant vacuum offset. Instead, the many-body energy per constituent can have a minimum at a nonzero density.

At zero temperature, let

\[
e(n)=\frac{\varepsilon(n)}{n}.
\]

Then

\[
p(n)
=
n^2\frac{de}{dn}.
\]

A finite-density self-bound state requires a point \(n_*>0\) satisfying

\[
\boxed{
\left.\frac{de}{dn}\right|_{n_*}=0,
\qquad
\left.\frac{d^2e}{dn^2}\right|_{n_*}>0.
}
\]

At that point

\[
p(n_*)=0,
\qquad
\varepsilon_0^{\rm EOS}=\varepsilon(n_*)=n_*e(n_*)>0
\]

if the energy density is positive.

The audit uses the dimensionless control

\[
e(n)
=e_*+rac K2\left(\frac{n}{n_*}-1\right)^2,
\qquad K>0,
\]

and verifies finite-density zero pressure plus positive local compressibility.

This is not a proposed black-hole-core EOS. It is a witness that interactions can, in principle, generate self-binding through a finite-density energy minimum.

Standard symmetric nuclear matter provides an external mechanism comparator: nuclear saturation density is defined at the minimum of the energy per baryon and at zero pressure, reflecting the balance of attractive and repulsive nuclear interactions.

Thus

\[
\boxed{
\text{interaction-generated saturation}
\Rightarrow
\text{positive-intercept-capable, conditionally}
}
\]

only when the actual microscopic interaction derives \(n_*\), the minimum, and the stable branch.

---

## Unified self-binding criterion

The four-branch audit suggests that the next black-hole successor-core closure should not begin by assuming a linear EOS. The more primitive target is an energy-density functional

\[
\varepsilon
=
\varepsilon(n,\rho_Q,s,J,\Omega,\ldots)
\]

or the corresponding quantum expectation value of the stress-energy tensor.

For a homogeneous zero-temperature conserved-density specialization,

\[
\mu=\frac{d\varepsilon}{dn},
\qquad
p=n\mu-\varepsilon.
\]

Equivalently, with \(e=\varepsilon/n\),

\[
p=n^2\frac{de}{dn}.
\]

The minimal candidate self-binding gate is therefore

\[
\boxed{
\exists n_*>0:
\quad
p(n_*)=0,
\quad
\varepsilon(n_*)>0,
\quad
\frac{dp}{dn}(n_*)>0.
}
\]

If this is derived from the quantum closure, then

\[
\boxed{
\varepsilon_0^{\rm EOS}:=\varepsilon(n_*)
}
\]

becomes a genuine microphysical output rather than a fitted constant.

The causal gate must still be checked on the resulting branch:

\[
0\le
\frac{dp}{d\varepsilon}
\le1.
\]

For the active non-equilibrium successor-core hypothesis, this equilibrium criterion is only the first coarse-grained slice. Transport, anisotropy, shear, flux, and formation transitions remain additional dynamic closure requirements.

---

## Formation threshold remains separate

The formation-admissibility threshold

\[
\varepsilon_{\rm form}
:=
\inf\{\varepsilon>0:F_{\rm core}\text{ satisfies its declared physical prerequisites}\}
\]

must remain distinct from

\[
\varepsilon_0^{\rm EOS}=\varepsilon(n_*).
\]

The two may coincide in a specific phase-transition model, but Formation/Property typing does not make them identical.

Therefore

\[
\boxed{
\varepsilon_{\rm form}
\neq_{\rm automatic}
\varepsilon_0^{\rm EOS}.
}
\]

---

## Branch decision matrix

| Branch | Intrinsic scale? | Positive finite-density \(p=0\)? | Current decision |
|---|---:|---:|---|
| Mass/gap only | Yes | Not automatic | Keep as scale carrier; insufficient alone |
| Vacuum/self-binding offset | Yes | Yes, if offset is physical | Survives |
| Interaction-generated RG scale | Yes | Not automatic | Survives scale gate; EOS still open |
| Interaction-generated saturation | Yes if \(n_*\) is derived | Yes | Survives conditionally |
| Exactly scale-free | No | No positive intercept for \(p=w\varepsilon\) | Reject for unique radius selection |

The strongest current conclusion is therefore

\[
\boxed{
\text{a positive }\varepsilon_0^{\rm EOS}
\text{ requires genuine self-binding structure, not merely a quantum mass/gap scale.}
}
\]

The self-binding can arise from a vacuum/phase-energy offset or from interactions that generate a stable finite-density minimum. A generated RG scale may underlie either mechanism, but is not itself sufficient.

---

## Consequence for the radius problem

BH-RB-017 supplied

\[
L_0
=
\frac{c^2}{\sqrt{G\varepsilon_0}}.
\]

BH-RB-019 sharpens the provenance requirement:

\[
\boxed{
R_{\min}\text{ candidate}
\text{ may use }\varepsilon_0
\text{ only after the quantum closure derives a positive self-bound state.}
}
\]

Therefore a free massive/gapped gas or an exactly scale-free phase cannot close the radius problem by itself.

The next calculation should construct the **minimal generic self-binding quantum closure**

\[
\varepsilon(n)
=
\varepsilon_{\rm vac}
+n m_*c^2
+\varepsilon_{\rm kin}(n;m_*)
+\varepsilon_{\rm int}(n;\lambda,\Lambda,\ldots)
\]

and test whether a finite \(n_*\) satisfying the self-binding, stability, and causal conditions can emerge without fitting \(n_*\) or \(\varepsilon_0\) to a desired black-hole radius.

This will be the natural target of BH-RB-020.

## Verdict

\[
\boxed{
\text{PASS\_WITH\_BOUNDARY /
QUANTUM\_CLOSURE\_BRANCHES\_SEPARATED /
POSITIVE\_EOS\_INTERCEPT\_REQUIRES\_SELF\_BINDING\_OR\_VACUUM\_OFFSET /
MASS\_GAP\_ALONE\_INSUFFICIENT /
SCALE\_FREE\_BRANCH\_REJECTED\_FOR\_RADIUS\_SELECTION /
MICROPHYSICAL\_CORE\_EOS\_NOT\_YET\_DERIVED}
}
\]

The accompanying script reports **15/15 PASS**.

## Reproducibility

```powershell
python audits/science/2026-09-15_dsd_gravity_quantum_closure_branch_gate.py --mode all
```

## External comparators

- Chodos, A., Jaffe, R. L., Johnson, K., Thorn, C. B., & Weisskopf, V. F., *New extended model of hadrons*, Physical Review D **9**, 3471 (1974), DOI: 10.1103/PhysRevD.9.3471. The model introduces a constant energy per unit volume \(B\) as a confining vacuum-energy offset.
- Zhang, C. & Mann, R. B., *Unified interacting quark matter and its astrophysical implications*, Physical Review D **103**, 063018 (2021), DOI: 10.1103/PhysRevD.103.063018. Used only for the conventional comparator \(p=(\varepsilon-4B_{\rm eff})/3\).
- Particle Data Group, *Quantum Chromodynamics* review, Review of Particle Physics 2026, for standard QCD running/asymptotic-freedom context.
- CERN lecture material on dimensional transmutation and asymptotic freedom, illustrating construction of an RG-invariant scale from running coupling and renormalization data.
- CompOSE reference manual, European Physical Journal A (2022), for the standard nuclear-matter saturation condition \(p=n^2 d(E/A)/dn=0\) at the minimum of the energy per baryon.
- *Theoretical and experimental constraints for the equation of state of dense and hot matter*, Living Reviews in Relativity (2024), for nuclear saturation as the balance point of attractive and repulsive interactions and for the role of microscopic many-body input in dense-matter EOS construction.

## Project-source continuity

- `DSD_Structural_Reorganization_Dynamics_EN(20260904-092544).pdf`: property labels do not canonically determine dynamic coefficients/operators; constitutive dynamic bridges are explicit downstream structure.
- `DSD_Channel_Indexed_Static_Aggregation_EN(9).pdf`: property-to-channel association and physical interpretation bridges are explicit; no physical constitutive law is introduced by the static layer.
- Notion `양자역학·상대론 — DSD 기술가능성 접점 분석`: standard quantum formalism remains an external specialization; DSD supplies describability/context structure rather than a replacement Hamiltonian or EOS.
