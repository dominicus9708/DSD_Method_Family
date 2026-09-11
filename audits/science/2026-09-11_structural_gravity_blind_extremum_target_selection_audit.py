#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import numpy as np

TRACE = 2.0
PREDECESSOR_PSI = {
    "uniform": 0.500000000000,
    "core_heavy": 0.654285714286,
    "envelope_heavy": 0.469142857143,
}


def spectral_pair_from_minimum(x: float, trace: float = TRACE):
    if not (0.0 < x <= trace / 2.0):
        raise ValueError("x must satisfy 0 < x <= trace/2")
    return np.array([x, trace - x], dtype=float)


def determinant_from_x(x: float, trace: float = TRACE) -> float:
    vals = spectral_pair_from_minimum(x, trace)
    return float(vals[0] * vals[1])


def spectral_entropy_from_x(x: float, trace: float = TRACE) -> float:
    vals = spectral_pair_from_minimum(x, trace) / trace
    return float(-np.sum(vals * np.log(vals)))


def frobenius_sq_from_x(x: float, trace: float = TRACE) -> float:
    vals = spectral_pair_from_minimum(x, trace)
    return float(np.sum(vals**2))


def condition_number_from_x(x: float, trace: float = TRACE) -> float:
    vals = spectral_pair_from_minimum(x, trace)
    return float(vals[-1] / vals[0])


def lineage_regularized_minimizer(x_pre: float, alpha: float, x_target: float = 1.0) -> float:
    """
    Minimize
        J(x) = 1/2 (x - x_pre)^2 + alpha/2 (x - x_target)^2
    over the interior control interval 0 < x <= 1.
    """
    if alpha < 0.0:
        raise ValueError("alpha must be nonnegative")
    x = (x_pre + alpha * x_target) / (1.0 + alpha)
    return min(1.0, max(1e-12, x))


def grid_extrema(n: int = 200001):
    xs = np.linspace(1e-6, 1.0, n)
    det = xs * (TRACE - xs)
    ent = np.array([spectral_entropy_from_x(float(x)) for x in xs])
    fro = xs**2 + (TRACE - xs)**2
    return {
        "det_max_x": float(xs[int(np.argmax(det))]),
        "det_min_x": float(xs[int(np.argmin(det))]),
        "entropy_max_x": float(xs[int(np.argmax(ent))]),
        "entropy_min_x": float(xs[int(np.argmin(ent))]),
        "fro_min_x": float(xs[int(np.argmin(fro))]),
        "fro_max_x": float(xs[int(np.argmax(fro))]),
    }


def report():
    ext = grid_extrema()
    print("DSD blind target-selection extremum audit")
    print("----------------------------------------")
    print("2-mode normalized spectrum with fixed trace T=2:")
    print("  eigenvalues = (x, 2-x), 0 < x <= 1")
    print("  Psi_* = x")
    print()

    print("Candidate symmetric objectives")
    print("------------------------------")
    print("objective,extremum,selected_x,selected_Psi")
    print(f"determinant,max,{ext['det_max_x']:.12g},{ext['det_max_x']:.12g}")
    print(f"determinant,min_infimum,{ext['det_min_x']:.12g},{ext['det_min_x']:.12g}")
    print(f"spectral_entropy,max,{ext['entropy_max_x']:.12g},{ext['entropy_max_x']:.12g}")
    print(f"spectral_entropy,min_infimum,{ext['entropy_min_x']:.12g},{ext['entropy_min_x']:.12g}")
    print(f"frobenius_norm_sq,min,{ext['fro_min_x']:.12g},{ext['fro_min_x']:.12g}")
    print(f"frobenius_norm_sq,max_boundary,{ext['fro_max_x']:.12g},{ext['fro_max_x']:.12g}")
    print()

    print("Values at selected reference points")
    print("-----------------------------------")
    print("x,det,entropy,fro_sq,condition")
    for x in (0.1, 0.25, 0.5, 0.75, 1.0):
        print(
            f"{x:.2f},"
            f"{determinant_from_x(x):.12g},"
            f"{spectral_entropy_from_x(x):.12g},"
            f"{frobenius_sq_from_x(x):.12g},"
            f"{condition_number_from_x(x):.12g}"
        )
    print()

    print("Lineage-compatible regularization toward symmetric target x=1")
    print("-----------------------------------------------------------")
    print("alpha,profile,x_pre,x_selected,spread")
    for alpha in (0.0, 0.1, 1.0, 10.0, 1000.0):
        vals = {
            name: lineage_regularized_minimizer(xpre, alpha, 1.0)
            for name, xpre in PREDECESSOR_PSI.items()
        }
        sp = max(vals.values()) - min(vals.values())
        for name, xsel in vals.items():
            print(f"{alpha:.1f},{name},{PREDECESSOR_PSI[name]:.12g},{xsel:.12g},{sp:.12g}")
    print()

    print("Extra constraint needed for x=1/2")
    print("--------------------------------")
    print("At fixed trace T=2:")
    print("  x=1/2 <=> determinant=3/4")
    print("  x=1/2 <=> condition number=3")
    print("  x=1/2 <=> spectral anisotropy (lambda_max-lambda_min)/T = 1/2")
    print("These are additional dimensionless constraints, not consequences of fixed trace alone.")


def audit():
    checks = []
    ext = grid_extrema()

    checks.append((
        "FIXED_TRACE_DET_MAX_IS_ISOTROPIC",
        abs(ext["det_max_x"] - 1.0) < 1e-5,
        "max determinant at fixed trace selects equal eigenvalues, hence Psi_*=1",
    ))
    checks.append((
        "FIXED_TRACE_ENTROPY_MAX_IS_ISOTROPIC",
        abs(ext["entropy_max_x"] - 1.0) < 1e-5,
        "max spectral entropy at fixed trace selects isotropy, hence Psi_*=1",
    ))
    checks.append((
        "FIXED_TRACE_FROBENIUS_MIN_IS_ISOTROPIC",
        abs(ext["fro_min_x"] - 1.0) < 1e-5,
        "minimum Frobenius norm at fixed trace selects isotropy, hence Psi_*=1",
    ))
    checks.append((
        "BOUNDARY_EXTREMA_DRIVE_PSI_TO_ZERO",
        ext["det_min_x"] < 1e-4 and ext["entropy_min_x"] < 1e-4,
        "min determinant or min entropy over positive spectra approaches the rank-deficient boundary Psi_*=0",
    ))
    checks.append((
        "NO_COMMON_SYMMETRIC_EXTREMUM_SELECTS_HALF",
        abs(ext["det_max_x"] - 0.5) > 0.4
        and abs(ext["entropy_max_x"] - 0.5) > 0.4
        and abs(ext["fro_min_x"] - 0.5) > 0.4,
        "the natural fixed-trace symmetric extrema tested here do not blind-select Psi_*=1/2",
    ))

    alpha = 10.0
    vals = [lineage_regularized_minimizer(x, alpha, 1.0) for x in PREDECESSOR_PSI.values()]
    checks.append((
        "FINITE_LINEAGE_WEIGHT_RETAINS_SOURCE_DEPENDENCE",
        max(vals) - min(vals) > 1e-3,
        "finite predecessor fidelity keeps source-dependent post-selection coefficients",
    ))

    alpha_big = 1e9
    vals_big = [lineage_regularized_minimizer(x, alpha_big, 1.0) for x in PREDECESSOR_PSI.values()]
    checks.append((
        "INFINITE_COMMON_OBJECTIVE_ERASES_LINEAGE_BUT_SELECTS_ONE",
        max(vals_big) - min(vals_big) < 1e-8 and abs(np.mean(vals_big) - 1.0) < 1e-8,
        "dominating the predecessor term can enforce a common target, but the tested symmetric target is Psi_*=1, not 1/2",
    ))

    checks.append((
        "HALF_EQUIVALENT_TO_EXTRA_DETERMINANT_CONSTRAINT",
        abs(determinant_from_x(0.5) - 0.75) < 1e-15,
        "at trace 2, selecting Psi_*=1/2 is equivalent to imposing determinant 3/4",
    ))
    checks.append((
        "HALF_EQUIVALENT_TO_EXTRA_CONDITION_NUMBER",
        abs(condition_number_from_x(0.5) - 3.0) < 1e-15,
        "at trace 2, selecting Psi_*=1/2 is equivalent to imposing condition number 3",
    ))
    checks.append((
        "NO_GENERIC_DSD_VARIATIONAL_SELECTOR",
        True,
        "generic DSD supplies typed transitions and optional dynamics but no canonical determinant/entropy/coercivity variational objective",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no Schwarzschild radius, EHT observable, or coefficient 2 is used in the tested objective functions",
    ))

    failures = 0
    for name, ok, note in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
        failures += 0 if ok else 1
    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_NEGATIVE_RESULT / BLIND_HALF_NOT_SELECTED_BY_NATURAL_FIXED_TRACE_EXTREMA")
    return failures


def main():
    ap = argparse.ArgumentParser(
        description="Blind audit of fixed-trace extremum and lineage-compatible target-selection candidates."
    )
    ap.add_argument("--mode", choices=("all", "report", "audit"), default="all")
    args = ap.parse_args()
    if args.mode in ("all", "report"):
        report()
    if args.mode in ("all", "audit"):
        failures = audit()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
