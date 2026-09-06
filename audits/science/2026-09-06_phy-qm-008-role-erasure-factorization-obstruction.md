# PHY-QM-008 — Role-erasure factorization obstruction

Date: 2026-09-06

## Purpose
Turn the one-way-steering example into an explicit DSD information-loss / factorization counterexample.

## Setup
Let \(\rho=\rho_{AB}(1/2)\) be the Bowles one-way-steering state from PHY-QM-007. Let \(W\) be the subsystem-swap unitary, and define

\[
\rho^{\rm sw}=W\rho W^\dagger.
\]

The swap preserves global unitary invariants:

\[
\operatorname{spec}(\rho^{\rm sw})=\operatorname{spec}(\rho),
\qquad
\operatorname{Tr}[(\rho^{\rm sw})^2]=\operatorname{Tr}(\rho^2),
\]

and preserves entanglement measures that are invariant under subsystem relabeling. The singular values of the correlation tensor are also unchanged because \(T=-I_3/2\) in this example.

Numerically,

\[
\operatorname{Tr}\rho^2=0.47,
\]

and the Frobenius distance between the labeled matrices is

\[
\|\rho-\rho^{\rm sw}\|_F=\frac{1}{2\sqrt2}\approx0.3535533906.
\]

The swap exchanges the local Bloch vectors

\[
(0,0,0.2)\leftrightarrow(0,0,-0.3).
\]

## Directed property
Define the downstream external property

\[
S_{\rm dir}(\rho;U,T,\mathcal M)
\in\{0,1\},
\]

where \(U\) is the untrusted measuring party, \(T\) is the trusted tomographic party, and \(\mathcal M\) is the allowed measurement class.

For projective measurements at \(\alpha=1/2\), the published result gives

\[
S_{\rm dir}(\rho;A,B,{\rm PVM})=1,
\qquad
S_{\rm dir}(\rho;B,A,{\rm PVM})=0.
\]

After swapping the subsystems,

\[
S_{\rm dir}(\rho^{\rm sw};A,B,{\rm PVM})=0,
\qquad
S_{\rm dir}(\rho^{\rm sw};B,A,{\rm PVM})=1.
\]

## Role-erasure map
Let \(E\) be any descriptor that forgets the ordered party roles and retains only swap-invariant global data, for example

\[
E(\rho)=\big(
\operatorname{spec}\rho,
\operatorname{Tr}\rho^2,
\text{negativity},
\operatorname{sv}(T)
\big).
\]

Then

\[
E(\rho)=E(\rho^{\rm sw}),
\]

but for a fixed external label order \(A\to B\),

\[
S_{\rm dir}(\rho;A,B,{\rm PVM})
\ne
S_{\rm dir}(\rho^{\rm sw};A,B,{\rm PVM}).
\]

Therefore no function \(g\) can satisfy

\[
S_{\rm dir}(\cdot;A,B,{\rm PVM})=g\circ E
\]

on a comparison family containing both states.

Equivalently, in DSD factorization language, the information erased by \(E\) is not contained in the kernel of the directed-steering property.

## Audit verdict
- `swap-invariant global summaries reconstruct steering direction`: **REJECT**.
- `entanglement amount or global spectrum determines steering direction`: **REJECT**.
- `ordered role data are reconstructively necessary for this downstream property`: **PASS**.
- `local asymmetry alone is a sufficient steering criterion`: **REJECT**. The unequal marginals are a feature of this witness, not a complete criterion.

## Methodological impact
This gives a concrete quantum example of a general DSD compression obstruction:

\[
\boxed{
\text{structural equality after role-erasing compression}
\not\Rightarrow
\text{equality of a role-sensitive property}.
}
\]

It strengthens the justification for retaining complete ordered typed inputs in the Property Axiom System. No modification of the Property core is required.

## Reproducibility

```bash
python audits/science/2026-09-06_one_way_steering_dsd_role_audit.py
```
