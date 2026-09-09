#!/usr/bin/env python3
"""QM Core 005F — Kraus / Stinespring / Environment-Unitary Realization Gate.

Finite-dimensional witnesses for:
- Kraus completeness and channel equality,
- Kraus non-uniqueness under unitary mixing,
- Stinespring isometric dilation and partial-trace recovery,
- environment-basis rotation non-uniqueness,
- finite-dimensional unitary extension with a fixed pure ancilla,
- Choi-rank/minimal-environment witness for amplitude damping,
- global-unitary reversibility versus reduced-channel irreversibility.

Only Python's standard library is used.
"""

from __future__ import annotations

import argparse
import math

Matrix = list[list[complex]]
TOL = 1e-10


def zeros(m: int, n: int) -> Matrix:
    return [[0j for _ in range(n)] for _ in range(m)]


def eye(n: int) -> Matrix:
    out = zeros(n, n)
    for i in range(n):
        out[i][i] = 1.0
    return out


def dagger(a: Matrix) -> Matrix:
    return [[a[i][j].conjugate() for i in range(len(a))] for j in range(len(a[0]))]


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


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: complex, a: Matrix) -> Matrix:
    return [[c * x for x in row] for row in a]


def kron(a: Matrix, b: Matrix) -> Matrix:
    ma, na = len(a), len(a[0])
    mb, nb = len(b), len(b[0])
    out = zeros(ma * mb, na * nb)
    for i in range(ma):
        for j in range(na):
            for r in range(mb):
                for s in range(nb):
                    out[i * mb + r][j * nb + s] = a[i][j] * b[r][s]
    return out


def close(a: complex | float, b: complex | float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def mat_close(a: Matrix, b: Matrix, tol: float = TOL) -> bool:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return False
    return all(close(a[i][j], b[i][j], tol)
               for i in range(len(a)) for j in range(len(a[0])))


def is_unitary(u: Matrix, tol: float = TOL) -> bool:
    return mat_close(matmul(dagger(u), u), eye(len(u)), tol)


def is_isometry(v: Matrix, tol: float = TOL) -> bool:
    return mat_close(matmul(dagger(v), v), eye(len(v[0])), tol)


def apply_operator(a: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(a, rho), dagger(a))


def apply_kraus(rho: Matrix, kraus: list[Matrix]) -> Matrix:
    out = zeros(len(kraus[0]), len(kraus[0]))
    for k in kraus:
        out = add(out, apply_operator(k, rho))
    return out


def partial_trace_env_2(joint: Matrix) -> Matrix:
    """Trace the second qubit in basis |system, environment>."""
    out = zeros(2, 2)
    for i in range(2):
        for j in range(2):
            out[i][j] = sum(joint[2 * i + e][2 * j + e] for e in range(2))
    return out


def matrix_rank(a: Matrix, tol: float = TOL) -> int:
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    rank = 0
    col = 0
    while rank < rows and col < cols:
        pivot = max(range(rank, rows), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) <= tol:
            col += 1
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        p = m[rank][col]
        m[rank] = [x / p for x in m[rank]]
        for r in range(rows):
            if r == rank:
                continue
            f = m[r][col]
            if abs(f) > tol:
                m[r] = [m[r][c] - f * m[rank][c] for c in range(cols)]
        rank += 1
        col += 1
    return rank


def vec(a: Matrix) -> list[complex]:
    return [a[i][j] for j in range(len(a[0])) for i in range(len(a))]


def outer(v: list[complex], w: list[complex]) -> Matrix:
    return [[x * y.conjugate() for y in w] for x in v]


def choi_from_kraus(kraus: list[Matrix]) -> Matrix:
    n = len(vec(kraus[0]))
    out = zeros(n, n)
    for k in kraus:
        vk = vec(k)
        out = add(out, outer(vk, vk))
    return out


def amplitude_damping_kraus(gamma: float) -> list[Matrix]:
    a = math.sqrt(1.0 - gamma)
    b = math.sqrt(gamma)
    return [
        [[1.0, 0.0], [0.0, a]],
        [[0.0, b], [0.0, 0.0]],
    ]


def amplitude_damping_isometry(gamma: float) -> Matrix:
    a = math.sqrt(1.0 - gamma)
    b = math.sqrt(gamma)
    return [
        [1.0, 0.0],
        [0.0, b],
        [0.0, a],
        [0.0, 0.0],
    ]


def amplitude_damping_unitary(gamma: float) -> Matrix:
    a = math.sqrt(1.0 - gamma)
    b = math.sqrt(gamma)
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, a, b, 0.0],
        [0.0, -b, a, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def basis_operators() -> list[Matrix]:
    return [
        [[1.0, 0.0], [0.0, 0.0]],
        [[0.0, 1.0], [0.0, 0.0]],
        [[0.0, 0.0], [1.0, 0.0]],
        [[0.0, 0.0], [0.0, 1.0]],
    ]


def sample_density() -> Matrix:
    return [
        [0.7, 0.15 + 0.10j],
        [0.15 - 0.10j, 0.3],
    ]


def check_kraus(gamma: float) -> list[tuple[str, bool]]:
    k0, k1 = amplitude_damping_kraus(gamma)
    completeness = add(matmul(dagger(k0), k0), matmul(dagger(k1), k1))

    invsqrt2 = 1.0 / math.sqrt(2.0)
    l0 = scale(invsqrt2, add(k0, k1))
    l1 = scale(invsqrt2, add(k0, scale(-1.0, k1)))
    mixed = [l0, l1]

    same_on_basis = all(
        mat_close(apply_kraus(x, [k0, k1]), apply_kraus(x, mixed))
        for x in basis_operators()
    )
    choi_rank = matrix_rank(choi_from_kraus([k0, k1]))

    return [
        ("Kraus completeness sum K†K = I", mat_close(completeness, eye(2))),
        ("unitary-mixed Kraus family gives the same channel", same_on_basis),
        ("amplitude-damping Choi rank is 2", choi_rank == 2),
        ("two-Kraus representation matches Choi-rank witness", len([k0, k1]) == choi_rank),
    ]


def check_dilation(gamma: float) -> list[tuple[str, bool]]:
    kraus = amplitude_damping_kraus(gamma)
    v = amplitude_damping_isometry(gamma)
    rho = sample_density()

    via_kraus = apply_kraus(rho, kraus)
    via_v = partial_trace_env_2(apply_operator(v, rho))

    h = scale(1.0 / math.sqrt(2.0), [[1.0, 1.0], [1.0, -1.0]])
    env_rotation = kron(eye(2), h)
    v_rot = matmul(env_rotation, v)
    via_v_rot = partial_trace_env_2(apply_operator(v_rot, rho))

    u = amplitude_damping_unitary(gamma)
    env0 = [[1.0, 0.0], [0.0, 0.0]]
    via_u = partial_trace_env_2(apply_operator(u, kron(rho, env0)))

    return [
        ("Stinespring map V is an isometry", is_isometry(v)),
        ("partial trace of V rho V† reproduces Kraus channel", mat_close(via_v, via_kraus)),
        ("environment rotation changes V representation", not mat_close(v_rot, v)),
        ("environment rotation leaves reduced channel unchanged", mat_close(via_v_rot, via_kraus)),
        ("finite-dimensional extension U is unitary", is_unitary(u)),
        ("U(rho⊗|0><0|)U† partial trace reproduces channel", mat_close(via_u, via_kraus)),
    ]


def check_reversibility_boundary(gamma: float) -> list[tuple[str, bool]]:
    u = amplitude_damping_unitary(gamma)
    rho0 = [[1.0, 0.0], [0.0, 0.0]]
    rho1 = [[0.0, 0.0], [0.0, 1.0]]
    out0 = apply_kraus(rho0, amplitude_damping_kraus(gamma))
    out1 = apply_kraus(rho1, amplitude_damping_kraus(gamma))

    input_trace_norm_difference = 2.0
    output_trace_norm_difference = abs(out0[0][0] - out1[0][0]) + abs(out0[1][1] - out1[1][1])

    return [
        ("global dilation U remains exactly reversible", is_unitary(u)),
        ("reduced channel strictly contracts a trace-norm witness",
         output_trace_norm_difference < input_trace_norm_difference - TOL),
        ("contraction equals 2(1-gamma)", close(output_trace_norm_difference, 2.0 * (1.0 - gamma))),
    ]


def run(mode: str, gamma: float) -> int:
    groups: list[tuple[str, list[tuple[str, bool]]]] = []
    if mode in ("all", "kraus"):
        groups.append(("KRAUS", check_kraus(gamma)))
    if mode in ("all", "dilation"):
        groups.append(("DILATION", check_dilation(gamma)))
    if mode in ("all", "reversibility"):
        groups.append(("REVERSIBILITY_BOUNDARY", check_reversibility_boundary(gamma)))

    all_ok = True
    for title, checks in groups:
        print(f"[{title}]")
        for label, ok in checks:
            all_ok = all_ok and ok
            print(f"{label:<72} {'PASS' if ok else 'FAIL'}")
        print()

    print("OVERALL:", "PASS_WITH_REFINEMENT" if all_ok else "FAIL")
    return 0 if all_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "kraus", "dilation", "reversibility"), default="all")
    parser.add_argument("--gamma", type=float, default=0.3)
    args = parser.parse_args()
    if not (0.0 < args.gamma < 1.0):
        parser.error("--gamma must satisfy 0 < gamma < 1 for the nontrivial witness.")
    return run(args.mode, args.gamma)


if __name__ == "__main__":
    raise SystemExit(main())
