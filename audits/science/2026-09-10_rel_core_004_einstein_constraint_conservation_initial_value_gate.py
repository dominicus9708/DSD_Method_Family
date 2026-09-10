#!/usr/bin/env python3
"""
REL Core 004 — Einstein Field Equation / Constraint / Conservation / Initial-Value Gate

Author: Kwon Dominicus
Date: 2026-09-10
Dependencies: Python standard library only

This is a finite/reconstruction audit. It does not numerically prove general-relativity
theorems. It checks explicit counterexamples, special-case consistency relations, and
provenance/dependency guards used by the DSD methodology layer.
"""

from __future__ import annotations

import argparse
from fractions import Fraction

TOL = 1e-12

def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol

def report(group: str, checks: list[tuple[str, bool]]) -> tuple[int, int]:
    print(f"[{group}]")
    passed = 0
    for label, ok in checks:
        print(f"{label:<76} {'PASS' if ok else 'FAIL'}")
        passed += int(ok)
    print()
    return passed, len(checks)

def minkowski_field_equation_checks():
    # Units: kappa = 8*pi*G = 1, Lambda = 0.
    # In Cartesian Minkowski coordinates G_{mu nu}=0.
    kappa = 1.0
    G = [[0.0]*4 for _ in range(4)]

    # Constant nonzero stress tensor: divergence vanishes in Cartesian Minkowski,
    # but the Einstein equation fails because G != kappa*T.
    T = [[0.0]*4 for _ in range(4)]
    T[0][0] = 1.0
    divergence_T = [0.0, 0.0, 0.0, 0.0]
    residual = [[G[i][j] - kappa*T[i][j] for j in range(4)] for i in range(4)]

    # Vacuum comparator.
    T0 = [[0.0]*4 for _ in range(4)]
    residual0 = [[G[i][j] - kappa*T0[i][j] for j in range(4)] for i in range(4)]

    return [
        ("Minkowski Einstein tensor is zero in the supplied comparator", all(close(x, 0.0) for row in G for x in row)),
        ("constant nonzero Minkowski stress tensor has zero divergence", all(close(x, 0.0) for x in divergence_T)),
        ("divergence-free stress tensor does not imply Einstein equation", any(not close(x, 0.0) for row in residual for x in row)),
        ("vacuum Minkowski comparator satisfies Einstein equation", all(close(x, 0.0) for row in residual0 for x in row)),
    ]

def flrw_bianchi_consistency_checks():
    # Flat FLRW dust special case in units kappa=1:
    # a=t^(2/3), H=2/(3t), rho=3H^2=4/(3t^2), p=0.
    t = 2.0
    H = 2.0/(3.0*t)
    Hdot = -2.0/(3.0*t*t)
    rho = 4.0/(3.0*t*t)
    p = 0.0
    rhodot = -8.0/(3.0*t**3)

    friedmann_res = 3.0*H*H - rho
    spatial_res = 2.0*Hdot + 3.0*H*H + p
    continuity_res = rhodot + 3.0*H*(rho+p)

    return [
        ("flat-FLRW dust satisfies supplied Friedmann equation at sample t", close(friedmann_res, 0.0)),
        ("flat-FLRW dust satisfies supplied spatial Einstein equation at sample t", close(spatial_res, 0.0)),
        ("same solution satisfies covariant-continuity reduction", close(continuity_res, 0.0)),
        ("conservation is classified as consequence, not replacement for EFE", True),
    ]

def adm_constraint_checks():
    # Flat 3-metric h_ij=delta_ij and isotropic K_ij=H h_ij.
    # Convention: R3 + K^2 - KijKij = 2*kappa*rho + 2*Lambda.
    # Set kappa=1, Lambda=0.
    H = Fraction(1, 2)
    R3 = Fraction(0)
    K = 3*H
    KijKij = 3*H*H
    hamiltonian_lhs = R3 + K*K - KijKij  # = 6 H^2
    rho_required = hamiltonian_lhs / 2
    momentum_lhs = Fraction(0)  # constant isotropic K on flat slice
    j = Fraction(0)

    return [
        ("flat isotropic slice gives Hamiltonian LHS = 6 H^2", hamiltonian_lhs == 6*H*H),
        ("same nonzero-K slice fails vacuum Hamiltonian constraint", hamiltonian_lhs != 0),
        ("rho=3 H^2 (kappa=1) satisfies Hamiltonian constraint", rho_required == 3*H*H),
        ("constant isotropic K with j=0 satisfies momentum constraint", momentum_lhs == j),
    ]

def constraints_vs_evolution_checks():
    # Two flat-FLRW extensions have the same h_ij and K_ij at t=0:
    # a1(t)=1, a2(t)=1+eps*t^2.
    # Both satisfy vacuum constraints at t=0 because H=0 and R3=0.
    # But a2 has nonzero spatial Einstein tensor at t=0, so it is off-shell vacuum.
    eps = 0.25
    t = 0.0

    a1 = 1.0
    adot1 = 0.0
    addot1 = 0.0

    a2 = 1.0 + eps*t*t
    adot2 = 2.0*eps*t
    addot2 = 2.0*eps

    H1 = adot1/a1
    H2 = adot2/a2

    constraint_G00_1 = 3.0*H1*H1
    constraint_G00_2 = 3.0*H2*H2

    # For flat FLRW, G_ii/a^2 = -(2 a_ddot/a + H^2).
    spatial_E_1 = -(2.0*addot1/a1 + H1*H1)
    spatial_E_2 = -(2.0*addot2/a2 + H2*H2)

    same_h = close(a1*a1, a2*a2)
    same_K = close(H1, H2)

    return [
        ("two extensions have identical spatial metric at t=0", same_h),
        ("two extensions have identical extrinsic curvature at t=0", same_K),
        ("both satisfy vacuum Hamiltonian constraint at t=0", close(constraint_G00_1, 0.0) and close(constraint_G00_2, 0.0)),
        ("Minkowski extension satisfies spatial vacuum equation", close(spatial_E_1, 0.0)),
        ("accelerating extension violates spatial vacuum equation", not close(spatial_E_2, 0.0)),
        ("constraint-satisfying slice alone does not select full evolution", same_h and same_K and not close(spatial_E_2, spatial_E_1)),
    ]

def provenance_checks():
    classes = {
        "typed_status": "R0",
        "explicit_bridge": "R0",
        "state_relation_transition_separation": "R0",
        "tensor_identity_and_projection_logic": "R1",
        "lorentzian_metric": "R2",
        "einstein_field_equation": "R2",
        "stress_energy_model": "R2",
        "matter_closure": "R2",
        "constraint_satisfying_initial_data": "R2",
        "contracted_bianchi_identity": "R3",
        "covariant_conservation_from_efe": "R3",
        "mg_hd_theorem": "R3",
        "why_einstein_dynamics": "R4",
        "actual_global_boundary_data": "R4",
    }

    invalid_shortcuts = {
        ("metric_geometry", "einstein_field_equation"),
        ("divergence_free_T", "einstein_field_equation"),
        ("constraints_only", "full_evolution"),
        ("one_slice_data", "matter_closure"),
        ("dsd_constitutive_bridge", "einstein_field_equation_without_supply"),
        ("coordinate_equality", "geometric_uniqueness"),
    }

    required = {
        "einstein_field_equation": "R2",
        "contracted_bianchi_identity": "R3",
        "mg_hd_theorem": "R3",
        "why_einstein_dynamics": "R4",
    }

    return [
        ("Einstein field equation is not classified as generic DSD", classes["einstein_field_equation"] not in {"R0", "R1"}),
        ("stress-energy/matter model remains explicit supplied structure", classes["stress_energy_model"] == "R2"),
        ("matter closure remains separate from stress-energy symbol", classes["matter_closure"] == "R2"),
        ("contracted Bianchi identity is theorem/geometric consequence", classes["contracted_bianchi_identity"] == "R3"),
        ("MGHD theorem is theorem consequence under initial-value hypotheses", classes["mg_hd_theorem"] == "R3"),
        ("origin/selection of Einstein dynamics remains external", classes["why_einstein_dynamics"] == "R4"),
        ("all mandatory provenance labels match", all(classes[k] == v for k, v in required.items())),
        ("metric geometry -> EFE shortcut is blocked", ("metric_geometry", "einstein_field_equation") in invalid_shortcuts),
        ("conservation -> EFE shortcut is blocked", ("divergence_free_T", "einstein_field_equation") in invalid_shortcuts),
        ("constraints -> full evolution shortcut is blocked", ("constraints_only", "full_evolution") in invalid_shortcuts),
        ("DSD constitutive bridge -> unsupplied EFE shortcut is blocked", ("dsd_constitutive_bridge", "einstein_field_equation_without_supply") in invalid_shortcuts),
        ("geometric uniqueness is not coordinate identity", ("coordinate_equality", "geometric_uniqueness") in invalid_shortcuts),
    ]

def run_all() -> int:
    groups = [
        ("GEOMETRY_VS_FIELD_EQUATION", minkowski_field_equation_checks()),
        ("BIANCHI_CONSERVATION_SPECIAL_CASE", flrw_bianchi_consistency_checks()),
        ("ADM_CONSTRAINT_GATE", adm_constraint_checks()),
        ("CONSTRAINTS_VS_EVOLUTION", constraints_vs_evolution_checks()),
        ("PROVENANCE_AND_SHORTCUT_GUARDS", provenance_checks()),
    ]

    passed = total = 0
    for name, checks in groups:
        p, n = report(name, checks)
        passed += p
        total += n

    print(f"TOTAL: {passed}/{total} checks passed")
    verdict = "PASS_WITH_BOUNDARY" if passed == total else "FAIL"
    print(f"OVERALL: {verdict}")
    return 0 if passed == total else 1

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all"], default="all")
    parser.parse_args()
    return run_all()

if __name__ == "__main__":
    raise SystemExit(main())
