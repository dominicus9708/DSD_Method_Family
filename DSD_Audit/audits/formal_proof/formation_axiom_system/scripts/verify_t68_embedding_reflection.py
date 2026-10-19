#!/usr/bin/env python3
"""Finite typed witness audit of F2 Theorem 6.8. Not a universal proof.

Run from DSD_Method_Family root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t68_embedding_reflection.py
Optional first CLI argument specifies an output JSON path. Stdlib only.
"""
import itertools
import json
import sys
from pathlib import Path

SOURCE_SHA256 = "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"
R = ("r1", "r2")
V = (0, 1)


def model(extended=False, shadow=False):
    if extended:
        m = dict(expr={"H": {"A"}, "X": {"B"}}, cfg={"GOOD": {"A"}, "BAD": {"A"}, "EXTRA": {"B"}},
                 restriction={("H", "H"), ("X", "X")},
                 real={("H", "GOOD"), ("X", "EXTRA")},
                 q={"A": 0, "B": 1},
                 role={("GOOD", "A", "r1"), ("GOOD", "A", "r2"),
                       ("BAD", "A", "r1"), ("EXTRA", "B", "r1")},
                 T={("GOOD", "r1"): 3, ("GOOD", "r2"): -2, ("EXTRA", "r1"): 17})
        if shadow:
            m["expr"]["SHADOW"] = {"A"}
            m["restriction"].add(("SHADOW", "SHADOW"))
            m["real"].add(("SHADOW", "BAD"))
            m["T"][("BAD", "r1")] = 5
    else:
        m = dict(expr={"h": {"a"}}, cfg={"pg": {"a"}, "pb": {"a"}},
                 restriction={("h", "h")}, real={("h", "pg")},
                 q={"a": 0},
                 role={("pg", "a", "r1"), ("pg", "a", "r2"), ("pb", "a", "r1")},
                 T={("pg", "r1"): 3, ("pg", "r2"): -2})
    m["desexpr"] = set(m["expr"])
    m["admexpr"] = set(m["expr"])
    m["admcfg"] = set(m["cfg"])
    m["lc"] = set(m["cfg"])
    m["bc"] = set(m["cfg"])
    m["material"] = set().union(*m["expr"].values())
    return m


def witnesses(m, p):
    return {(H, h) for H, h in m["restriction"]
            if h in m["desexpr"] and (h, p) in m["real"]
            and p in m["admcfg"] and p in m["lc"] and p in m["bc"]}


def psi(m, p):
    return bool(witnesses(m, p))


def candidates(m):
    return set(itertools.product(m["cfg"], m["material"], ("lambda",), V, R))


def channels(m):
    return {(p, a, "lambda", v, r) for p, a, r in m["role"]
            for v in V if psi(m, p) and m["q"].get(a, object()) == v}


def full_model_check(m):
    # Primitive I: describable expressions are admitted; typed records.
    assert m["desexpr"] <= m["admexpr"] <= set(m["expr"])
    # Primitive II: identity restrictions and material/anchor inheritance
    # (all anchors are the fixed 's0').
    for h in m["admexpr"]:
        assert (h, h) in m["restriction"]
    for H, h in m["restriction"]:
        assert H in m["expr"] and h in m["admexpr"]
        assert m["expr"][h] <= m["expr"][H]
    # Primitive III: realized expressions support all active material.
    for h, p in m["real"]:
        assert h in m["expr"] and p in m["cfg"] and m["cfg"][p] <= m["expr"][h]
    Astar = set().union(*(m["cfg"][p] for p in m["cfg"] if psi(m, p)))
    assert set(m["q"]) <= Astar and set(m["q"].values()) <= set(V)  # Primitive V
    assert all((p in m["cfg"] and a in m["material"] and r in R)
               for p, a, r in m["role"])
    C = channels(m)
    assert C <= candidates(m)  # Closure VI
    assert set(m["T"]) == {(p, r) for p, a, lam, v, r in C}
    for n in range(len(C) + 1):
        for F in itertools.combinations(sorted(C), n):
            # Closure VII: finite sums, including empty family.
            assert isinstance(sum(m["T"][p, r] for p, a, lam, v, r in F), int)
    return C


def inject(c):
    p, a, lam, v, r = c
    return ({"pg": "GOOD", "pb": "BAD"}[p], {"a": "A"}[a], lam, v, r)


def map_check(L, M, witness_reflection=True):
    # Special typed injections: fM(a)=A, fE(h)=H, fP(pg)=GOOD,
    # fP(pb)=BAD, tau_lambda=id, tau_role=id, I_lambda=id, J=id.
    for p in L["cfg"]:
        im = {"pg": "GOOD", "pb": "BAD"}[p]
        assert {"A" for a in L["cfg"][p]} == (M["cfg"][im] & {"A"})  # R1
        for key in ("admcfg", "lc", "bc"):
            assert (p in L[key]) == (im in M[key])  # R2
        if witness_reflection:
            assert not psi(M, im) or psi(L, p), "witness reflection"
    assert M["expr"]["H"] & {"A"} == {"A"}
    assert ("h" in L["desexpr"]) == ("H" in M["desexpr"])
    assert ("h" in L["admexpr"]) == ("H" in M["admexpr"])
    assert (("h", "h") in L["restriction"]) == (("H", "H") in M["restriction"])  # R3
    for p in L["cfg"]:
        im = {"pg": "GOOD", "pb": "BAD"}[p]
        assert (("h", p) in L["real"]) == (("H", im) in M["real"])  # R3
        for r in R:
            assert ((p, "a", r) in L["role"]) == ((im, "A", r) in M["role"])  # R5
    for v in V:
        assert (L["q"].get("a") == v) == (M["q"].get("A") == v)  # R4
    for c in channels(L):
        assert inject(c) in channels(M)
        p, a, lam, v, r = c
        assert L["T"][p, r] == M["T"][inject(c)[0], r]  # F6, J=id
    return True


def verify():
    L, M = model(), model(extended=True)
    src, dst = full_model_check(L), full_model_check(M)
    map_check(L, M)
    eq = sum(1 for c in candidates(L)
             if (c in src) == (inject(c) in dst))
    assert eq == len(candidates(L)) == 8
    assert len(src) == 2 and len(dst) == 3
    img = {inject(c) for c in src}
    assert len(img) == len(src) and len(dst - img) == 1
    comps = 0
    for n in range(len(src) + 1):
        for F in itertools.combinations(sorted(src), n):
            assert sum(L["T"][p, r] for p, a, lam, v, r in F) == sum(
                M["T"][p, r] for p, a, lam, v, r in {inject(c) for c in F})
            comps += 1
    assert comps == 4 and L["q"]["a"] == 0 and sum(L["T"].values()) == 1
    Mbad = model(extended=True, shadow=True)
    full_model_check(Mbad)
    map_check(L, Mbad, witness_reflection=False)
    assert not psi(L, "pb") and psi(Mbad, "BAD")
    assert ("pb", "a", "lambda", 0, "r1") not in src
    assert ("BAD", "A", "lambda", 0, "r1") in channels(Mbad)
    detected = False
    try:
        map_check(L, Mbad)
    except AssertionError as exc:
        detected = str(exc) == "witness reflection"
    assert detected
    return dict(audit_id="FAS-F2-T6.8-001", source_sha256=SOURCE_SHA256,
                source_admitted_channels=len(src), target_admitted_channels=len(dst),
                target_only_admitted_channels=len(dst - img),
                candidate_channel_equivalences=eq, finite_subset_composites=comps,
                defined_zero_assignment_present=True,
                component_terms_not_identified_with_assignment_values=True,
                witness_reflection_independent_necessity_shown=True,
                all_finite_checks_passed=True, finite_checks_not_universal_proof=True,
                external_independent_verification=False)


def main():
    result = verify()
    out = (Path(sys.argv[1]) if len(sys.argv) > 1 else
           Path(__file__).resolve().parent.parent / "results" / "t68_embedding_reflection.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print("FAS-F2-T6.8-001 PASS:", result)
    print("OUTPUT:", out)


if __name__ == "__main__":
    main()
