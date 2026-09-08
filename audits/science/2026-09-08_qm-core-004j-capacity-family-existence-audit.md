# QM Core Reconstruction 004J — Capacity-Family Existence Gate

Date: 2026-09-08  
Status: **PASS_WITH_REFINEMENT**  
Program: **Core-Theory Reconstruction Challenge**  
Target: resolve the final `CFE-QM` item isolated by QM Core 004E without identifying DSD channel count with operational capacity and without hiding the family-existence assumption inside the restriction axiom.

## 1. Exact comparator target

The external comparator's Subspace Axiom contains two logically distinct statements:

1. **family existence**: for every positive integer `N`, there exists a dynamical state space of capacity `N`;
2. **recursive restriction**: excluding one outcome of any maximal perfectly distinguishing measurement gives a lower-capacity dynamical system equivalent to the `N-1` member.

QM Core 004I addressed the universal restriction/equivalence part. The present audit isolates the first clause:

```text
CFE-QM  Capacity-Family Existence
For every N >= 1, there exists an admitted dynamical state space of operational capacity N.
```

This is not a statement about channel number, vector-space dimension, Hilbert dimension, axis rank, or property arity.

## 2. Generic DSD does not imply CFE-QM

The four-layer DSD core does not contain an existence axiom saying that a physical specialization must realize systems of every operational capacity.

Formation permits finite admitted channel composition, but channel count is not operational capacity. Property supports typed partial data but does not force a measurement family of each size. Static Aggregation works on supplied realized carriers. Dynamics evolves supplied admissible systems and does not manufacture a new system family indexed by every positive integer.

Therefore:

\[
\boxed{\text{generic DSD} \not\Rightarrow \mathrm{CFE\!-
QM}.}
\]

## 3. Two non-implications

### 3.1 Unbounded composite capacities alone do not fill the integers

Suppose a theory realizes only capacities

\[
\{1,2,4,8,16,\ldots\}.
\]

The realized capacities are unbounded, but capacities `3,5,6,7,...` need not exist.

Thus:

\[
\boxed{\text{unbounded realized capacity} \not\Rightarrow \mathrm{CFE\!-
QM}}
\]

without a downward-descent rule.

### 3.2 Downward recursion alone can stop at a finite ceiling

The family

\[
\{1,2,3,4\}
\]

is downward closed under `m -> m-1`, but contains no system of capacity `5` or above.

Thus:

\[
\boxed{\text{downward closure} \not\Rightarrow \mathrm{CFE\!-
QM}}
\]

without an unbounded source of capacities.

These are counterexamples to implications between interface conditions, not counterexamples to quantum mechanics or DSD.

## 4. Avoiding circularity with 004I

The comparator's usual wording says that the restricted face of an `N`-system is equivalent to `Omega_{N-1}`. Taken literally, this already presupposes that the `N-1` family member exists.

Therefore CFE-QM must not be "derived" by simply citing ULRRDE-QM in that family-indexed form.

For the existence proof we isolate an intrinsic, non-circular descent condition:

```text
IDDC-QM  Intrinsic Descriptive Descent Closure
```

For any admitted dynamical system `S` of finite operational capacity `m >= 2`, an admitted outcome-exclusion restriction exists whose retained state/effect/dynamics structure is itself a valid dynamical system of capacity exactly `m-1`.

`IDDC-QM` does not name or presuppose a previously existing `Q_{m-1}` object. Once a family representative is chosen, the stronger 004I equivalence interface can compare the intrinsic descendant with that representative.

## 5. Unbounded capacities from one nontrivial seed

Introduce the second precursor:

```text
IFPC-QM  Iterated Finite Product Composition
```

There exists at least one admitted seed system `S` with

\[
q:=\operatorname{Cap}(S)\ge2,
\]

and for every finite `k` an admitted `k`-fold independent composite exists. Product preparations and product measurements remain available so that any `q` perfectly distinguishable seed states generate at least `q^k` perfectly distinguishable product states.

Hence, if the actual capacity of the `k`-fold composite is `M_k`,

\[
\boxed{M_k\ge q^k.}
\]

No exact capacity multiplicativity is required.

Because `q >= 2`, the lower bound `q^k` is unbounded. Therefore the realized capacity set is unbounded.

## 6. Capacity-family completion theorem

Let `R` be the set of realized finite operational capacities.

Assume:

1. `R` contains a nontrivial seed capacity `q >= 2`;
2. `IFPC-QM` supplies composite systems with capacities `M_k >= q^k` for every finite `k`;
3. `IDDC-QM` gives intrinsic descent from every realized `m >= 2` to a realized `m-1` system.

Then:

\[
\boxed{R=\mathbb N_{>0}.}
\]

### Proof

Take arbitrary `N >= 1`.

Choose `k` so that

\[
q^k\ge N.
\]

By IFPC-QM there is a realized composite of finite capacity

\[
M_k\ge q^k\ge N.
\]

Apply IDDC-QM repeatedly:

\[
M_k\to M_k-1\to\cdots\to N.
\]

Thus a valid dynamical system of capacity exactly `N` is realized. Since `N` was arbitrary, every positive integer capacity is realized. QED.

Equivalently, an unbounded subset of the positive integers that is closed under predecessor is all of the positive integers.

## 7. What the theorem does not use

The proof does **not** require:

```text
exact capacity multiplicativity
V_AB = V_A tensor V_B
local tomography
no-restriction
Born rule
Hilbert dimension
channel count = capacity
```

The only composite fact needed is the operational lower bound from independent product distinguishability.

## 8. Provenance and anti-post-hoc status

Current conservative classification:

```text
OCD capacity definition / joint distinguishability      B  GENERAL_OPERATIONAL_DERIVATION
product distinguishability lower bound                  CONDITIONAL GENERAL RESULT
IFPC-QM                                                  D  PROVISIONAL EXACT-COMPARATOR PRECURSOR
IDDC-QM                                                  D  EXACT-COMPARATOR REFINEMENT
CFE-QM                                                   CONDITIONAL_DERIVATION FROM D INPUTS
```

`IFPC-QM` is not promoted to Class B merely because it sounds operationally general. It was isolated during the quantum comparator stage and must be independently tested outside the QM target before any provenance upgrade.

Likewise `IDDC-QM` is a strengthened restriction condition discovered while matching the Subspace Axiom.

Therefore this result does not add independent A/B evidence that generic DSD derives quantum theory.

## 9. CFE-QM resolution

The old monolithic lock

```text
CFE-QM = assume a system of every capacity N
```

can be refined.

It is sufficient to supply:

```text
one nontrivial finite-capacity seed
+ iterated finite independent composition
+ intrinsic exact one-step capacity descent
```

and family existence follows as a theorem.

Hence the final 004E gap is no longer left unclassified.

## 10. QM Core 004E lock status after 004J

```text
OSC-QM       classified: Class D
CRG-QM       classified: Class D
ETC-QM       conditional derivation after ILPC-QM + LDC-QM + linearization
ULRRDE-QM    conditional derivation after LFRR-QM + CMT-QM
CFE-QM       conditional derivation after IFPC-QM + IDDC-QM + nontrivial seed
```

All five original exact-interface gaps have now been classified or decomposed.

This does **not** yet license the statement that generic DSD derives complex quantum mechanics, because several decisive inputs remain Class C/D. It does mean that the QM Core 004 exact-interface audit is ready for synthesis.

## 11. Reproducibility witness

```bash
python audits/science/2026-09-08_qm_core_004j_capacity_family_existence_gate.py --mode all
```

The finite script checks the two non-implications and finite instances of the seed-product-descent construction. The infinite theorem is the elementary argument in Section 6, not an empirical conclusion from finite code.

## 12. Verdict

**PASS_WITH_REFINEMENT**

CFE-QM is not a generic DSD consequence and must not be inferred from channel count. However, the exact external assumption "a capacity-N system exists for every N" can be decomposed into a nontrivial seed, arbitrarily iterated independent product composition, and intrinsic one-step capacity descent. Under those explicit conditions, capacity-family existence follows mathematically rather than remaining an additional family-wide primitive.
