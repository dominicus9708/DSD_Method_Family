#!/usr/bin/env python3
"""
QM Core 002 — integrated DSD reconstruction witness for quantum instruments.

Tests:
1. Two distinct instruments with the same POVM produce the same outcome probabilities.
2. Their conditional post-measurement states and unconditioned disturbance differ.
3. Lüders Z instrument is repeatable; same-POVM reprepare-plus instrument is not.
4. A zero-probability branch has a defined zero subnormalized branch operator and
   defined zero probability, while the normalized conditional state is undefined.
5. The branch-resolved aggregate reconstructs both probability vector and
   unconditioned channel output.

Standard library only.
"""

from __future__ import annotations

import argparse
import math
from typing import Dict, List, Sequence

Matrix = List[List[complex]]
TOL = 1e-10


def zeros(n: int, m: int) -> Matrix:
    return [[0j for _ in range(m)] for _ in range(n)]


def mat_add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_scale(c: complex, a: Matrix) -> Matrix:
    return [[c * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mat_mul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def dagger(a: Matrix) -> Matrix:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(min(len(a), len(a[0]))))


def mat_close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    return all(
        abs(a[i][j] - b[i][j]) <= tol
        for i in range(len(a))
        for j in range(len(a[0]))
    )


def scalar_close(a: complex, b: complex, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def outer(v: Sequence[complex], w: Sequence[complex]) -> Matrix:
    return [[v[i] * w[j].conjugate() for j in range(len(w))] for i in range(len(v))]


I: Matrix = [[1 + 0j, 0j], [0j, 1 + 0j]]
X: Matrix = [[0j, 1 + 0j], [1 + 0j, 0j]]
P0: Matrix = [[1 + 0j, 0j], [0j, 0j]]
P1: Matrix = [[0j, 0j], [0j, 1 + 0j]]

ket0 = [1 + 0j, 0j]
ket1 = [0j, 1 + 0j]
ket_plus = [1 / math.sqrt(2) + 0j, 1 / math.sqrt(2) + 0j]
RHO_PLUS = outer(ket_plus, ket_plus)

Instrument = Dict[str, List[Matrix]]


def branch_map(kraus: Sequence[Matrix], rho: Matrix) -> Matrix:
    out = zeros(len(rho), len(rho[0]))
    for k in kraus:
        out = mat_add(out, mat_mul(mat_mul(k, rho), dagger(k)))
    return out


def instrument_branches(inst: Instrument, rho: Matrix) -> Dict[str, Matrix]:
    return {label: branch_map(kraus, rho) for label, kraus in inst.items()}


def branch_probabilities(branches: Dict[str, Matrix]) -> Dict[str, float]:
    return {label: trace(tau).real for label, tau in branches.items()}


def conditional_state(tau: Matrix) -> Matrix | None:
    p = trace(tau).real
    if abs(p) <= TOL:
        return None
    return mat_scale(1.0 / p, tau)


def unconditioned_state(branches: Dict[str, Matrix]) -> Matrix:
    out = zeros(2, 2)
    for tau in branches.values():
        out = mat_add(out, tau)
    return out


def effect_from_branch(kraus: Sequence[Matrix]) -> Matrix:
    out = zeros(2, 2)
    for k in kraus:
        out = mat_add(out, mat_mul(dagger(k), k))
    return out


def expectation(rho: Matrix, effect: Matrix) -> float:
    return trace(mat_mul(rho, effect)).real


def make_luders_z() -> Instrument:
    return {"0": [P0], "1": [P1]}


def make_reprepare_plus_same_povm() -> Instrument:
    k0 = outer(ket_plus, ket0)
    k1 = outer(ket_plus, ket1)
    return {"0": [k0], "1": [k1]}


def test_same_povm_different_instrument() -> None:
    luders = make_luders_z()
    reprepare = make_reprepare_plus_same_povm()

    for label, expected in (("0", P0), ("1", P1)):
        assert mat_close(effect_from_branch(luders[label]), expected)
        assert mat_close(effect_from_branch(reprepare[label]), expected)

    b_l = instrument_branches(luders, RHO_PLUS)
    b_r = instrument_branches(reprepare, RHO_PLUS)
    p_l = branch_probabilities(b_l)
    p_r = branch_probabilities(b_r)

    assert scalar_close(p_l["0"], 0.5)
    assert scalar_close(p_l["1"], 0.5)
    assert all(abs(p_l[k] - p_r[k]) <= TOL for k in p_l)

    u_l = unconditioned_state(b_l)
    u_r = unconditioned_state(b_r)

    assert not mat_close(u_l, u_r)
    assert scalar_close(expectation(u_l, X), 0.0)
    assert scalar_close(expectation(u_r, X), 1.0)

    print("[same-povm] PASS")
    print(f"  probabilities Lüders   = ({p_l['0']:.12f}, {p_l['1']:.12f})")
    print(f"  probabilities reprepare= ({p_r['0']:.12f}, {p_r['1']:.12f})")
    print("  same POVM/readout, different unconditioned state and disturbance")


def test_conditioned_repeatability() -> None:
    luders = make_luders_z()
    reprepare = make_reprepare_plus_same_povm()

    for label, projector in (("0", P0), ("1", P1)):
        tau_l = instrument_branches(luders, RHO_PLUS)[label]
        rho_l = conditional_state(tau_l)
        assert rho_l is not None
        assert scalar_close(expectation(rho_l, projector), 1.0)

        tau_r = instrument_branches(reprepare, RHO_PLUS)[label]
        rho_r = conditional_state(tau_r)
        assert rho_r is not None
        assert scalar_close(expectation(rho_r, projector), 0.5)

    print("[repeatability] PASS")
    print("  Lüders Z: conditioned outcome repeats with probability 1")
    print("  same-POVM reprepare-plus: repeated Z outcome probability is 1/2")


def test_zero_probability_status() -> None:
    luders = make_luders_z()
    branches = instrument_branches(luders, P0)

    tau1 = branches["1"]
    p1 = trace(tau1).real
    rho1 = conditional_state(tau1)

    assert mat_close(tau1, zeros(2, 2))
    assert scalar_close(p1, 0.0)
    assert rho1 is None

    print("[zero-status] PASS")
    print("  branch operator tau_1 = defined zero operator")
    print("  probability p_1       = defined zero")
    print("  normalized conditional state = undefined (division by zero)")


def test_branch_aggregate_postprocessing() -> None:
    for name, inst in (("luders", make_luders_z()), ("reprepare", make_reprepare_plus_same_povm())):
        branches = instrument_branches(inst, RHO_PLUS)
        probs = branch_probabilities(branches)
        uncond = unconditioned_state(branches)

        assert scalar_close(sum(probs.values()), 1.0)
        assert scalar_close(trace(uncond), 1.0)

        reconstructed_probs = {k: trace(v).real for k, v in branches.items()}
        reconstructed_uncond = zeros(2, 2)
        for v in branches.values():
            reconstructed_uncond = mat_add(reconstructed_uncond, v)

        assert all(abs(probs[k] - reconstructed_probs[k]) <= TOL for k in probs)
        assert mat_close(uncond, reconstructed_uncond)

        print(f"[aggregate:{name}] PASS")
        print("  branch aggregate -> probability vector")
        print("  branch aggregate -> unconditioned output state")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "same-povm", "repeatability", "zero-status", "aggregate"),
        default="all",
    )
    args = parser.parse_args()

    tests = {
        "same-povm": test_same_povm_different_instrument,
        "repeatability": test_conditioned_repeatability,
        "zero-status": test_zero_probability_status,
        "aggregate": test_branch_aggregate_postprocessing,
    }

    if args.mode == "all":
        for fn in tests.values():
            fn()
        print("OVERALL: PASS_WITH_REFINEMENT")
    else:
        tests[args.mode]()


if __name__ == "__main__":
    main()
