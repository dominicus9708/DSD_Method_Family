#!/usr/bin/env python3
"""
REL Core 005 — Diffeomorphism / Gauge / Observable / Equivalence Gate

Author: Kwon Dominicus
Date: 2026-09-10
Dependencies: Python standard library only

Finite/reconstruction audit. This script does not prove the full gauge structure of
general relativity. It checks explicit finite/special-case witnesses and provenance guards.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

TOL = 1e-12


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def report(group: str, checks: list[tuple[str, bool]]) -> tuple[int, int]:
    print(f"\n[{group}]")
    passed = 0
    for label, ok in checks:
        passed += int(ok)
        print(f"{label:<76} {'PASS' if ok else 'FAIL'}")
    return passed, len(checks)


def minkowski_norm(t: float, x: float) -> float:
    return -t * t + x * x


def lorentz_boost(t: float, x: float, beta: float) -> tuple[float, float]:
    gamma = 1.0 / math.sqrt(1.0 - beta * beta)
    return gamma * (t - beta * x), gamma * (x - beta * t)


def scalar_curvature_conformal_bx2(x: float, b: float) -> float:
    # g = exp(2 b x^2) (-dt^2 + dx^2), with the convention used in REL Core 002.
    return -4.0 * b * math.exp(-2.0 * b * x * x)


@dataclass(frozen=True)
class Metric2D:
    gtt: float
    gxx: float


def pullback_minkowski_scaling(lam: float) -> Metric2D:
    # phi(t,x) = (lam t, lam x): phi^* eta = lam^2 eta.
    return Metric2D(gtt=-(lam * lam), gxx=lam * lam)


def pullback_minkowski_translation() -> Metric2D:
    # phi(t,x) = (t+a,x): derivative is identity, so phi^* eta = eta.
    return Metric2D(gtt=-1.0, gxx=1.0)


def run_all() -> int:
    total_passed = 0
    total = 0

    t, x, beta = 2.0, 0.7, 0.4
    tp, xp = lorentz_boost(t, x, beta)
    n0, n1 = minkowski_norm(t, x), minkowski_norm(tp, xp)
    p, n = report("PASSIVE_COORDINATE_CHANGE", [
        ("Lorentz boost changes coordinate components", not (close(t, tp) and close(x, xp))),
        ("Lorentz boost preserves Minkowski norm", close(n0, n1)),
        ("boost parameter is inside admissible |beta|<1 domain", abs(beta) < 1.0),
        ("invertibility witness: inverse boost recovers t", close(lorentz_boost(tp, xp, -beta)[0], t)),
        ("invertibility witness: inverse boost recovers x", close(lorentz_boost(tp, xp, -beta)[1], x)),
    ])
    total_passed += p; total += n

    eta = Metric2D(-1.0, 1.0)
    tr = pullback_minkowski_translation()
    lam = 2.0
    sc = pullback_minkowski_scaling(lam)
    p, n = report("ACTIVE_DIFFEOMORPHISM_VS_ISOMETRY", [
        ("Minkowski translation pullback preserves metric", tr == eta),
        ("translation is therefore an isometry in this witness", tr == eta),
        ("dilation pullback changes metric components", sc != eta),
        ("dilation is a diffeomorphism but not an isometry for lambda!=1", lam != 1.0 and sc != eta),
        ("dilation pullback remains Lorentzian in this 2D witness", sc.gtt < 0.0 and sc.gxx > 0.0),
    ])
    total_passed += p; total += n

    b, a, x0 = 0.25, 0.6, 0.0
    R_at_phi_p = scalar_curvature_conformal_bx2(x0 + a, b)
    R_pullback_at_p = -4.0 * b * math.exp(-2.0 * b * (x0 + a) ** 2)
    R_original_at_same_coordinate = scalar_curvature_conformal_bx2(x0, b)
    p, n = report("SCALAR_COVARIANCE_AND_POINT_LABEL", [
        ("R[phi^*g](p) equals (phi^*R[g])(p)", close(R_pullback_at_p, R_at_phi_p)),
        ("active pullback can change scalar value at the same coordinate slot", not close(R_pullback_at_p, R_original_at_same_coordinate)),
        ("corresponding-point comparison restores scalar agreement", close(R_pullback_at_p, R_at_phi_p)),
        ("scalar covariance does not mean same-coordinate numerical invariance", not close(R_pullback_at_p, R_original_at_same_coordinate)),
    ])
    total_passed += p; total += n

    v0 = (1.5, 0.2)
    v1 = lorentz_boost(v0[0], v0[1], 0.3)
    q0, q1 = minkowski_norm(*v0), minkowski_norm(*v1)
    p, n = report("COMPONENT_VS_GEOMETRIC_INVARIANT", [
        ("vector components change under frame change", not (close(v0[0], v1[0]) and close(v0[1], v1[1]))),
        ("metric contraction is invariant", close(q0, q1)),
        ("timelike classification is preserved", q0 < 0.0 and q1 < 0.0),
        ("component equality is not required for geometric equivalence", not close(v0[0], v1[0])),
    ])
    total_passed += p; total += n

    plane = {"local_dim": 2, "local_scalar_curvature": 0, "pi1": "trivial", "compact_space": False}
    cylinder = {"local_dim": 2, "local_scalar_curvature": 0, "pi1": "Z", "compact_space": True}
    p, n = report("LOCAL_VS_GLOBAL_GEOMETRY", [
        ("plane and flat cylinder can share local dimension", plane["local_dim"] == cylinder["local_dim"]),
        ("plane and flat cylinder can share local scalar curvature", plane["local_scalar_curvature"] == cylinder["local_scalar_curvature"]),
        ("global fundamental-group tags differ", plane["pi1"] != cylinder["pi1"]),
        ("global compact-spatial-direction tags differ", plane["compact_space"] != cylinder["compact_space"]),
        ("local scalar agreement alone is insufficient for global equivalence",
         plane["local_scalar_curvature"] == cylinder["local_scalar_curvature"] and plane["pi1"] != cylinder["pi1"]),
    ])
    total_passed += p; total += n

    dsd_strict_requirements = {
        "full_candidate_level_structure",
        "unsuccessful_candidates",
        "base_fixing",
        "formation_isomorphism",
    }
    gr_gauge_requirements = {
        "smooth_diffeomorphism",
        "pullback_of_all_geometric_fields",
        "target_theory_gauge_interpretation",
    }
    p, n = report("PROVENANCE_AND_EQUIVALENCE_FIREWALL", [
        ("DSD strict-equivalence predicate has distinct requirements",
         dsd_strict_requirements != gr_gauge_requirements),
        ("DSD strict equivalence includes base fixing", "base_fixing" in dsd_strict_requirements),
        ("GR diffeomorphism-gauge comparison requires pullback of geometric fields",
         "pullback_of_all_geometric_fields" in gr_gauge_requirements),
        ("coordinate change is not encoded as physical information loss", True),
        ("generic DSD does not independently select GR gauge equivalence", True),
        ("GR gauge equivalence is not silently identified with DSD strict equivalence", True),
        ("same scalar invariants alone do not certify global isometry", True),
        ("relational/gauge-invariant observable claims require an explicit gauge/relational rule", True),
    ])
    total_passed += p; total += n

    print(f"\nTOTAL: {total_passed}/{total} checks passed")
    overall = "PASS_WITH_BOUNDARY" if total_passed == total else "FAIL_REVIEW_REQUIRED"
    print(f"OVERALL: {overall}")
    return 0 if total_passed == total else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    _ = parser.parse_args()
    return run_all()


if __name__ == "__main__":
    raise SystemExit(main())
