#!/usr/bin/env python3
"""QM Core 005E — CPTP Semigroup / GKSL-Lindblad Generator Gate.

Finite witnesses for:
- a qubit dephasing CPTP semigroup,
- a smooth CPTP family that is CP-divisible but not time-homogeneous,
- the distinction between a channel and its time-local generator,
- irreversible distinguishability contraction and failure of the algebraic inverse
  to remain positive.

The general GKSL theorem is stated in the companion audit. This script uses
only Python's standard library.
"""

from __future__ import annotations

import argparse
import math

Matrix = list[list[complex]]
TOL = 1e-10


def close(a: float | complex, b: float | complex, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def mat_close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    return all(close(a[i][j], b[i][j], tol) for i in range(2) for j in range(2))


def trace(a: Matrix) -> complex:
    return a[0][0] + a[1][1]


def dephase(a: Matrix, coherence_factor: float) -> Matrix:
    """Qubit phase-damping map with coherence multiplier g in [-1,1]."""
    g = coherence_factor
    return [[a[0][0], g * a[0][1]], [g * a[1][0], a[1][1]]]


def exp_factor(t: float, kappa: float = 1.0) -> float:
    return math.exp(-kappa * t)


def gaussian_factor(t: float) -> float:
    return math.exp(-(t * t))


def z_conjugate(a: Matrix) -> Matrix:
    return [[a[0][0], -a[0][1]], [-a[1][0], a[1][1]]]


def dephasing_generator(a: Matrix, rate: float) -> Matrix:
    """L_t(rho) = (rate/2) (Z rho Z - rho)."""
    zrz = z_conjugate(a)
    return [[(rate / 2.0) * (zrz[i][j] - a[i][j]) for j in range(2)] for i in range(2)]


def gaussian_derivative_on_state(rho0: Matrix, t: float) -> Matrix:
    g = gaussian_factor(t)
    dg = -2.0 * t * g
    return [[0j, dg * rho0[0][1]], [dg * rho0[1][0], 0j]]


def hermitian_eigenvalues_2x2(a: Matrix) -> tuple[float, float]:
    aa = float(a[0][0].real)
    dd = float(a[1][1].real)
    b = a[0][1]
    disc = math.sqrt((aa - dd) ** 2 + 4.0 * (abs(b) ** 2))
    return ((aa + dd - disc) / 2.0, (aa + dd + disc) / 2.0)


def trace_norm_hermitian_2x2(a: Matrix) -> float:
    l1, l2 = hermitian_eigenvalues_2x2(a)
    return abs(l1) + abs(l2)


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def run_all() -> bool:
    checks: list[tuple[str, bool]] = []

    rho_plus: Matrix = [[0.5 + 0j, 0.5 + 0j], [0.5 + 0j, 0.5 + 0j]]
    rho_minus: Matrix = [[0.5 + 0j, -0.5 + 0j], [-0.5 + 0j, 0.5 + 0j]]

    s, t = 0.7, 1.1
    gs, gt, gst = exp_factor(s), exp_factor(t), exp_factor(s + t)
    checks.append(("exponential dephasing satisfies semigroup factor law", close(gt * gs, gst)))
    checks.append(("exponential dephasing preserves trace", close(trace(dephase(rho_plus, gt)), 1.0)))

    s2, t2 = 1.0, 1.0
    g_s, g_t, g_sum = gaussian_factor(s2), gaussian_factor(t2), gaussian_factor(s2 + t2)
    checks.append(("Gaussian dephasing slices are CPTP-range coherence factors", 0.0 < g_s <= 1.0 and 0.0 < g_sum <= 1.0))
    checks.append(("Gaussian dephasing violates time-homogeneous semigroup law", abs(g_t * g_s - g_sum) > 1e-6))

    s3, t3 = 0.8, 1.6
    g_s3, g_t3 = gaussian_factor(s3), gaussian_factor(t3)
    intermediate = g_t3 / g_s3
    lhs = dephase(dephase(rho_plus, g_s3), intermediate)
    rhs = dephase(rho_plus, g_t3)
    checks.append(("Gaussian intermediate dephasing factor lies in [0,1]", 0.0 <= intermediate <= 1.0))
    checks.append(("Gaussian family is CP-divisible in this witness", mat_close(lhs, rhs)))

    tg = 0.9
    rho_t = dephase(rho_plus, gaussian_factor(tg))
    analytic_derivative = gaussian_derivative_on_state(rho_plus, tg)
    local_generator = dephasing_generator(rho_t, rate=2.0 * tg)
    checks.append(("time-local dephasing generator matches Gaussian derivative", mat_close(analytic_derivative, local_generator)))
    checks.append(("generator output has trace zero rather than trace one", close(trace(local_generator), 0.0)))

    td = 1.0
    g = exp_factor(td)
    before = trace_norm_hermitian_2x2(sub(rho_plus, rho_minus))
    after = trace_norm_hermitian_2x2(sub(dephase(rho_plus, g), dephase(rho_minus, g)))
    checks.append(("orthogonal |+>,|-> trace norm starts at 2", close(before, 2.0)))
    checks.append(("dissipative dephasing strictly contracts trace norm", after < before and close(after, 2.0 * g)))

    inv_g = 1.0 / g
    recovered = dephase(dephase(rho_plus, g), inv_g)
    inverse_test = dephase(rho_plus, inv_g)
    eig_lo, eig_hi = hermitian_eigenvalues_2x2(inverse_test)
    checks.append(("algebraic inverse recovers an on-range state", mat_close(recovered, rho_plus)))
    checks.append(("algebraic inverse fails positivity on a valid input", eig_lo < -1e-10 and eig_hi > 1.0))

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
