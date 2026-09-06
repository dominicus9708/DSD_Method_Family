#!/usr/bin/env python3
"""
DSD / Quantum Darwinism heterogeneous-fragment audit.

This script studies a deliberately restricted binary cq pointer-record specialization:
    rho_SF = 1/2 sum_{s=0,1} |s><s| tensor |e_s^F><e_s^F|
with product conditional fragment records. If environment unit i has conditional-state
overlap c_i in [0,1], then a fragment F has overlap
    C_F = product_{i in F} c_i.

For this specialization:
    I_QMI(S:F) = H2((1 + C_F)/2)
and the optimal binary discrimination error is the Helstrom error
    e_F = (1 - sqrt(1 - C_F^2))/2,
giving the accessible binary information
    I_acc(F) = 1 - H2(e_F).

Define additive record weights w_i = -log(c_i). A threshold C_F <= tau is equivalent
to sum_{i in F} w_i >= -log(tau).

The "disjoint sufficient-fragment redundancy" computed here is a DSD audit
diagnostic for heterogeneous discrete environments. It is not asserted to be
identical to every standard Quantum Darwinism redundancy convention.
"""

from __future__ import annotations

import argparse
import itertools
import math
from functools import lru_cache


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def qmi_from_overlap(c: float) -> float:
    return h2((1.0 + c) / 2.0)


def accessible_from_overlap(c: float) -> float:
    err = (1.0 - math.sqrt(max(0.0, 1.0 - c * c))) / 2.0
    return 1.0 - h2(err)


def overlap_threshold(delta: float, diagnostic: str) -> float:
    target = 1.0 - delta
    lo, hi = 0.0, 1.0
    fn = qmi_from_overlap if diagnostic == "qmi" else accessible_from_overlap
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if fn(mid) >= target:
            lo = mid
        else:
            hi = mid
    return lo


def exact_disjoint_redundancy(weights, threshold=1.0):
    """Exact maximum number of pairwise-disjoint sufficient subsets.

    Bitmask dynamic programming; intended for n <= 22.
    """
    n = len(weights)
    if n > 22:
        raise ValueError("exact bitmask solver limited to n <= 22")

    sums = [0.0] * (1 << n)
    for mask in range(1, 1 << n):
        lb = mask & -mask
        i = lb.bit_length() - 1
        sums[mask] = sums[mask ^ lb] + weights[i]

    minimal_covers = []
    for mask in range(1, 1 << n):
        if sums[mask] + 1e-12 < threshold:
            continue
        mm = mask
        is_minimal = True
        while mm:
            lb = mm & -mm
            if sums[mask ^ lb] + 1e-12 >= threshold:
                is_minimal = False
                break
            mm ^= lb
        if is_minimal:
            minimal_covers.append(mask)

    covers_by_item = [[] for _ in range(n)]
    for cover in minimal_covers:
        mm = cover
        while mm:
            lb = mm & -mm
            i = lb.bit_length() - 1
            covers_by_item[i].append(cover)
            mm ^= lb

    @lru_cache(None)
    def dp(mask):
        if mask == 0:
            return 0, ()
        i = (mask & -mask).bit_length() - 1
        best_count, best_parts = dp(mask ^ (1 << i))
        for cover in covers_by_item[i]:
            if cover & mask == cover:
                count, parts = dp(mask ^ cover)
                if count + 1 > best_count:
                    best_count = count + 1
                    best_parts = parts + (cover,)
        return best_count, best_parts

    count, masks = dp((1 << n) - 1)
    groups = [[i for i in range(n) if mask >> i & 1] for mask in masks]
    return count, groups


def greedy_largest_smallest(weights, threshold=1.0):
    """A simple heuristic used only as a control, not as an optimal algorithm."""
    items = sorted(enumerate(weights), key=lambda x: x[1])
    groups = []
    while items:
        idx, weight = items.pop()
        group = [idx]
        total = weight
        while total + 1e-12 < threshold and items:
            j, w = items.pop(0)
            group.append(j)
            total += w
        if total + 1e-12 >= threshold:
            groups.append(group)
        else:
            break
    return len(groups), groups


def observer_capacity(weights, access_sets, threshold=1.0):
    """Maximum observers assignable pairwise-disjoint sufficient fragments."""
    n = len(weights)
    options = []
    for access in access_sets:
        inds = sorted(set(access))
        masks = []
        for r in range(1, len(inds) + 1):
            for comb in itertools.combinations(inds, r):
                total = sum(weights[i] for i in comb)
                if total + 1e-12 < threshold:
                    continue
                if all(total - weights[j] < threshold - 1e-12 for j in comb):
                    masks.append(sum(1 << j for j in comb))
        options.append(masks)

    @lru_cache(None)
    def dp(observer, used_mask):
        if observer == len(options):
            return 0, ()
        best_count, best_assign = dp(observer + 1, used_mask)
        for mask in options[observer]:
            if mask & used_mask:
                continue
            count, assign = dp(observer + 1, used_mask | mask)
            if count + 1 > best_count:
                best_count = count + 1
                best_assign = assign + ((observer, mask),)
        return best_count, best_assign

    count, assignment = dp(0, 0)
    decoded = [(o, [i for i in range(n) if mask >> i & 1]) for o, mask in assignment]
    return count, decoded


def print_group_summary(weights, groups, threshold=1.0):
    for k, group in enumerate(groups, start=1):
        total = sum(weights[i] for i in group)
        print(f"  fragment {k}: indices={group}, weight={total:.6f}, sufficient={total >= threshold - 1e-12}")


def mode_threshold(delta):
    print("=== Threshold transform ===")
    for diagnostic in ("qmi", "accessible"):
        tau = overlap_threshold(delta, diagnostic)
        W = -math.log(tau)
        print(f"{diagnostic:10s}: delta={delta:.6f}, tau={tau:.15f}, W=-ln(tau)={W:.15f}")


def mode_counterexample():
    print("=== Same global overlap / different redundancy ===")
    A = [0.5] * 8
    B = [3.5, 0.5] + [0.0] * 6
    for name, weights in (("distributed", A), ("concentrated", B)):
        count, groups = exact_disjoint_redundancy(weights, 1.0)
        total = sum(weights)
        global_overlap = math.exp(-total)
        print(f"{name}: total_weight={total:.6f}, global_overlap={global_overlap:.12f}, R_opt={count}")
        print_group_summary(weights, groups)


def mode_heterogeneous():
    print("=== Heterogeneous exact-cover control ===")
    weights = [0.14, 0.58, 0.05, 0.18, 0.75, 0.09, 0.13, 0.14, 0.84, 0.21]
    print(f"weights={weights}")
    print(f"total={sum(weights):.6f}, capacity_upper_bound=floor(total)={math.floor(sum(weights))}")
    opt_count, opt_groups = exact_disjoint_redundancy(weights, 1.0)
    greedy_count, greedy_groups = greedy_largest_smallest(weights, 1.0)
    print(f"exact R_opt={opt_count}")
    print_group_summary(weights, opt_groups)
    print(f"simple greedy R={greedy_count}")
    print_group_summary(weights, greedy_groups)


def mode_observer():
    print("=== Observer-access control ===")
    weights = [0.6] * 6
    physical, groups = exact_disjoint_redundancy(weights, 1.0)
    print(f"physical disjoint redundancy={physical}")
    print_group_summary(weights, groups)
    distributed = [{0, 1}, {2, 3}, {4, 5}]
    bottleneck = [{0, 1}, {0, 1}, {0, 1}]
    for name, access in (("distributed_access", distributed), ("shared_bottleneck", bottleneck)):
        count, assignment = observer_capacity(weights, access, 1.0)
        print(f"{name}: observer_capacity={count}, assignment={assignment}")


def mode_causal(c_info):
    print("=== Conditional causal-availability control ===")
    weights = [0.6] * 6
    distances = [1.0, 1.2, 2.1, 2.3, 3.1, 3.2]
    for t in (1.0, 1.2, 2.3, 3.2):
        reachable = [i for i, d in enumerate(distances) if d <= c_info * t + 1e-12]
        reachable_weights = [weights[i] for i in reachable]
        count, local_groups = exact_disjoint_redundancy(reachable_weights, 1.0)
        groups = [[reachable[j] for j in group] for group in local_groups]
        print(f"t={t:.2f}: reachable={reachable}, R_reachable={count}, groups={groups}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["all", "threshold", "counterexample", "heterogeneous", "observer", "causal"], default="all")
    parser.add_argument("--delta", type=float, default=0.1)
    parser.add_argument("--c-info", type=float, default=1.0)
    args = parser.parse_args()

    if args.mode in ("all", "threshold"):
        mode_threshold(args.delta)
    if args.mode in ("all", "counterexample"):
        mode_counterexample()
    if args.mode in ("all", "heterogeneous"):
        mode_heterogeneous()
    if args.mode in ("all", "observer"):
        mode_observer()
    if args.mode in ("all", "causal"):
        mode_causal(args.c_info)


if __name__ == "__main__":
    main()
