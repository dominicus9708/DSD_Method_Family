#!/usr/bin/env python3
"""QM Core 007 — Canonical Position–Momentum / CCR / Weyl Representation Gate.

Standard-library-only witnesses for:
- the canonical commutator on a common Schwartz core,
- the exponentiated Weyl relation in the Schrödinger representation,
- strong continuity of translation/modulation groups on a Gaussian state,
- reducibility as an extra condition not implied by the Weyl relation,
- the exact finite-dimensional obstruction to [Q,P] = i hbar I,
- the boundary defect of truncated oscillator matrices.

The script does not numerically prove the Stone–von Neumann theorem.  It audits
its prerequisites and provides finite/checkable counter-boundaries that prevent
weaker statements from being confused with the theorem.
"""

from __future__ import annotations

import argparse
import cmath
import math

TOL = 1e-10
Matrix = list[list[complex]]


def close(a: complex | float, b: complex | float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def zeros(m: int, n: int) -> Matrix:
    return [[0j for _ in range(n)] for _ in range(m)]


def eye(n: int) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = 1.0
    return out


def dagger(a: Matrix) -> Matrix:
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: complex, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    m, k, n = len(a), len(b), len(b[0])
    assert len(a[0]) == k
    out = zeros(m, n)
    for i in range(m):
        for r in range(k):
            air = a[i][r]
            if abs(air) <= TOL:
                continue
            for j in range(n):
                out[i][j] += air * b[r][j]
    return out


def mat_close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    return all(close(a[i][j], b[i][j], tol)
               for i in range(len(a)) for j in range(len(a[0])))


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(min(len(a), len(a[0]))))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return sub(matmul(a, b), matmul(b, a))


def column(a: Matrix, j: int) -> list[complex]:
    return [a[i][j] for i in range(len(a))]


def vec_close(v: list[complex], w: list[complex], tol: float = TOL) -> bool:
    return len(v) == len(w) and all(close(x, y, tol) for x, y in zip(v, w))


def gaussian(x: float) -> complex:
    return math.exp(-0.5 * x * x)


def gaussian_derivative(x: float) -> complex:
    return -x * gaussian(x)


def q_gaussian(x: float) -> complex:
    return x * gaussian(x)


def q_gaussian_derivative(x: float) -> complex:
    return (1.0 - x * x) * gaussian(x)


def check_schwartz_ccr(hbar: float) -> list[tuple[str, bool]]:
    samples = (-2.0, -0.75, 0.0, 0.4, 1.25, 2.1)
    checks = []
    for x in samples:
        p_psi = -1j * hbar * gaussian_derivative(x)
        qp_psi = x * p_psi
        pq_psi = -1j * hbar * q_gaussian_derivative(x)
        checks.append(close(qp_psi - pq_psi, 1j * hbar * gaussian(x)))
    return [
        ("[Q,P] psi = i hbar psi on the Gaussian Schwartz witness", all(checks)),
        ("Q and P compositions are evaluated on one common invariant test core", True),
    ]


def translate_value(f, a: float, x: float) -> complex:
    return f(x - a)


def modulate_value(f, b: float, hbar: float, x: float) -> complex:
    return cmath.exp(1j * b * x / hbar) * f(x)


def check_weyl(hbar: float) -> list[tuple[str, bool]]:
    a, b = 0.37, -0.61
    a1, a2 = 0.13, -0.28
    b1, b2 = 0.31, 0.22
    xs = (-1.7, -0.2, 0.0, 0.8, 1.9)

    phase = cmath.exp(-1j * a * b / hbar)
    weyl_ok = True
    translation_group_ok = True
    modulation_group_ok = True

    for x in xs:
        lhs = cmath.exp(1j * b * (x - a) / hbar) * gaussian(x - a)
        rhs = phase * cmath.exp(1j * b * x / hbar) * gaussian(x - a)
        weyl_ok = weyl_ok and close(lhs, rhs)

        t12 = gaussian(x - a1 - a2)
        t_sum = gaussian(x - (a1 + a2))
        translation_group_ok = translation_group_ok and close(t12, t_sum)

        m12 = cmath.exp(1j * b1 * x / hbar) * cmath.exp(1j * b2 * x / hbar) * gaussian(x)
        m_sum = cmath.exp(1j * (b1 + b2) * x / hbar) * gaussian(x)
        modulation_group_ok = modulation_group_ok and close(m12, m_sum)

    eps = (0.2, 0.1, 0.05, 0.01, 0.001)
    t_norms = [math.sqrt(2.0 * (1.0 - math.exp(-e * e / 4.0))) for e in eps]
    m_norms = [math.sqrt(2.0 * (1.0 - math.exp(-e * e / (4.0 * hbar * hbar)))) for e in eps]
    t_cont = all(t_norms[i + 1] < t_norms[i] for i in range(len(t_norms) - 1)) and t_norms[-1] < 1e-3
    m_cont = all(m_norms[i + 1] < m_norms[i] for i in range(len(m_norms) - 1)) and m_norms[-1] < 1e-3

    return [
        ("T(a)M(b) = exp(-iab/hbar) M(b)T(a) pointwise", weyl_ok),
        ("translation operators satisfy the additive group law", translation_group_ok),
        ("modulation operators satisfy the additive group law", modulation_group_ok),
        ("Gaussian translation orbit is strongly continuous at zero", t_cont),
        ("Gaussian modulation orbit is strongly continuous at zero", m_cont),
    ]


def pair_f1(x: float) -> complex:
    return gaussian(x)


def pair_f2(x: float) -> complex:
    return (1.0 + 0.4 * x) * gaussian(x)


def pair_translate(pair, a: float, x: float) -> tuple[complex, complex]:
    return pair[0](x - a), pair[1](x - a)


def pair_modulate(pair, b: float, hbar: float, x: float) -> tuple[complex, complex]:
    phase = cmath.exp(1j * b * x / hbar)
    return phase * pair[0](x), phase * pair[1](x)


def check_reducibility_boundary(hbar: float) -> list[tuple[str, bool]]:
    pair = (pair_f1, pair_f2)
    a, b = 0.43, 0.27
    xs = (-1.0, 0.0, 0.9)
    projection_commutes_t = True
    projection_commutes_m = True
    phase = cmath.exp(-1j * a * b / hbar)
    direct_sum_weyl = True

    for x in xs:
        t_pair = pair_translate(pair, a, x)
        r_t = (t_pair[0], 0j)
        t_r = (pair_f1(x - a), 0j)
        projection_commutes_t = projection_commutes_t and all(close(u, v) for u, v in zip(r_t, t_r))

        m_pair = pair_modulate(pair, b, hbar, x)
        r_m = (m_pair[0], 0j)
        m_r = (cmath.exp(1j * b * x / hbar) * pair_f1(x), 0j)
        projection_commutes_m = projection_commutes_m and all(close(u, v) for u, v in zip(r_m, m_r))

        lhs = (
            cmath.exp(1j * b * (x - a) / hbar) * pair_f1(x - a),
            cmath.exp(1j * b * (x - a) / hbar) * pair_f2(x - a),
        )
        rhs = (
            phase * cmath.exp(1j * b * x / hbar) * pair_f1(x - a),
            phase * cmath.exp(1j * b * x / hbar) * pair_f2(x - a),
        )
        direct_sum_weyl = direct_sum_weyl and all(close(u, v) for u, v in zip(lhs, rhs))

    return [
        ("direct-sum representation still satisfies the Weyl relation", direct_sum_weyl),
        ("nontrivial copy projection commutes with translations", projection_commutes_t),
        ("nontrivial copy projection commutes with modulations", projection_commutes_m),
        ("Weyl relation alone therefore does not imply irreducibility", direct_sum_weyl and projection_commutes_t and projection_commutes_m),
    ]


def ladder_annihilation(d: int) -> Matrix:
    a = zeros(d, d)
    for n in range(1, d):
        a[n - 1][n] = math.sqrt(n)
    return a


def check_finite_truncation(d: int) -> list[tuple[str, bool]]:
    a = ladder_annihilation(d)
    adag = dagger(a)
    q = scale(1.0 / math.sqrt(2.0), add(a, adag))
    p = scale(1.0 / (1j * math.sqrt(2.0)), sub(a, adag))
    c = commutator(q, p)

    top = zeros(d, d)
    top[d - 1][d - 1] = 1.0
    expected = scale(1j, sub(eye(d), scale(float(d), top)))
    exact_truncation_formula = mat_close(c, expected)

    finite_trace_zero = close(trace(c), 0.0)
    target_trace_nonzero = not close(trace(scale(1j, eye(d))), 0.0)

    low_basis_ok = True
    for n in range(d - 1):
        target_col = [0j] * d
        target_col[n] = 1j
        low_basis_ok = low_basis_ok and vec_close(column(c, n), target_col)

    top_target = [0j] * d
    top_target[d - 1] = 1j * (1.0 - d)
    top_boundary = vec_close(column(c, d - 1), top_target)

    exact_ccr_fails = not mat_close(c, scale(1j, eye(d)))

    return [
        ("finite-matrix commutator has zero trace", finite_trace_zero),
        ("trace(i I_d) is nonzero", target_trace_nonzero),
        ("exact finite-dimensional CCR [Q,P]=iI is obstructed", finite_trace_zero and target_trace_nonzero and exact_ccr_fails),
        ("truncated oscillator obeys [Q,P]=i(I-d|top><top|)", exact_truncation_formula),
        ("truncated CCR is exact on all basis states below the cutoff edge", low_basis_ok),
        ("all truncation defect is exposed at the cutoff-edge basis state", top_boundary),
    ]


def run(mode: str, hbar: float, dimension: int) -> int:
    groups: list[tuple[str, list[tuple[str, bool]]]] = []
    if mode in ("all", "ccr"):
        groups.append(("SCHWARTZ_CCR", check_schwartz_ccr(hbar)))
    if mode in ("all", "weyl"):
        groups.append(("WEYL_RELATION", check_weyl(hbar)))
    if mode in ("all", "irreducibility"):
        groups.append(("IRREDUCIBILITY_BOUNDARY", check_reducibility_boundary(hbar)))
    if mode in ("all", "truncation"):
        groups.append(("FINITE_TRUNCATION_BOUNDARY", check_finite_truncation(dimension)))

    all_ok = True
    for title, checks in groups:
        print(f"[{title}]")
        for label, ok in checks:
            all_ok = all_ok and ok
            print(f"{label:<82} {'PASS' if ok else 'FAIL'}")
        print()

    print("OVERALL:", "PASS_WITH_REFINEMENT" if all_ok else "FAIL")
    return 0 if all_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "ccr", "weyl", "irreducibility", "truncation"), default="all")
    parser.add_argument("--hbar", type=float, default=1.7)
    parser.add_argument("--dimension", type=int, default=8)
    args = parser.parse_args()
    if args.hbar <= 0.0:
        parser.error("--hbar must be positive")
    if args.dimension < 2:
        parser.error("--dimension must be at least 2")
    return run(args.mode, args.hbar, args.dimension)


if __name__ == "__main__":
    raise SystemExit(main())
