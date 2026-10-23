#!/usr/bin/env python3
"""P11 auxiliary finite edge cases for Kwon Dominicus general Property Axiom System.

Not a proof of universal theorems. Standard-library only.
Usage: python verify_p11_empty_dependency_edges.py [output_json]
"""
from __future__ import annotations
from itertools import product
import json
import sys
from pathlib import Path

SHA = "03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"
INHERITED = {"h": ("h0", "h1")}
PROFILES = {"p": ("u",), "q": ("u", "u"), "r": ("h", "u"), "t": ("v", "u")}
DEPS = {k: ("d1", "d2") for k in PROFILES}


def carrier(M, s):
    return INHERITED[s] if s in INHERITED else M["supply"].get(s)


def available(M, k):
    return all(carrier(M, s) is not None for s in PROFILES[k])


def typed_inputs(M, k):
    if not available(M, k):
        return None
    return set(product(*(carrier(M, s) for s in PROFILES[k])))


def model(supply, declared, payload=None):
    M = {"supply": dict(supply), "declared": frozenset(declared), "data": {}}
    payload = payload or {}
    for k in M["declared"]:
        if not available(M, k):
            assert k not in payload, "cannot attach typed primitive coordinates to unavailable kind"
            continue
        universe = typed_inputs(M, k)
        P = payload.get(k, {})
        ap = set(P.get("ap", universe))
        sat = {d: set(P.get("sat", {}).get(d, universe)) for d in DEPS[k]}
        xi = dict(P.get("xi", {}))
        assert ap <= universe and all(x <= universe for x in sat.values())
        assert set(xi) <= ap and all(set(xi) <= x for x in sat.values())
        M["data"][k] = {"ap": ap, "sat": sat, "xi": xi}
    return M


def product_map(k, x, phi):
    return tuple(xi if s in INHERITED else phi[s][xi] for xi, s in zip(x, PROFILES[k]))


def fwd(A, B, phi):
    if not set(A["supply"]) <= set(B["supply"]) or not A["declared"] <= B["declared"]:
        return False
    if set(phi) != set(A["supply"]):
        return False
    for s in phi:
        if set(phi[s]) != set(A["supply"][s]) or any(y not in B["supply"][s] for y in phi[s].values()):
            return False
    for k in A["declared"]:
        if not available(A, k):
            continue
        a, b = A["data"][k], B["data"][k]
        if any(product_map(k, x, phi) not in b["ap"] for x in a["ap"]):
            return False
        if any(product_map(k, x, phi) not in b["sat"][d] for d in DEPS[k] for x in a["sat"][d]):
            return False
        if any(b["xi"].get(product_map(k, x, phi), object()) != z for x, z in a["xi"].items()):
            return False
    return True


def emb(A, B, phi):
    if not fwd(A, B, phi) or any(len(set(f.values())) != len(f) for f in phi.values()):
        return False
    for k in A["declared"]:
        if not available(A, k):
            continue
        a, b = A["data"][k], B["data"][k]
        for x in typed_inputs(A, k):
            y = product_map(k, x, phi)
            if (x in a["ap"]) != (y in b["ap"]):
                return False
            if any((x in a["sat"][d]) != (y in b["sat"][d]) for d in DEPS[k]):
                return False
            if (x in a["xi"]) != (y in b["xi"]):
                return False
    return True


def strict(A, B, phi):
    if set(A["supply"]) != set(B["supply"]) or A["declared"] != B["declared"]:
        return False
    if not emb(A, B, phi):
        return False
    if any(len(phi[s]) != len(B["supply"][s]) for s in phi):
        return False
    inverse = {s: {v: k for k, v in phi[s].items()} for s in phi}
    return emb(B, A, inverse)


def transport(A, phi):
    supply = {s: tuple(phi[s][x] for x in A["supply"][s]) for s in A["supply"]}
    payload = {}
    for k, dat in A["data"].items():
        T = lambda x: product_map(k, x, phi)
        payload[k] = {"ap": {T(x) for x in dat["ap"]},
                      "sat": {d: {T(x) for x in dat["sat"][d]} for d in DEPS[k]},
                      "xi": {T(x): z for x, z in dat["xi"].items()}}
    return model(supply, A["declared"], payload)


def run():
    checks = {}
    # Distinguish undefined carrier from supplied empty set. F3 literal is undefined
    # for the first case; it is a well-typed, vacuous condition in the second.
    U = model({}, ["p"])
    E = model({"u": ()}, ["p"])
    checks["declared_unavailable_has_no_product"] = typed_inputs(U, "p") is None and "p" not in U["data"]
    checks["declared_available_empty_has_empty_product"] = typed_inputs(E, "p") == set() and "p" in E["data"]
    checks["unavailable_to_available_empty_is_one_way_forward"] = fwd(U, E, {}) and not strict(U, E, {})
    checks["empty_identity_is_strict"] = strict(E, E, {"u": {}})
    S = model({"u": (0,)}, ["p"])
    checks["available_empty_injects_into_singleton_not_strict"] = emb(E, S, {"u": {}}) and not strict(E, S, {"u": {}})
    # Source/target both available, but B declares another kind: bijective embedding != strict.
    A = model({"u": (0, 1)}, ["p"])
    B = model({"u": (0, 1)}, ["p", "q"])
    id2 = {"u": {0: 0, 1: 1}}
    checks["bijective_embedding_not_strict_when_declarations_differ"] = emb(A, B, id2) and not strict(A, B, id2)
    # Two prerequisites, zero/nonzero, repeated sort and inherited identity.
    X = model({"u": (0, 1), "v": ("v0", "v1")}, ["p", "q", "r", "t"], {
        "p": {"sat": {"d1": {(0,), (1,)}, "d2": {(0,)}}, "xi": {(0,): 0}},
        "q": {"sat": {"d1": {(0, 1), (1, 0)}, "d2": {(0, 1)}}, "xi": {(0, 1): 2}},
        "r": {"sat": {"d1": {("h0", 0), ("h1", 1)}, "d2": {("h1", 1)}}, "xi": {("h1", 1): 0}},
        "t": {"sat": {"d1": {("v0", 0), ("v1", 1)}, "d2": {("v1", 1)}}, "xi": {("v1", 1): 2}},
    })
    swap = {"u": {0: 1, 1: 0}, "v": {"v0": "v1", "v1": "v0"}}
    Y = transport(X, swap)
    back = {"u": {1: 0, 0: 1}, "v": {"v1": "v0", "v0": "v1"}}
    checks["mixed_repeated_inherited_swap_strict_both_directions"] = strict(X, Y, swap) and strict(Y, X, back)
    checks["two_prerequisites_intersection_and_zero_nonzero"] = (set(X["data"]["p"]["xi"]) == {(0,)}
        and X["data"]["p"]["xi"][(0,)] == 0 and X["data"]["q"]["xi"][(0, 1)] == 2)
    checks["inherited_sort_identity_and_repeated_coordinates"] = (
        product_map("r", ("h0", 0), swap) == ("h0", 1)
        and product_map("q", (0, 1), swap) == (1, 0)
        and product_map("t", ("v0", 0), swap) == ("v1", 1))
    invalid = False
    try:
        model({"u": (0, 1)}, ["p"], {"p": {"sat": {"d2": {(0,)}}, "xi": {(1,): 0}}})
    except AssertionError:
        invalid = True
    checks["assignment_failing_second_prerequisite_rejected"] = invalid
    assert all(checks.values()), checks
    return {"case": "PA-P11-20260901-EMPTY-MULTIDEPENDENCY-EDGES", "source_sha256": SHA,
            "tested_edge_cases": len(checks), "checks": checks,
            "all_pass": True, "general_theorem_machine_proof": False,
            "manuscript_modified": False, "original_experiment_modified": False,
            "FPA": "OPEN"}

if __name__ == "__main__":
    r = run()
    p = (Path(sys.argv[1]) if len(sys.argv) > 1 else
         Path(__file__).resolve().parent.parent / "results/p11_empty_dependency_edges.json")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(r, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print("P11 EDGE CHECK PASS", r["tested_edge_cases"], "source-specific cases")
