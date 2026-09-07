#!/usr/bin/env python3
"""
Standard-QM + special-relativity typed-interface audit for DSD research.

This script deliberately avoids alternative quantum-gravity models.
It checks four structural points using only elementary finite-dimensional
quantum mechanics, Lorentz kinematics, and explicit type separation:

1. Z-only qubit readout is not informationally complete; XYZ is.
2. A Lorentz boost is invertible and therefore is not, by itself, a lossy
   readout of an event coordinate record.
3. Local operations on separate tensor factors commute exactly in the test.
4. Equal finite cardinalities do not create a declared cross-type bridge.

No DSD gravitational law is encoded here.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Iterable, Sequence


# -----------------------------------------------------------------------------
# Small linear-algebra helpers
# -----------------------------------------------------------------------------


def matrix_rank(rows: Sequence[Sequence[float]], tol: float = 1e-12) -> int:
    a = [list(map(float, row)) for row in rows]
    if not a:
        return 0
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        pivot = max(range(r, m), key=lambda i: abs(a[i][c]), default=r)
        if r >= m or abs(a[pivot][c]) <= tol:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        piv = a[r][c]
        a[r] = [x / piv for x in a[r]]
        for i in range(m):
            if i == r:
                continue
            fac = a[i][c]
            if abs(fac) > tol:
                a[i] = [x - fac * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def matmul(a: Sequence[Sequence[complex]], b: Sequence[Sequence[complex]]):
    m = len(a)
    k = len(a[0])
    assert k == len(b)
    n = len(b[0])
    return [
        [sum(a[i][t] * b[t][j] for t in range(k)) for j in range(n)]
        for i in range(m)
    ]


def kron(a: Sequence[Sequence[complex]], b: Sequence[Sequence[complex]]):
    out = []
    for row_a in a:
        for row_b in b:
            row = []
            for x in row_a:
                row.extend(x * y for y in row_b)
            out.append(row)
    return out


def matrices_equal(a, b, tol: float = 1e-12) -> bool:
    return all(
        abs(a[i][j] - b[i][j]) <= tol
        for i in range(len(a))
        for j in range(len(a[0]))
    )


# -----------------------------------------------------------------------------
# Audit 1: qubit tomography as readout-fiber test
# -----------------------------------------------------------------------------


def tomography_audit() -> dict[str, int | bool]:
    # In Bloch-vector coordinates, expectation values of X,Y,Z read the
    # corresponding components. Z-only therefore has rank 1; XYZ rank 3.
    z_only = [[0.0, 0.0, 1.0]]
    xyz = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]
    rz = matrix_rank(z_only)
    rxyz = matrix_rank(xyz)
    return {
        "z_rank": rz,
        "xyz_rank": rxyz,
        "z_informationally_complete": rz == 3,
        "xyz_informationally_complete": rxyz == 3,
    }


# -----------------------------------------------------------------------------
# Audit 2: Lorentz boost invertibility
# -----------------------------------------------------------------------------


def lorentz_boost_x(beta: float):
    if not (-1.0 < beta < 1.0):
        raise ValueError("beta must satisfy |beta| < 1")
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    # Coordinates ordered as (ct, x, y, z).
    return [
        [gamma, -gamma * beta, 0.0, 0.0],
        [-gamma * beta, gamma, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def determinant_4x4(m) -> float:
    # Gaussian elimination determinant, sufficient for the numerical audit.
    a = [list(map(float, row)) for row in m]
    det = 1.0
    sign = 1.0
    n = 4
    for c in range(n):
        pivot = max(range(c, n), key=lambda i: abs(a[i][c]))
        if abs(a[pivot][c]) < 1e-14:
            return 0.0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            sign *= -1.0
        piv = a[c][c]
        det *= piv
        for i in range(c + 1, n):
            fac = a[i][c] / piv
            for j in range(c, n):
                a[i][j] -= fac * a[c][j]
    return sign * det


def lorentz_audit(beta: float = 0.6) -> dict[str, float | bool]:
    lam = lorentz_boost_x(beta)
    det = determinant_4x4(lam)
    return {
        "beta": beta,
        "determinant": det,
        "invertible": abs(det) > 1e-12,
        "det_close_to_one": abs(det - 1.0) < 1e-10,
    }


# -----------------------------------------------------------------------------
# Audit 3: local tensor-factor operation ordering
# -----------------------------------------------------------------------------


def local_operation_order_audit() -> dict[str, bool]:
    I = [[1 + 0j, 0j], [0j, 1 + 0j]]
    X = [[0j, 1 + 0j], [1 + 0j, 0j]]
    Z = [[1 + 0j, 0j], [0j, -1 + 0j]]

    ua = kron(X, I)
    ub = kron(I, Z)
    ab = matmul(ua, ub)
    ba = matmul(ub, ua)

    return {
        "UA_UB_equals_UB_UA": matrices_equal(ab, ba),
    }


# -----------------------------------------------------------------------------
# Audit 4: typed-dimension non-identification
# -----------------------------------------------------------------------------


@dataclass(frozen=True)
class TypedSpace:
    name: str
    cardinality: int
    semantic_type: str


def typed_dimension_audit() -> dict[str, object]:
    spaces = [
        TypedSpace("Hilbert basis labels", 4, "quantum_state_representation"),
        TypedSpace("spacetime coordinate indices", 4, "manifold_coordinate_index"),
        TypedSpace("DSD selected channels", 4, "dsd_channel_index"),
    ]
    equal_cardinality = len({s.cardinality for s in spaces}) == 1
    same_semantic_type = len({s.semantic_type for s in spaces}) == 1
    declared_bridges: list[tuple[str, str]] = []
    return {
        "equal_cardinality": equal_cardinality,
        "same_semantic_type": same_semantic_type,
        "declared_bridge_count": len(declared_bridges),
        "automatic_identification_allowed": same_semantic_type and bool(declared_bridges),
    }


# -----------------------------------------------------------------------------
# Main report
# -----------------------------------------------------------------------------


def report() -> int:
    print("STANDARD QM + SR TYPED INTERFACE AUDIT")
    print("No alternative quantum-gravity theory is used.\n")

    t = tomography_audit()
    print("[1] Qubit tomography")
    for k, v in t.items():
        print(f"{k}: {v}")
    print()

    l = lorentz_audit()
    print("[2] Lorentz boost")
    for k, v in l.items():
        print(f"{k}: {v}")
    print()

    o = local_operation_order_audit()
    print("[3] Local tensor-factor order")
    for k, v in o.items():
        print(f"{k}: {v}")
    print()

    d = typed_dimension_audit()
    print("[4] Typed dimensions")
    for k, v in d.items():
        print(f"{k}: {v}")
    print()

    assert t["z_rank"] == 1
    assert t["xyz_rank"] == 3
    assert not t["z_informationally_complete"]
    assert t["xyz_informationally_complete"]
    assert l["invertible"]
    assert l["det_close_to_one"]
    assert o["UA_UB_equals_UB_UA"]
    assert d["equal_cardinality"]
    assert not d["same_semantic_type"]
    assert d["declared_bridge_count"] == 0
    assert not d["automatic_identification_allowed"]

    print("AUDIT RESULT: PASS_WITH_BOUNDARY")
    print("- measurement completeness is map-dependent")
    print("- invertible coordinate change is not information loss")
    print("- factorized local quantum operations commute in the test")
    print("- equal dimension counts do not create a cross-theory identity")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
