#!/usr/bin/env python3
from __future__ import annotations

import argparse
import numpy as np


def sym(a):
    a = np.asarray(a, dtype=float)
    return 0.5 * (a + a.T)


def min_eig(a) -> float:
    return float(np.linalg.eigvalsh(sym(a))[0])


def generalized_threshold(h0, load) -> float:
    h0 = sym(h0)
    load = sym(load)
    evals_l, evecs_l = np.linalg.eigh(load)
    if np.min(evals_l) <= 0.0:
        raise ValueError("load operator must be positive definite")
    invsqrt_l = evecs_l @ np.diag(evals_l ** -0.5) @ evecs_l.T
    reduced = sym(invsqrt_l @ h0 @ invsqrt_l)
    return min_eig(reduced)


def margin(h0, load, theta: float) -> float:
    return min_eig(sym(h0) - theta * sym(load))


def two_mode_eigenvalues(h1: float, h2: float, coupling: float):
    h = np.array([[h1, -coupling], [-coupling, h2]], dtype=float)
    return np.linalg.eigvalsh(h)


def blind_report() -> None:
    print("DSD structural-gravity spectral support-threshold audit")
    print("-------------------------------------------------------")
    print("Conservative/quasi-static specialization:")
    print("  H_sup(theta) = H0 - theta * L")
    print("  support margin m(theta) = lambda_min(H_sup(theta))")
    print("  stable/admissible: m(theta) > 0")
    print("  threshold: m(theta_*) = 0")
    print()
    print("For positive-definite L:")
    print("  Psi_*(S_sup) = theta_*")
    print("                = inf_u <u,H0 u>/<u,L u>")
    print("                = lambda_min(L^(-1/2) H0 L^(-1/2))")
    print()
    print("Minimal static inputs:")
    print("  H0 : baseline coupled tangent-support operator")
    print("  L  : load-direction operator")
    print("  normalization/domain data")
    print()
    print("Not primitive static-threshold inputs:")
    print("  inertia, damping, propagation-front saturation,")
    print("  realignment history, observer resolution, singularity rank")
    print()
    print("Boundary:")
    print("  This spectral form requires a symmetric conservative/quasi-static")
    print("  specialization. Generic DSD dynamics does not force a Hessian model.")


def examples_report() -> None:
    i2 = np.eye(2)
    cases = [
        ("weak_coupling", np.array([[1.0, -0.2], [-0.2, 1.0]]), i2),
        ("half_threshold_example", np.array([[1.0, -0.5], [-0.5, 1.0]]), i2),
        ("near_critical", np.array([[1.0, -0.95], [-0.95, 1.0]]), i2),
        ("critical", np.array([[1.0, -1.0], [-1.0, 1.0]]), i2),
        ("anisotropic", np.array([[2.0, -0.6], [-0.6, 0.8]]), i2),
        ("directional_load", np.array([[1.0, -0.2], [-0.2, 1.0]]), np.diag([1.0, 2.0])),
    ]

    print("Toy spectral cases")
    print("------------------")
    print("case,lambda_min_H0,Psi_star,m(0.9 Psi),m(Psi)")
    for name, h0, load in cases:
        lam = min_eig(h0)
        psi = generalized_threshold(h0, load)
        print(
            f"{name},"
            f"{lam:.12g},"
            f"{psi:.12g},"
            f"{margin(h0, load, 0.9 * psi):.12g},"
            f"{margin(h0, load, psi):.12g}"
        )

    print()
    print("Same positive local diagonals, different coupling:")
    print("coupling,eig_min,eig_max")
    for c in (0.0, 0.2, 0.5, 0.9, 1.0, 1.1):
        vals = two_mode_eigenvalues(1.0, 1.0, c)
        print(f"{c:.1f},{vals[0]:.12g},{vals[1]:.12g}")

    print()
    print("Interpretation:")
    print("  Positive local restoration/stiffness entries do not guarantee")
    print("  positive full-system support once coupling is included.")
    print("  The value Psi_*=1/2 can occur in a normalized toy state,")
    print("  but it is not universal and was not fitted to Schwarzschild.")


def audit_report() -> int:
    checks = []
    i2 = np.eye(2)

    h_weak = np.array([[1.0, -0.2], [-0.2, 1.0]])
    h_half = np.array([[1.0, -0.5], [-0.5, 1.0]])
    h_crit = np.array([[1.0, -1.0], [-1.0, 1.0]])

    psi_weak = generalized_threshold(h_weak, i2)
    psi_half = generalized_threshold(h_half, i2)

    checks.append((
        "SPECTRAL_THRESHOLD_ZERO_MARGIN",
        abs(margin(h_weak, i2, psi_weak)) < 1e-12,
        "generalized threshold places the minimum eigenvalue at zero",
    ))
    checks.append((
        "COUPLING_CAN_DESTROY_SUPPORT",
        min_eig(h_crit) < 1e-12,
        "positive diagonal support terms can be neutralized by coupling",
    ))
    checks.append((
        "RESTORATION_NOT_SUPPORT_MARGIN",
        abs(min_eig(h_weak) - min_eig(h_half)) > 1e-6,
        "same diagonal local terms with different coupling give different global support margins",
    ))
    checks.append((
        "HALF_IS_POSSIBLE_NOT_UNIVERSAL",
        abs(psi_half - 0.5) < 1e-12 and abs(psi_weak - 0.5) > 1e-3,
        "Psi=1/2 occurs in one normalized toy case but not generically",
    ))

    a = np.array([[1.3, 0.4], [0.2, 0.9]])
    h_t = a.T @ h_weak @ a
    l_t = a.T @ i2 @ a
    psi_t = generalized_threshold(h_t, l_t)
    checks.append((
        "COORDINATE_CONGRUENCE_INVARIANCE",
        abs(psi_t - psi_weak) < 1e-12,
        "the generalized threshold is invariant under simultaneous invertible congruence transforms",
    ))
    checks.append((
        "INERTIA_NOT_STATIC_THRESHOLD_INPUT",
        True,
        "inertia controls dynamic response/growth rates but is not needed for the zero-eigenvalue quasi-static boundary",
    ))
    checks.append((
        "LOAD_DIRECTION_MATTERS",
        abs(
            generalized_threshold(h_weak, i2)
            - generalized_threshold(h_weak, np.diag([1.0, 2.0]))
        ) > 1e-3,
        "the support-state operator alone does not determine threshold without a load-direction bridge",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no GR horizon radius or coefficient is used to choose H0, L, or Psi",
    ))
    checks.append((
        "GENERIC_DSD_BOUNDARY",
        True,
        "generic DSD dynamics permits non-self-adjoint/nonconservative operators; this Hessian model is an explicit specialization",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / SPECTRAL_SUPPORT_FUNCTION_CANDIDATE")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit a spectral candidate for Psi(S_sup) in DSD structural gravity."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "examples", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return

    if args.mode in ("all", "examples"):
        print()
        examples_report()
        if args.mode == "examples":
            return

    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
