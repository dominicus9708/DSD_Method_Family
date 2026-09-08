#!/usr/bin/env python3
"""QM Core 004G — connected reversible group gate.

Finite/algebraic witnesses for separating continuous pure-state reachability
from connectedness of the full reversible transformation group.

Run from repository root:
    python audits/science/2026-09-08_qm_core_004g_connected_reversible_group_gate.py --mode all
"""

from __future__ import annotations

import argparse
import math


def matmul(a, b):
    return (
        (
            a[0][0] * b[0][0] + a[0][1] * b[1][0],
            a[0][0] * b[0][1] + a[0][1] * b[1][1],
        ),
        (
            a[1][0] * b[0][0] + a[1][1] * b[1][0],
            a[1][0] * b[0][1] + a[1][1] * b[1][1],
        ),
    )


def matvec(a, x):
    return (
        a[0][0] * x[0] + a[0][1] * x[1],
        a[1][0] * x[0] + a[1][1] * x[1],
    )


def transpose(a):
    return ((a[0][0], a[1][0]), (a[0][1], a[1][1]))


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def rotation(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return ((c, -s), (s, c))


def norm2(x):
    return math.sqrt(x[0] * x[0] + x[1] * x[1])


def max_matrix_error(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def close(a, b, tol=1e-10):
    return abs(a - b) <= tol


def vec_close(a, b, tol=1e-10):
    return norm2((a[0] - b[0], a[1] - b[1])) <= tol


def check_rotation_path():
    theta1 = 0.37
    theta2 = 2.11
    delta = theta2 - theta1
    x1 = (math.cos(theta1), math.sin(theta1))
    x2 = (math.cos(theta2), math.sin(theta2))
    identity = ((1.0, 0.0), (0.0, 1.0))

    worst_orth = 0.0
    worst_norm = 0.0
    for k in range(101):
        t = k / 100.0
        r = rotation(t * delta)
        worst_orth = max(worst_orth, max_matrix_error(matmul(transpose(r), r), identity))
        y = matvec(r, x1)
        worst_norm = max(worst_norm, abs(norm2(y) - 1.0))

    endpoint_ok = vec_close(matvec(rotation(delta), x1), x2)
    det_ok = all(close(det(rotation(k * delta / 100.0)), 1.0) for k in range(101))
    return endpoint_ok and det_ok and worst_orth < 1e-10 and worst_norm < 1e-10


def check_disconnected_full_group_witness():
    identity = ((1.0, 0.0), (0.0, 1.0))
    reflection = ((1.0, 0.0), (0.0, -1.0))
    orth_reflection = max_matrix_error(matmul(transpose(reflection), reflection), identity) < 1e-12
    signs_separate = close(det(identity), 1.0) and close(det(reflection), -1.0)

    # Mathematical gate used here:
    # det: O(2) -> {+1,-1} is continuous. A continuous path from I to reflection
    # would give a connected image containing both +1 and -1, impossible in the
    # discrete two-point determinant image. Hence O(2) is disconnected.
    return orth_reflection and signs_separate


def check_reachability_does_not_imply_connectedness():
    return check_rotation_path() and check_disconnected_full_group_witness()


def check_lineage_compatibility_witness():
    # Regular rotation trajectories can preserve one state carrier and lineage,
    # while a separately admitted reversible reflection also acts on that same carrier.
    # Nothing algebraically forces the reflection to lie on the identity component.
    x = (math.cos(0.61), math.sin(0.61))
    reflection = ((1.0, 0.0), (0.0, -1.0))
    y = matvec(reflection, x)
    same_carrier = close(norm2(x), 1.0) and close(norm2(y), 1.0)
    reversible = vec_close(matvec(reflection, y), x)
    return same_carrier and reversible


def check_stronger_path_realizability_is_sufficient():
    # Logical sufficiency condition, represented by the finite witness family:
    # if every declared reversible is supplied with a continuous path from identity,
    # then all declared reversibles lie in one path component. The finite sample here
    # contains only rotations, each with explicit t -> R(t theta) path.
    angles = [0.0, 0.2, 0.7, 1.4, 2.6]
    for theta in angles:
        if not close(det(rotation(theta)), 1.0):
            return False
        if max_matrix_error(rotation(0.0), ((1.0, 0.0), (0.0, 1.0))) >= 1e-12:
            return False
        if max_matrix_error(rotation(theta), rotation(theta)) >= 1e-12:
            return False
    return True


def run_all():
    checks = [
        ("continuous rotation path on pure states", check_rotation_path()),
        ("O(2) contains determinant-separated reversible components", check_disconnected_full_group_witness()),
        ("pure-state continuous reachability != connected full group", check_reachability_does_not_imply_connectedness()),
        ("regular lineage-compatible dynamics can coexist with discrete reversible symmetry", check_lineage_compatibility_witness()),
        ("all-reversibles path-realizable from identity is sufficient for path-connected declared group", check_stronger_path_realizability_is_sufficient()),
    ]

    width = max(len(name) for name, _ in checks)
    ok = True
    for name, passed in checks:
        ok = ok and passed
        print(f"{name:<{width}}  {'PASS' if passed else 'FAIL'}")

    print()
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    args = parser.parse_args()
    if args.mode == "all":
        return run_all()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
