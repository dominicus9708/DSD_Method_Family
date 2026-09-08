# QM Core Reconstruction 005B — Trace Normalization / Instrument Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: separate complete positivity from normalization preservation, derive the trace-preserving / trace-nonincreasing split from a general operational normalization structure where possible, and reconnect QM Core 002 instruments with QM Core 005A composite admissibility.

## 1. Question

QM Core 005A established that positivity, even together with trace preservation, is insufficient for quantum composite dynamics:

\[
\text{positive + TP}\not\Rightarrow\text{CP}.
\]

The present step asks the complementary question:

> Once complete positivity is handled separately, what forces deterministic quantum evolution to preserve trace, while selective measurement branches are only trace non-increasing and their sum is trace preserving?

The main goal is to avoid treating `CPTP` as one indivisible imported label.

## 2. Standard quantum instrument structure

For finite-dimensional Hilbert spaces, a deterministic quantum channel is a completely positive trace-preserving linear map.

A selective quantum operation is completely positive and trace non-increasing.
A finite quantum instrument is a family

\[
\{\mathcal I_i\}_{i=1}^m
\]

of completely positive trace-nonincreasing maps such that

\[
\mathcal E:=\sum_i\mathcal I_i
\]

is trace preserving.

For a normalized input state \(\rho\),

\[
p_i=\operatorname{Tr}\mathcal I_i(\rho)
\]

is the outcome probability, and if \(p_i>0\),

\[
\rho_i'=\frac{\mathcal I_i(\rho)}{p_i}
\]

is the normalized conditional output.

Standard references include Mark M. Wilde, *Quantum Information Theory*, 2nd ed., Sec. 4.6.8, and John Watrous, *The Theory of Quantum Information*, Ch. 2.

## 3. General ordered-carrier normalization theorem

QM Core 004D already produced, conditionally on explicit operational randomization and separating readouts, a finite-dimensional ordered real carrier

\[
(V,V_+,u,\Omega),
\]

where \(V_+\) is the positive cone, \(u\) is the normalization functional, and normalized states satisfy

\[
\Omega=\{x\in V_+:u(x)=1\}.
\]

This permits a normalization theorem that is not specifically quantum.

### Theorem 3.1 — deterministic normalization implies normalization-functional preservation

Let \(D:V\to V\) be a positive linear map and assume

\[
D(\Omega)\subseteq\Omega.
\]

Then for every \(x\in V_+\),

\[
\boxed{u(Dx)=u(x).}
\]

### Proof

If \(x=0\), the result is immediate.
For nonzero \(x\in V_+\), write

\[
x=u(x)\omega,
\qquad
\omega:=x/u(x)\in\Omega.
\]

By linearity and deterministic normalization,

\[
u(Dx)=u(x)u(D\omega)=u(x).
\]

If the positive cone spans \(V\), the equality extends linearly to all of \(V\). QED.

Thus normalization preservation is a general operational consequence of a deterministic positive linear dynamics on an ordered normalized state carrier; it need not be inserted first as a quantum trace formula.

## 4. General branch theorem

Let \(B_1,\ldots,B_m:V\to V\) be positive linear branch maps and suppose

\[
D:=\sum_i B_i
\]

is deterministic in the sense of Theorem 3.1.

For every \(x\in V_+\), positivity gives

\[
u(B_i x)\ge0,
\]

and

\[
\sum_i u(B_i x)
=u(Dx)
=u(x).
\]

Therefore each branch satisfies

\[
\boxed{0\le u(B_i x)\le u(x).}
\]

Hence every branch is normalization-nonincreasing while the branch sum is normalization-preserving.

For a normalized state \(\omega\), define

\[
p_i(\omega):=u(B_i\omega).
\]

Then

\[
p_i\ge0,
\qquad
\sum_i p_i=1.
\]

This is the general operational structure underlying the quantum instrument normalization rule.

## 5. Quantum specialization

Now supply the finite-dimensional complex Hilbert-state representation.
The ordered cone is the positive-semidefinite cone and

\[
u(X)=\operatorname{Tr}X.
\]

Theorem 3.1 becomes

\[
\boxed{
\text{normalized deterministic linear state evolution}
\Longrightarrow
\text{trace preservation}.
}
\]

The branch theorem becomes

\[
\boxed{
\operatorname{Tr}\mathcal I_i(X)\le\operatorname{Tr}X
\quad(X\ge0)
}
\]

and

\[
\boxed{
\sum_i\mathcal I_i\text{ is trace preserving}.
}
\]

Combining this with QM Core 005A's ancilla-compatible complete-positivity requirement gives the standard split:

```text
deterministic branch sum    -> CPTP
selective branch            -> CPTNI
```

The normalization part therefore has a more general operational derivation than the CP part.

## 6. Direct trace proof

The Hilbert-space statement can also be proved without referring to the ordered-carrier notation.

Let \(\Phi\) be linear and assume

\[
\operatorname{Tr}\Phi(\rho)=1
\]

for every density operator \(\rho\).
For nonzero \(X\ge0\), write

\[
X=(\operatorname{Tr}X)\rho,
\qquad
\rho=X/\operatorname{Tr}X.
\]

Then

\[
\operatorname{Tr}\Phi(X)
=(\operatorname{Tr}X)\operatorname{Tr}\Phi(\rho)
=\operatorname{Tr}X.
\]

By linear decomposition this extends to all operators.
Thus deterministic normalized-state evolution forces trace preservation once linearity and the trace normalization representation are supplied.

## 7. Kraus normalization criterion

For a CP map

\[
\mathcal I(X)=\sum_\alpha K_\alpha X K_\alpha^\dagger,
\]

let

\[
A:=\sum_\alpha K_\alpha^\dagger K_\alpha.
\]

Then

\[
\operatorname{Tr}\mathcal I(X)
=\operatorname{Tr}(XA).
\]

Therefore

\[
\boxed{
\mathcal I\text{ is trace non-increasing}
\iff
A\le I,
}
\]

while

\[
\boxed{
\mathcal I\text{ is trace preserving}
\iff
A=I.
}
\]

For an instrument with Kraus families \(K_{i\alpha}\),

\[
\boxed{
\sum_{i,\alpha}K_{i\alpha}^\dagger K_{i\alpha}=I
}
\]

is the deterministic normalization condition.

## 8. Zero-probability branch and DSD status discipline

Let

\[
\tau_i:=\mathcal I_i(\rho)\ge0,
\qquad
p_i:=\operatorname{Tr}\tau_i.
\]

If

\[
p_i=0,
\]

positivity implies that all eigenvalues of \(\tau_i\) are nonnegative and sum to zero, so

\[
\boxed{\tau_i=0.}
\]

The branch output is therefore a **defined zero positive operator**.
However

\[
\rho_i'=\tau_i/p_i
\]

is undefined because division by zero is not permitted.

This exactly preserves the distinction already emphasized in the DSD Formation / Property / Dynamics layers between defined zero and undefinedness.
The quantum specialization should therefore record

```text
branch output tau_i = 0       DEFINED_ZERO
branch probability p_i = 0    DEFINED_ZERO
conditional normalized state  UNDEFINED
```

rather than replacing the undefined conditional state with a numerical zero matrix.

## 9. Relation to QM Core 002

QM Core 002 used

\[
\tau_i=\mathcal I_i(\rho),
\quad
p_i=\operatorname{Tr}\tau_i,
\quad
\rho_i'=\tau_i/p_i\;(p_i>0),
\quad
\rho'=\sum_i\tau_i.
\]

The present gate now supplies the normalization logic beneath that structure:

1. branch positivity/CP gives admissible subnormalized branch states;
2. deterministic branch aggregation gives total normalization;
3. branch weights are the normalization functional applied to subnormalized records;
4. each branch is automatically non-increasing because all branch weights are nonnegative and sum to the input normalization;
5. a zero branch remains a defined zero record while normalized conditioning is undefined.

Thus QM Core 002 and QM Core 005A are connected through a single branch-resolved dynamics interface rather than two unrelated imported formulas.

## 10. What DSD does and does not supply

The DSD source layers support the following pre-existing distinctions:

```text
complete instantaneous-state admissibility
supplied constitutive/dynamic laws
defined zero versus undefined status
finite downstream aggregation without automatic physical normalization
```

They do **not** by themselves supply:

```text
Hilbert trace as normalization functional
quantum positive cone
complete positivity
Kraus representation
quantum instrument semantics
```

The static aggregation layer's finite sums are therefore not identified with probability normalization merely because both use addition. The quantum branch normalization rule enters only after the explicit ordered-state / Hilbert-state specialization.

## 11. Provenance

Conservative classification:

```text
DSD status separation: defined zero vs undefined                 A  PRE_EXISTING_DSD
DSD dynamic slice admissibility / supplied law discipline       A  PRE_EXISTING_DSD
ordered-carrier normalization functional from 004D              B  GENERAL_OPERATIONAL_DERIVATION
Theorem 3.1 deterministic normalization preservation            B  GENERAL_OPERATIONAL_RESULT
positive branch-sum theorem                                     B  GENERAL_OPERATIONAL_RESULT
Hilbert trace representation                                    SUPPLIED / C
complete positivity / ACE-QM                                    C + conditional standard result from 005A
quantum instrument interpretation                               C  TARGET_SPECIALIZATION
CPTP/CPTNI conclusion                                           CONDITIONAL COMBINATION
```

This is stronger than simply importing `CPTP` as a primitive label: the normalization half of the standard quantum dynamics condition is recoverable from a more general operational structure.

It is not an independent DSD derivation of complete quantum dynamics because the CP/Hilbert/composite ingredients remain target-specific or supplied.

## 12. Reproducibility witness

```bash
python audits/science/2026-09-08_qm_core_005b_trace_normalization_instrument_gate.py --mode all
```

The exact finite witness uses a two-outcome projective instrument on

\[
\rho=
\begin{pmatrix}
3/4&1/4\\
1/4&1/4
\end{pmatrix}.
\]

It verifies branch traces \(3/4\) and \(1/4\), their unit sum, the trace-preserving nonselective map, a CP trace-decreasing nondeterministic control, a CP trace-increasing invalid branch control, and a zero-probability branch.

## 13. Verdict

**PASS_WITH_REFINEMENT**

The trace-preserving / trace-nonincreasing split can be decomposed cleanly from complete positivity. On a general ordered normalized carrier, deterministic positive linear evolution preserves the normalization functional, while positive selective branches whose sum is deterministic are automatically normalization non-increasing. In the supplied Hilbert specialization this becomes TP/TNI; combined with the CP requirement isolated in QM Core 005A, it yields the standard CPTP/CPTNI channel-and-instrument structure. The zero-probability branch also reproduces the pre-existing DSD defined-zero/undefined distinction exactly.

Next target: **QM Core 005C — reversible-channel / unitary gate**, testing whether reversible CPTP dynamics with a CPTP inverse forces unitary conjugation, and separating that theorem from the stronger claim that every continuous DSD evolution must be unitary.
