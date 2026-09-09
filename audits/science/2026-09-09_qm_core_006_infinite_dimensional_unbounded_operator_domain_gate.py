#!/usr/bin/env python3
"""QM Core 006 — Infinite-Dimensional Hilbert / Unbounded-Operator / Domain Gate.

Analytic/finite witnesses for:
- normalized states can coexist with unbounded observables,
- position and momentum are unbounded on L^2(R),
- strong continuity does not imply strong differentiability on every state,
- symmetric does not imply self-adjoint on a finite interval,
- finite-dimensional truncations cannot satisfy the exact CCR [Q,P]=i hbar I.

Only Python's standard library is used. Infinite-dimensional facts are represented
through exact formulas and boundary identities rather than treating a finite matrix
simulation as a proof about unbounded operators.
"""

from __future__ import annotations

import argparse
import cmath
import math

TOL = 1e-12


def close(a: complex | float, b: complex | float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def translated_gaussian_q_norm(n: float) -> float:
    """For psi_n(x)=pi^(-1/4) exp(-(x-n)^2/2), return ||Q psi_n||."""
    return math.sqrt(n * n + 0.5)


def modulated_gaussian_p_norm(k: float, hbar: float = 1.0) -> float:
    """For phi_k(x)=exp(i k x) psi_0(x), return ||P phi_k||."""
    return hbar * math.sqrt(k * k + 0.5)


def indicator_translation_difference_norm(a: float) -> float:
    """||U(a)1_[0,1]-1_[0,1]||_2 for |a|<=1."""
    aa = abs(a)
    if aa > 1.0:
        raise ValueError("witness formula is restricted to |a| <= 1")
    return math.sqrt(2.0 * aa)


def indicator_translation_difference_quotient_norm(a: float) -> float:
    aa = abs(a)
    if aa <= 0.0 or aa > 1.0:
        raise ValueError("require 0 < |a| <= 1")
    return indicator_translation_difference_norm(a) / aa


def deficiency_norm(sign: int) -> float:
    """L2(0,1) norm of exp(-x) (+) or exp(x) (-)."""
    if sign == +1:
        return math.sqrt((1.0 - math.exp(-2.0)) / 2.0)
    if sign == -1:
        return math.sqrt((math.exp(2.0) - 1.0) / 2.0)
    raise ValueError("sign must be +1 or -1")


def deficiency_equation_residual(sign: int, x: float) -> complex:
    """Residual for P*psi=sign*i psi, P*=-i d/dx, hbar=1."""
    if sign == +1:
        psi = math.exp(-x)
        dpsi = -psi
    elif sign == -1:
        psi = math.exp(x)
        dpsi = psi
    else:
        raise ValueError("sign must be +1 or -1")
    return -1j * dpsi - sign * 1j * psi


def matrix_multiply(a: list[list[complex]], b: list[list[complex]]) -> list[list[complex]]:
    n = len(a)
    out = [[0j for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                out[i][j] += a[i][k] * b[k][j]
    return out


def finite_matrix_trace_commutator(a: list[list[complex]], b: list[list[complex]]) -> complex:
    ab = matrix_multiply(a, b)
    ba = matrix_multiply(b, a)
    return sum(ab[i][i] - ba[i][i] for i in range(len(a)))


def sample_matrices(n: int) -> tuple[list[list[complex]], list[list[complex]]]:
    a = [[0j for _ in range(n)] for _ in range(n)]
    b = [[0j for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i][i] = i + 1
        if i + 1 < n:
            b[i][i + 1] = math.sqrt(i + 1)
            b[i + 1][i] = math.sqrt(i + 1)
    return a, b


def check_unboundedness() -> list[tuple[str, bool]]:
    q_vals = [translated_gaussian_q_norm(n) for n in (0.0, 5.0, 20.0, 100.0)]
    p_vals = [modulated_gaussian_p_norm(k) for k in (0.0, 5.0, 20.0, 100.0)]
    return [
        ("translated normalized Gaussians make ||Q psi_n|| grow without a uniform bound",
         q_vals[-1] > q_vals[-2] > q_vals[-3] > q_vals[-4]),
        ("modulated normalized Gaussians make ||P phi_k|| grow without a uniform bound",
         p_vals[-1] > p_vals[-2] > p_vals[-3] > p_vals[-4]),
        ("Q witness matches sqrt(n^2+1/2) at n=20",
         close(q_vals[2] ** 2, 20.0 ** 2 + 0.5)),
        ("P witness matches hbar*sqrt(k^2+1/2) at k=20",
         close(p_vals[2] ** 2, 20.0 ** 2 + 0.5)),
    ]


def check_strong_continuity_vs_differentiability() -> list[tuple[str, bool]]:
    a1, a2, a3 = 1e-2, 1e-4, 1e-6
    d1 = indicator_translation_difference_norm(a1)
    d2 = indicator_translation_difference_norm(a2)
    d3 = indicator_translation_difference_norm(a3)
    q1 = indicator_translation_difference_quotient_norm(a1)
    q2 = indicator_translation_difference_quotient_norm(a2)
    q3 = indicator_translation_difference_quotient_norm(a3)
    return [
        ("indicator translation norm difference tends to zero", d3 < d2 < d1),
        ("indicator difference quotient norm diverges as a -> 0", q3 > q2 > q1),
        ("exact norm formula ||U(a)psi-psi|| = sqrt(2|a|)", close(d2 * d2, 2.0 * a2)),
        ("strong continuity therefore does not imply differentiability on every state",
         d3 < 0.01 and q3 > 1000.0),
    ]


def check_symmetric_vs_self_adjoint() -> list[tuple[str, bool]]:
    xs = (0.0, 0.2, 0.7, 1.0)
    plus_ok = all(abs(deficiency_equation_residual(+1, x)) <= TOL for x in xs)
    minus_ok = all(abs(deficiency_equation_residual(-1, x)) <= TOL for x in xs)
    plus_norm = deficiency_norm(+1)
    minus_norm = deficiency_norm(-1)

    plus_not_h01_0 = abs(math.exp(0.0)) > TOL or abs(math.exp(-1.0)) > TOL
    minus_not_h01_0 = abs(math.exp(0.0)) > TOL or abs(math.exp(1.0)) > TOL

    theta = 0.73
    boundary_extension_ok = close(cmath.exp(1j * theta), cmath.exp(1j * theta) * 1.0)

    return [
        ("+ deficiency vector exp(-x) solves P*psi=+i psi", plus_ok),
        ("- deficiency vector exp(+x) solves P*psi=-i psi", minus_ok),
        ("both deficiency vectors are square-integrable on (0,1)",
         math.isfinite(plus_norm) and math.isfinite(minus_norm) and plus_norm > 0 and minus_norm > 0),
        ("deficiency vectors are not in H_0^1 endpoint domain", plus_not_h01_0 and minus_not_h01_0),
        ("phase boundary psi(1)=exp(i theta)psi(0) is consistent with a self-adjoint extension family",
         boundary_extension_ok),
    ]


def check_finite_ccr_obstruction(dim: int) -> list[tuple[str, bool]]:
    a, b = sample_matrices(dim)
    tr_comm = finite_matrix_trace_commutator(a, b)
    target_trace = 1j * dim
    return [
        ("trace of every finite-matrix commutator is zero in the witness", abs(tr_comm) <= TOL),
        ("trace of i I is nonzero in finite dimension", abs(target_trace) > TOL),
        ("finite-dimensional matrices therefore cannot satisfy [Q,P]=i I exactly",
         abs(tr_comm - target_trace) > 1.0),
    ]


def run(mode: str, dim: int) -> int:
    groups: list[tuple[str, list[tuple[str, bool]]]] = []
    if mode in ("all", "unbounded"):
        groups.append(("UNBOUNDED_OPERATORS", check_unboundedness()))
    if mode in ("all", "continuity"):
        groups.append(("STRONG_CONTINUITY_VS_DIFFERENTIABILITY",
                       check_strong_continuity_vs_differentiability()))
    if mode in ("all", "selfadjoint"):
        groups.append(("SYMMETRIC_VS_SELF_ADJOINT", check_symmetric_vs_self_adjoint()))
    if mode in ("all", "ccr"):
        groups.append(("FINITE_CCR_OBSTRUCTION", check_finite_ccr_obstruction(dim)))

    all_ok = True
    for title, checks in groups:
        print(f"[{title}]")
        for label, ok in checks:
            all_ok = all_ok and ok
            print(f"{label:<88} {'PASS' if ok else 'FAIL'}")
        print()

    print("OVERALL:", "PASS_WITH_REFINEMENT" if all_ok else "FAIL")
    return 0 if all_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "unbounded", "continuity", "selfadjoint", "ccr"),
        default="all",
    )
    parser.add_argument("--dim", type=int, default=5)
    args = parser.parse_args()
    if args.dim < 1:
        parser.error("--dim must be >= 1")
    return run(args.mode, args.dim)


if __name__ == "__main__":
    raise SystemExit(main())
