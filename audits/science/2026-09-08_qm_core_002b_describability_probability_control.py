#!/usr/bin/env python3
"""
QM Core 002B — DSD describability-difference / objective probability-control witness.

Standard-library only.

The script tests a finite-dimensional qubit specialization of the identity

    ||rho-E||_HS^2 = Tr(rho^2) + Tr(E^2) - 2 Tr(rho E)

and therefore, between two times,

    2 Delta p = I_D + Delta purity + Delta effect_norm,

where
    p = Tr(rho E),
    I_D = D_before^2 - D_after^2.

For a fixed rank-one target effect E=P0, Delta effect_norm = 0.

The tests separate:
1. fixed-purity target approach: distance reduction iff target probability rises;
2. an open-system positive witness: amplitude damping raises P0 probability;
3. a counterexample: depolarization reduces total HS distance while P0 probability falls;
4. access-only change: observer/access metadata can change without objective Born probability;
5. the corrected DSD interaction score exactly reproduces Delta p in all physical-state tests.

This does NOT introduce a non-Born probability law.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from typing import Callable

TOL = 1e-12


@dataclass(frozen=True)
class BlochState:
    x: float
    y: float
    z: float

    def norm2(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def validate(self) -> None:
        if self.norm2() > 1.0 + TOL:
            raise ValueError(f"unphysical Bloch vector: |r|^2={self.norm2()}")

    def purity(self) -> float:
        self.validate()
        return 0.5 * (1.0 + self.norm2())

    def p0(self) -> float:
        self.validate()
        return 0.5 * (1.0 + self.z)

    def hs2_to_p0(self) -> float:
        # E=P0 is rank-one, hence Tr(E^2)=1.
        return self.purity() + 1.0 - 2.0 * self.p0()


def close(a: float, b: float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def interaction_terms(before: BlochState, after: BlochState) -> tuple[float, float, float, float]:
    """
    Returns:
        I_D             = D_before^2 - D_after^2
        Delta_purity    = purity_after - purity_before
        J_objective     = I_D + Delta_purity  (fixed P0 effect)
        Delta_p         = p0_after - p0_before

    Exact identity:
        Delta_p = J_objective / 2.
    """
    i_d = before.hs2_to_p0() - after.hs2_to_p0()
    d_purity = after.purity() - before.purity()
    j_objective = i_d + d_purity
    delta_p = after.p0() - before.p0()
    return i_d, d_purity, j_objective, delta_p


def test_fixed_purity_target_approach() -> None:
    # Pure |+> -> pure state at alpha=pi/6 relative to |0>.
    before = BlochState(1.0, 0.0, 0.0)
    after = BlochState(math.sqrt(3.0) / 2.0, 0.0, 0.5)

    i_d, d_purity, j, delta_p = interaction_terms(before, after)

    assert close(before.purity(), 1.0)
    assert close(after.purity(), 1.0)
    assert i_d > 0.0
    assert close(d_purity, 0.0)
    assert delta_p > 0.0
    assert close(delta_p, j / 2.0)
    assert close(before.p0(), 0.5)
    assert close(after.p0(), 0.75)

    print("[fixed-purity target approach] PASS")
    print(f"  p0: {before.p0():.6f} -> {after.p0():.6f}")
    print(f"  D_HS^2: {before.hs2_to_p0():.6f} -> {after.hs2_to_p0():.6f}")
    print(f"  I_D={i_d:.6f}, Delta purity={d_purity:.6f}, Delta p={delta_p:.6f}")


def amplitude_damping(state: BlochState, gamma: float) -> BlochState:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must be in [0,1]")
    s = math.sqrt(1.0 - gamma)
    # Standard amplitude damping toward |0> in the z convention used here.
    return BlochState(
        s * state.x,
        s * state.y,
        (1.0 - gamma) * state.z + gamma,
    )


def test_open_system_positive_witness() -> None:
    before = BlochState(1.0, 0.0, 0.0)  # |+>
    after = amplitude_damping(before, 0.5)

    i_d, d_purity, j, delta_p = interaction_terms(before, after)

    assert i_d > 0.0
    assert d_purity < 0.0
    assert j > 0.0
    assert delta_p > 0.0
    assert close(delta_p, j / 2.0)
    assert close(before.p0(), 0.5)
    assert close(after.p0(), 0.75)

    print("[open-system positive witness] PASS")
    print(f"  p0: {before.p0():.6f} -> {after.p0():.6f}")
    print(f"  D_HS^2: {before.hs2_to_p0():.6f} -> {after.hs2_to_p0():.6f}")
    print(f"  I_D={i_d:.6f}, Delta purity={d_purity:.6f}, J={j:.6f}")


def depolarize(state: BlochState, lam: float) -> BlochState:
    # Isotropic qubit depolarizing contraction r -> lam r.
    # The selected lam=0.8 lies in the CPTP interval [-1/3,1].
    return BlochState(lam * state.x, lam * state.y, lam * state.z)


def test_distance_only_counterexample() -> None:
    before = BlochState(0.8, 0.0, 0.5)
    after = depolarize(before, 0.8)

    i_d, d_purity, j, delta_p = interaction_terms(before, after)

    # Total Hilbert-Schmidt distance to P0 shrinks...
    assert i_d > 0.0
    # ...yet the target Born probability falls because purity drops more strongly.
    assert delta_p < 0.0
    assert d_purity < -i_d
    assert j < 0.0
    assert close(delta_p, j / 2.0)

    print("[distance-only counterexample] PASS")
    print(f"  p0: {before.p0():.6f} -> {after.p0():.6f}  (falls)")
    print(f"  D_HS^2: {before.hs2_to_p0():.6f} -> {after.hs2_to_p0():.6f}  (also falls)")
    print(f"  I_D={i_d:.6f}, Delta purity={d_purity:.6f}, J={j:.6f}")
    print("  conclusion: distance reduction alone is not sufficient under purity-changing dynamics")


def test_access_only_change() -> None:
    state = BlochState(1.0, 0.0, 0.0)
    # DSD access/observer record is allowed to change independently of rho and E.
    access_gap_before = 1.0
    access_gap_after = 0.0

    assert access_gap_after < access_gap_before
    assert close(state.p0(), 0.5)

    # Objective quantum state/effect pair is unchanged, so objective Born probability is unchanged.
    before = state
    after = state
    i_d, d_purity, j, delta_p = interaction_terms(before, after)
    assert close(i_d, 0.0)
    assert close(d_purity, 0.0)
    assert close(j, 0.0)
    assert close(delta_p, 0.0)

    print("[access-only change] PASS")
    print("  access gap: 1.0 -> 0.0")
    print(f"  objective p0 remains {state.p0():.6f}")
    print("  conclusion: access/knowledge improvement alone does not raise objective Born probability")


def test_corrected_score_identity() -> None:
    cases = [
        (BlochState(1.0, 0.0, 0.0), BlochState(math.sqrt(3.0) / 2.0, 0.0, 0.5)),
        (BlochState(1.0, 0.0, 0.0), amplitude_damping(BlochState(1.0, 0.0, 0.0), 0.5)),
        (BlochState(0.8, 0.0, 0.5), depolarize(BlochState(0.8, 0.0, 0.5), 0.8)),
    ]

    for before, after in cases:
        _, _, j, delta_p = interaction_terms(before, after)
        assert close(delta_p, j / 2.0)

    print("[corrected objective interaction score] PASS")
    print("  Delta p = (I_D + Delta purity)/2 for every fixed-P0 witness")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all", "pure", "open", "counterexample", "access", "identity"),
        default="all",
    )
    args = parser.parse_args()

    tests: dict[str, Callable[[], None]] = {
        "pure": test_fixed_purity_target_approach,
        "open": test_open_system_positive_witness,
        "counterexample": test_distance_only_counterexample,
        "access": test_access_only_change,
        "identity": test_corrected_score_identity,
    }

    if args.mode == "all":
        for test in tests.values():
            test()
        print("OVERALL: PASS_WITH_REFINEMENT")
    else:
        tests[args.mode]()


if __name__ == "__main__":
    main()
