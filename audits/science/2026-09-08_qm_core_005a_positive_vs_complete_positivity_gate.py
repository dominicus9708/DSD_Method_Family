#!/usr/bin/env python3
"""QM Core 005A — Positive-vs-Complete-Positivity Gate.

Standard-library-only finite witness for the distinction between positivity on
an isolated quantum system and complete positivity under an identity extension.

The companion audit contains the general proof:
- matrix transposition is positive and trace-preserving;
- the partial transpose of a Bell state has a negative eigenvalue;
- therefore positivity does not imply complete positivity.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from typing import Iterable

Q = Fraction


def zeros(n: int) -> list[list[Q]]:
    return [[Q(0) for _ in range(n)] for _ in range(n)]


def trace(a: list[list[Q]]) -> Q:
    return sum(a[i][i] for i in range(len(a)))


def matvec(a: list[list[Q]], v: list[Q]) -> list[Q]:
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def dot(v: Iterable[Q], w: Iterable[Q]) -> Q:
    return sum(x * y for x, y in zip(v, w))


def bell_projector() -> list[list[Q]]:
    """|Phi+><Phi+| in basis |00>,|01>,|10>,|11>."""
    out = zeros(4)
    h = Q(1, 2)
    for i, j in ((0, 0), (0, 3), (3, 0), (3, 3)):
        out[i][j] = h
    return out


def partial_transpose_first_qubit(a: list[list[Q]]) -> list[list[Q]]:
    """Apply T ⊗ id to a 2-qubit operator."""
    if len(a) != 4 or any(len(row) != 4 for row in a):
        raise ValueError("expected a 4x4 two-qubit matrix")

    out = zeros(4)
    for r in range(4):
        i, alpha = divmod(r, 2)
        for c in range(4):
            j, beta = divmod(c, 2)
            out[2 * j + alpha][2 * i + beta] = a[r][c]
    return out


def run_all() -> bool:
    checks: list[tuple[str, bool]] = []

    rho = bell_projector()
    pt = partial_transpose_first_qubit(rho)

    checks.append(("Bell projector has unit trace", trace(rho) == 1))
    checks.append(("partial transpose preserves trace", trace(pt) == 1))

    psi_minus = [Q(0), Q(1), Q(-1), Q(0)]
    lhs = matvec(pt, psi_minus)
    rhs = [Q(-1, 2) * x for x in psi_minus]
    checks.append(("partial transpose has eigenvalue -1/2", lhs == rhs))

    quadratic = dot(psi_minus, lhs)
    checks.append(("partial transpose is not positive semidefinite", quadratic == -1))

    choi_normalized = pt
    choi_q = dot(psi_minus, matvec(choi_normalized, psi_minus))
    checks.append(("transpose Choi witness is negative", choi_q < 0))

    identity_extended = rho
    id_q = dot(psi_minus, matvec(identity_extended, psi_minus))
    checks.append(("identity extension remains positive on control vector", id_q >= 0))

    for name, passed in checks:
        print(f"{name:<68} {'PASS' if passed else 'FAIL'}")

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
