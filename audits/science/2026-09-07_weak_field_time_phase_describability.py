#!/usr/bin/env python3
"""
Standard weak-field relativity + nonrelativistic QM describability audit.

No quantum-gravity theory is used.
The classical gravitational potential/background is supplied externally.

Checks:
1. weak-field stationary proper-time difference,
2. standard Schrödinger phase from V=m*Phi,
3. agreement of phase scaling with mc^2 * Delta tau / hbar at first order,
4. phase-to-probability fiber collisions,
5. non-identifiability of DeltaPhi and T from their product alone.
"""

from __future__ import annotations

import argparse
import math

C = 299_792_458.0
HBAR = 1.054_571_817e-34


def weak_field_delta_tau(delta_phi: float, coordinate_time: float) -> float:
    """First-order stationary weak-field relation Delta tau ~= DeltaPhi*T/c^2."""
    return delta_phi * coordinate_time / (C * C)


def schrodinger_phase_difference(mass: float, delta_phi: float, coordinate_time: float) -> float:
    """Relative phase from the standard potential-energy term V=m*Phi."""
    return -mass * delta_phi * coordinate_time / HBAR


def proper_time_phase_difference(mass: float, delta_tau: float) -> float:
    """Weak-field comparator -mc^2*DeltaTau/hbar."""
    return -mass * C * C * delta_tau / HBAR


def bright_port_probability(delta_phase: float) -> float:
    """Equal-amplitude two-path interference control P+=(1+cos phase)/2."""
    return 0.5 * (1.0 + math.cos(delta_phase))


def phase_equivalent_probability_family(theta: float, k: int) -> tuple[float, float, float]:
    a = theta
    b = theta + 2.0 * math.pi * k
    c = -theta + 2.0 * math.pi * k
    return (
        bright_port_probability(a),
        bright_port_probability(b),
        bright_port_probability(c),
    )


def report(mass: float, delta_phi: float, coordinate_time: float) -> int:
    dtau = weak_field_delta_tau(delta_phi, coordinate_time)
    phase_v = schrodinger_phase_difference(mass, delta_phi, coordinate_time)
    phase_tau = proper_time_phase_difference(mass, dtau)
    mismatch = abs(phase_v - phase_tau)

    print("STANDARD WEAK-FIELD RELATIVITY + QM DESCRIBABILITY AUDIT")
    print("Classical background supplied externally; no quantum-gravity premise.\n")
    print(f"mass_kg: {mass:.12g}")
    print(f"delta_phi_m2_s2: {delta_phi:.12g}")
    print(f"coordinate_time_s: {coordinate_time:.12g}")
    print(f"delta_tau_s: {dtau:.12g}")
    print(f"phase_from_mPhi_rad: {phase_v:.12g}")
    print(f"phase_from_proper_time_rad: {phase_tau:.12g}")
    print(f"absolute_phase_mismatch: {mismatch:.12g}")
    print()

    p0, p2pi, pminus = phase_equivalent_probability_family(0.731, 3)
    print("[probability fiber witness]")
    print(f"P(theta): {p0:.15g}")
    print(f"P(theta+6pi): {p2pi:.15g}")
    print(f"P(-theta+6pi): {pminus:.15g}")
    same_prob = max(abs(p0 - p2pi), abs(p0 - pminus)) < 1e-12
    print(f"same_probability: {same_prob}")
    print()

    # Product-identifiability witness: two different (DeltaPhi,T) pairs with
    # the same product give the same first-order DeltaTau and phase.
    phi1, t1 = 2.0, 3.0
    phi2, t2 = 1.0, 6.0
    prod_equal = abs(phi1 * t1 - phi2 * t2) < 1e-15
    tau_equal = abs(
        weak_field_delta_tau(phi1, t1) - weak_field_delta_tau(phi2, t2)
    ) < 1e-30
    phase_equal = abs(
        schrodinger_phase_difference(mass, phi1, t1)
        - schrodinger_phase_difference(mass, phi2, t2)
    ) < 1e-12

    print("[parameter identifiability witness]")
    print(f"pair1=(DeltaPhi={phi1}, T={t1})")
    print(f"pair2=(DeltaPhi={phi2}, T={t2})")
    print(f"same_DeltaPhi_times_T: {prod_equal}")
    print(f"same_first_order_DeltaTau: {tau_equal}")
    print(f"same_phase: {phase_equal}")
    print()

    assert mismatch < 1e-9 * max(1.0, abs(phase_v))
    assert same_prob
    assert prod_equal and tau_equal and phase_equal

    print("AUDIT RESULT: PASS_WITH_BOUNDARY")
    print("- coordinate time, proper time, phase and probability remain typed separately")
    print("- the weak-field phase bridge holds only under the stated supplied assumptions")
    print("- probability does not uniquely reconstruct phase")
    print("- phase/proper-time data do not separately identify DeltaPhi and T")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mass", type=float, default=1.0e-26, help="particle/system mass in kg")
    parser.add_argument("--delta-phi", type=float, default=1.0, help="potential difference in m^2/s^2")
    parser.add_argument("--time", type=float, default=1.0, help="coordinate holding time in s")
    args = parser.parse_args()
    return report(args.mass, args.delta_phi, args.time)


if __name__ == "__main__":
    raise SystemExit(main())
