#!/usr/bin/env python3
"""QM Core 004H — exact tomographic composite tensor gate.

Standard-library-only finite linear witnesses for separating:
1) local-product readout injectivity,
2) independent product preparation/effect availability,
3) global carrier dimension,
4) exact tensor-carrier equality.

Run from repository root:
    python audits/science/2026-09-08_qm_core_004h_exact_tomographic_tensor_gate.py --mode all
"""

from __future__ import annotations

import argparse
from fractions import Fraction


def matrix_rank(rows):
    rows = [list(map(Fraction, r)) for r in rows]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if rows[i][c] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(m):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [rows[i][j] - f * rows[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def matvec(a, x):
    return tuple(
        sum(Fraction(a[i][j]) * Fraction(x[j]) for j in range(len(x)))
        for i in range(len(a))
    )


def kron_vec(a, b):
    return tuple(Fraction(x) * Fraction(y) for x in a for y in b)


def kron_matrix(a, b):
    out = []
    for row_a in a:
        for row_b in b:
            row = []
            for x in row_a:
                row.extend(Fraction(x) * Fraction(y) for y in row_b)
            out.append(tuple(row))
    return tuple(out)


def check_restricted_composite_ldc_without_full_products():
    # K_A=K_B=2, so a full tensor carrier would have dimension 4.
    # Let the global carrier be only W=span(e00,e01,e10) in R^4.
    w_basis = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
    ]
    # All four local-product coordinate readouts are available; restricted to W
    # they still separate every vector in W.
    readout_matrix_on_w = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]
    ldc_holds = matrix_rank(readout_matrix_on_w) == 3

    local_a = [(1, 0), (0, 1)]
    local_b = [(1, 0), (0, 1)]
    product_basis = [kron_vec(a, b) for a in local_a for b in local_b]
    full_product_rank = matrix_rank(product_basis)
    global_dim = matrix_rank(w_basis)

    # e11=(0,0,0,1) is an independent product basis direction but absent from W.
    missing_product = product_basis[-1] not in w_basis
    return ldc_holds and global_dim == 3 and full_product_rank == 4 and missing_product, (
        global_dim,
        full_product_rank,
        ldc_holds,
        missing_product,
    )


def check_product_availability_without_ldc():
    # R^5 contains the full four-dimensional product tensor subspace plus one
    # irreducibly global/relational coordinate h.
    product_basis_5 = [
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
    ]
    global_basis_5 = product_basis_5 + [(0, 0, 0, 0, 1)]
    local_product_readout = [
        (1, 0, 0, 0, 0),
        (0, 1, 0, 0, 0),
        (0, 0, 1, 0, 0),
        (0, 0, 0, 1, 0),
    ]
    product_available = matrix_rank(product_basis_5) == 4
    readout_rank = matrix_rank(local_product_readout)
    global_dim = matrix_rank(global_basis_5)
    hidden_h = matvec(local_product_readout, global_basis_5[-1]) == (0, 0, 0, 0)
    ldc_fails = readout_rank < global_dim and hidden_h
    return product_available and ldc_fails, (
        matrix_rank(product_basis_5),
        readout_rank,
        global_dim,
        hidden_h,
    )


def check_exact_tensor_two_sided_dimension_squeeze():
    k_a = 2
    k_b = 2
    tensor_dim = k_a * k_b

    # Independent product basis directions provide K_AB >= K_A K_B.
    product_basis = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    lower = matrix_rank(product_basis)

    # A separating local-product readout with K_A*K_B independent coordinates
    # gives K_AB <= K_A*K_B.
    local_readout = [
        (1, 0, 0, 0),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (0, 0, 0, 1),
    ]
    upper = matrix_rank(local_readout)

    exact = lower == tensor_dim == upper
    return exact, (lower, tensor_dim, upper)


def check_product_probability_factorization():
    state_a = (Fraction(3, 5), Fraction(2, 5))
    state_b = (Fraction(1, 4), Fraction(3, 4))
    effect_a = (Fraction(1), Fraction(0))
    effect_b = (Fraction(0), Fraction(1))

    p_a = sum(x * y for x, y in zip(effect_a, state_a))
    p_b = sum(x * y for x, y in zip(effect_b, state_b))
    product_state = kron_vec(state_a, state_b)
    product_effect = kron_vec(effect_a, effect_b)
    p_ab = sum(x * y for x, y in zip(product_effect, product_state))
    return p_ab == p_a * p_b == Fraction(9, 20), (p_a, p_b, p_ab)


def check_product_normalization():
    state_a = (Fraction(1, 3), Fraction(2, 3))
    state_b = (Fraction(4, 7), Fraction(3, 7))
    u_a = (Fraction(1), Fraction(1))
    u_b = (Fraction(1), Fraction(1))
    state_ab = kron_vec(state_a, state_b)
    u_ab = kron_vec(u_a, u_b)
    lhs = sum(x * y for x, y in zip(u_ab, state_ab))
    rhs = (
        sum(x * y for x, y in zip(u_a, state_a))
        * sum(x * y for x, y in zip(u_b, state_b))
    )
    return lhs == rhs == 1, (lhs, rhs)


def check_local_transformation_tensor_action():
    # This is conditional on product transformations being explicitly admitted.
    swap = ((0, 1), (1, 0))
    identity = ((1, 0), (0, 1))
    t_ab = kron_matrix(swap, identity)
    e00 = (1, 0, 0, 0)
    e10 = (0, 0, 1, 0)
    transformed = matvec(t_ab, e00)
    return transformed == e10, transformed


def run_all():
    checks = [
        (
            "LDC can hold on a restricted composite without full product availability",
            check_restricted_composite_ldc_without_full_products,
        ),
        (
            "independent product subspace can exist while LDC fails from a global coordinate",
            check_product_availability_without_ldc,
        ),
        (
            "product lower bound + LDC upper bound force exact tensor dimension",
            check_exact_tensor_two_sided_dimension_squeeze,
        ),
        ("product probability factorization witness", check_product_probability_factorization),
        ("product normalization witness", check_product_normalization),
        (
            "declared local transformations admit tensor-product action",
            check_local_transformation_tensor_action,
        ),
    ]

    ok = True
    for name, fn in checks:
        try:
            passed, detail = fn()
            ok = ok and passed
            print(f"{name:<78} {'PASS' if passed else 'FAIL'}  {detail}")
        except Exception as exc:
            ok = False
            print(f"{name:<78} FAIL  {exc}")

    print()
    print("OVERALL:", "PASS_WITH_REFINEMENT" if ok else "FAIL")
    return 0 if ok else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    _ = parser.parse_args()
    raise SystemExit(run_all())


if __name__ == "__main__":
    main()
