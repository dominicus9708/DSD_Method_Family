#!/usr/bin/env python3
"""
Finite counterexample audit for the minimum QFT -> DSD gravity common interface.

This is a structural toy witness only.  The four source coordinates
(rho, flux, pressure, anisotropy) stand for a finite selected projection
of renormalized stress-energy data.  The response map is deliberately
synthetic and is NOT a gravitational or QFT law.

Purpose:
1. test whether a reduced DSD gravity source bridge is sufficient for
   a selected comparator response;
2. exhibit a same-bridge / different-response fiber collision;
3. verify the linear kernel criterion by explicit witnesses.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from itertools import combinations, product
from typing import Callable, Sequence, Tuple


@dataclass(frozen=True)
class Source:
    rho: int
    flux: int
    pressure: int
    anisotropy: int


Bridge = Callable[[Source], Tuple[int, ...]]
Response = Callable[[Source], Tuple[int, ...]]


def bridge_rho(s: Source) -> Tuple[int, ...]:
    return (s.rho,)


def bridge_rho_pressure(s: Source) -> Tuple[int, ...]:
    return (s.rho, s.pressure)


def bridge_full(s: Source) -> Tuple[int, ...]:
    return (s.rho, s.flux, s.pressure, s.anisotropy)


def toy_comparator_response(s: Source) -> Tuple[int, ...]:
    """
    Synthetic response used only to test factorization.

    It reads sectors that rho-only and (rho, pressure) bridges may discard.
    No physical meaning is assigned to the numerical coefficients.
    """
    return (
        s.rho + 2 * s.pressure + s.anisotropy,
        s.flux + s.anisotropy,
    )


def cube_sources() -> list[Source]:
    return [Source(*vals) for vals in product((0, 1), repeat=4)]


def violating_pairs(
    sources: Sequence[Source],
    bridge: Bridge,
    response: Response,
) -> list[tuple[Source, Source]]:
    """
    Return pairs in one bridge fiber with different comparator responses.
    Any returned pair proves that response cannot factor through bridge
    on the tested source family.
    """
    bad: list[tuple[Source, Source]] = []
    for a, b in combinations(sources, 2):
        if bridge(a) == bridge(b) and response(a) != response(b):
            bad.append((a, b))
    return bad


def linear_bridge_rho(v: Tuple[int, int, int, int]) -> Tuple[int, ...]:
    return (v[0],)


def linear_bridge_rho_pressure(v: Tuple[int, int, int, int]) -> Tuple[int, ...]:
    return (v[0], v[2])


def linear_response(v: Tuple[int, int, int, int]) -> Tuple[int, ...]:
    rho, flux, pressure, anisotropy = v
    return (
        rho + 2 * pressure + anisotropy,
        flux + anisotropy,
    )


def kernel_witnesses() -> dict[str, tuple[Tuple[int, ...], Tuple[int, ...], Tuple[int, ...]]]:
    """
    Explicit d with C(d)=0 but H(d)!=0 where available.
    This witnesses ker(C) not subset ker(H).
    """
    candidates = {
        "rho": (0, 0, 1, 0),
        "rho_pressure": (0, 1, 0, 0),
    }
    out = {}
    for name, d in candidates.items():
        bridge = linear_bridge_rho if name == "rho" else linear_bridge_rho_pressure
        out[name] = (d, bridge(d), linear_response(d))
    return out


def report() -> int:
    sources = cube_sources()
    tests = [
        ("rho", bridge_rho),
        ("rho_pressure", bridge_rho_pressure),
        ("full", bridge_full),
    ]

    print("QFT -> DSD gravity minimum-interface finite witness")
    print("source family size:", len(sources))
    print("response is synthetic; no physical-law claim is made")
    print()

    for name, bridge in tests:
        bad = violating_pairs(sources, bridge, toy_comparator_response)
        factorizes_on_test_family = len(bad) == 0
        print(f"[{name}]")
        print("violating fiber pairs:", len(bad))
        print("factorizes on tested family:", factorizes_on_test_family)
        if bad:
            a, b = bad[0]
            print("first witness A:", a)
            print("first witness B:", b)
            print("shared bridge output:", bridge(a))
            print("response(A):", toy_comparator_response(a))
            print("response(B):", toy_comparator_response(b))
        print()

    print("[linear kernel witnesses]")
    for name, (d, cd, hd) in kernel_witnesses().items():
        print(f"{name}: d={d}, C(d)={cd}, H(d)={hd}")
        assert all(x == 0 for x in cd)
        assert any(x != 0 for x in hd)

    assert not violating_pairs(sources, bridge_full, toy_comparator_response)
    assert violating_pairs(sources, bridge_rho, toy_comparator_response)
    assert violating_pairs(sources, bridge_rho_pressure, toy_comparator_response)

    print()
    print("AUDIT RESULT: reduced scalar/partial bridges are insufficient for this")
    print("toy comparator; the full selected source record is sufficient on the")
    print("tested finite family. Physical sufficiency remains an external-theory")
    print("question and requires an admissible QFT source class and real response law.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=("all",),
        default="all",
        help="Run the complete finite factorization audit.",
    )
    parser.parse_args()
    return report()


if __name__ == "__main__":
    raise SystemExit(main())
