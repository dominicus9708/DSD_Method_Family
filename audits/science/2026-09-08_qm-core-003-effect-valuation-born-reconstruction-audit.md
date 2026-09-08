# QM Core Reconstruction 003 — Effect-Valuation / Born-Rule Reconstruction Pressure Test

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: **whether the Born trace rule remains primitive once the integrated DSD Formation / Property / Static Aggregation / Dynamics architecture is combined with a supplied finite-dimensional Hilbert-effect carrier**

## 1. Research question

QM Core 001 reconstructed the state–transition–readout factorization.
QM Core 002 reconstructed quantum instruments as branch-resolved DSD measurement objects.
QM Core 002B showed that a DSD quantum describability-difference scalar by itself is not sufficient to control objective probability; a property-complete descriptor such as distance/purity/effect-norm is required.

The present step asks the more aggressive question:

> If DSD is allowed to use its full four-layer structure, can the Born probability rule be moved from an externally supplied primitive assignment to a derived representation theorem?

The paper-local scope defenses are not treated as global prohibitions.

The hard gates are:

```text
type consistency across the four DSD layers
mathematical well-definedness
exact agreement with standard finite-dimensional quantum probability
clear identification of every still-supplied quantum primitive
```

## 2. Supplied quantum carrier

Fix a finite-dimensional complex Hilbert space \(\mathcal H\).

Let

\[
\mathrm{Eff}(\mathcal H)
=
\{E:0\le E\le I\}
\]

be the quantum effect carrier.

A finite measurement context is a finite POVM

\[
\mathcal M=\{E_1,\ldots,E_n\},
\qquad
\sum_i E_i=I.
\]

At this step the Hilbert/effect carrier is still supplied.
The purpose is to determine whether the probability pairing itself must still be supplied independently.

## 3. DSD probability specialization before choosing a density operator

For a DSD state record \(s\), define a typed effect-valuation property

\[
\omega_s:\mathrm{Eff}(\mathcal H)\to[0,1].
\]

The intended DSD placement is:

```text
Formation
    stable system / measurement-context / effect / outcome identity

Property
    typed state-effect valuation record
    QWEIGHT(state,effect) -> [0,1]

Static Aggregation
    context normalization over every admitted finite POVM

Cross-context gluing
    the same admitted effect identity has the same QWEIGHT
    in every POVM context in which it occurs

Dynamics
    transports the state valuation or, dually, the effect readout
```

This does not yet assume

\[
\omega_s(E)=\operatorname{Tr}(\rho E).
\]

## 4. DSD effect-gluing and context-normalization conditions

For every admitted finite POVM context

\[
\mathcal M=\{E_i\}_{i=1}^n,
\qquad
\sum_iE_i=I,
\]

require the property-side finite aggregate to satisfy

\[
\boxed{
\sum_i\omega_s(E_i)=1.
}
\]

Also require an explicit cross-context identity/gluing rule:

\[
\boxed{
E\text{ is the same admitted effect in }\mathcal M,\mathcal N
\Longrightarrow
\omega_s(E|\mathcal M)=\omega_s(E|\mathcal N).
}
\]

This is probability-value context independence for the same operational effect.
It is not a deterministic hidden-variable value assignment and is not identified with the stronger noncontextuality assumptions excluded by Kochen–Specker arguments.

## 5. Coarse-graining additivity follows

Let \(E,F\in\mathrm{Eff}(\mathcal H)\) with

\[
E+F\le I.
\]

Define

\[
R=I-E-F.
\]

Then both

\[
\{E,F,R\}
\]

and

\[
\{E+F,R\}
\]

are admissible finite POVMs.

Context normalization gives

\[
\omega_s(E)+\omega_s(F)+\omega_s(R)=1
\]

and

\[
\omega_s(E+F)+\omega_s(R)=1.
\]

Because the same effect \(R\) has the same value in both contexts by the gluing rule,

\[
\boxed{
\omega_s(E+F)=\omega_s(E)+\omega_s(F).
}
\]

Hence finite coarse-graining additivity is not an independent probability postulate once the DSD specialization contains:

```text
effect identity across contexts
+
normalized finite context aggregation.
```

The same reasoning yields

\[
\omega_s(0)=0,
\qquad
\omega_s(I)=1.
\]

## 6. Conditional Born-representation theorem

### Theorem 6.1 — DSD effect-valuation representation theorem

Fix a finite-dimensional complex Hilbert effect carrier \(\mathrm{Eff}(\mathcal H)\).
Suppose a DSD state record \(s\) supplies a globally applicable effect valuation

\[
\omega_s:\mathrm{Eff}(\mathcal H)\to[0,1]
\]

such that:

1. the same effect identity is glued across every admitted measurement context;
2. every finite POVM context has normalized DSD aggregate
   \[
   \sum_i\omega_s(E_i)=1.
   \]

Then the valuation is additive on coexistent effects.
By the generalized Gleason/Busch effect-valuation theorem, there exists a unique density operator \(\rho_s\) such that

\[
\boxed{
\omega_s(E)=\operatorname{Tr}(\rho_sE)
\qquad
\forall E\in\mathrm{Eff}(\mathcal H).
}
\]

Therefore, within this supplied Hilbert-effect specialization,

\[
\boxed{
\text{normalized context aggregation}
+
\text{effect gluing}
\Longrightarrow
\text{Born trace representation}.
}
\]

### Status of the theorem

The implication from DSD context normalization/gluing to finite additivity is proved directly above.

The representation of every normalized additive effect valuation by a density operator is a standard external mathematical theorem, not a new DSD theorem.
The relevant generalized result applies also to two-dimensional Hilbert spaces, unlike the original projection-only Gleason theorem.

Standard references:

- P. Busch, *Quantum states and generalized observables: a simple proof of Gleason's theorem*, arXiv:quant-ph/9909073.
- V. J. Wright and S. Weigert, *Gleason-Type Theorems from Cauchy's Functional Equation*, Foundations of Physics 49, 594–606 (2019).

## 7. Consequence for the status of QBORN

QM Core 001R treated

\[
\Xi_{\mathrm{QBORN}}(\rho,E)=\operatorname{Tr}(\rho E)
\]

as a supplied quantum specialization.

The present result permits a stronger placement.

Instead declare

```text
QWEIGHT:
    (state-record, effect-record) -> [0,1]
```

together with the DSD context-normalization and effect-gluing requirements.

Then, on a supplied full Hilbert-effect carrier,

\[
\boxed{
\mathrm{QBORN}
}
\]

need not remain an independent probability formula.
It is the unique density-operator representation of the admissible effect valuation.

Thus the probability rule is demoted from

```text
supplied numerical pairing
```

to

```text
derived representation
```

inside this specialization.

The Hilbert-effect carrier itself remains supplied.

## 8. Pure-projective sector and QM Core 002B

For pure state and pure target effect,

\[
\rho=P_\psi=|\psi\rangle\langle\psi|,
\qquad
E=P_\phi=|\phi\rangle\langle\phi|,
\]

the representation theorem yields

\[
p_\phi
=
\operatorname{Tr}(P_\psi P_\phi)
=
|\langle\phi|\psi\rangle|^2.
\]

For the QM Core 002B Hilbert–Schmidt difference,

\[
D_Q^2
=
\operatorname{Tr}[(P_\psi-P_\phi)^2],
\]

one has

\[
D_Q^2
=
2-2p_\phi,
\]

hence

\[
\boxed{
p_\phi=1-\frac12D_Q^2.
}
\]

Therefore the earlier pure-projective "describability difference versus probability" relation is not merely heuristic once the effect-valuation representation is fixed.

It is a derived identity in the pure-projective sector.

For mixed states and general effects the richer 002B identity remains necessary:

\[
2p_E
=
\operatorname{Tr}(\rho^2)
+
\operatorname{Tr}(E^2)
-
\|\rho-E\|_{\mathrm{HS}}^2.
\]

Thus distance alone is sufficient only on a constrained property stratum such as fixed purity and fixed effect norm.

## 9. No-free-probability-lift corollary

Suppose one proposes a DSD-modified probability law

\[
\widetilde\omega_s(E)
=
\operatorname{Tr}(\rho E)+g_s(E).
\]

If \(\widetilde\omega_s\) still satisfies all of:

```text
same full Hilbert-effect carrier
same cross-context effect identity
[0,1]-valued effect assignment
normalization on every finite POVM
coarse-graining consistency
```

then Theorem 6.1 applies again.

Therefore there exists another density operator \(\widetilde\rho_s\) such that

\[
\boxed{
\widetilde\omega_s(E)
=
\operatorname{Tr}(\widetilde\rho_sE).
}
\]

Hence an admissible probability "lift" that preserves the full structure is not a new extra probability scalar.
It is absorbed into a changed state representation.

Accordingly,

\[
\boxed{
\text{objective probability increase under the standard effect structure}
}
\]

must occur through at least one of:

```text
state change
effect / measurement change
instrument / dynamics change
```

rather than by attaching a free additional DSD bonus to a fixed \((\rho,E)\).

A genuinely new probability law with fixed state/effect representation would have to violate or replace at least one current assumption, for example:

```text
full Hilbert-effect carrier
cross-context effect gluing
POVM normalization / coarse-graining additivity
standard state-effect representation
```

Such a violation would be a new-physics claim and would require independent empirical evidence.

## 10. Finite exact witness: context-normalized nonlinear rule fails gluing

Take

\[
\rho=\operatorname{diag}(3/4,1/4).
\]

Compare the fine POVM

\[
E_1=\frac12P_0,
\qquad
E_2=\frac12P_0,
\qquad
E_3=P_1
\]

with the coarse POVM

\[
\{P_0,P_1\}.
\]

Born valuation gives

\[
\left(\frac38,\frac38,\frac14\right)
\]

for the fine context, so

\[
\omega(E_1)+\omega(E_2)=\frac34=\omega(P_0).
\]

Now define a nonlinear per-context rule by squaring Born weights and renormalizing inside each context.

The fine context gives

\[
\left(\frac9{22},\frac9{22},\frac2{11}\right),
\]

so the refined \(P_0\) total is

\[
\frac9{11}.
\]

The coarse context gives

\[
\left(\frac9{10},\frac1{10}\right),
\]

so the same \(P_0\) receives value

\[
\frac9{10}.
\]

Thus

\[
\boxed{
\frac9{11}\ne\frac9{10}.
}
\]

The nonlinear rule normalizes separately inside each measurement context but fails cross-context effect gluing.

This explicitly demonstrates that

\[
\boxed{
\text{context normalization alone}
\not\Rightarrow
\text{Born representation}.
}
\]

The effect-identity/gluing requirement is substantive.

## 11. Finite qubit reconstruction witness

For the qubit Bloch vector

\[
r=\left(\frac13,-\frac14,\frac12\right),
\]

the three positive Pauli effects

\[
P_x^+,
\quad P_y^+,
\quad P_z^+
\]

receive values

\[
\omega(P_x^+)=\frac23,
\qquad
\omega(P_y^+)=\frac38,
\qquad
\omega(P_z^+)=\frac34.
\]

The values reconstruct

\[
r_x=2\omega(P_x^+)-1=\frac13,
\]

\[
r_y=2\omega(P_y^+)-1=-\frac14,
\]

\[
r_z=2\omega(P_z^+)-1=\frac12.
\]

The Bloch norm is approximately

\[
0.650854<1,
\]

so the reconstructed density operator is positive.

This is only a finite tomography witness.
The universal representation theorem is the external Busch/Gleason-type theorem.

## 12. Relation to the four DSD layers

The four layers now perform distinct functions.

```text
Formation
    identifies system, measurement context, effect and outcome records;
    provides the stable identity needed for cross-context gluing.

Property
    carries QWEIGHT as a typed state-effect valuation;
    retains applicability and status information.

Static Aggregation
    aggregates every finite measurement context;
    normalized aggregate = 1;
    comparison of coarse/fine contexts produces effect additivity.

Dynamics
    changes the state/effect/instrument when objective probabilities change;
    the 001 Schrödinger/Heisenberg duality remains the dynamic compatibility rule.
```

The Formation and Static layers therefore contribute directly to the Born reconstruction pressure test rather than serving as passive wrappers.

## 13. Main conceptual result

The strongest justified statement from QM Core 003 is

\[
\boxed{
\text{DSD does not yet derive Hilbert quantum structure,}
}
\]

but

\[
\boxed{
\text{once the Hilbert effect carrier is admitted,}
\quad
\text{DSD-style context identity + normalized aggregation}
\quad
\text{are strong enough to force the standard Born representation.}
}
\]

This is substantially stronger than merely inserting an already-known Born formula into a DSD property slot.

It identifies exactly where the remaining quantum primitive now resides:

\[
\boxed{
\text{the unresolved target is the Hilbert/effect geometry itself, not the trace probability pairing.}
}
\]

## 14. Verdict

### Standard mathematical result

**PASS**

The generalized effect-valuation representation theorem is standard and applies to the supplied finite-dimensional Hilbert-effect specialization, including qubits.

### Integrated DSD reconstruction

\[
\boxed{\textbf{PASS\_WITH\_REFINEMENT}}
\]

Refinements established:

1. `QWEIGHT` plus context normalization/gluing is more primitive than directly supplying `QBORN`;
2. effect additivity is derived by comparing coarse and refined measurement contexts;
3. the Born trace rule becomes a representation theorem once the full Hilbert-effect carrier is supplied;
4. a nonlinear context-normalized alternative can fail DSD cross-context gluing;
5. an extra DSD probability lift that preserves the full effect-valuation structure is absorbed into a changed density state rather than becoming an independent probability bonus;
6. QM Core 002B distance-control remains valid as a derived geometric control relation, but distance alone is not the universal probability primitive.

## 15. Reproducibility

Python:

```text
audits/science/2026-09-08_qm_core_003_effect_valuation_born_reconstruction.py
```

Run from repository root:

```bash
python audits/science/2026-09-08_qm_core_003_effect_valuation_born_reconstruction.py --mode all
```

The script uses the Python standard library only.

Expected summary:

```text
Born coarse-graining consistency           PASS
nonlinear context-rule gluing obstruction  PASS
qubit valuation tomography                 PASS
additive probability lift as state shift   PASS

OVERALL: PASS_WITH_REFINEMENT
```

## 16. Next aggressive target

The remaining core obstacle has moved.

The next question is no longer simply

```text
why the Born trace rule?
```

but

```text
why is the admissible state/effect carrier Hilbertian?
```

The next reconstruction gate should therefore pressure-test:

```text
QM Core 004
Hilbert/effect geometry from DSD formation,
boundedness, distinguishability, composition,
and reconstruction requirements.
```

Possible outcomes must be separated:

```text
Hilbert geometry derivable;
Hilbert geometry sharply constrained but not unique;
additional quantum axiom still required;
counterexample family survives.
```
