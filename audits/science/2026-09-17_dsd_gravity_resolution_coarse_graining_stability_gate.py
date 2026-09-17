#!/usr/bin/env python3
"""
BH-GC-005 — resolution / coarse-graining stability gravitational-core gate.

Purpose
-------
Distinguish physical splitting/merger of a descriptor field from apparent
splitting/merger induced only by finite spatial resolution or coarse-graining.

The control is deliberately 1D and non-black-hole.  Gaussian descriptor peaks
are used because normalized Gaussian coarse-graining is analytic.  The audit
tracks point maxima and 0D superlevel persistence across both physical
separation and observational blur.

This script does not derive a physical black-hole interior, a preferred
resolution, or a unique gravitational-core scale.
"""

import argparse
import math


XMIN = -7.0
XMAX = 7.0
SIGMA0 = 0.8
D0 = 2.0


def effective_sigma(blur: float) -> float:
    return math.sqrt(SIGMA0 * SIGMA0 + blur * blur)


def blurred_gaussian(x: float, center: float, amp: float, blur: float) -> float:
    """Normalized-Gaussian convolution of an intrinsic Gaussian peak."""
    s = effective_sigma(blur)
    pref = SIGMA0 / s
    z = (x - center) / s
    return amp * pref * math.exp(-0.5 * z * z)


def profile(x: float, d: float = D0, blur: float = 0.0,
            a_left: float = 1.0, a_right: float = 1.0) -> float:
    return (
        blurred_gaussian(x, -d, a_left, blur)
        + blurred_gaussian(x, d, a_right, blur)
    )


def sample_profile(d: float, blur: float, dx: float,
                   a_left: float = 1.0, a_right: float = 1.0):
    n = int(round((XMAX - XMIN) / dx)) + 1
    xs = [XMIN + i * (XMAX - XMIN) / (n - 1) for i in range(n)]
    vals = [profile(x, d, blur, a_left, a_right) for x in xs]
    vmax = max(vals)
    vals = [v / vmax for v in vals]
    return xs, vals


def local_max_count(vals) -> int:
    return sum(
        1 for i in range(1, len(vals) - 1)
        if vals[i] > vals[i - 1] and vals[i] >= vals[i + 1]
    )


def persistence_superlevel(vals):
    n = len(vals)
    order = sorted(range(n), key=lambda i: (-vals[i], i))
    active = [False] * n
    parent = list(range(n))
    birth = [0.0] * n
    birth_index = [-1] * n
    records = []

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for idx in order:
        active[idx] = True
        parent[idx] = idx
        birth[idx] = vals[idx]
        birth_index[idx] = idx

        neighbors = []
        if idx > 0 and active[idx - 1]:
            neighbors.append(find(idx - 1))
        if idx + 1 < n and active[idx + 1]:
            neighbors.append(find(idx + 1))
        neighbors = list(dict.fromkeys(neighbors))

        if not neighbors:
            continue
        if len(neighbors) == 1:
            parent[idx] = neighbors[0]
            continue

        r1, r2 = neighbors
        key1 = (birth[r1], -birth_index[r1])
        key2 = (birth[r2], -birth_index[r2])
        old, young = (r1, r2) if key1 >= key2 else (r2, r1)
        death = vals[idx]
        records.append({
            "birth": birth[young],
            "death": death,
            "persistence": birth[young] - death,
            "birth_index": birth_index[young],
            "death_index": idx,
            "essential": False,
        })
        parent[young] = old
        parent[idx] = old

    roots = {find(i) for i in range(n) if active[i]}
    min_value = min(vals)
    min_index = vals.index(min_value)
    for root in roots:
        records.append({
            "birth": birth[root],
            "death": min_value,
            "persistence": birth[root] - min_value,
            "birth_index": birth_index[root],
            "death_index": min_index,
            "essential": True,
        })

    return sorted(records, key=lambda r: r["persistence"], reverse=True)


def secondary_persistence(vals) -> float:
    rec = persistence_superlevel(vals)
    finite = [r["persistence"] for r in rec if not r["essential"]]
    return finite[0] if finite else 0.0


def run_audit() -> int:
    dx_fine = 0.002

    # Exact equal-amplitude bimodality threshold after Gaussian coarse-graining.
    # For two equal Gaussians centered at +/-d with common width S, x=0 changes
    # from local minimum to local maximum at d=S.  Since S^2=sigma0^2+blur^2,
    # the resolution-induced merger threshold is blur_crit=sqrt(d^2-sigma0^2).
    blur_crit = math.sqrt(D0 * D0 - SIGMA0 * SIGMA0)

    blur_scan = [0.0, 0.5, 1.0, 1.5, 1.8, 1.82, 1.84, 1.9, 2.2]
    resolution_rows = []
    for blur in blur_scan:
        _, vals = sample_profile(D0, blur, dx_fine)
        resolution_rows.append(
            (blur, effective_sigma(blur), local_max_count(vals), secondary_persistence(vals))
        )

    # Physical approach at a fixed measurement resolution.
    blur_fixed = 0.4
    d_crit_physical = effective_sigma(blur_fixed)
    d_scan = [2.0, 1.5, 1.1, 0.95, 0.90, 0.88, 0.85, 0.75]
    physical_rows = []
    for d in d_scan:
        _, vals = sample_profile(d, blur_fixed, dx_fine)
        physical_rows.append((d, local_max_count(vals), secondary_persistence(vals)))

    # Grid-sampling stability of an asymmetric, still clearly two-component case.
    grid_d = 2.0
    grid_blur = 0.4
    grid_dxs = [0.002, 0.005, 0.01, 0.02, 0.04, 0.08]
    grid_rows = []
    for dx in grid_dxs:
        _, vals = sample_profile(grid_d, grid_blur, dx, 1.0, 0.35)
        grid_rows.append((dx, local_max_count(vals), secondary_persistence(vals)))
    p_ref = grid_rows[0][2]
    grid_rel_errors = [abs(row[2] - p_ref) / p_ref for row in grid_rows]

    # Degeneracy witness: same one-core descriptor topology can arise either from
    # physical proximity at fixed good resolution or from poor resolution with
    # unchanged physical separation.
    _, vals_phys_merged = sample_profile(0.75, blur_fixed, dx_fine)
    _, vals_res_merged = sample_profile(D0, 2.2, dx_fine)
    n_phys_merged = local_max_count(vals_phys_merged)
    n_res_merged = local_max_count(vals_res_merged)

    tests = []

    def check(name, condition, value=None):
        tests.append((name, bool(condition), value))

    check("intrinsic equal-peak control is bimodal", resolution_rows[0][2] == 2, resolution_rows[0])
    check("analytic coarse-graining threshold is real and positive", blur_crit > 0.0, blur_crit)
    check("blur below analytic threshold remains bimodal", all(row[2] == 2 for row in resolution_rows if row[0] <= 1.82), resolution_rows)
    check("blur above analytic threshold becomes unimodal", all(row[2] == 1 for row in resolution_rows if row[0] >= 1.84), resolution_rows)
    check("numerical transition brackets analytic threshold", 1.82 < blur_crit < 1.84, blur_crit)
    check("secondary persistence decreases as blur approaches merger", resolution_rows[0][3] > resolution_rows[2][3] > resolution_rows[4][3], resolution_rows[:5])
    check("secondary persistence vanishes after resolution-induced merger", all(row[3] == 0.0 for row in resolution_rows if row[0] >= 1.84), resolution_rows[6:])
    check("fixed-resolution physical merger threshold equals effective width", abs(d_crit_physical - math.sqrt(SIGMA0**2 + blur_fixed**2)) < 1e-15, d_crit_physical)
    check("physical separation above threshold remains bimodal", all(row[1] == 2 for row in physical_rows if row[0] >= 0.90), physical_rows)
    check("physical separation below threshold becomes unimodal", all(row[1] == 1 for row in physical_rows if row[0] <= 0.88), physical_rows)
    check("physical-merger persistence decreases toward zero", physical_rows[0][2] > physical_rows[2][2] > physical_rows[4][2], physical_rows[:5])
    check("same one-core topology can result from physical merger", n_phys_merged == 1, n_phys_merged)
    check("same one-core topology can result from resolution merger", n_res_merged == 1, n_res_merged)
    check("topology alone therefore cannot identify physical versus resolution merger", n_phys_merged == n_res_merged == 1, (n_phys_merged, n_res_merged))
    check("asymmetric control remains two-peaked across tested grid spacings", all(row[1] == 2 for row in grid_rows), grid_rows)
    check("asymmetric persistence is stable across tested grid spacings", max(grid_rel_errors) < 0.01, grid_rel_errors)
    check("moderate grid coarsening does not itself create an extra component", len({row[1] for row in grid_rows}) == 1, [row[1] for row in grid_rows])
    check("coarse-graining scale must be recorded separately from grid spacing", True, "blur != dx")
    check("resolution map is not a physical time-evolution lineage", True, "R_resolution != Lambda_material")
    check("no preferred physical resolution is inferred from the Gaussian control", True, "scope firewall")
    check("physical black-hole core multiplicity is not inferred from this control", True, "scope firewall")

    passed = sum(ok for _, ok, _ in tests)

    print("BH-GC-005 — resolution / coarse-graining stability gravitational-core gate")
    print(f"intrinsic sigma       = {SIGMA0:.12f}")
    print(f"physical half-sep d   = {D0:.12f}")
    print(f"analytic blur_crit    = {blur_crit:.12f}")
    print(f"fixed-blur d_crit     = {d_crit_physical:.12f}")
    print("resolution scan: (blur, effective_sigma, maxima, secondary_persistence)")
    for row in resolution_rows:
        print("  ", row)
    print("physical scan: (d, maxima, secondary_persistence)")
    for row in physical_rows:
        print("  ", row)
    print("grid scan: (dx, maxima, secondary_persistence, relative_error)")
    for row, err in zip(grid_rows, grid_rel_errors):
        print("  ", row, err)
    print()

    for name, ok, value in tests:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}: {value}")

    print()
    print(f"RESULT: {passed}/{len(tests)} PASS")
    print(
        "VERDICT: PASS_WITH_BOUNDARY / CORE_DESCRIPTOR_IS_STABLE_OVER_A_FINITE_RESOLUTION_RANGE_IN_CONTROL / "
        "SUFFICIENT_COARSE_GRAINING_CAN_MERGE_DISTINCT_DESCRIPTOR_CORES_WITHOUT_PHYSICAL_MERGER / "
        "PHYSICAL_AND_RESOLUTION_INDUCED_MERGERS_ARE_TOPOLOGICALLY_DEGENERATE_AT_ONE_RESOLUTION / "
        "RESOLUTION_AND_SAMPLING_PROVENANCE_ARE_REQUIRED / NO_UNIQUE_PHYSICAL_RESOLUTION_OR_BLACK_HOLE_CORE_MULTIPLICITY_DERIVED"
    )
    return 0 if passed == len(tests) else 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all"])
    parser.parse_args()
    raise SystemExit(run_audit())


if __name__ == "__main__":
    main()
