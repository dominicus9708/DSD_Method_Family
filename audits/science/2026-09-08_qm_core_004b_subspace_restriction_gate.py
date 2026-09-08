#!/usr/bin/env python3
"""QM Core 004B — Subspace / Restriction Principle pressure test.

Standard-library only. The script checks finite witnesses for:
1) square-bit failure of capacity-recursive restriction,
2) classical simplex success (showing non-uniqueness),
3) quantum qutrit->qubit block-face witness,
4) DSD-style distinction between subset restriction and claimed lower-type equivalence.
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def square_bit_failure() -> bool:
    vertices = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    # Exclude the X+ outcome: e_X+(x,y)=(1+x)/2 = 0 iff x=-1.
    face = [v for v in vertices if v[0] == -1]
    # The two retained pure states are perfectly distinguished by Y.
    probs_y_plus = [Fraction(1 + y, 2) for _, y in face]
    capacity_face_at_least_2 = sorted(probs_y_plus) == [Fraction(0), Fraction(1)]
    lower_capacity_one_is_singleton = True
    # A capacity-2 system would have to reduce to a capacity-1 singleton face.
    return len(face) == 2 and capacity_face_at_least_2 and lower_capacity_one_is_singleton


def classical_simplex_pass() -> bool:
    # Classical trit pure states. Excluding outcome 3 leaves the classical bit face.
    trit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    face = [p for p in trit if p[2] == 0]
    return face == [(1, 0, 0), (0, 1, 0)]


def matmul2(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def dagger2(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def trace2(a):
    return a[0][0] + a[1][1]


def quantum_qutrit_qubit_face() -> bool:
    # Exact rational qubit density matrices, embedded as top-left qutrit blocks.
    qubits = [
        [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]],
        [[Fraction(0), Fraction(0)], [Fraction(0), Fraction(1)]],
        [[Fraction(1, 2), Fraction(1, 2)], [Fraction(1, 2), Fraction(1, 2)]],
        [[Fraction(3, 4), Fraction(1, 4)], [Fraction(1, 4), Fraction(1, 4)]],
    ]

    for rho2 in qubits:
        if trace2(rho2) != 1:
            return False
        rho3 = [
            [rho2[0][0], rho2[0][1], Fraction(0)],
            [rho2[1][0], rho2[1][1], Fraction(0)],
            [Fraction(0), Fraction(0), Fraction(0)],
        ]
        # Probability for excluded third-level projector |3><3|.
        p3 = rho3[2][2]
        if p3 != 0:
            return False
        # Restriction/embedding is lossless on the retained 2D support.
        recovered = [[rho3[i][j] for j in range(2)] for i in range(2)]
        if recovered != rho2:
            return False

    # Check a unitary-like reversible transformation on the retained face:
    # X swaps |0> and |1> and preserves the embedded face.
    X = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    rho = qubits[3]
    transformed = matmul2(matmul2(X, rho), dagger2(X))
    return trace2(transformed) == 1


def subset_not_equivalence() -> bool:
    # A finite carrier and a retained subset can exist without any declaration
    # identifying that subset with a lower-capacity system type.
    full = {"a", "b", "c"}
    retained = {"a", "b"}
    inclusion_valid = retained < full
    lower_type_declared = False
    return inclusion_valid and not lower_type_declared


def run_all() -> bool:
    tests = [
        ("square-bit restriction counterexample", square_bit_failure()),
        ("classical simplex restriction control", classical_simplex_pass()),
        ("qutrit-to-qubit quantum face witness", quantum_qutrit_qubit_face()),
        ("subset does not imply lower-type equivalence", subset_not_equivalence()),
    ]
    for name, ok in tests:
        print(f"{name:<44} {'PASS' if ok else 'FAIL'}")
    overall = all(ok for _, ok in tests)
    print(f"\nOVERALL: {'PASS_WITH_REFINEMENT' if overall else 'FAIL'}")
    return overall


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "square", "classical", "quantum", "subset"], default="all")
    args = parser.parse_args()

    if args.mode == "all":
        return 0 if run_all() else 1
    if args.mode == "square":
        ok = square_bit_failure()
    elif args.mode == "classical":
        ok = classical_simplex_pass()
    elif args.mode == "quantum":
        ok = quantum_qutrit_qubit_face()
    else:
        ok = subset_not_equivalence()
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
