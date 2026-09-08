#!/usr/bin/env python3
"""QM Core 005C — Reversible Channel / Unitary Gate.

Exact finite witnesses for:
- a unitary channel with a physical CPTP inverse,
- a CPTP depolarizing channel that is algebraically invertible but whose
  inverse is not positive on the whole state space,
- trace-distance contraction under the nonunitary channel,
- the distinction between algebraic invertibility and physical reversibility.

The general theorem is stated in the companion audit.  This script uses only
Python's standard library and exact Fraction arithmetic.
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


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Fraction, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def trace(a: Matrix) -> Fraction:
    return sum(a[i][i] for i in range(len(a)))


def identity(n: int) -> Matrix:
    return [[F(1 if i == j else 0) for j in range(n)] for i in range(n)]


def conjugate_by_real_unitary(u: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(u, rho), transpose(u))


def depolarizing(a: Matrix, lam: Fraction = F(1, 2)) -> Matrix:
    """Linear qubit depolarizing map: lam*A + (1-lam) Tr(A) I/2."""
    return add(scale(lam, a), scale((1 - lam) * trace(a) / 2, identity(2)))


def depolarizing_inverse(a: Matrix, lam: Fraction = F(1, 2)) -> Matrix:
    """Algebraic inverse for lam != 0; not generally positive."""
    return add(scale(1 / lam, a), scale(-(1 - lam) * trace(a) / (2 * lam), identity(2)))


def diagonal_trace_norm(a: Matrix) -> Fraction:
    assert a[0][1] == 0 and a[1][0] == 0
    return abs(a[0][0]) + abs(a[1][1])


def run_all() -> bool:
    checks: list[tuple[str, bool]] = []

    rho0: Matrix = [[F(1), F(0)], [F(0), F(0)]]
    rho1: Matrix = [[F(0), F(0)], [F(0), F(1)]]
    pauli_x: Matrix = [[F(0), F(1)], [F(1), F(0)]]

    # Exact unitary control: X rho X is its own inverse.
    ux0 = conjugate_by_real_unitary(pauli_x, rho0)
    ux_back = conjugate_by_real_unitary(pauli_x, ux0)
    checks.append(("Pauli-X channel maps |0><0| to |1><1|", ux0 == rho1))
    checks.append(("Pauli-X inverse channel recovers the input", ux_back == rho0))
    checks.append(("unitary channel preserves normalization", trace(ux0) == trace(rho0) == 1))

    # Nonunitary CPTP control: lambda=1/2 depolarizing channel.
    d0 = depolarizing(rho0)
    d1 = depolarizing(rho1)
    checks.append(("depolarizing outputs normalized diagonal states", trace(d0) == 1 and trace(d1) == 1))
    checks.append(("depolarizing output on |0> is diag(3/4,1/4)", d0 == [[F(3, 4), F(0)], [F(0), F(1, 4)]]))

    # The superoperator is algebraically invertible for lambda != 0.
    recovered = depolarizing_inverse(d0)
    checks.append(("algebraic depolarizing inverse recovers an on-range input", recovered == rho0))

    # But the inverse is not positive on the whole state space.
    bad_inverse_output = depolarizing_inverse(rho0)
    checks.append(("algebraic inverse maps a valid state to diag(3/2,-1/2)", bad_inverse_output == [[F(3, 2), F(0)], [F(0), F(-1, 2)]]))
    checks.append(("algebraic inverse is therefore not positive", bad_inverse_output[1][1] < 0))

    # Trace distance is contracted by the depolarizing map.
    in_norm = diagonal_trace_norm(sub(rho0, rho1))
    out_norm = diagonal_trace_norm(sub(d0, d1))
    checks.append(("orthogonal-state trace norm starts at 2", in_norm == 2))
    checks.append(("depolarizing trace norm contracts to 1", out_norm == 1))

    for name, passed in checks:
        print(f"{name:<72} {'PASS' if passed else 'FAIL'}")

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
