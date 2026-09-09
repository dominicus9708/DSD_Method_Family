#!/usr/bin/env python3
"""QM Core 005D — Continuous Unitary / Hamiltonian Generator Gate.

Finite-dimensional witnesses for the distinctions:

- unitary at each time,
- continuous/smooth unitary path,
- one-parameter unitary group,
- time-dependent Hermitian generator,
- time-independent Hamiltonian generator,
- channel-level Hamiltonian gauge H ~ H + c I.

The general Stone theorem and propagator results are stated in the companion
audit.  This script uses only Python's standard library.
"""

from __future__ import annotations

import argparse
import cmath

Matrix = list[list[complex]]
TOL = 1e-10


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return [
        [sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: complex, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def adjoint(a: Matrix) -> Matrix:
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def identity(n: int) -> Matrix:
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(n)] for i in range(n)]


def max_abs(a: Matrix) -> float:
    return max(abs(x) for row in a for x in row)


def close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    return max_abs(sub(a, b)) <= tol


def diag_exp_from_h(hdiag: tuple[float, float], phase_scale: float) -> Matrix:
    return [
        [cmath.exp(-1j * phase_scale * hdiag[0]), 0.0j],
        [0.0j, cmath.exp(-1j * phase_scale * hdiag[1])],
    ]


def diag_matrix(hdiag: tuple[float, float]) -> Matrix:
    return [[complex(hdiag[0]), 0.0j], [0.0j, complex(hdiag[1])]]


def conjugate(u: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(u, rho), adjoint(u))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def run_all() -> bool:
    checks: list[tuple[str, bool]] = []

    # Units: hbar = 1.
    hdiag = (1.0, 2.0)
    h0 = diag_matrix(hdiag)
    ident = identity(2)

    # Positive control: V(t) = exp(-i t H0) is a one-parameter unitary group.
    t = 0.7
    s = -0.2
    vt = diag_exp_from_h(hdiag, t)
    vs = diag_exp_from_h(hdiag, s)
    vts = diag_exp_from_h(hdiag, t + s)
    checks.append(("group control is unitary", close(matmul(adjoint(vt), vt), ident)))
    checks.append(("group control satisfies V(t+s)=V(t)V(s)", close(vts, matmul(vt, vs))))

    # Smooth unitary path that is not a one-parameter group:
    # W(t) = exp(-i t^2 H0).
    w1 = diag_exp_from_h(hdiag, 1.0)
    w2 = diag_exp_from_h(hdiag, 4.0)  # W(2): phase_scale = 2^2
    checks.append(("quadratic-time path is unitary", close(matmul(adjoint(w1), w1), ident)))
    checks.append(("quadratic-time path violates the group law", not close(w2, matmul(w1, w1))))

    # Nevertheless it has a time-dependent Hermitian generator H(t)=2 t H0.
    tq = 0.4
    wt = diag_exp_from_h(hdiag, tq * tq)
    dwt: Matrix = [
        [(-1j * 2.0 * tq * hdiag[0]) * wt[0][0], 0.0j],
        [0.0j, (-1j * 2.0 * tq * hdiag[1]) * wt[1][1]],
    ]
    ht = scale(2.0 * tq, h0)
    checks.append(("smooth non-group path obeys i dW/dt = H(t) W", close(scale(1j, dwt), matmul(ht, wt))))
    checks.append(("time-dependent generator H(t)=2tH0 is Hermitian", close(ht, adjoint(ht))))

    # A continuous unitary path need not be differentiable:
    # N(t)=exp(-i |t| H0) has opposite one-sided derivatives at t=0.
    right_derivative = scale(-1j, h0)
    left_derivative = scale(+1j, h0)
    checks.append(("continuous |t|-path has unequal one-sided derivatives at 0", not close(right_derivative, left_derivative)))

    # Channel-level energy-zero gauge:
    # H and H + cI generate the same density-operator conjugation channel.
    c = 3.0
    hshift_diag = (hdiag[0] + c, hdiag[1] + c)
    u = diag_exp_from_h(hdiag, t)
    ushift = diag_exp_from_h(hshift_diag, t)
    rho: Matrix = [
        [0.6 + 0.0j, 0.2 + 0.1j],
        [0.2 - 0.1j, 0.4 + 0.0j],
    ]
    out = conjugate(u, rho)
    out_shift = conjugate(ushift, rho)
    checks.append(("H and H+cI generate the same density-operator channel", close(out, out_shift)))

    hshift = add(h0, scale(c, ident))
    l0 = scale(-1j, commutator(h0, rho))
    lshift = scale(-1j, commutator(hshift, rho))
    checks.append(("commutator channel generator is invariant under H -> H+cI", close(l0, lshift)))

    for name, passed in checks:
        print(f"{name:<76} {'PASS' if passed else 'FAIL'}")

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
