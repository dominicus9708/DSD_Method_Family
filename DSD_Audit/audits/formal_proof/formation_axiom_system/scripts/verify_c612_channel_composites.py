#!/usr/bin/env python3
"""F2 C6.12: finite, clause-interface witness for strict channel family transport.

Illustrative typed Clause VI and E1-E9 data only: not a model completeness
certificate or a general proof. Uses Python standard library.
From DSD_Method_Family repository root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c612_channel_composites.py
Optional first argument: output JSON path.
"""
import itertools
import json
import sys
from pathlib import Path

SRC_SHA = "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"
pmap = {"p0": "P0", "p1": "P1"}
amap = {"a": "A", "b": "B"}
kmap = {"alpha": "chi", "beta": "psi"}
rmap = {"r": "R", "s": "S"}
vspaces = {"alpha": (0, 1), "beta": (0, 2)}
imaps = {"alpha": {0: 0, 1: 7}, "beta": {0: 0, 2: 9}}
source_psi = {"p0": True, "p1": False}
source_graph = {("a", "alpha", 0), ("b", "beta", 2)}
source_role = {("p0", "a", "alpha", "r"), ("p0", "a", "alpha", "s"),
               ("p0", "b", "beta", "s"), ("p1", "b", "beta", "r")}

def candidate_source():
    return {(p, a, k, v, r) for p, a, k, r in itertools.product(
        pmap, amap, kmap, rmap) for v in vspaces[k]}

def transform(c):
    p, a, k, v, r = c
    return (pmap[p], amap[a], kmap[k], imaps[k][v], rmap[r])

target_psi = {pmap[p]: ok for p, ok in source_psi.items()}
target_graph = {(amap[a], kmap[k], imaps[k][v]) for a, k, v in source_graph}
target_role = {(pmap[p], amap[a], kmap[k], rmap[r])
               for p, a, k, r in source_role}

def admitted(c, psi, graph, role):
    p, a, k, v, r = c
    return bool(psi[p]) and (a, k, v) in graph and (p, a, k, r) in role

def powerset(xs):
    ordered = tuple(sorted(xs))
    return [frozenset(combination) for n in range(len(ordered) + 1)
            for combination in itertools.combinations(ordered, n)]

def verify():
    assert all(len(set(x.values())) == len(x) for x in
               (pmap, amap, kmap, rmap))
    assert all(len(set(v.values())) == len(v) and v[0] == 0
               for v in imaps.values())
    candidates = candidate_source()
    images = {transform(c) for c in candidates}
    assert len(images) == len(candidates) == 32
    lhs = {c for c in candidates if admitted(
        c, source_psi, source_graph, source_role)}
    rhs = {c for c in images if admitted(
        c, target_psi, target_graph, target_role)}
    reflected = sum(admitted(c, source_psi, source_graph, source_role) ==
                    admitted(transform(c), target_psi, target_graph, target_role)
                    for c in candidates)
    assert reflected == 32 and {transform(c) for c in lhs} == rhs
    assert len(lhs) == len(rhs) == 3

    # T values are independent of the assigned quantity value (including 0).
    terms = {c: t for c, t in zip(sorted(lhs), (3, -3, 5))}
    J = lambda x: 2 * x  # an R-linear isomorphism with zero preserved
    target_terms = {transform(c): J(terms[c]) for c in lhs}
    source_families = powerset(lhs)
    target_families = powerset(rhs)
    family_images = {frozenset(transform(c) for c in F) for F in source_families}
    assert len(source_families) == len(target_families) == len(family_images) == 8
    assert family_images == set(target_families)
    inverse = {transform(c): c for c in lhs}
    inverse_checks = 0
    composite_checks = 0
    cancellation_checks = 0
    for F in source_families:
        image = frozenset(transform(c) for c in F)
        assert frozenset(inverse[d] for d in image) == F
        inverse_checks += 1
        left = J(sum(terms[c] for c in F))
        right = sum(target_terms[d] for d in image)
        assert left == right
        composite_checks += 1
        if F and sum(terms[c] for c in F) == 0:
            cancellation_checks += 1
    assert cancellation_checks >= 1
    assert any(c[3] == 0 for c in lhs)

    # Breaking role reflection while leaving the candidate bijection intact
    # produces a target-only channel: the source strict premise no longer holds.
    absent = next(c for c in candidates if c not in lhs and source_psi[c[0]]
                  and (c[1], c[2], c[3]) in source_graph)
    role_extended = set(target_role)
    role_extended.add((pmap[absent[0]], amap[absent[1]], kmap[absent[2]],
                       rmap[absent[4]]))
    enlarged = {d for d in images if admitted(d, target_psi, target_graph, role_extended)}
    assert len(enlarged) == 4 and len(lhs) == 3
    assert transform(absent) in enlarged

    return {
        "case_id": "FAS-F2-C6.12-001",
        "source_sha256": SRC_SHA,
        "finite_scope": "typed Clause VI/E1-E9 interface fixture, not full-model general theorem proof",
        "all_checks_passed": True,
        "candidate_source_image_equivalences": reflected,
        "admitted_channels_each_side": len(lhs),
        "finite_families_each_side": len(source_families),
        "inverse_finite_family_checks": inverse_checks,
        "composite_checks": composite_checks,
        "nonempty_zero_sum_families": cancellation_checks,
        "defined_zero_channel_included": True,
        "role_reflection_removed_target_channels": len(enlarged),
        "role_reflection_removed_strict_premise_fails": True,
        "linearity_J_example": "J(x)=2*x over R",
        "finite_checks_not_universal_proof": True,
        "independent_external_validation": False,
    }

def main():
    result = verify()
    out = (Path(sys.argv[1]) if len(sys.argv) > 1 else
           Path(__file__).resolve().parent.parent / "results" / "c612_channel_composites.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("C6.12 selected finite checks PASS")
    print("OUTPUT", out)

if __name__ == "__main__":
    main()
