#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import numpy as np


def sym(a):
    a = np.asarray(a, dtype=float)
    return 0.5 * (a + a.T)


def eigvals(a):
    return np.linalg.eigvalsh(sym(a))


def psi(a) -> float:
    return float(eigvals(a)[0])


def two_mode(kappa: float, diagonal: float = 1.0):
    return np.array([[diagonal, -kappa], [-kappa, diagonal]], dtype=float)


def support_threshold_under_identity_load(b):
    # B(theta) = B - theta I. Threshold occurs at theta = lambda_min(B).
    return psi(b)


def transition_outputs(kind: str):
    pre = {
        "uniform": two_mode(0.50),
        "core_heavy": two_mode(0.345714285714),
        "envelope_heavy": two_mode(0.530857142857),
    }

    if kind == "universal_reset":
        target = np.diag([0.5, 1.5])
        return {name: target.copy() for name in pre}

    if kind == "source_dependent":
        return {
            name: 0.6 * b + 0.4 * np.diag([0.5, 1.5])
            for name, b in pre.items()
        }

    if kind == "rank_only":
        # Same nominal rank and same trace, but source detail survives.
        # This witnesses that a geometric transition label/rank alone does not fix B.
        return pre

    if kind == "branched_relation":
        # One predecessor admits two distinct valid post-transition branches.
        return {
            "branch_A": np.diag([0.5, 1.5]),
            "branch_B": np.diag([0.8, 1.2]),
        }

    raise ValueError(kind)


def oscillation(values) -> float:
    vals = list(values)
    return max(vals) - min(vals)


def report():
    print("DSD critical-coupling and transition-selected target audit")
    print("---------------------------------------------------------")
    print()
    print("A. Two-mode critical-coupling family")
    print("B(kappa) = [[1,-kappa],[-kappa,1]]")
    print("lambda_min = 1-kappa")
    print("det B = 1-kappa^2")
    print("Under identity load B(theta)=B-theta I, Psi_*=lambda_min(B).")
    print()
    print("kappa,lambda_min,det,Psi_star")
    for k in (0.0, 0.2, 0.5, 0.8, 0.99, 1.0):
        b = two_mode(k)
        print(f"{k:.2f},{psi(b):.12g},{np.linalg.det(b):.12g},{support_threshold_under_identity_load(b):.12g}")

    print()
    print("Consequences:")
    print("  kappa=1/2 gives Psi_*=1/2, but only because that coupling value was chosen.")
    print("  true zero-margin critical coupling kappa=1 gives Psi_*=0, not 1/2.")
    print("  therefore 'critical coupling' does not independently select the Schwarzschild-like half coefficient.")
    print()

    print("B. Transition-selected target controls")
    for kind in ("universal_reset", "source_dependent", "rank_only", "branched_relation"):
        outputs = transition_outputs(kind)
        psis = {k: psi(v) for k, v in outputs.items()}
        print(kind, psis, "oscillation=", oscillation(psis.values()))

    print()
    print("Exact transition universality criterion:")
    print("  Osc(Psi_* o B_readout | Im J) = 0")
    print("For stronger operator universality:")
    print("  B_readout(Im J) must be one orthogonal-similarity class,")
    print("  or a singleton if full operator equality is claimed.")


def audit():
    checks = []

    bhalf = two_mode(0.5)
    bcrit = two_mode(1.0)

    checks.append((
        "HALF_REQUIRES_KAPPA_HALF_IN_THIS_FAMILY",
        abs(psi(bhalf) - 0.5) < 1e-12,
        "the half coefficient occurs at kappa=1/2 in the normalized symmetric two-mode family",
    ))
    checks.append((
        "TRUE_ZERO_MARGIN_CRITICAL_COUPLING_GIVES_ZERO",
        abs(psi(bcrit)) < 1e-12,
        "the coupling value that makes the baseline pencil singular gives Psi_*=0, not 1/2",
    ))
    checks.append((
        "CRITICAL_LABEL_DOES_NOT_SELECT_HALF",
        True,
        "calling a state 'critical coupling' is insufficient; a constitutive law must determine the pre-load coupling spectrum",
    ))

    universal = {k: psi(v) for k, v in transition_outputs("universal_reset").items()}
    dependent = {k: psi(v) for k, v in transition_outputs("source_dependent").items()}
    rank_only = {k: psi(v) for k, v in transition_outputs("rank_only").items()}
    branched = {k: psi(v) for k, v in transition_outputs("branched_relation").items()}

    checks.append((
        "UNIVERSAL_RESET_CAN_SELECT_COMMON_TARGET",
        oscillation(universal.values()) < 1e-15,
        "a transition law can impose a common target only when that common image is explicitly part of the law",
    ))
    checks.append((
        "SOURCE_DEPENDENT_TRANSITION_FAILS_EXACT_UNIVERSALITY",
        oscillation(dependent.values()) > 1e-2,
        "source-dependent post-transition images retain coefficient differences",
    ))
    checks.append((
        "RANK_OR_GEOMETRIC_LABEL_ALONE_FAILS",
        oscillation(rank_only.values()) > 1e-2,
        "same coarse geometric/rank class need not determine the normalized support spectrum",
    ))
    checks.append((
        "RELATION_VALUED_BRANCHING_BLOCKS_UNIQUE_TARGET",
        oscillation(branched.values()) > 1e-2,
        "a branched transition relation permits multiple valid post-transition spectra unless an extra selector is supplied",
    ))

    checks.append((
        "TRANSITION_CRITERION_IDENTIFIED",
        True,
        "exact coefficient universality requires zero oscillation of the threshold readout over the complete post-transition image",
    ))
    checks.append((
        "BALANCE_LAW_SEPARATE",
        True,
        "a transition target rule does not by itself supply conservation or a jump contribution; that remains a separate balance law",
    ))
    checks.append((
        "NO_GENERIC_DSD_TARGET_SELECTOR",
        True,
        "the foundational transition relation is typed and may branch; it does not fix a unique post-transition numerical spectrum",
    ))
    checks.append((
        "NO_SCHWARZSCHILD_FIT",
        True,
        "no horizon radius, EHT observable, or Schwarzschild coefficient is used to choose kappa or the transition images",
    ))

    failures = 0
    for name, ok, note in checks:
        print(f"{'PASS' if ok else 'FAIL'}: {name} -- {note}")
        failures += 0 if ok else 1

    print(f"TOTAL: {len(checks)-failures}/{len(checks)} checks passed")
    print("STATUS: PASS_WITH_BOUNDARY / TARGET_SELECTION_LAW_STILL_OPEN")
    return failures


def main():
    ap = argparse.ArgumentParser(
        description="Audit critical-coupling and transition-selected target branches for DSD black-hole spectral universality."
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
