# REL Extension 002 — Relativity Reconstruction Selectors / Causal–Projective–Metric Recovery Gate

Date: 2026-09-10  
Status: **PASS_WITH_BOUNDARY**  
Program: **Core-Theory Reconstruction Challenge — Standard Relativity Extension Track**

## 1. Purpose

REL Extension 001 established that generic DSD does not independently select a physical Lorentzian spacetime carrier, four-dimensionality, Lorentzian signature, the numerical relativistic light speed, or Einstein dynamics.

The next question is the relativity analogue of the selector audits used in the quantum track:

> If weaker observational/geometrical structures are supplied explicitly, how far can one reconstruct relativistic geometry without inserting the full metric at the beginning?

The gate separates:

```text
light-ray / causal data
free-fall path data
conformal structure
projective structure
Weyl-compatible structure
metric scale / pseudo-Riemannian representative
Einstein dynamics
```

No successful comparator theorem is back-counted as a theorem of generic DSD.

---

## 2. External reconstruction comparator

The main external comparator is the Ehlers–Pirani–Schild (EPS) constructive program and later mathematical clarification.

Under the usual EPS-type assumptions, light propagation is associated with conformal structure and freely falling massive trajectories with projective structure. Matveev and Scholz (2020) proved the central light-cone compatibility statement in the setting of an indefinite metric on an n-dimensional manifold with n >= 3: a compatible projective and conformal pair is Weyl compatible.

This result is used only as an external theorem comparator.

A modern re-analysis by Wheeler (2025) stresses that the EPS conclusion depends on restrictions on the connection class, including the torsion-free affine setup and the representation used for conformal symmetry. Therefore this audit does not promote the EPS route to an assumption-free derivation of physical spacetime geometry.

The operational/reconstruction premises themselves remain supplied selector data.

---

## 3. Conformal light-cone gate

Let

\[
\eta=\operatorname{diag}(-1,+1,+1,+1)
\]

and

\[
g'=\Omega^2\eta,
\qquad \Omega=3.
\]

For each tested null vector k,

\[
\eta(k,k)=0
\quad\Longleftrightarrow\quad
g'(k,k)=0.
\]

Timelike and spacelike signs are also preserved by positive conformal rescaling.

However the norm scale changes. For u=(1,0,0,0),

\[
\sqrt{-g'(u,u)}=\Omega\sqrt{-\eta(u,u)}.
\]

Therefore

\[
\boxed{\text{light-cone structure}\not\Rightarrow\text{metric scale}.}
\]

The finite witness does not prove the full theorem that suitable complete null-cone data determine exactly a conformal class; that is external differential geometry. It verifies the required non-uniqueness direction.

---

## 4. Projective free-fall gate

For torsion-free affine connections, the standard projective-equivalence relation is

\[
\Gamma'^i{}_{jk}
=
\Gamma^i{}_{jk}
+\delta^i_j\psi_k
+\delta^i_k\psi_j.
\]

Contracting with a tangent v gives

\[
(\Gamma'-\Gamma)^i{}_{jk}v^jv^k
=2\psi(v)v^i.
\]

The difference is tangent-parallel, so the affine parameterization changes while the unparameterized geodesic curve is preserved.

The regression witness verifies explicitly that two different connection representatives can therefore encode the same unparameterized path family.

Hence

\[
\boxed{\text{unparameterized free-fall paths}\not\Rightarrow\text{unique affine connection}.}
\]

The projective class is the appropriate comparator object only after the torsion-free affine modeling assumptions are supplied.

---

## 5. Conformal versus projective information

For a conformal rescaling

\[
g'=e^{2\sigma}g,
\]

the Levi-Civita connections satisfy locally

\[
\Delta\Gamma^i{}_{jk}
=
\delta^i_j\partial_k\sigma
+\delta^i_k\partial_j\sigma
-g_{jk}\partial^i\sigma.
\]

For a null vector k, the last term vanishes after contraction because g(k,k)=0, leaving a tangent-parallel shift. Thus null geodesic directions are conformally preserved.

For a generic timelike vector u the final term does not vanish and the shift need not be tangent-parallel.

The finite witness therefore confirms:

\[
\boxed{\text{same conformal light cones}\not\Rightarrow\text{same timelike projective structure}.}
\]

This is why light rays and free fall provide genuinely different reconstruction information.

---

## 6. Weyl compatibility and integrability boundary

Matveev–Scholz prove, for the stated n >= 3 indefinite-signature setting, that light-cone compatibility of the conformal and projective structures yields Weyl compatibility.

A Weyl structure still contains a scale connection 1-form. In a representative (g,phi), integrability requires the relevant Weyl 1-form to be locally closed, and a global reduction to a single pseudo-Riemannian gauge requires the corresponding global exactness/topological conditions.

The audit includes two finite controls:

```text
phi = d(ax)        -> d phi = 0
phi = x dy         -> d phi = dx wedge dy != 0
```

Hence

\[
\boxed{\text{Weyl compatibility}\not\Rightarrow\text{integrability by itself}.}
\]

An additional physical or geometrical condition is required before the scale connection can be removed in the relevant domain.

---

## 7. DSD selector provenance

The following are not generic-DSD outputs in this audit:

```text
observed light-ray family
observed free-fall worldline family
smooth-manifold regularity assumptions
torsion-free affine connection model
projective-equivalence rule
conformal-equivalence rule
light-cone compatibility assumption
clock / scale-integrability condition
Einstein field equation
```

DSD can type, separate, compare, and audit these records, but the names of DSD channels/properties/lineages do not turn them into empirical light rays, free-fall geodesics, or a gravitational field equation.

This follows the same provenance rule used in the quantum reconstruction track: a supplied selector remains supplied even when a standard theorem successfully reconstructs a target structure from it.

---

## 8. Comparator caveat

The gate records two external facts simultaneously rather than forcing one to erase the other.

First, Matveev–Scholz (2020) provide a rigorous proof of the EPS light-cone compatibility conjecture in their stated setting.

Second, Wheeler (2025) argues that a wider class of connections/reparameterizations and the full conformal symmetry representation leave additional freedom, and that the original EPS route contains substantive restrictions.

Therefore the audit uses this conservative classification:

```text
EPS / Matveev-Scholz route:
  VALID CONDITIONAL COMPARATOR under its explicit hypotheses

claim that observed paths alone uniquely force the full physical geometry:
  NOT ESTABLISHED here

claim that generic DSD derives those comparator hypotheses:
  REJECTED
```

This distinction is important for preventing a successful reconstruction theorem from becoming circular evidence for DSD.

---

## 9. Deterministic regression result

Run from repository root:

```bash
python audits/science/2026-09-10_rel_extension_002_causal_projective_metric_recovery_gate.py --mode all
```

Observed result:

```text
CONFORMAL_LIGHT_CONE: PASS
PROJECTIVE_FREE_FALL: PASS
CONFORMAL_PROJECTIVE_COMPATIBILITY: PASS
WEYL_INTEGRABILITY: PASS
SELECTOR_PROVENANCE: PASS
COMPARATOR_SCOPE: PASS
TOTAL: 43/43 checks passed
OVERALL: PASS_WITH_BOUNDARY
```

The Python checks are finite algebraic/logical witnesses. They do not constitute a new proof of the full EPS reconstruction theorem and do not empirically test general relativity.

---

## 10. Verdict

**PASS_WITH_BOUNDARY**.

The selector ladder is viable as a conditional reconstruction framework:

\[
\text{light-ray data}
\leadsto
\text{conformal information},
\]

\[
\text{free-fall paths}
\leadsto
\text{projective information},
\]

and, under explicit compatibility and regularity hypotheses,

\[
(\mathscr C,\mathscr P)
\leadsto
\text{Weyl-compatible geometry}.
\]

But the provenance remains:

\[
\boxed{
\text{conditional recovery from supplied selectors}
\neq
\text{generic-DSD derivation of physical spacetime geometry}.
}
\]

Metric scale, global pseudo-Riemannian reduction, physical spacetime dimension/signature, and Einstein dynamics remain separate questions.

No DSD core-paper contradiction was found at this gate.

---

## 11. External references

- J. Ehlers, F. A. E. Pirani, A. Schild, *The Geometry of Free Fall and Light Propagation* (1972; republication, General Relativity and Gravitation 44, 1587–1609, 2012), DOI: 10.1007/s10714-012-1353-4.
- V. S. Matveev, E. Scholz, *Light cone and Weyl compatibility of conformal and projective structures*, General Relativity and Gravitation 52, 66 (2020), arXiv:2001.01494.
- N. Linnemann, J. Read, *Constructive Axiomatics in Spacetime Physics Part I: Walkthrough to the Ehlers-Pirani-Schild Axiomatisation*, arXiv:2112.14063.
- J. T. Wheeler, *Geometry from geodesics: fine-tuning Ehlers, Pirani, and Schild*, General Relativity and Gravitation 57, 31 (2025), arXiv:2404.03815.

These are external comparators and are not counted as DSD-derived evidence.

---

## 12. Next target

**REL Extension 003 — Clock / Weyl Integrability / Metric-Scale Recovery Gate**.

The next audit should isolate exactly what additional data or assumptions are required to pass from conformal/projective/Weyl structure to a pseudo-Riemannian metric scale usable by physical clocks.

Required separations:

```text
conformal class
Weyl scale connection
closed vs exact Weyl 1-form
local vs global integrability
proper-time scale
standard-clock assumption
second-clock-effect criterion
coordinate units vs physical calibration
metric reconstruction vs Einstein dynamics
```

The goal is not to assume a clock and then claim the metric was independently derived. Every chronometric premise must receive its own provenance label.
