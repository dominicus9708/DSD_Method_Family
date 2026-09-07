#!/usr/bin/env python3
"""
PHY-REL-007 — Standard-domain relation-layer audit.

Standard-library finite witnesses for the Track-2 capstone audit of:
  symmetry / invariance,
  curvature,
  Einstein-equation relation,
  covariant-conservation logic.

The script deliberately keeps these as standard differential-geometric / GR
comparators supplied from outside DSD. It does not derive GR from DSD, does not
identify any DSD aggregate with T_{mu nu}, and does not identify relativistic c
with DSD c_info.
"""

from __future__ import annotations

import argparse
import math


TOL = 1e-12


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    rows = len(a)
    cols = len(b[0])
    inner = len(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def transpose(a: list[list[float]]) -> list[list[float]]:
    return [list(row) for row in zip(*a)]


def max_abs_diff(a: list[list[float]], b: list[list[float]]) -> float:
    return max(abs(x - y) for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def lorentz_boost(beta: float) -> list[list[float]]:
    if not (-1.0 < beta < 1.0):
        raise ValueError("beta must satisfy |beta| < 1")
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    return [
        [gamma, -gamma * beta],
        [-gamma * beta, gamma],
    ]


def det2(a: list[list[float]]) -> float:
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def symmetry_audit(beta: float = 0.6) -> dict[str, object]:
    """Check Lambda^T eta Lambda = eta in 1+1 Minkowski space."""
    eta = [[-1.0, 0.0], [0.0, 1.0]]
    lam = lorentz_boost(beta)
    lhs = matmul(matmul(transpose(lam), eta), lam)
    error = max_abs_diff(lhs, eta)
    return {
        "beta": beta,
        "det_lambda": det2(lam),
        "metric_invariance_error": error,
        "lorentz_invariance_relation_holds": error < TOL,
        "proper_boost": abs(det2(lam) - 1.0) < TOL,
    }


def conformal_metric_at_origin(a: float) -> list[list[float]]:
    """g=e^{2 phi}(dx^2+dy^2), phi=a(x^2+y^2); at origin phi=0."""
    _ = a
    return [[1.0, 0.0], [0.0, 1.0]]


def first_metric_derivatives_at_origin(a: float) -> tuple[float, float]:
    """Both first derivatives vanish because grad phi(0,0)=0."""
    _ = a
    return (0.0, 0.0)


def gaussian_curvature_at_origin(a: float) -> float:
    """
    For g=e^{2 phi}(dx^2+dy^2), K=-e^{-2phi} Delta phi.
    phi=a(x^2+y^2), so Delta phi=4a and phi(0)=0.
    """
    return -4.0 * a


def curvature_audit() -> dict[str, object]:
    flat_a = 0.0
    curved_a = 0.25
    g_flat = conformal_metric_at_origin(flat_a)
    g_curved = conformal_metric_at_origin(curved_a)
    dg_flat = first_metric_derivatives_at_origin(flat_a)
    dg_curved = first_metric_derivatives_at_origin(curved_a)
    k_flat = gaussian_curvature_at_origin(flat_a)
    k_curved = gaussian_curvature_at_origin(curved_a)
    return {
        "same_pointwise_metric": g_flat == g_curved,
        "same_first_derivatives": dg_flat == dg_curved,
        "flat_curvature_at_origin": k_flat,
        "curved_curvature_at_origin": k_curved,
        "curvatures_differ": abs(k_flat - k_curved) > TOL,
        "pointwise_metric_and_first_jet_insufficient_for_curvature": (
            g_flat == g_curved
            and dg_flat == dg_curved
            and abs(k_flat - k_curved) > TOL
        ),
    }


def conservation_vs_einstein_audit(rho: float = 1.0) -> dict[str, object]:
    """
    Minkowski control in geometrized units with kappa=8*pi.

    G_{mu nu}=0 for Minkowski. A constant nonzero tensor
    T=diag(rho,0,0,0) has vanishing ordinary/covariant divergence in Cartesian
    Minkowski coordinates, but does not satisfy G=kappa T when rho != 0.

    This is a finite counterexample to 'conservation alone implies Einstein equation'.
    """
    kappa = 8.0 * math.pi
    g_einstein = [[0.0 for _ in range(4)] for _ in range(4)]
    stress = [[0.0 for _ in range(4)] for _ in range(4)]
    stress[0][0] = rho

    residual = [
        [g_einstein[i][j] - kappa * stress[i][j] for j in range(4)]
        for i in range(4)
    ]
    max_residual = max(abs(x) for row in residual for x in row)

    # Constant Cartesian components in Minkowski -> partial derivatives vanish,
    # and the Cartesian Christoffel symbols vanish.
    divergence = [0.0, 0.0, 0.0, 0.0]

    return {
        "rho": rho,
        "covariant_divergence_T": divergence,
        "T_is_covariantly_conserved": all(abs(x) < TOL for x in divergence),
        "einstein_equation_max_residual": max_residual,
        "einstein_equation_satisfied": max_residual < TOL,
        "conservation_does_not_imply_einstein_equation": (
            all(abs(x) < TOL for x in divergence) and max_residual > TOL
        ),
    }


def bianchi_einstein_implication_audit() -> dict[str, object]:
    """
    Algebraic implication ledger:
      div G = 0  (contracted Bianchi)
      G + Lambda g = kappa T, with constant Lambda and metric compatibility
      => div T = 0.

    This function records the implication structure, not a numerical derivation of
    an arbitrary spacetime solution.
    """
    div_g = 0.0
    div_metric = 0.0
    lambda_constant = True
    kappa_nonzero = True

    implied_div_t = 0.0 if (
        abs(div_g) < TOL and abs(div_metric) < TOL and lambda_constant and kappa_nonzero
    ) else math.nan

    return {
        "contracted_bianchi_div_G": div_g,
        "metric_compatibility_div_g": div_metric,
        "Lambda_constant": lambda_constant,
        "kappa_nonzero": kappa_nonzero,
        "EFE_plus_Bianchi_implies_div_T_zero": abs(implied_div_t) < TOL,
    }


def report() -> int:
    print("PHY-REL-007 — STANDARD-DOMAIN RELATION-LAYER AUDIT")
    print("Comparators: Lorentz invariance, differential curvature, Einstein relation, conservation.\n")

    s = symmetry_audit()
    print("[1] Symmetry / invariance")
    for key, value in s.items():
        print(f"{key}: {value}")
    print()

    c = curvature_audit()
    print("[2] Curvature / differential dependence")
    for key, value in c.items():
        print(f"{key}: {value}")
    print()

    e = conservation_vs_einstein_audit()
    print("[3] Conservation is weaker than Einstein equation")
    for key, value in e.items():
        print(f"{key}: {value}")
    print()

    b = bianchi_einstein_implication_audit()
    print("[4] Bianchi + Einstein relation -> covariant conservation")
    for key, value in b.items():
        print(f"{key}: {value}")
    print()

    assert s["lorentz_invariance_relation_holds"]
    assert s["proper_boost"]
    assert c["pointwise_metric_and_first_jet_insufficient_for_curvature"]
    assert e["T_is_covariantly_conserved"]
    assert not e["einstein_equation_satisfied"]
    assert e["conservation_does_not_imply_einstein_equation"]
    assert b["EFE_plus_Bianchi_implies_div_T_zero"]

    print("SCOPED OUTCOMES")
    print("Lorentz symmetry under supplied group action: VALID_IN_DOMAIN")
    print("symmetry label without supplied action/invariance relation: NOT_SUFFICIENT_FOR_EXTENSION")
    print("pointwise metric value -> curvature: NOT_SUFFICIENT_FOR_EXTENSION")
    print("curvature as differential-geometric relation: VALID_IN_DOMAIN")
    print("Einstein equation = one-slice state coordinate: NON_IDENTICAL")
    print("covariant conservation alone -> Einstein equation: REJECTED")
    print("EFE + contracted Bianchi -> covariant conservation: VALID_IN_DOMAIN")
    print("SUMMARY: PASS_WITH_REFINEMENT")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
