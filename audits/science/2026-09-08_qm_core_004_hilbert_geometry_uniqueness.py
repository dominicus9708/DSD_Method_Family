#!/usr/bin/env python3
"""
QM Core 004 — Hilbert/effect geometry uniqueness pressure test.

Standard library only. Uses exact Fractions for finite witnesses.

This script checks:
1) a non-Hilbert square state space satisfies basic DSD-style operational gates:
   bounded normalized convex carrier (finite vertex witness), positive normalized effects,
   separating readouts, finite measurement normalization, and pure-state transitivity
   under a reversible symmetry group;
2) pure-state transitivity alone does not force Hilbert geometry;
3) local-tomography dimension counting distinguishes complex from real quantum theory
   for two-level systems;
4) therefore current DSD generic structure does not by itself select complex Hilbert
   geometry; stronger cross-paper composition/symmetry assumptions are required.
"""

from fractions import Fraction
from itertools import combinations
import argparse

F = Fraction

# ---------------------------------------------------------------------
# Square-bit finite operational witness
# ---------------------------------------------------------------------

UNIT = (F(1), F(0), F(0))

SQUARE_STATES = (
    (F(1), F(1)),
    (F(-1), F(1)),
    (F(-1), F(-1)),
    (F(1), F(-1)),
)

# affine effect e(x,y) = a + b x + c y
EFFECTS = {
    "X+": (F(1, 2), F(1, 2), F(0)),
    "X-": (F(1, 2), F(-1, 2), F(0)),
    "Y+": (F(1, 2), F(0), F(1, 2)),
    "Y-": (F(1, 2), F(0), F(-1, 2)),
}

CONTEXTS = (
    ("X+", "X-"),
    ("Y+", "Y-"),
)

def eval_effect(effect, state):
    a, b, c = effect
    x, y = state
    return a + b*x + c*y

def effect_is_valid(effect):
    return all(F(0) <= eval_effect(effect, s) <= F(1) for s in SQUARE_STATES)

def contexts_are_normalized():
    for names in CONTEXTS:
        for s in SQUARE_STATES:
            if sum(eval_effect(EFFECTS[n], s) for n in names) != F(1):
                return False
    return True

def effects_separate_vertices():
    for s, t in combinations(SQUARE_STATES, 2):
        if not any(eval_effect(e, s) != eval_effect(e, t) for e in EFFECTS.values()):
            return False
    return True

def rot90(state):
    x, y = state
    return (-y, x)

def orbit(seed, steps=4):
    out = []
    x = seed
    for _ in range(steps):
        out.append(x)
        x = rot90(x)
    return tuple(out)

def pure_transitivity_witness():
    return set(orbit(SQUARE_STATES[0], 4)) == set(SQUARE_STATES)

# ---------------------------------------------------------------------
# Local-tomography dimension witness
# ---------------------------------------------------------------------

def K_complex(d):
    # real dimension of Hermitian dxd matrices
    return d*d

def K_real(d):
    # real dimension of real symmetric dxd matrices
    return d*(d+1)//2

def local_tomography_dimension_check(Kfun, da=2, db=2):
    lhs = Kfun(da*db)
    rhs = Kfun(da)*Kfun(db)
    return lhs, rhs, lhs == rhs

# ---------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------

def run_square():
    print("SQUARE-BIT NON-HILBERT WITNESS")
    print("all selected effects valid:", all(effect_is_valid(e) for e in EFFECTS.values()))
    print("measurement contexts normalized:", contexts_are_normalized())
    print("selected effects separate pure vertices:", effects_separate_vertices())
    print("90-degree reversible symmetry transitive on 4 pure vertices:", pure_transitivity_witness())
    print("pure vertex count:", len(SQUARE_STATES))
    print("RESULT: basic bounded/normalized/separating/transitive gates do not uniquely force Hilbert geometry.")

def run_local_tomography():
    print("LOCAL-TOMOGRAPHY DIMENSION WITNESS")
    c_lhs, c_rhs, c_ok = local_tomography_dimension_check(K_complex)
    r_lhs, r_rhs, r_ok = local_tomography_dimension_check(K_real)
    print(f"complex 2x2 composite: K_AB={c_lhs}, K_A*K_B={c_rhs}, local-tomography dimension match={c_ok}")
    print(f"real 2x2 composite:    K_AB={r_lhs}, K_A*K_B={r_rhs}, local-tomography dimension match={r_ok}")
    print(f"real-theory excess global parameters over local-product count: {r_lhs-r_rhs}")
    print("RESULT: local tomography is a substantive discriminator; it is not implied by generic DSD finite composition.")

def run_all():
    run_square()
    print()
    run_local_tomography()
    print()
    checks = [
        all(effect_is_valid(e) for e in EFFECTS.values()),
        contexts_are_normalized(),
        effects_separate_vertices(),
        pure_transitivity_witness(),
        local_tomography_dimension_check(K_complex)[2],
        not local_tomography_dimension_check(K_real)[2],
    ]
    print("OVERALL:", "PASS_WITH_REFINEMENT" if all(checks) else "FAIL")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["all", "square", "local-tomography"], default="all")
    args = p.parse_args()
    if args.mode == "square":
        run_square()
    elif args.mode == "local-tomography":
        run_local_tomography()
    else:
        run_all()

if __name__ == "__main__":
    main()
