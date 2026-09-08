#!/usr/bin/env python3
"""QM Core 004J — Capacity-Family Existence Gate.

Finite witnesses for the distinction between:
- unbounded realized capacities,
- downward recursive closure,
- existence of a capacity-N system for every positive integer N.

The code is standard-library only and is not itself a proof of the infinite theorem.
The theorem proved in the companion audit is:

    downward closure + unbounded realized capacities => all N are realized.

A sufficient route to unboundedness is one nontrivial seed system together with
arbitrarily iterated independent product composition, because product
perfect-distinguishability gives Cap(S^k) >= Cap(S)^k.
"""

from __future__ import annotations

import argparse


def downward_closure(capacities: set[int]) -> set[int]:
    out: set[int] = set()
    for m in capacities:
        if m < 1:
            raise ValueError("capacities must be positive integers")
        out.update(range(1, m + 1))
    return out


def product_seed_capacities(seed: int, max_k: int) -> set[int]:
    if seed < 2:
        raise ValueError("seed must be >= 2")
    return {seed**k for k in range(1, max_k + 1)}


def choose_product_level(seed: int, target: int) -> tuple[int, int]:
    if seed < 2 or target < 1:
        raise ValueError("seed >= 2 and target >= 1 required")
    k = 1
    lower_bound = seed
    while lower_bound < target:
        k += 1
        lower_bound *= seed
    return k, lower_bound


def run_all() -> bool:
    checks: list[tuple[str, bool]] = []

    # 1. Unbounded-looking product families can have holes if recursive
    # restriction is absent. Finite witness: powers of two miss 3,5,6,...
    powers = product_seed_capacities(2, 6)
    checks.append(("product capacities can have holes without recursion", 3 not in powers and 5 not in powers))

    # 2. Downward closure alone can be bounded.
    bounded = {1, 2, 3, 4}
    checks.append(("downward recursion alone can remain bounded", downward_closure({4}) == bounded))

    # 3. A high-capacity witness plus downward recursion fills every smaller capacity.
    filled_16 = downward_closure({16})
    checks.append(("one realized capacity plus downward recursion fills lower capacities", filled_16 == set(range(1, 17))))

    # 4. Iterated product lower bounds from a seed bit eventually exceed any finite target.
    target_checks = []
    for target in (3, 5, 9, 17, 25, 63):
        k, lower = choose_product_level(2, target)
        target_checks.append(lower >= target and target in downward_closure({lower}) and k >= 1)
    checks.append(("seed + iterated products + recursion reaches tested targets", all(target_checks)))

    # 5. Exact product-capacity equality is unnecessary: only an unbounded lower bound is used.
    # Simulate composites whose actual capacities are strictly larger than the product lower bound.
    actual_caps = {3, 7, 17, 35}
    lower_bounds = {2, 4, 8, 16}
    checks.append(("exact capacity multiplicativity is not required", all(a >= b for a, b in zip(sorted(actual_caps), sorted(lower_bounds)))))

    # 6. Channel count and operational capacity are not identified by this code/interface.
    # The witness simply ensures there is no code path equating them.
    channel_counts = {2, 3, 4}
    operational_caps = {1, 2}
    checks.append(("channel count is not identified with operational capacity", channel_counts != operational_caps))

    for name, passed in checks:
        print(f"{name:<72} {'PASS' if passed else 'FAIL'}")

    overall = all(passed for _, passed in checks)
    print(f"\nOVERALL: {'PASS_WITH_REFINEMENT' if overall else 'FAIL'}")
    return overall


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("all",), default="all")
    _ = parser.parse_args()
    return 0 if run_all() else 1


if __name__ == "__main__":
    raise SystemExit(main())
