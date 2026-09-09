#!/usr/bin/env python3
"""QM Core 005G — Naimark / Measurement-Dilation / Instrument Realization Gate.

Finite-dimensional witnesses for:
- a genuine non-projective qubit POVM,
- Naimark isometric dilation into a projective measurement on a larger space,
- ancilla-plus-unitary realization of the same POVM,
- preservation of outcome probabilities,
- non-uniqueness of measurement realizations,
- same POVM effects with different quantum instruments/post-measurement states,
- distinction between POVM statistics and instrument dynamics.

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
    return all(
        close(a[i][j], b[i][j], tol)
        for i in range(len(a))
        for j in range(len(a[0]))
    )


def trace(a: Matrix) -> complex:
    return sum(a[i][i] for i in range(min(len(a), len(a[0]))))


def is_unitary(u: Matrix, tol: float = TOL) -> bool:
    return mat_close(matmul(dagger(u), u), eye(len(u)), tol)


def is_isometry(v: Matrix, tol: float = TOL) -> bool:
    return mat_close(matmul(dagger(v), v), eye(len(v[0])), tol)


def is_projection(p: Matrix, tol: float = TOL) -> bool:
    return mat_close(matmul(p, p), p, tol) and mat_close(dagger(p), p, tol)


def apply_operator(a: Matrix, rho: Matrix) -> Matrix:
    return matmul(matmul(a, rho), dagger(a))


def partial_trace_env_2(joint: Matrix) -> Matrix:
    out = zeros(2, 2)
    for i in range(2):
        for j in range(2):
            out[i][j] = sum(joint[2 * i + e][2 * j + e] for e in range(2))
    return out


def normalize_branch(x: Matrix) -> Matrix:
    p = trace(x).real
    if p <= TOL:
        raise ValueError("Cannot normalize zero-probability branch.")
    return scale(1.0 / p, x)


def binary_unsharp_povm(a: float, b: float) -> tuple[Matrix, Matrix]:
    e0 = [[a, 0.0], [0.0, b]]
    e1 = [[1.0 - a, 0.0], [0.0, 1.0 - b]]
    return e0, e1


def measurement_operators(a: float, b: float) -> tuple[Matrix, Matrix]:
    m0 = [[math.sqrt(a), 0.0], [0.0, math.sqrt(b)]]
    m1 = [[math.sqrt(1.0 - a), 0.0], [0.0, math.sqrt(1.0 - b)]]
    return m0, m1


def naimark_isometry(a: float, b: float) -> Matrix:
    m0, m1 = measurement_operators(a, b)
    return [
        [m0[0][0], 0.0],
        [m1[0][0], 0.0],
        [0.0, m0[1][1]],
        [0.0, m1[1][1]],
    ]


def ancilla_projectors() -> tuple[Matrix, Matrix]:
    p0 = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
    ]
    p1 = [
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]
    return p0, p1


def ancilla_unitary(a: float, b: float) -> Matrix:
    sa, ca = math.sqrt(a), math.sqrt(1.0 - a)
    sb, cb = math.sqrt(b), math.sqrt(1.0 - b)
    return [
        [sa, -ca, 0.0, 0.0],
        [ca,  sa, 0.0, 0.0],
        [0.0, 0.0, sb, -cb],
        [0.0, 0.0, cb,  sb],
    ]


def outcome_controlled_system_x() -> Matrix:
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
    ]


def branch_from_joint(joint: Matrix, projector: Matrix) -> Matrix:
    selected = matmul(matmul(projector, joint), projector)
    return partial_trace_env_2(selected)


def sample_density() -> Matrix:
    return [[0.5, 0.5], [0.5, 0.5]]


def check_povm_and_naimark(a: float, b: float) -> list[tuple[str, bool]]:
    e0, e1 = binary_unsharp_povm(a, b)
    v = naimark_isometry(a, b)
    p0, p1 = ancilla_projectors()
    pulled0 = matmul(matmul(dagger(v), p0), v)
    pulled1 = matmul(matmul(dagger(v), p1), v)

    return [
        ("POVM effects sum to I", mat_close(add(e0, e1), eye(2))),
        ("E0 is genuinely non-projective", not is_projection(e0)),
        ("E1 is genuinely non-projective", not is_projection(e1)),
        ("Naimark V is an isometry", is_isometry(v)),
        ("dilated outcome projectors are projective", is_projection(p0) and is_projection(p1)),
        ("dilated projectors are orthogonal", mat_close(matmul(p0, p1), zeros(4, 4))),
        ("dilated projectors sum to I", mat_close(add(p0, p1), eye(4))),
        ("V† P0 V = E0", mat_close(pulled0, e0)),
        ("V† P1 V = E1", mat_close(pulled1, e1)),
    ]


def check_unitary_realization(a: float, b: float) -> list[tuple[str, bool]]:
    e0, e1 = binary_unsharp_povm(a, b)
    m0, m1 = measurement_operators(a, b)
    u = ancilla_unitary(a, b)
    p0, p1 = ancilla_projectors()
    rho = sample_density()
    anc0 = [[1.0, 0.0], [0.0, 0.0]]
    joint = apply_operator(u, kron(rho, anc0))
    b0 = branch_from_joint(joint, p0)
    b1 = branch_from_joint(joint, p1)

    p0_direct = trace(matmul(e0, rho)).real
    p1_direct = trace(matmul(e1, rho)).real

    return [
        ("ancilla realization U is unitary", is_unitary(u)),
        ("outcome-0 branch equals M0 rho M0†", mat_close(b0, apply_operator(m0, rho))),
        ("outcome-1 branch equals M1 rho M1†", mat_close(b1, apply_operator(m1, rho))),
        ("outcome-0 probability matches Tr(E0 rho)", close(trace(b0).real, p0_direct)),
        ("outcome-1 probability matches Tr(E1 rho)", close(trace(b1).real, p1_direct)),
        ("outcome probabilities normalize", close(trace(b0).real + trace(b1).real, 1.0)),
    ]


def check_instrument_nonuniqueness(a: float, b: float) -> list[tuple[str, bool]]:
    e0, e1 = binary_unsharp_povm(a, b)
    m0, m1 = measurement_operators(a, b)
    x = [[0.0, 1.0], [1.0, 0.0]]
    n0 = m0
    n1 = matmul(x, m1)

    effect_n0 = matmul(dagger(n0), n0)
    effect_n1 = matmul(dagger(n1), n1)

    rho = sample_density()
    l0 = apply_operator(m0, rho)
    l1 = apply_operator(m1, rho)
    alt0 = apply_operator(n0, rho)
    alt1 = apply_operator(n1, rho)

    luders_total = add(l0, l1)
    alt_total = add(alt0, alt1)

    u = ancilla_unitary(a, b)
    w = outcome_controlled_system_x()
    u_alt = matmul(w, u)

    anc0 = [[1.0, 0.0], [0.0, 0.0]]
    p0, p1 = ancilla_projectors()
    joint = apply_operator(u, kron(rho, anc0))
    joint_alt = apply_operator(u_alt, kron(rho, anc0))
    base_probabilities = [trace(branch_from_joint(joint, p)).real for p in (p0, p1)]
    alt_probabilities = [trace(branch_from_joint(joint_alt, p)).real for p in (p0, p1)]

    return [
        ("alternative instrument has the same E0", mat_close(effect_n0, e0)),
        ("alternative instrument has the same E1", mat_close(effect_n1, e1)),
        ("same POVM gives identical outcome probabilities", all(close(x, y) for x, y in zip(base_probabilities, alt_probabilities))),
        ("conditional outcome-1 states differ", not mat_close(normalize_branch(l1), normalize_branch(alt1))),
        ("nonselective channels differ", not mat_close(luders_total, alt_total)),
        ("alternative indirect-measurement unitary is unitary", is_unitary(u_alt)),
    ]


def run(mode: str, a: float, b: float) -> int:
    groups: list[tuple[str, list[tuple[str, bool]]]] = []
    if mode in ("all", "naimark"):
        groups.append(("NAIMARK", check_povm_and_naimark(a, b)))
    if mode in ("all", "unitary"):
        groups.append(("UNITARY_REALIZATION", check_unitary_realization(a, b)))
    if mode in ("all", "instrument"):
        groups.append(("INSTRUMENT_NONUNIQUENESS", check_instrument_nonuniqueness(a, b)))

    all_ok = True
    for title, checks in groups:
        print(f"[{title}]")
        for label, ok in checks:
            all_ok = all_ok and ok
            print(f"{label:<74} {'PASS' if ok else 'FAIL'}")
        print()

    print("OVERALL:", "PASS_WITH_REFINEMENT" if all_ok else "FAIL")
    return 0 if all_ok else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all", "naimark", "unitary", "instrument"), default="all")
    parser.add_argument("--a", type=float, default=0.8)
    parser.add_argument("--b", type=float, default=0.2)
    args = parser.parse_args()
    if not (0.0 < args.a < 1.0 and 0.0 < args.b < 1.0):
        parser.error("--a and --b must lie strictly between 0 and 1.")
    if close(args.a, args.b):
        parser.error("--a and --b should differ for the nontrivial witness.")
    return run(args.mode, args.a, args.b)


if __name__ == "__main__":
    raise SystemExit(main())
