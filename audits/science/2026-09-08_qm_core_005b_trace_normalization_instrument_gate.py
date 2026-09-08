#!/usr/bin/env python3
"""QM Core 005B — Trace Normalization / Instrument Gate.

Finite exact witnesses for:
- deterministic normalization preservation,
- selective trace-nonincreasing branches,
- branch-sum trace preservation,
- zero-probability branch handling,
- a completely positive but trace-increasing invalid branch control.

The general proofs are in the companion audit.  This script uses only Python's
standard library and exact Fraction arithmetic.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

F = Fraction
Matrix = list[list[Fraction]]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def transpose(a: Matrix) -> Matrix:
    return [list(row) for row in zip(*a)]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def kraus_branch(k: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(k, rho), transpose(k))


def zero_matrix(n: int) -> Matrix:
    return [[F(0) for _ in range(n)] for _ in range(n)]


def run_all() -> bool:
    checks: list[tuple[str, bool]] = []

    rho: Matrix = [
        [F(3, 4), F(1, 4)],
        [F(1, 4), F(1, 4)],
    ]
    p0: Matrix = [[F(1), F(0)], [F(0), F(0)]]
    p1: Matrix = [[F(0), F(0)], [F(0), F(1)]]

    # Projective two-branch instrument.
    b0 = kraus_branch(p0, rho)
    b1 = kraus_branch(p1, rho)
    total = add(b0, b1)

    checks.append(("input state is normalized", trace(rho) == 1))
    checks.append(("branch probabilities are 3/4 and 1/4", trace(b0) == F(3, 4) and trace(b1) == F(1, 4)))
    checks.append(("selective branches are trace non-increasing", trace(b0) <= trace(rho) and trace(b1) <= trace(rho)))
    checks.append(("branch probabilities sum to one", trace(b0) + trace(b1) == 1))
    checks.append(("nonselective branch sum preserves trace", trace(total) == trace(rho)))

    # A CP linear scaling map X -> X/2 is trace non-increasing but cannot be a
    # deterministic normalized-state evolution by itself.
    half_out = scale(F(1, 2), rho)
    checks.append(("CP trace-decreasing map fails deterministic normalization", trace(half_out) == F(1, 2)))

    # A CP map X -> 4 X can be represented by the single Kraus operator 2 I,
    # but it is not a valid selective branch because its output trace exceeds 1.
    two_i: Matrix = [[F(2), F(0)], [F(0), F(2)]]
    inflated = kraus_branch(two_i, rho)
    checks.append(("CP trace-increasing control is not a valid branch", trace(inflated) == 4 and trace(inflated) > trace(rho)))

    # Zero-probability branch: P1 acting on |0><0| gives the zero positive operator.
    rho0: Matrix = [[F(1), F(0)], [F(0), F(0)]]
    zero_branch = kraus_branch(p1, rho0)
    checks.append(("zero-probability positive branch is the zero operator", trace(zero_branch) == 0 and zero_branch == zero_matrix(2)))

    # Kraus normalization conditions for the projective instrument.
    ksum = add(matmul(transpose(p0), p0), matmul(transpose(p1), p1))
    identity: Matrix = [[F(1), F(0)], [F(0), F(1)]]
    checks.append(("instrument Kraus completeness sum equals identity", ksum == identity))

    for name, passed in checks:
        print(f"{name:<70} {'PASS' if passed else 'FAIL'}")

    overall = all(passed for _, passed in checks)
    print(f"\nOVERALL: {'PASS_WITH_REFINEMENT' if overall else 'FAIL'}")
    return overall


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    _ = parser.parse_args()
    return 0 if run_all() else 1


if __name__ == "__main__":
    raise SystemExit(main())
