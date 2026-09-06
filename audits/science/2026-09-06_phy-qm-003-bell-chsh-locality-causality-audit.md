# PHY-QM-003 — Bell–CHSH locality, entanglement, and causal-support separation

Date: 2026-09-06
Status: PASS_WITH_BOUNDARY
Case origin: standard quantum-mechanical finite witness + synthetic no-signalling control

## 1. DSD interface lock

```text
FORMATION_LAYER: not materially used
PROPERTY_CORE: used for typed state / measurement-context records
STATIC_AGGREGATION_LAYER: used for readout/fiber and reconstruction audit
DYNAMICS_LAYER: used only to compare with causal-support / c_info semantics
REALIZED_AXIS_SPECIALIZATION: not supplied
OTHER_SPECIALIZATION: two-qubit Hilbert tensor-product + Born-rule measurement bridge
```

The quantum Hilbert structure, tensor-product decomposition, observables, Born rule, Bell-local factorization, and no-signalling conditions are external domain structures. They are not derived from the DSD core.

## 2. Bell scenario

Inputs:

```text
x,y ∈ {0,1}
a,b ∈ {−1,+1}
```

A conditional behavior is

```text
P(a,b|x,y).
```

Define correlators

```text
E_xy = Σ_{a,b} a b P(a,b|x,y)
```

and CHSH score

```text
S = E_00 + E_01 + E_10 − E_11.
```

## 3. Bell-local completion

Under a Bell-local hidden-variable model with measurement independence,

```text
P(a,b|x,y) = ∫ dλ q(λ) P(a|x,λ) P(b|y,λ).
```

The deterministic extreme points are specified by four signs

```text
(A0,A1,B0,B1) ∈ {−1,+1}^4.
```

For every one of the 16 deterministic strategies,

```text
S = A0B0 + A0B1 + A1B0 − A1B1 ∈ {−2,+2}.
```

Exhaustive count:

```text
S = −2 : 8 strategies
S = +2 : 8 strategies
```

Hence convex mixtures satisfy

```text
|S| ≤ 2.
```

DSD interpretation: this is a global Bell-local/factorizable completion constraint, not merely a statement that each local measurement result is defined.

## 4. Quantum witness

Use

```text
|Φ+> = (|00>+|11>)/sqrt(2)
A0 = Z
A1 = X
B0 = (Z+X)/sqrt(2)
B1 = (Z−X)/sqrt(2)
```

The Born-rule bridge gives

```text
E = [[ 1/sqrt(2),  1/sqrt(2)],
     [ 1/sqrt(2), -1/sqrt(2)]]
```

so

```text
S_QM = 2 sqrt(2) ≈ 2.82842712474619.
```

This violates the Bell-local bound while remaining within the standard Tsirelson bound.

The local expectations vanish:

```text
<A0>=<A1>=<B0>=<B1>=0.
```

The corresponding joint probabilities are

```text
P(a,b|x,y)=1/4[1+a b E_xy]
```

for this unbiased witness. For a positive correlation E_xy=1/sqrt(2),

```text
P(same sign) per same-sign outcome     = 0.4267766952966369
P(opposite sign) per opposite outcome = 0.0732233047033631
```

## 5. Operational no-signalling audit

The quantum table satisfies

```text
Σ_b P(a,b|x,0) = Σ_b P(a,b|x,1) = 1/2
Σ_a P(a,b|0,y) = Σ_a P(a,b|1,y) = 1/2.
```

Therefore the remote measurement choice does not change the local outcome distribution in this witness.

Audit boundary:

```text
Bell-local factorization != operational no-signalling.
```

A CHSH violation excludes the stated Bell-local completion assumptions; it does not by itself establish superluminal controllable information transmission.

## 6. PR-box separation control

Use the standard no-signalling box with bit outputs α,β and

```text
α XOR β = x y
```

with the two satisfying output pairs equiprobable. In ±1 notation its correlations are

```text
E_PR = [[+1,+1],[+1,−1]]
```

and

```text
S_PR = 4.
```

Its local marginals are still uniform and independent of the remote input.

Thus the finite witness separates three domains:

```text
Bell-local bound     : |S| ≤ 2
quantum bound        : |S| ≤ 2 sqrt(2)
no-signalling algebraic witness : |S| = 4 achievable by PR box
```

The numerical bounds are external quantum/information-theoretic results, not DSD-derived constants.

## 7. DSD causal-support boundary

Structural Reorganization Dynamics defines finite propagation only after localization, metric/time, evolution, and representation assumptions are supplied. Its c_info is a dynamical support bound.

The static no-signalling equations above are weaker and conceptually different:

```text
NO_SIGNALLING_TABLE
  = remote setting does not change local marginal statistics

DSD_CAUSAL_SUPPORT_BOUND
  = a declared perturbation/distinguishability support cannot propagate faster than c_info
```

Therefore:

```text
no-signalling table does not derive c_info,
c_info is not Bell-local factorization,
CHSH violation does not imply violation of c_info.
```

A future DSD quantum-relativistic specialization must keep these ledgers separate.

## 8. Local readout fiber and information loss

Any (2,2,2) no-signalling behavior can be parameterized by

```text
(A0,A1,B0,B1,C00,C01,C10,C11)
```

through

```text
P(a,b|x,y)=1/4[1+a A_x+b B_y+a b C_xy]
```

subject to positivity.

The local-marginal readout

```text
M(P)=(A0,A1,B0,B1)
```

has rank 4 in this 8-parameter affine representation, leaving a 4-dimensional correlation fiber.

Hence equal local marginal data do not reconstruct the joint correlation structure.

The CHSH summary is one scalar linear functional on the four correlation coordinates,

```text
S(C)=C00+C01+C10−C11.
```

Thus its kernel in correlation space has dimension 3. Even local marginals plus the single CHSH number leave a 3-dimensional information-loss sector in the 8-parameter no-signalling representation.

This is a direct instance of the DSD static-aggregation rule that aggregate equality does not reconstruct full typed/support structure without injectivity.

## 9. Main DSD result

The Bell witness separates four logically different questions:

```text
LOCAL_RECORD_DEFINABILITY
  Are local typed outcomes/probabilities defined in each measurement context?

GLOBAL_BELL_LOCAL_COMPLETION
  Does one factorized hidden-variable model glue all contexts?

JOINT_CORRELATION_DESCRIBABILITY
  Does the supplied quantum representation determine the full P(a,b|x,y)?

CAUSAL_SIGNAL_SUPPORT
  Can controllable information/perturbation support propagate outside the allowed causal bound?
```

The quantum witness answers these differently:

```text
local records: defined
Bell-local completion: fails for CHSH witness
joint quantum correlations: defined by supplied Hilbert/Born bridge
operational superluminal signalling: absent in the witness
DSD c_info dynamics: not inferred from the static table
```

Therefore the safe DSD statement is

```text
Bell nonlocality != superluminal signalling != DSD causal-support violation.
```

## 10. Relation to previous PHY-QM audits

PHY-QM-001 showed

```text
local context-wise assignment != global noncontextual completion.
```

PHY-QM-002 separated contextuality from entanglement.

PHY-QM-003 now adds

```text
Bell-local factorization != no-signalling != causal propagation bound.
```

This is the first current DSD quantum-interface witness in which the quantum context/entanglement side and the relativity/causal-support side can be placed in one finite comparison without identifying them.

## 11. Verdict

```text
PASS_WITH_BOUNDARY
```

Confirmed within the supplied external quantum specialization:

- deterministic Bell-local strategies give |S|<=2;
- the selected entangled quantum state reaches 2sqrt(2);
- the same quantum table is operationally no-signalling;
- a PR-box control is no-signalling yet reaches S=4;
- local marginal readout loses the 4 correlation coordinates;
- CHSH alone loses three independent correlation directions;
- Bell locality, no-signalling, and DSD c_info must remain distinct concepts.

Not established:

- DSD does not derive the Born rule, Hilbert tensor product, Tsirelson bound, Bell theorem, or relativistic light cone;
- CHSH violation does not prove any DSD-specific dynamical law;
- no-signalling statistics alone do not establish finite-speed propagation dynamics.

## 12. Reproducibility

Script:

```text
audits/science/2026-09-06_bell_chsh_dsd_locality_causality.py
```

Run from repository root:

```bash
python audits/science/2026-09-06_bell_chsh_dsd_locality_causality.py
```

Dependencies:

```text
python >= 3.10
numpy
```

## 13. Next audit target

Use the same (2,2,2) interface to separate:

```text
state entanglement
Bell nonlocality
steering
local tomography / reconstruction
causal support
```

A useful next finite control is a Werner-state sweep, because entanglement can survive in parameter regions where the standard CHSH witness no longer violates the local bound. This tests whether DSD incorrectly equates `entangled`, `Bell-nonlocal`, and `locally unreconstructible` states.
