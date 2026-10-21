#!/usr/bin/env python3
r"""F2 C6.26 selected full-Formation finite models; not a universal proof.

Windows, from cloned DSD_Method_Family repository root:
  python .\DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_c626_channel_cardinality.py
Optional first argument sets output JSON file. Only Python standard library.
"""
import json
import sys
from itertools import combinations, permutations
from pathlib import Path

SOURCE_SHA = "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a"


def build(name, active_roles, terms):
    # All models share B, F2, typed carriers and external anchoring.
    d = dict(name=name, B={"s0"}, field="F2", material={"a"},
             expr={"h"}, cfg={"p"}, kind={"lam"}, roles={"r", "s"},
             mat={"h": {"a"}}, act={"p": {"a"}},
             anch_e={"h": {"a": "s0"}}, anch_p={"p": {"a": "s0"}},
             adm_e={"h"}, des_e={"h"}, restriction={("h", "h")},
             realize={("h", "p")}, adm_p={"p"}, lc={"p"}, bc={"p"},
             V={"lam": {0}}, zero={"lam": 0},
             Q={"lam": {"a"}}, q={("a", "lam"): 0}, negligible=set(),
             role_rel={("p", "a", "lam", r) for r in active_roles}, W={0, 1})
    # Primitive Axioms I, II, III: admission and anchored structural soundness.
    assert d["des_e"] <= d["adm_e"]
    assert all((h, h) in d["restriction"] for h in d["adm_e"])
    assert all(d["mat"][h] <= d["mat"][H] and
               all(d["anch_e"][h][a] == d["anch_e"][H][a]
                   for a in d["mat"][h]) for H, h in d["restriction"])
    assert all(d["act"][p] <= d["mat"][h] and
               all(d["anch_p"][p][a] == d["anch_e"][h][a]
                   for a in d["act"][p]) for h, p in d["realize"])
    # Definitional Clause IV, with actual Res/Realize witness.
    d["psi"] = {p: (p in d["adm_p"] and p in d["lc"] and p in d["bc"] and
                     any((H, h) in d["restriction"] and h in d["des_e"] and
                         (h, p) in d["realize"]
                         for H in d["expr"] for h in d["expr"])) for p in d["cfg"]}
    d["Kdes"] = {p for p in d["cfg"] if d["psi"][p]}
    d["Astar"] = set().union(*(d["act"][p] for p in d["Kdes"]))
    d["descfg"] = dict(d["psi"])
    # Primitive Axiom V: global partial assignment with defined ZERO.
    assert all(Q <= d["Astar"] for Q in d["Q"].values())
    assert all(v in d["V"][k] for (a, k), v in d["q"].items())
    d["gamma"] = {k: {(a, d["q"][(a, k)]) for a in d["Q"][k]} for k in d["kind"]}
    # Clause VI: existence of a channel is NOT the same as term=0.
    d["U"] = {(p, a, k, v, r) for p in d["cfg"] for a in d["material"]
              for k in d["kind"] for v in d["V"][k] for r in d["roles"]}
    d["C"] = {c for c in d["U"] if d["descfg"][c[0]] and
              (c[1], c[3]) in d["gamma"][c[2]] and
              (c[0], c[1], c[2], c[4]) in d["role_rel"]}
    d["Chan"] = {c: c in d["C"] for c in d["U"]}
    # Independently SUPPLIED terms T only on admitted channels; Clause VII.
    assert set(terms) == set(active_roles)
    d["T"] = {c: terms[c[4]] for c in d["C"]}
    assert set(d["T"]) == d["C"] and set(d["T"].values()) <= d["W"]
    d["Dcomp"] = {frozenset(q) for n in range(len(d["C"]) + 1)
                  for q in combinations(sorted(d["C"]), n)}
    d["Comp"] = {q: sum(d["T"][c] for c in q) % 2 for q in d["Dcomp"]}
    assert d["Comp"][frozenset()] == 0
    return d


def trace(d, c):
    p, a, k, v, r = c
    return {(H, h, p, a, k, v, r) for H, h in d["restriction"]
            if h in d["des_e"] and (h, p) in d["realize"] and
            p in d["adm_p"] and p in d["lc"] and p in d["bc"] and
            (a, v) in d["gamma"][k] and (p, a, k, r) in d["role_rel"]}


def comparisons(L, M):
    # All other typed bijections and the one-dimensional F2-linear iso J are identity.
    result = []
    for target_order in permutations(sorted(M["roles"])):
        rmap = dict(zip(sorted(L["roles"]), target_order))
        E8 = all(((p, a, k, r) in L["role_rel"]) ==
                 ((p, a, k, rmap[r]) in M["role_rel"])
                 for p in L["cfg"] for a in L["material"]
                 for k in L["kind"] for r in L["roles"])
        # E1-E7 are true in this selected family of otherwise identical cores.
        assert (L["B"], L["mat"], L["q"], L["gamma"], L["Kdes"]) == \
               (M["B"], M["mat"], M["q"], M["gamma"], M["Kdes"])
        if E8:
            mapped = {(p, a, k, v, rmap[r]): L["T"][(p, a, k, v, r)]
                      for p, a, k, v, r in L["C"]}
            assert set(mapped) == M["C"]
            E9 = all(M["T"][c] == t for c, t in mapped.items())
        else:
            E9 = None  # No induced admitted-channel bijection for failed E8.
        result.append({"role_map": rmap, "E1_to_E7": True, "E8": E8,
                       "E9": E9, "strict": E8 and E9 is True})
    return result


def check():
    L = build("L", {"r"}, {"r": 0})
    M = build("M", {"r", "s"}, {"r": 0, "s": 0})
    Z = build("Z", set(), {})
    P = build("P", {"r"}, {"r": 0})
    Q = build("Q", {"r"}, {"r": 1})
    neg, pos, same_count_bad, empty_nonempty = (comparisons(L, X) for X in (M, P, Q, Z))
    assert all(len(x) == 2 for x in (neg, pos, same_count_bad, empty_nonempty))
    assert [len(d["C"]) for d in (L, M, Z, P, Q)] == [1, 2, 0, 1, 1]
    assert not any(r["strict"] for r in neg + same_count_bad + empty_nonempty)
    assert sum(r["strict"] for r in pos) == 1
    assert sum(r["E8"] for r in pos) == 1
    assert sum(r["E8"] for r in same_count_bad) == 1
    assert sum(r["strict"] for r in same_count_bad) == 0
    assert all(not r["E8"] for r in neg + empty_nonempty)
    assert all((c in d["C"]) == bool(trace(d, c)) for d in (L, M, Z, P, Q) for c in d["U"])
    assert all(len(d["U"]) == 2 for d in (L, M, Z, P, Q))
    assert all(d["Comp"][frozenset(d["C"])] == 0 for d in (L, M, Z, P))
    assert Q["Comp"][frozenset(Q["C"])] == 1
    assert all(d["q"][("a", "lam")] == 0 for d in (L, M, Z, P, Q))
    return {"audit_id": "FAS-F2-C6.26-001", "source_sha256": SOURCE_SHA,
            "all_checks_passed": True, "models_checked": 5,
            "primitive_axioms": ["I", "II", "III", "V"],
            "closure_clauses": ["IV", "VI", "VII"],
            "typed_channel_candidates_per_model": 2,
            "trace_equivalences": 10,
            "nonvacuous_role_map_candidates": 2,
            "negative_channel_counts": [len(L["C"]), len(M["C"])],
            "negative_role_carrier_counts": [len(L["roles"]), len(M["roles"])],
            "negative_role_map_rows": neg, "negative_E8_passes": 0,
            "negative_full_family_composites": [0, 0],
            "empty_vs_singleton_channels": [len(Z["C"]), len(L["C"])],
            "positive_channel_counts": [len(L["C"]), len(P["C"])],
            "positive_strict_isomorphisms": sum(r["strict"] for r in pos),
            "positive_role_map_rows": pos,
            "same_cardinality_but_term_mismatch_counts": [len(L["C"]), len(Q["C"])],
            "same_cardinality_but_term_mismatch_strict": False,
            "same_count_bad_rows": same_count_bad,
            "defined_zero_is_not_absence": True,
            "finite_example_not_universal_proof": True,
            "independent_external_validation": False}


def main():
    result = check()
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else (Path(__file__).resolve().parent.parent /
            "results" / "c626_channel_cardinality.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print("C6.26 finite source-typed checks PASS: five models, ten trace tests")
    print("OUTPUT:", out)


if __name__ == "__main__":
    main()
