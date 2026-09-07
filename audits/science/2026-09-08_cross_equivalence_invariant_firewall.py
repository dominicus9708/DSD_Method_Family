#!/usr/bin/env python3
"""
Cross-theory equivalence/invariant firewall witness for DSD Track 2.

Checks:
1. Equal selected Lorentz invariants need not classify an entire multi-vector configuration.
2. Quantum pure-state vectors differing only by global phase are physically ray-equivalent
   while their raw vector coordinates differ; projector/readout data are unchanged.
3. The script reports scoped outcomes only. It does not identify either standard-theory
   equivalence with DSD strict formation/property equivalence.

Standard-library only.
"""

from __future__ import annotations

import argparse
import cmath
import math

TOL = 1e-12


def minkowski_dot(a: tuple[float, float], b: tuple[float, float]) -> float:
    """1+1 Minkowski product with signature (-,+)."""
    return -a[0] * b[0] + a[1] * b[1]


def lorentz_selected_invariant_collision() -> dict[str, object]:
    # Configuration A: ordered pair (u_A, v_A)
    u_a = (1.0, 0.0)
    v_a = (0.0, 1.0)

    # Configuration B: same individual squared norms, different mutual product.
    u_b = (1.0, 0.0)
    v_b = (1.0, math.sqrt(2.0))

    selected_a = (minkowski_dot(u_a, u_a), minkowski_dot(v_a, v_a))
    selected_b = (minkowski_dot(u_b, u_b), minkowski_dot(v_b, v_b))
    mutual_a = minkowski_dot(u_a, v_a)
    mutual_b = minkowski_dot(u_b, v_b)

    selected_equal = all(abs(x - y) <= TOL for x, y in zip(selected_a, selected_b))
    mutual_differs = abs(mutual_a - mutual_b) > TOL

    # Any single Lorentz transformation applied to both vectors preserves every pairwise
    # Minkowski inner product. Therefore differing mutual products obstruct one common
    # Lorentz transformation between the ordered-pair configurations.
    not_same_lorentz_orbit_for_pair = selected_equal and mutual_differs

    return {
        "selected_invariants_A": selected_a,
        "selected_invariants_B": selected_b,
        "selected_invariants_equal": selected_equal,
        "mutual_inner_product_A": mutual_a,
        "mutual_inner_product_B": mutual_b,
        "mutual_inner_product_differs": mutual_differs,
        "same_selected_invariants_not_complete_for_pair_orbit": not_same_lorentz_orbit_for_pair,
    }


def projector(v: tuple[complex, complex]) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return (
        (v[0] * v[0].conjugate(), v[0] * v[1].conjugate()),
        (v[1] * v[0].conjugate(), v[1] * v[1].conjugate()),
    )


def max_matrix_difference(a, b) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def quantum_global_phase_audit() -> dict[str, object]:
    psi = (complex(1.0 / math.sqrt(3.0)), complex(math.sqrt(2.0 / 3.0)))
    theta = math.pi / 3.0
    phase = cmath.exp(1j * theta)
    phi = tuple(phase * z for z in psi)

    raw_vectors_differ = any(abs(a - b) > TOL for a, b in zip(psi, phi))
    p_psi = projector(psi)
    p_phi = projector(phi)
    projector_diff = max_matrix_difference(p_psi, p_phi)

    z_prob_psi = (abs(psi[0]) ** 2, abs(psi[1]) ** 2)
    z_prob_phi = (abs(phi[0]) ** 2, abs(phi[1]) ** 2)
    z_prob_equal = all(abs(a - b) <= TOL for a, b in zip(z_prob_psi, z_prob_phi))

    return {
        "phase_theta": theta,
        "raw_vectors_differ": raw_vectors_differ,
        "projector_max_difference": projector_diff,
        "projectors_equal": projector_diff <= TOL,
        "z_measurement_probabilities_psi": z_prob_psi,
        "z_measurement_probabilities_phi": z_prob_phi,
        "z_probabilities_equal": z_prob_equal,
        "ray_equivalence_erases_global_phase": raw_vectors_differ and projector_diff <= TOL,
    }


def report() -> int:
    print("CROSS-THEORY EQUIVALENCE / INVARIANT FIREWALL")
    print()

    rel = lorentz_selected_invariant_collision()
    print("[1] Lorentz selected-invariant collision")
    for key, value in rel.items():
        print(f"{key}: {value}")
    print()

    qm = quantum_global_phase_audit()
    print("[2] Quantum global-phase quotient")
    for key, value in qm.items():
        print(f"{key}: {value}")
    print()

    assert rel["selected_invariants_equal"]
    assert rel["mutual_inner_product_differs"]
    assert rel["same_selected_invariants_not_complete_for_pair_orbit"]
    assert qm["raw_vectors_differ"]
    assert qm["projectors_equal"]
    assert qm["z_probabilities_equal"]
    assert qm["ray_equivalence_erases_global_phase"]

    print("SCOPED OUTCOMES")
    print("selected Lorentz invariant values: VALID_IN_DOMAIN")
    print("selected invariant equality -> full standard equivalence: NOT_SUFFICIENT_FOR_EXTENSION")
    print("quantum raw vector equality = physical pure-state equality: REJECTED")
    print("quantum ray/global-phase equivalence: VALID_IN_DOMAIN")
    print("standard equivalence = DSD strict equivalence without an explicit typed map: NON_IDENTICAL")
    print("SUMMARY: PASS_WITH_BOUNDARY")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
