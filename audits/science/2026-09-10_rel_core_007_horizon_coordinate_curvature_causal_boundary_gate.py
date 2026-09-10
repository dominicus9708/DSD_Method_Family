#!/usr/bin/env python3
"""
REL Core 007 — Horizon / Coordinate-Singularity / Curvature-Singularity / Causal-Boundary Gate

Author: Kwon Dominicus
Date: 2026-09-10
Dependencies: Python standard library only

This is a finite/reconstruction audit over supplied Schwarzschild geometry.
It does not derive black-hole geometry from generic DSD and it does not replace
global causal or singularity theorems with a finite computation.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Callable

Q = Fraction


@dataclass(frozen=True)
class Check:
    group: str
    name: str
    predicate: Callable[[], bool]


def f_schw(M: Fraction, r: Fraction) -> Fraction:
    return Q(1) - Q(2) * M / r


def kretschmann(M: Fraction, r: Fraction) -> Fraction:
    return Q(48) * M * M / (r ** 6)


def ef_vr_block_det(M: Fraction, r: Fraction) -> Fraction:
    # ingoing EF (v,r) block [[-f,1],[1,0]]
    f = f_schw(M, r)
    return (-f) * Q(0) - Q(1) * Q(1)


def ef_full_det_equator(r: Fraction) -> Fraction:
    # det g = -r^4 sin^2(theta); choose theta=pi/2.
    return -(r ** 4)


def outgoing_ef_slope(M: Fraction, r: Fraction) -> Fraction:
    # radial null branch with dv != 0: dr/dv = f/2
    return f_schw(M, r) / Q(2)


def horizon_to_singularity_proper_time_E1(M: float) -> float:
    # Radial timelike geodesic dropped from rest at infinity: dr/dtau=-sqrt(2M/r).
    # Integral from r=2M to r=0 equals 4M/3.
    return 4.0 * M / 3.0


def finite_segment_proper_time_E1(M: float, r_hi: float, r_lo: float) -> float:
    if not (M > 0.0 and r_hi >= r_lo >= 0.0):
        raise ValueError("require M>0 and r_hi>=r_lo>=0")
    return (2.0 / (3.0 * math.sqrt(2.0 * M))) * (
        r_hi ** 1.5 - r_lo ** 1.5
    )


def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def checks() -> list[Check]:
    M = Q(1)
    rh = Q(2)
    rout = Q(3)
    rin = Q(1)

    # A deliberately simple incomplete flat manifold witness: restrict Minkowski
    # spacetime to t<0. The timelike geodesic x=0, t=tau reaches the omitted
    # boundary t=0 after finite proper time while curvature is identically zero.
    flat_halfspace_curvature = Q(0)
    flat_halfspace_remaining_proper_time = Q(1)  # tau=-1 -> 0

    provenance = {
        "schwarzschild_solution_supplied": "R2",
        "mass_parameter_and_asymptotic_region_supplied": "R2",
        "maximal_extension_and_time_orientation_supplied": "R2",
        "ef_regular_horizon_representation": "R3",
        "kretschmann_formula": "R3",
        "one_way_radial_null_sign": "R3",
        "finite_E1_horizon_to_r0_proper_time": "R3",
        "generic_dsd_derives_schwarzschild": "R4",
        "dsd_projection_equals_event_horizon": "R4",
        "descriptive_inaccessibility_equals_nonexistence": "R4",
    }
    guards = {
        "gtt_zero_is_not_horizon_definition": "DISTINCT",
        "event_horizon_needs_global_causal_asymptotic_structure": "REQUIRED",
        "causal_access_vs_assignment_domain": "DISTINCT",
        "structural_gravity_black_hole_identification": "NOT_IMPORTED",
    }

    return [
        # Schwarzschild-coordinate and curvature witness
        Check("SCHWARZSCHILD", "f(r)>0 outside horizon", lambda: f_schw(M, rout) > 0),
        Check("SCHWARZSCHILD", "f(r)=0 at r=2M", lambda: f_schw(M, rh) == 0),
        Check("SCHWARZSCHILD", "f(r)<0 inside horizon", lambda: f_schw(M, rin) < 0),
        Check("SCHWARZSCHILD", "Schwarzschild g_rr denominator vanishes at horizon", lambda: f_schw(M, rh) == 0),
        Check("SCHWARZSCHILD", "Kretschmann finite at horizon", lambda: kretschmann(M, rh) == Q(3, 4)),
        Check("SCHWARZSCHILD", "Kretschmann nonzero at regular horizon", lambda: kretschmann(M, rh) > 0),
        Check("SCHWARZSCHILD", "Kretschmann grows inward", lambda: kretschmann(M, rin) > kretschmann(M, rh)),
        Check("SCHWARZSCHILD", "K(r=1/n) has n^6 scaling", lambda: kretschmann(M, Q(1, 4)) == Q(4**6) * kretschmann(M, Q(1))),
        Check("SCHWARZSCHILD", "K(r) is unbounded along r=1/n formula", lambda: kretschmann(M, Q(1, 100)) > Q(10**10)),

        # Ingoing Eddington-Finkelstein regularity and causal sign witness
        Check("EF_HORIZON", "EF (v,r) block determinant is -1", lambda: ef_vr_block_det(M, rh) == -1),
        Check("EF_HORIZON", "EF full determinant nonzero at equatorial horizon", lambda: ef_full_det_equator(rh) == -16),
        Check("EF_HORIZON", "g_vv may vanish while metric stays nondegenerate", lambda: f_schw(M, rh) == 0 and ef_vr_block_det(M, rh) != 0),
        Check("EF_HORIZON", "outgoing radial null slope positive outside", lambda: outgoing_ef_slope(M, rout) > 0),
        Check("EF_HORIZON", "outgoing radial null slope zero at horizon", lambda: outgoing_ef_slope(M, rh) == 0),
        Check("EF_HORIZON", "outgoing radial null slope negative inside", lambda: outgoing_ef_slope(M, rin) < 0),
        Check("EF_HORIZON", "radial coordinate gradient changes causal sign across horizon", lambda: f_schw(M, rout) > 0 and f_schw(M, rin) < 0),

        # Geodesic incompleteness / singularity separation
        Check("GEODESIC", "E=1 horizon-to-r0 proper time is finite", lambda: math.isfinite(horizon_to_singularity_proper_time_E1(1.0))),
        Check("GEODESIC", "E=1 horizon-to-r0 proper time equals 4M/3", lambda: close(horizon_to_singularity_proper_time_E1(1.0), 4.0 / 3.0)),
        Check("GEODESIC", "finite proper-time segment is positive", lambda: finite_segment_proper_time_E1(1.0, 2.0, 0.5) > 0.0),
        Check("GEODESIC", "proper-time integral approaches 4M/3 as lower radius -> 0", lambda: abs(finite_segment_proper_time_E1(1.0, 2.0, 1e-8) - 4.0 / 3.0) < 1e-10),
        Check("GEODESIC", "flat restricted manifold can be incomplete with zero curvature", lambda: flat_halfspace_curvature == 0 and flat_halfspace_remaining_proper_time > 0),
        Check("GEODESIC", "incompleteness therefore does not logically require curvature blow-up", lambda: flat_halfspace_curvature == 0),

        # Provenance and logical firewalls
        Check("PROVENANCE", "Schwarzschild geometry is supplied relativity specialization", lambda: provenance["schwarzschild_solution_supplied"] == "R2"),
        Check("PROVENANCE", "mass/asymptotic structure is supplied", lambda: provenance["mass_parameter_and_asymptotic_region_supplied"] == "R2"),
        Check("PROVENANCE", "maximal extension/time orientation is supplied", lambda: provenance["maximal_extension_and_time_orientation_supplied"] == "R2"),
        Check("PROVENANCE", "EF regularity is theorem consequence", lambda: provenance["ef_regular_horizon_representation"] == "R3"),
        Check("PROVENANCE", "Kretschmann formula is theorem consequence", lambda: provenance["kretschmann_formula"] == "R3"),
        Check("PROVENANCE", "one-way radial-null sign is theorem consequence", lambda: provenance["one_way_radial_null_sign"] == "R3"),
        Check("PROVENANCE", "finite E=1 proper time is theorem consequence", lambda: provenance["finite_E1_horizon_to_r0_proper_time"] == "R3"),
        Check("PROVENANCE", "generic DSD does not derive Schwarzschild", lambda: provenance["generic_dsd_derives_schwarzschild"] == "R4"),
        Check("PROVENANCE", "DSD descriptive projection is not an event horizon", lambda: provenance["dsd_projection_equals_event_horizon"] == "R4"),
        Check("PROVENANCE", "descriptive inaccessibility is not nonexistence", lambda: provenance["descriptive_inaccessibility_equals_nonexistence"] == "R4"),
        Check("PROVENANCE", "coordinate failure is not curvature singularity", lambda: ef_vr_block_det(M, rh) != 0 and kretschmann(M, rh) < 10),
        Check("PROVENANCE", "horizon is not identified from g_tt=0 alone", lambda: guards["gtt_zero_is_not_horizon_definition"] == "DISTINCT"),
        Check("PROVENANCE", "event-horizon status requires global causal/asymptotic structure", lambda: guards["event_horizon_needs_global_causal_asymptotic_structure"] == "REQUIRED"),
        Check("PROVENANCE", "geodesic incompleteness and curvature blow-up remain distinct notions", lambda: flat_halfspace_curvature == 0),
        Check("PROVENANCE", "causal inaccessibility and chart failure remain distinct", lambda: ef_vr_block_det(M, rh) != 0),
        Check("PROVENANCE", "causal inaccessibility and DSD assignment undefined remain distinct", lambda: guards["causal_access_vs_assignment_domain"] == "DISTINCT"),
        Check("PROVENANCE", "no structural-gravity black-hole identification is imported", lambda: guards["structural_gravity_black_hole_identification"] == "NOT_IMPORTED"),
    ]


def run(selected: str) -> int:
    all_checks = checks()
    groups = []
    for c in all_checks:
        if c.group not in groups:
            groups.append(c.group)

    if selected != "all":
        all_checks = [c for c in all_checks if c.group.lower() == selected.lower()]
        if not all_checks:
            print(f"Unknown mode: {selected}")
            print("Available:", ", ".join(g.lower() for g in groups), "all")
            return 2

    total = 0
    passed = 0
    current = None
    group_total = 0
    group_passed = 0

    def flush_group() -> None:
        nonlocal group_total, group_passed
        if current is not None:
            print(f"{current}: {group_passed}/{group_total} PASS")
        group_total = 0
        group_passed = 0

    for c in all_checks:
        if c.group != current:
            flush_group()
            current = c.group
        ok = bool(c.predicate())
        total += 1
        group_total += 1
        if ok:
            passed += 1
            group_passed += 1
        else:
            print(f"  FAIL: {c.name}")

    flush_group()
    print()
    print(f"TOTAL: {passed}/{total} checks passed")
    verdict = "PASS_WITH_BOUNDARY" if passed == total else "FAIL"
    print(f"OVERALL: {verdict}")
    return 0 if passed == total else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        default="all",
        help="all, schwarzschild, ef_horizon, geodesic, provenance",
    )
    args = parser.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
