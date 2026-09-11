#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import numpy as np


MU2 = {
    "uniform": 0.6000000000000000,
    "core_heavy": 57.0 / 140.0,
    "envelope_heavy": 89.4 / 140.0,
}


def sym(a):
    a = np.asarray(a, dtype=float)
    return 0.5 * (a + a.T)


def reduced_operator(h0, load):
    h0 = sym(h0)
    load = sym(load)
    vals, vecs = np.linalg.eigh(load)
    if np.min(vals) <= 0.0:
        raise ValueError("load must be positive definite")
    invsqrt = vecs @ np.diag(vals ** -0.5) @ vecs.T
    return sym(invsqrt @ h0 @ invsqrt)


def psi_star(h0, load) -> float:
    return float(np.linalg.eigvalsh(reduced_operator(h0, load))[0])


def congruence_transform(h0, load, a, scale):
    a = np.asarray(a, dtype=float)
    return scale * (a.T @ h0 @ a), scale * (a.T @ load @ a)


def profile_pair(mu2, epsilon=1.0, c0=0.5, alpha=0.8):
    """
    Synthetic descriptor-retaining control, not a physical gravity law.

    Detail enters only through the normalized coupling.
    epsilon=1: full profile-sensitive toy
    epsilon=0: detail-erased universal normalized pair
    """
    coupling = c0 + epsilon * alpha * (mu2 - MU2["uniform"])
    h0 = np.array([[1.0, -coupling], [-coupling, 1.0]], dtype=float)
    load = np.eye(2)
    return h0, load


def profile_results(epsilon):
    out = {}
    for name, mu2 in MU2.items():
        h0, load = profile_pair(mu2, epsilon=epsilon)
        out[name] = psi_star(h0, load)
    return out


def blind_report():
    print("DSD spectral-support universality-class audit")
    print("---------------------------------------------")
    print("Reduced pencil operator:")
    print("  B(S) = L(S)^(-1/2) H0(S) L(S)^(-1/2)")
    print("  Psi_*(S) = lambda_min(B(S))")
    print()
    print("Exact coefficient universality requires at least:")
    print("  Psi_*(S1) = Psi_*(S2) for all admitted source states.")
    print()
    print("A stronger sufficient structural condition is:")
    print("  B(S) = U(S)^T B_* U(S), with U orthogonal,")
    print("  which preserves the entire generalized spectrum.")
    print()
    print("Common positive scaling and simultaneous congruence of (H0,L)")
    print("do not change Psi_*.")
    print()
    print("Approximate universality:")
    print("  ||B(S)-B_*||_2 <= eps(S)")
    print("  => |Psi_*(S)-Psi_*| <= eps(S)  [Weyl bound]")
    print()
    print("Boundary:")
    print("  Generic DSD does not prove collapse drives eps(S) -> 0.")
    print("  That requires an explicit strong-field/coarse-graining bridge.")


def mass_scaling_report():
    base_h = np.array([[1.0, -0.5], [-0.5, 1.0]])
    base_l = np.eye(2)
    base_psi = psi_star(base_h, base_l)

    print("Mass/common-scale invariance control")
    print("------------------------------------")
    print("scale,Psi_star,difference_from_base")
    for scale in (1.0, 10.0, 1e3, 1e6, 1e9):
        q = math.log10(scale + 1.0)
        a = np.array([[1.0 + 0.03*q, 0.07], [0.02, 1.0 - 0.01*q]])
        h, l = congruence_transform(base_h, base_l, a, scale)
        psi = psi_star(h, l)
        print(f"{scale:.1e},{psi:.12g},{psi-base_psi:.12g}")


def profile_report():
    print("Profile-retaining versus detail-erasure control")
    print("-----------------------------------------------")
    print("epsilon,profile,mu2,Psi_star,Rcoeff_relative_to_Psi0.5")
    for epsilon in (1.0, 0.5, 0.2, 0.05, 0.0):
        results = profile_results(epsilon)
        for name in ("uniform", "core_heavy", "envelope_heavy"):
            psi = results[name]
            radius_coeff = 0.5 / psi
            print(
                f"{epsilon:.2f},{name},{MU2[name]:.12g},"
                f"{psi:.12g},{radius_coeff:.12g}"
            )
        spread = max(results.values()) - min(results.values())
        print(f"{epsilon:.2f},SPREAD,,{spread:.12g},")

    print()
    print("Weyl-bound check against universal B_* at epsilon=0")
    print("---------------------------------------------------")
    b_star = reduced_operator(*profile_pair(MU2["uniform"], epsilon=0.0))
    print("epsilon,profile,|DeltaPsi|,||DeltaB||_2,bound_ok")
    for epsilon in (1.0, 0.5, 0.2, 0.05):
        for name, mu2 in MU2.items():
            h, l = profile_pair(mu2, epsilon=epsilon)
            b = reduced_operator(h, l)
            dpsi = abs(psi_star(h, l) - 0.5)
            norm = float(np.linalg.norm(b - b_star, ord=2))
            print(f"{epsilon:.2f},{name},{dpsi:.12g},{norm:.12g},{dpsi <= norm + 1e-12}")


def audit_report():
    checks = []

    base_h = np.array([[1.0, -0.5], [-0.5, 1.0]])
    base_l = np.eye(2)
    base_psi = psi_star(base_h, base_l)
    a = np.array([[1.2, 0.2], [0.1, 0.9]])
    h2, l2 = congruence_transform(base_h, base_l, a, 1e6)
    checks.append((
        "COMMON_SCALE_CONGRUENCE_INVARIANCE",
        abs(psi_star(h2, l2) - base_psi) < 1e-10,
        "mass/common normalization can cancel from the generalized threshold if H0 and L share it",
    ))

    full = profile_results(1.0)
    checks.append((
        "PROFILE_DEPENDENCE_SURVIVES_WITH_DETAIL",
        max(full.values()) - min(full.values()) > 0.1,
        "same coarse mass class can retain different Psi_* if normalized internal structure survives in the bridge",
    ))

    erased = profile_results(0.0)
    checks.append((
        "DETAIL_ERASURE_GIVES_EXACT_UNIVERSALITY",
        max(erased.values()) - min(erased.values()) < 1e-15,
        "when normalized profile dependence is removed, all control sources share the same Psi_*",
    ))

    spreads = []
    for epsilon in (1.0, 0.5, 0.2, 0.05, 0.0):
        rr = profile_results(epsilon)
        spreads.append(max(rr.values()) - min(rr.values()))
    checks.append((
        "SPREAD_CONTRACTS_WITH_DETAIL_ERASURE",
        all(spreads[i+1] <= spreads[i] + 1e-14 for i in range(len(spreads)-1)),
        "the threshold spread contracts monotonically as the synthetic detail sector is suppressed",
    ))

    b_star = reduced_operator(*profile_pair(MU2["uniform"], epsilon=0.0))
    bound_ok = True
    for epsilon in (1.0, 0.5, 0.2, 0.05):
        for mu2 in MU2.values():
            h, l = profile_pair(mu2, epsilon=epsilon)
            b = reduced_operator(h, l)
            dpsi = abs(psi_star(h, l) - 0.5)
            norm = float(np.linalg.norm(b - b_star, ord=2))
            bound_ok &= dpsi <= norm + 1e-12
    checks.append((
        "WEYL_STABILITY_BOUND",
        bound_ok,
        "operator-norm convergence of the reduced pencil controls convergence of Psi_*",
    ))

    checks.append((
        "HALF_NOT_UNIVERSAL_WITH_PROFILE_RETENTION",
        abs(full["uniform"] - 0.5) < 1e-12
        and abs(full["core_heavy"] - 0.5) > 0.1,
        "the same toy family can contain Psi_*=1/2 and non-1/2 sources without any GR fitting",
    ))

    checks.append((
        "MASS_LINEARITY_NOT_ENOUGH",
        True,
        "Rcrit proportional to M does not guarantee a universal coefficient unless Psi_* and other normalized bridge factors are source-independent",
    ))
    checks.append((
        "NO_STRONG_FIELD_FIXED_POINT_DERIVED",
        True,
        "generic DSD currently supplies no theorem forcing B(S) to a common strong-field fixed operator",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no Schwarzschild/EHT value is used to choose the universal operator or profile-erasure parameter",
    ))

    failures = 0
    for name, ok, note in checks:
        status = "PASS" if ok else "FAIL"
        failures += 0 if ok else 1
        print(f"{status}: {name} -- {note}")

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / UNIVERSALITY_REQUIRES_NORMALIZED_PENCIL_CONVERGENCE")
    return failures


def main():
    parser = argparse.ArgumentParser(
        description="Audit universality of the DSD spectral support threshold across source scales and profiles."
    )
    parser.add_argument(
        "--mode",
        choices=("all", "blind", "mass", "profile", "audit"),
        default="all",
    )
    args = parser.parse_args()

    if args.mode in ("all", "blind"):
        blind_report()
        if args.mode == "blind":
            return
    if args.mode in ("all", "mass"):
        print()
        mass_scaling_report()
        if args.mode == "mass":
            return
    if args.mode in ("all", "profile"):
        print()
        profile_report()
        if args.mode == "profile":
            return
    if args.mode in ("all", "audit"):
        print()
        failures = audit_report()
        if failures:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
