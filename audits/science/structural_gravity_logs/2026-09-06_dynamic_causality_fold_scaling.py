#!/usr/bin/env python3
"""Kinetic/causality and near-fold scaling audit for reciprocal DSD gravity.

Historical repository path keeps `structural_gravity_logs` for continuity.

This script does not derive inertia, damping, c_info, or a universal gravity law.
It audits a conditional radial specialization against the second-order DSD
dynamical interface and computes local characteristic constraints and the
continuum saddle-node curvature of the already-recorded static branch.

Dimensionless axis dynamics (conditional specialization):

    nu_A a_tt + delta_A a_t - ell_A^2 L_2 a + a = source,

with tau = c_* t / R and

    nu_A    = mu_A c_*^2 / (R_A R^2),
    delta_A = D_A c_* / (R_A R),
    ell_A^2 = T_A / (R_A R^2).

Hence the axis principal speed is

    c_A / c_* = ell_A / sqrt(nu_A).

For the uniaxial axis metric used in the static branch,

    h_A^{-1} eigenvalues = (exp(-2 beta a/3), exp(beta a/3), exp(beta a/3)),

so the field characteristic speed relative to c_* ranges from
exp(-beta a/3) radially to exp(beta a/6) tangentially.

The script can also import `2026-09-06_continuum_twofield_radial_bvp.py`
and estimate the saddle-node curvature

    epsilon_fold - epsilon = C (a_boundary-a_fold)^2 + O(q^3).
"""

from __future__ import annotations

import argparse
import importlib.util
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BVP = HERE / "2026-09-06_continuum_twofield_radial_bvp.py"


def load_bvp():
    spec = importlib.util.spec_from_file_location("dsd_continuum_bvp", BVP)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BVP}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def characteristic_audit(beta: float, a_max: float, ell: float, cstar_over_cinfo: float | None):
    radial_speed_factor = math.exp(-beta * a_max / 3.0)
    tangential_speed_factor = math.exp(beta * a_max / 6.0)
    field_headroom = 1.0 / tangential_speed_factor

    ratio = field_headroom if cstar_over_cinfo is None else cstar_over_cinfo
    nu_min_axis = ell * ell * ratio * ratio

    print(f"beta={beta:.12g}")
    print(f"a_max={a_max:.12g}")
    print(f"ell={ell:.12g}")
    print(f"field_radial_speed_over_cstar={radial_speed_factor:.12g}")
    print(f"field_tangential_max_speed_over_cstar={tangential_speed_factor:.12g}")
    print(f"required_cstar_over_cinfo_max={field_headroom:.12g}")
    print(f"used_cstar_over_cinfo={ratio:.12g}")
    print(f"axis_nu_min_for_cinfo_bound={nu_min_axis:.12g}")
    print("shared_sharp_cone_axis_condition: nu_A >= ell_A^2")
    print("dynamic_outgoing_boundary: U_tau + U - 1 + p(a_b) U_s = 0")


def fold_scaling(beta: float, chi: float, ell: float, a_lo: float, a_hi: float, h: float):
    bvp = load_bvp()
    a_fold, eps_fold, eps_contact = bvp.fold_point(beta, chi, ell, a_lo, a_hi)
    lo, _ = bvp.solve_point(beta, chi, ell, a_fold - h)
    hi, _ = bvp.solve_point(beta, chi, ell, a_fold + h)
    C = (eps_fold - 0.5 * (lo.epsilon + hi.epsilon)) / (h * h)
    susceptibility_prefactor = 1.0 / (2.0 * math.sqrt(C))

    print(f"beta={beta:.12g}")
    print(f"chi={chi:.12g}")
    print(f"ell={ell:.12g}")
    print(f"a_fold={a_fold:.12f}")
    print(f"epsilon_fold={eps_fold:.12f}")
    print(f"epsilon_a1_contact={eps_contact:.12f}")
    print(f"curvature_step={h:.12g}")
    print(f"fold_curvature_C={C:.12f}")
    print(f"susceptibility_prefactor_1_over_2sqrtC={susceptibility_prefactor:.12f}")
    print("near_fold: epsilon_fold-epsilon = C q^2 + O(q^3)")
    print("static_susceptibility: da_b/depsilon ~ [2 sqrt(C)]^-1 delta^-1/2")
    print("generic_conservative_soft_frequency: omega ~ delta^(1/4)")
    print("generic_fixed_damping_relaxation_time: tau_relax ~ delta^(-1/2)")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=("characteristic", "fold"), default="characteristic")
    p.add_argument("--beta", type=float, default=2.0)
    p.add_argument("--chi", type=float, default=0.5)
    p.add_argument("--ell", type=float, default=0.1)
    p.add_argument("--a-max", type=float, default=0.62850146055)
    p.add_argument("--cstar-over-cinfo", type=float, default=None)
    p.add_argument("--a-lo", type=float, default=0.55)
    p.add_argument("--a-hi", type=float, default=0.70)
    p.add_argument("--h", type=float, default=0.003)
    args = p.parse_args()

    if args.mode == "characteristic":
        characteristic_audit(args.beta, args.a_max, args.ell, args.cstar_over_cinfo)
    else:
        fold_scaling(args.beta, args.chi, args.ell, args.a_lo, args.a_hi, args.h)


if __name__ == "__main__":
    main()
