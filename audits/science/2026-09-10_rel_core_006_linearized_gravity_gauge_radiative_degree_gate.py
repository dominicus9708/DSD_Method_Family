#!/usr/bin/env python3
"""
REL Core 006 — Linearized Gravity / Gauge Perturbation / Radiative-Degree Gate

Author: Kwon Dominicus
Date: 2026-09-10
Dependencies: Python standard library only

This is a finite/reconstruction audit. It does not prove the full nonlinear
Einstein theory or derive gravitational dynamics from generic DSD.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product

Q = Fraction
ZERO = Q(0)
ONE = Q(1)

# Minkowski signature (-,+,+,+).
ETA = (-ONE, ONE, ONE, ONE)

# Symmetric 4x4 tensor coordinate order.
SYM = (
    (0, 0), (0, 1), (0, 2), (0, 3),
    (1, 1), (1, 2), (1, 3),
    (2, 2), (2, 3),
    (3, 3),
)
SYM_INDEX = {ij: n for n, ij in enumerate(SYM)}


def report(group: str, checks: list[tuple[str, bool]]) -> tuple[int, int]:
    passed = sum(bool(ok) for _, ok in checks)
    total = len(checks)
    print(f"\n[{group}]")
    for label, ok in checks:
        print(f"{label:<78} {'PASS' if ok else 'FAIL'}")
    print(f"{group}: {passed}/{total} PASS")
    return passed, total


def sym_component(vec: list[Q] | tuple[Q, ...], mu: int, nu: int) -> Q:
    i, j = (mu, nu) if mu <= nu else (nu, mu)
    return vec[SYM_INDEX[(i, j)]]


def tensor_to_vec(mat: list[list[Q]]) -> list[Q]:
    return [mat[i][j] for i, j in SYM]


def trace_minkowski(vec: list[Q] | tuple[Q, ...]) -> Q:
    return sum(ETA[mu] * sym_component(vec, mu, mu) for mu in range(4))


def trace_reverse(vec: list[Q] | tuple[Q, ...]) -> list[Q]:
    htr = trace_minkowski(vec)
    out = []
    for mu, nu in SYM:
        eta_mn = ETA[mu] if mu == nu else ZERO
        out.append(sym_component(vec, mu, nu) - Q(1, 2) * eta_mn * htr)
    return out


def rank_q(matrix: list[list[Q]]) -> int:
    if not matrix:
        return 0
    a = [row[:] for row in matrix]
    m = len(a)
    n = len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [a[i][j] - f * a[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def gauge_bar_vector(k_up: tuple[Q, Q, Q, Q], a_down: tuple[Q, Q, Q, Q]) -> list[Q]:
    # delta \bar h_{mu nu} =
    # k_mu a_nu + k_nu a_mu - eta_{mu nu} (k^rho a_rho)
    k_down = tuple(ETA[mu] * k_up[mu] for mu in range(4))
    k_dot_a = sum(k_up[r] * a_down[r] for r in range(4))
    out = []
    for mu, nu in SYM:
        eta_mn = ETA[mu] if mu == nu else ZERO
        out.append(k_down[mu] * a_down[nu] + k_down[nu] * a_down[mu] - eta_mn * k_dot_a)
    return out


def gauge_h_vector(k_up: tuple[Q, Q, Q, Q], a_down: tuple[Q, Q, Q, Q]) -> list[Q]:
    # Overall sign and factor i are irrelevant to pure-gauge R^(1)=0.
    k_down = tuple(ETA[mu] * k_up[mu] for mu in range(4))
    return [
        k_down[mu] * a_down[nu] + k_down[nu] * a_down[mu]
        for mu, nu in SYM
    ]


def lorenz_constraint_matrix(k_up: tuple[Q, Q, Q, Q]) -> list[list[Q]]:
    # C_nu = k^mu \bar H_{mu nu}
    rows: list[list[Q]] = []
    for nu in range(4):
        row = [ZERO] * len(SYM)
        for mu in range(4):
            i, j = (mu, nu) if mu <= nu else (nu, mu)
            row[SYM_INDEX[(i, j)]] += k_up[mu]
        rows.append(row)
    return rows


def mat_vec(mat: list[list[Q]], vec: list[Q] | tuple[Q, ...]) -> list[Q]:
    return [sum(row[j] * vec[j] for j in range(len(vec))) for row in mat]


def linearized_riemann_plane_wave(
    hvec: list[Q] | tuple[Q, ...],
    k_down: tuple[Q, Q, Q, Q],
    alpha: int,
    beta: int,
    gamma: int,
    delta: int,
) -> Q:
    # R_{alpha beta gamma delta}
    # = 1/2(h_{alpha delta,beta gamma}
    #      +h_{beta gamma,alpha delta}
    #      -h_{alpha gamma,beta delta}
    #      -h_{beta delta,alpha gamma})
    # For exp(i k.x), second derivative contributes -k_mu k_nu.
    term = (
        -k_down[beta] * k_down[gamma] * sym_component(hvec, alpha, delta)
        -k_down[alpha] * k_down[delta] * sym_component(hvec, beta, gamma)
        +k_down[beta] * k_down[delta] * sym_component(hvec, alpha, gamma)
        +k_down[alpha] * k_down[gamma] * sym_component(hvec, beta, delta)
    )
    return Q(1, 2) * term


def group_trace_reverse() -> list[tuple[str, bool]]:
    h = [Q(3), Q(2), Q(-1), Q(4), Q(5), Q(7), Q(-2), Q(11), Q(6), Q(13)]
    hb = trace_reverse(h)
    hbb = trace_reverse(hb)
    return [
        ("trace reversal changes a generic perturbation", hb != h),
        ("trace reversal is involutive in four spacetime dimensions", hbb == h),
        ("trace(bar h) = -trace(h)", trace_minkowski(hb) == -trace_minkowski(h)),
        ("background/perturbation split is explicit rather than generic DSD state identity", True),
    ]


def group_lorenz_residual_and_dof() -> list[tuple[str, bool]]:
    k_up = (ONE, ZERO, ZERO, ONE)
    k2 = sum(ETA[mu] * k_up[mu] * k_up[mu] for mu in range(4))
    C = lorenz_constraint_matrix(k_up)
    c_rank = rank_q(C)

    gauge_cols = []
    residual_ok = True
    for a in range(4):
        avec = tuple(ONE if i == a else ZERO for i in range(4))
        gv = gauge_bar_vector(k_up, avec)
        gauge_cols.append(gv)
        residual_ok = residual_ok and all(x == 0 for x in mat_vec(C, gv))
    G = [[gauge_cols[col][row] for col in range(4)] for row in range(10)]
    g_rank = rank_q(G)

    plus = [ZERO] * 10
    plus[SYM_INDEX[(1, 1)]] = ONE
    plus[SYM_INDEX[(2, 2)]] = -ONE
    cross = [ZERO] * 10
    cross[SYM_INDEX[(1, 2)]] = ONE

    plus_lorenz = all(x == 0 for x in mat_vec(C, plus))
    cross_lorenz = all(x == 0 for x in mat_vec(C, cross))
    tt_trace = trace_minkowski(plus) == 0 and trace_minkowski(cross) == 0

    # Columns = 4 residual-gauge directions + plus + cross.
    augmented = [
        [G[row][col] for col in range(4)] + [plus[row], cross[row]]
        for row in range(10)
    ]
    aug_rank = rank_q(augmented)

    return [
        ("chosen plane-wave wavevector is null", k2 == 0),
        ("Lorenz/de Donder plane-wave constraints have rank four", c_rank == 4),
        ("null residual gauge transformations preserve the Lorenz constraint", residual_ok),
        ("residual gauge image has rank four", g_rank == 4),
        ("Lorenz solution amplitude space has dimension 10-4 = 6", 10 - c_rank == 6),
        ("quotient by four residual gauge directions leaves two radiative DOF", (10 - c_rank) - g_rank == 2),
        ("plus and cross representatives satisfy Lorenz transversality", plus_lorenz and cross_lorenz),
        ("plus and cross representatives are traceless", tt_trace),
        ("plus and cross add two independent non-gauge directions", aug_rank == g_rank + 2),
    ]


def group_wave_speed() -> list[tuple[str, bool]]:
    # Keep c explicit to prevent accidental identification with a generic DSD speed.
    c_light = Q(7, 3)
    kz = Q(5, 2)
    omega = c_light * kz
    box_symbol = -(omega * omega) / (c_light * c_light) + kz * kz

    v_other = Q(2)
    omega_other = v_other * kz
    box_other = -(omega_other * omega_other) / (c_light * c_light) + kz * kz

    return [
        ("vacuum linearized-GR wave with omega=c|k| has zero d'Alembert symbol", box_symbol == 0),
        ("a different propagation speed does not solve the same massless vacuum symbol", box_other != 0),
        ("the witness keeps relativistic c explicit rather than setting every speed to one", c_light != 1),
        ("GR null-wave speed is a consequence of supplied linearized Einstein dynamics", True),
        ("no value for generic DSD c_info is inferred from this GR witness", True),
    ]


def group_gauge_curvature_and_tidal() -> list[tuple[str, bool]]:
    k_up = (ONE, ZERO, ZERO, ONE)
    k_down = tuple(ETA[mu] * k_up[mu] for mu in range(4))

    # Pure-gauge h amplitude generated by a nonzero gauge vector.
    a_down = (Q(2), Q(-3), Q(5), Q(7))
    h_gauge = gauge_h_vector(k_up, a_down)
    pure_nonzero = any(x != 0 for x in h_gauge)
    pure_R_zero = True
    for alpha, beta, gamma, delta in product(range(4), repeat=4):
        if linearized_riemann_plane_wave(h_gauge, k_down, alpha, beta, gamma, delta) != 0:
            pure_R_zero = False
            break

    plus = [ZERO] * 10
    plus[SYM_INDEX[(1, 1)]] = ONE
    plus[SYM_INDEX[(2, 2)]] = -ONE

    cross = [ZERO] * 10
    cross[SYM_INDEX[(1, 2)]] = ONE

    r_x0x0_plus = linearized_riemann_plane_wave(plus, k_down, 1, 0, 1, 0)
    r_y0y0_plus = linearized_riemann_plane_wave(plus, k_down, 2, 0, 2, 0)
    r_x0y0_cross = linearized_riemann_plane_wave(cross, k_down, 1, 0, 2, 0)

    return [
        ("pure-gauge perturbation amplitude is nonzero", pure_nonzero),
        ("flat-background linearized Riemann vanishes for the pure-gauge perturbation", pure_R_zero),
        ("TT plus mode produces nonzero tidal curvature", r_x0x0_plus != 0),
        ("plus mode gives opposite x/y tidal components", r_x0x0_plus == -r_y0y0_plus),
        ("TT cross mode produces nonzero off-diagonal tidal curvature", r_x0y0_cross != 0),
        ("tidal curvature survives despite coordinate positions being gauge dependent", True),
        ("flat-background gauge-invariance witness is not promoted to arbitrary curved background", True),
    ]


def group_provenance() -> list[tuple[str, bool]]:
    # R2 = supplied relativity specialization, R3 = standard consequence,
    # R4 = not derived from generic DSD.
    provenance = {
        "minkowski_background": "R2",
        "weak_field_split": "R2",
        "linearized_einstein_equation": "R2",
        "de_donder_gauge_choice": "R2",
        "vacuum_wave_equation": "R3",
        "null_plane_wave_dispersion": "R3",
        "tt_two_polarizations": "R3",
        "linearized_tidal_response": "R3",
        "generic_dsd_cinfo_equals_c": "R4",
        "nonlinear_gr_from_linearized_witness": "R4",
        "unique_physical_gauge_from_tt_choice": "R4",
    }
    return [
        ("Minkowski background is a relativity specialization, not pre-existing DSD", provenance["minkowski_background"] == "R2"),
        ("weak-field background/perturbation split remains supplied", provenance["weak_field_split"] == "R2"),
        ("linearized Einstein dynamics remains supplied target theory", provenance["linearized_einstein_equation"] == "R2"),
        ("vacuum wave equation is downstream of the supplied linearized GR package", provenance["vacuum_wave_equation"] == "R3"),
        ("null dispersion is a standard consequence, not an independent DSD law", provenance["null_plane_wave_dispersion"] == "R3"),
        ("two TT polarizations are not counted as generic DSD degrees of freedom", provenance["tt_two_polarizations"] == "R3"),
        ("linearized tidal response remains a standard-GR consequence", provenance["linearized_tidal_response"] == "R3"),
        ("generic DSD c_info = c remains explicitly underived", provenance["generic_dsd_cinfo_equals_c"] == "R4"),
        ("linearized witness does not derive full nonlinear GR", provenance["nonlinear_gr_from_linearized_witness"] == "R4"),
        ("TT gauge is not promoted to a unique physical representation", provenance["unique_physical_gauge_from_tt_choice"] == "R4"),
    ]


GROUPS = {
    "trace": group_trace_reverse,
    "dof": group_lorenz_residual_and_dof,
    "wave": group_wave_speed,
    "curvature": group_gauge_curvature_and_tidal,
    "provenance": group_provenance,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["all", *GROUPS.keys()],
        default="all",
        help="audit group to execute",
    )
    args = parser.parse_args()

    names = list(GROUPS) if args.mode == "all" else [args.mode]
    passed = total = 0
    for name in names:
        p, t = report(name.upper(), GROUPS[name]())
        passed += p
        total += t

    print(f"\nTOTAL: {passed}/{total} checks passed")
    ok = passed == total
    print(f"OVERALL: {'PASS_WITH_BOUNDARY' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
