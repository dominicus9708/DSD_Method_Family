#!/usr/bin/env python3
"""
QM Core 004A — DSD composition / local tomography / continuous reversibility gate.

Standard-library-only finite and parameter-count witnesses.

Run from the DSD_Method_Family repository root:
    python audits/science/2026-09-08_qm_core_004a_composition_local_tomography_gate.py --mode all
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import product


def mat_apply(M, v):
    return (
        M[0][0] * v[0] + M[0][1] * v[1],
        M[1][0] * v[0] + M[1][1] * v[1],
    )


def square_bit_gate():
    vertices = {(1, 1), (1, -1), (-1, 1), (-1, -1)}
    mats = []
    for perm in ((0, 1), (1, 0)):
        for s0, s1 in product((1, -1), repeat=2):
            M = [[0, 0], [0, 0]]
            M[0][perm[0]] = s0
            M[1][perm[1]] = s1
            M = tuple(tuple(row) for row in M)
            if {mat_apply(M, v) for v in vertices} == vertices:
                mats.append(M)

    mats = list(dict.fromkeys(mats))
    orbit = {mat_apply(M, (1, 1)) for M in mats}

    assert len(mats) == 8
    assert orbit == vertices

    return {
        "group_size": len(mats),
        "orbit_size": len(orbit),
        "pure_state_transitive": orbit == vertices,
        "continuous_transitivity_forced": False,
    }


def composition_gate():
    local_A = (0, 1)
    local_B = (0, 1)

    product_composite = [(a, b) for a, b in product(local_A, local_B)]
    relational_composite = [
        (a, b, h) for a, b, h in product(local_A, local_B, (0, 1))
    ]

    def local_readout_rel(s):
        return s[:2]

    fibers = defaultdict(list)
    for s in relational_composite:
        fibers[local_readout_rel(s)].append(s)

    max_fiber = max(len(v) for v in fibers.values())
    assert len(product_composite) == 4
    assert len(relational_composite) == 8
    assert max_fiber == 2

    return {
        "local_A_states": len(local_A),
        "local_B_states": len(local_B),
        "product_global_states": len(product_composite),
        "relational_global_states": len(relational_composite),
        "max_local_readout_fiber": max_fiber,
        "local_tomography_relational": max_fiber == 1,
        "composition_rule_unique_from_locals": False,
    }


def K_complex(d):
    return d * d


def K_real(d):
    return d * (d + 1) // 2


def standard_dimension_gate():
    complex_local = K_complex(2)
    complex_global = K_complex(4)
    real_local = K_real(2)
    real_global = K_real(4)

    complex_product = complex_local * complex_local
    real_product = real_local * real_local

    assert complex_global == complex_product == 16
    assert real_global == 10
    assert real_product == 9
    assert real_global != real_product

    return {
        "complex_local_K": complex_local,
        "complex_global_K": complex_global,
        "complex_local_product_K": complex_product,
        "complex_local_tomography_count": complex_global == complex_product,
        "real_local_K": real_local,
        "real_global_K": real_global,
        "real_local_product_K": real_product,
        "real_local_tomography_count": real_global == real_product,
        "real_global_excess": real_global - real_product,
    }


def spin_factor_survivor_gate():
    n = 4
    K = n + 1
    K_AB = K * K

    assert n != 3
    assert K == 5
    assert K_AB == 25

    return {
        "ball_dimension": n,
        "single_system_K": K,
        "locally_tomographic_product_K": K_AB,
        "continuous_pure_state_transitivity_available": True,
        "is_complex_qubit_bloch_ball": n == 3,
    }


def print_block(title, data):
    print(title)
    for key, value in data.items():
        print(f"{key:40s} {value}")
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "square", "composition", "dimensions", "spin"),
        default="all",
    )
    args = parser.parse_args()

    results = {}

    if args.mode in ("all", "square"):
        results["square"] = square_bit_gate()
        print_block("SQUARE-BIT REVERSIBILITY GATE", results["square"])

    if args.mode in ("all", "composition"):
        results["composition"] = composition_gate()
        print_block("COMPOSITION / LOCAL-READOUT GATE", results["composition"])

    if args.mode in ("all", "dimensions"):
        results["dimensions"] = standard_dimension_gate()
        print_block("REAL VS COMPLEX TOMOGRAPHY COUNT", results["dimensions"])

    if args.mode in ("all", "spin"):
        results["spin"] = spin_factor_survivor_gate()
        print_block("NON-COMPLEX LOCALLY-TOMOGRAPHIC SURVIVOR", results["spin"])

    if args.mode == "all":
        assert results["square"]["pure_state_transitive"]
        assert not results["square"]["continuous_transitivity_forced"]
        assert not results["composition"]["composition_rule_unique_from_locals"]
        assert not results["composition"]["local_tomography_relational"]
        assert results["dimensions"]["complex_local_tomography_count"]
        assert not results["dimensions"]["real_local_tomography_count"]
        assert not results["spin"]["is_complex_qubit_bloch_ball"]
        print("OVERALL: PASS_WITH_REFINEMENT")


if __name__ == "__main__":
    main()
