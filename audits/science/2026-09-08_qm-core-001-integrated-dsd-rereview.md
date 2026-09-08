# QM Core Reconstruction 001R — Integrated Four-Layer DSD Re-review

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Supersedes: the *integration verdict* of `2026-09-08_qm-core-descriptive-factorization-reconstruction-audit.md`; the earlier audit is retained as historical evidence.

## 1. Changed review premise

This re-review deliberately removes paper-local scope defenses as global DSD prohibitions.

The four DSD papers are treated as one layered theory:

```text
Formation Axiom System
-> Property Axiom System
-> Channel-Indexed Static Aggregation
-> Structural Reorganization Dynamics
```

A sentence such as "the present paper is static" or "this layer does not derive a constitutive law" is interpreted as a scope statement about that manuscript, not as a theorem that DSD as a whole may never connect the layers.

The remaining hard gates are:

```text
type consistency
logical consistency across the four layers
mathematical well-definedness
agreement with locked standard-QM predictions
```

## 2. Why the first audit was too conservative

The first QM Core 001 audit used a flattened record

\[
\mathfrak Q
=
(\mathcal S,\mathcal F,\mathcal A,\mathcal M,\Gamma,\Phi)
\]

and correctly proved the prediction identity

\[
\Phi_F\circ\mathcal E
=
\Phi_{\mathcal E^*(F)}.
\]

However, it described the quantum primitives mainly as external objects "organized by DSD roles."

Under the present integrated-DSD premise, that description underuses the four-paper architecture.

The stronger question is:

> Can the quantum specialization be placed inside the actual DSD dependency chain so that Formation, Property, Static Aggregation, and Dynamics each do nonredundant work?

The answer for the tested finite-dimensional prediction core is yes.

## 3. Source-derived cross-paper constraints

### 3.1 Formation identity

In the Formation Axiom System, an admitted channel has typed identity

\[
c=(p,a,\lambda,v,\rho_{\rm role}),
\]

and the assigned value \(v\) is part of channel identity.

Therefore if a time-varying Born probability \(p_i(t)\) were placed directly in the Stage-VI assigned-value coordinate, changing the probability would change inherited channel identity.

### 3.2 Property layer

The Property Axiom System permits:

```text
typed profiles
applicability
contextual prerequisites
partial assignments
auxiliary carriers
downstream representations
```

and explicitly sits between Stage-VI formation and later aggregation/dynamics.

This makes quantum state, effect, and Born-pair records natural candidates for a quantum property specialization.

### 3.3 Static aggregation

The static paper permits selected defined property records to be sent through an explicit typed bridge into a Banach output and finitely aggregated.

The output may be vector-valued, and equality of aggregate values need not reconstruct the typed support.

### 3.4 Dynamics

Structural Reorganization Dynamics permits time-indexed Property slices and time-dependent downstream coordinates over a fixed Stage-VI formation background.

Each time slice used by the static interface must remain a valid static slice.

This gives a direct route for ordinary quantum evolution without forcing every changing quantum number into formation-channel identity.

## 4. Integrated DSD quantum specialization

Fix a finite-dimensional complex Hilbert carrier \(\mathcal H\) for the present specialization.

Define a layered record schematically by

\[
\boxed{
\mathfrak Q_{\rm DSD}(t)
=
\left(
F_L^{\le6},
P_Q(t),
\Theta_{\mathcal M},
S_Q(t),
\Gamma_Q
\right).
}
\]

The components have different DSD roles.

### 4.1 Formation layer — stable experiment/protocol support

Use \(F_L^{\le6}\) to retain the identity of the admitted system, preparation/measurement configuration, outcome channel, quantity kind, and role.

For a regular dynamical run, routine variation of \(\rho_t\) or \(p_i(t)\) should not be hidden inside the inherited Stage-VI value coordinate unless one intentionally wants a formation-level transition and lineage update.

### 4.2 Property layer — quantum state/effect/Born records

A convenient quantum specialization may declare property kinds such as

```text
QSTATE:
    preparation/system -> density-operator carrier

QEFFECT:
    (measurement, outcome) -> effect carrier

QBORN:
    (state-record, effect-record) -> [0,1]
```

with prerequisites enforcing the declared Hilbert carrier and measurement compatibility.

The standard finite-dimensional specialization supplies

\[
\rho\ge0,\qquad \operatorname{Tr}\rho=1,
\]

\[
0\le E_i\le I,
\]

and

\[
\Xi_{\rm QBORN}(\rho,E_i)
=
\operatorname{Tr}(\rho E_i).
\]

At this stage the Born pairing is a typed property assignment, not a Stage-VI channel identity coordinate.

## 5. Born measurement as a DSD static aggregate

For a finite POVM

\[
\mathcal M=\{E_1,\ldots,E_m\},
\qquad
\sum_iE_i=I,
\]

let the defined Born property records be

\[
r_i=(\mathrm{QBORN},(\rho,E_i),p_i),
\qquad
p_i=\operatorname{Tr}(\rho E_i).
\]

Take the output space

\[
U_{\mathcal M}=\mathbb R^m
\]

and the explicit bridge

\[
\Theta_{\mathcal M}(r_i)=p_i e_i.
\]

Then the property-side static aggregate is

\[
\boxed{
\operatorname{Agg}^{\Theta_{\mathcal M}}(G_{\mathcal M})
=
\sum_{i=1}^m p_i e_i
=
(p_1,\ldots,p_m).
}
\]

Thus the ordinary Born probability vector is an exact finite DSD static aggregate of typed property records.

Normalization,

\[
\sum_i p_i=1,
\]

comes from the quantum specialization

\[
\sum_iE_i=I,\qquad \operatorname{Tr}\rho=1,
\]

not from finite aggregation alone.

This is important: DSD supplies the typed aggregation architecture; the quantum specialization supplies the quantum relation that makes the resulting vector a probability distribution.

## 6. Dynamic quantum slice

Let a supplied CPTP channel act on the state property:

\[
\rho_{t'}
=
\mathcal E(\rho_t).
\]

Then the DSD dynamic slice changes

\[
P_Q(t)\to P_Q(t')
\]

while the regular Formation protocol may remain fixed.

At each time,

\[
P_Q(t)
\longmapsto
\operatorname{Agg}^{\Theta_{\mathcal M}}(G_{\mathcal M}(t))
=
\left(
\operatorname{Tr}[\rho_tE_i]
\right)_i.
\]

This realizes the cross-paper chain

\[
\boxed{
F_L^{\le6}
\to
P_Q(t)
\to
\operatorname{Agg}^{\Theta_{\mathcal M}}(P_Q(t))
\quad
\text{with}
\quad
P_Q(t)\xrightarrow{\Gamma_Q}P_Q(t').
}
\]

The static aggregate is therefore a time-slice readout of the dynamic Property state, rather than a replacement for that state.

## 7. Schrödinger/Heisenberg factorization inside the integrated chain

For a channel \(\mathcal E\),

\[
\operatorname{Tr}[\mathcal E(\rho)E_i]
=
\operatorname{Tr}[\rho\,\mathcal E^*(E_i)].
\]

Therefore the same DSD static readout can be obtained by either:

```text
state-side update:
rho -> E(rho), effect fixed

readout-side pullback:
rho fixed, effect -> E*(effect)
```

so

\[
\boxed{
\operatorname{Agg}_{\mathcal M}
\circ
\Gamma_Q
=
\operatorname{Agg}_{\Gamma_Q^*\mathcal M}
}
\]

at the prediction level, with the obvious typed interpretation of the transformed measurement family.

The Schrödinger/Heisenberg distinction is therefore represented as two placements of one supplied quantum transition relative to the DSD dynamic-state / static-readout interface.

## 8. New DSD-specific placement consequence

This is the strongest new conclusion of the re-review.

Because Formation makes assigned value part of operational-channel identity while Dynamics treats ordinary Property evolution over a fixed formation background as regular dynamics,

\[
\boxed{
\text{routine quantum state/probability evolution belongs downstream of stable formation identity}
}
\]

for the natural regular-epoch specialization.

If one instead encodes \(p_i(t)\) as the Stage-VI value coordinate,

\[
c_i(t)
=
(p,a,\lambda,p_i(t),\rho_{\rm role}),
\]

then

\[
p_i(t)\neq p_i(t')
\Longrightarrow
c_i(t)\neq c_i(t'),
\]

and one has a formation-level identity change requiring lineage.

This is not a standard-QM theorem. It is a DSD cross-paper placement constraint generated by combining the four DSD definitions.

It provides a nontrivial answer to the question "what changes when QM is written in DSD rather than merely renamed?"

## 9. Finite witness

The companion script uses a qubit prepared in \(|+\rangle\), a Z-basis POVM, and amplitude damping with

\[
\gamma=\frac14.
\]

Initial static readout:

\[
(0.5,0.5).
\]

After the channel:

\[
(0.625,0.375).
\]

The Formation protocol record is kept fixed while the Property state slice evolves.

The script also verifies:

1. the same probabilities from state-forward and effect-backward channel placement;
2. invariance of the Born readout under joint basis re-expression;
3. that inserting a changing Born probability into the Formation value coordinate changes the Formation channel tuple.

All numerical checks pass.

## 10. Re-review verdict

### 10.1 What is now stronger

The earlier statement

```text
standard QM primitives are supplied externally and organized by DSD roles
```

is too weak for the integrated four-paper reading.

Replace it, for this finite-dimensional specialization, with:

\[
\boxed{
\text{standard quantum primitives instantiate a four-layer DSD specialization
whose layer placement is constrained by DSD identity, property, aggregation,
and dynamic-slice rules.}
}
\]

The quantum prediction core is not merely placed next to DSD.

It is representable as an actual specialization of the DSD dependency chain.

### 10.2 Current statuses

```text
standard finite-dimensional prediction equality:
    PASS

Schrodinger/Heisenberg factorization:
    PASS

Born vector as typed DSD static aggregate:
    PASS

CPTP state evolution as Property-slice dynamics over fixed Formation protocol:
    PASS

four-paper integrated DSD reconstruction:
    PASS_WITH_REFINEMENT

prior flat-record interpretation as the strongest DSD reading:
    SUPERSEDED

Born rule uniquely forced by current DSD axioms:
    NOT_YET_DERIVED

Hilbert-space structure uniquely forced by current DSD axioms:
    NOT_YET_DERIVED

complete positivity uniquely forced by current DSD axioms:
    NOT_YET_DERIVED

new quantum prediction:
    NOT_ESTABLISHED
```

The last three are no longer excluded because a paper said "outside scope."

They are open derivation targets.

If DSD later derives them from cross-paper constraints, the status may be upgraded. If countermodels show several incompatible quantum-like specializations survive the same DSD structure, then they remain constitutive specialization axioms.

## 11. Identity of the program

This re-review supports the stronger programmatic interpretation:

\[
\boxed{
\mathrm{DSD}
=
\text{Formation}
+
\text{Property}
+
\text{Static Aggregation}
+
\text{Structural Reorganization Dynamics}
}
\]

as one layered theory, with quantum mechanics tested as a full specialization rather than as an external example attached to one paper.

The correct next target is therefore not merely another "interface comparison."

It is:

```text
QM Core 002
quantum instrument / outcome-conditioned state transition
```

with the explicit goal of reconstructing measurement probability, conditioned transition, unconditioned channel, disturbance, and repeatability inside the same four-layer DSD specialization.
