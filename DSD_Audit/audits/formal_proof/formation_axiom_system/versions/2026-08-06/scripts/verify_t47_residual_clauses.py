#!/usr/bin/env python3
r"""Reproduce the six finite source-described residual counterinterpretations of FAS Theorem 4.7.

Python 3.10+ standard library. Does not formally verify arbitrary set-theoretic models.
Run at DSD_Method_Family repository root on Windows 11:
py -3.11 DSD_Audit\audits\formal_proof\formation_axiom_system\scripts\verify_t47_residual_clauses.py --output DSD_Audit\audits\formal_proof\formation_axiom_system\results\t47_residual_clauses.json
"""
import argparse
import json
from pathlib import Path

RESIDUALS = ("R1", "R2", "R3", "R4", "R5", "R6")


def base():
    # Shared nondegenerate kernel of manuscript §4.1.
    return {
        "expressions": {"g": {"mat": ["a"], "anch": {"a": "s0"}}},
        "configs": {"p": {"act": ["a"], "anch": {"a": "s0"}}},
        "admexpr": ["g"], "desexpr": ["g"],
        "admcfg": ["p"], "lc": ["p"], "bc": ["p"],
        "res": [["g", "g"]], "realize": [["g", "p"]],
        "q": {"a": 1}, "role": [["p", "a", "lambda", "rho"]],
    }


def example(target):
    m = base()
    if target == "R1":
        m["expressions"]["x"] = {"mat": ["b"], "anch": {"b": "s0"}}
        m["desexpr"].append("x")
    elif target == "R2":
        m["expressions"]["H"] = {"mat": ["b"], "anch": {"b": "s0"}}
        m["expressions"]["h"] = {"mat": ["b"], "anch": {"b": "s1"}}
        m["admexpr"] += ["H", "h"]
        m["res"] += [["H", "H"], ["h", "h"], ["H", "h"]]
    elif target == "R3":
        m["expressions"]["H"] = {"mat": ["b"], "anch": {"b": "s0"}}
        m["expressions"]["h"] = {"mat": ["b"], "anch": {"b": "s0"}}
        m["admexpr"].append("H")
        m["res"] += [["H", "H"], ["H", "h"]]
    elif target == "R4":
        m["expressions"]["h"] = {"mat": ["b"], "anch": {"b": "s0"}}
        m["admexpr"].append("h")
    elif target == "R5":
        m["expressions"]["h"] = {"mat": ["b"], "anch": {"b": "s0"}}
        m["admexpr"].append("h")
        m["res"].append(["h", "h"])
        m["configs"]["p_prime"] = {"act": ["b"], "anch": {"b": "s1"}}
        m["realize"].append(["h", "p_prime"])
    elif target == "R6":
        m["q"]["b"] = 1
    else:
        raise ValueError(target)
    return m


def restricted_equal(f, g, retained):
    # The paper's f|A means restriction to A intersect dom(f).
    return {a: f[a] for a in retained if a in f} == g


def check(m):
    es, ps = m["expressions"], m["configs"]
    adm, desc = set(m["admexpr"]), set(m["desexpr"])
    assert len({"a", "b"}) == 2 and len({"s0", "s1"}) == 2
    for e in es.values():
        assert set(e["mat"]) <= {"a", "b"}
        assert set(e["anch"]) == set(e["mat"])
        assert set(e["anch"].values()) <= {"s0", "s1"}
    for p in ps.values():
        assert set(p["act"]) <= {"a", "b"}
        assert set(p["anch"]) == set(p["act"])
        assert set(p["anch"].values()) <= {"s0", "s1"}
    assert adm <= set(es) and desc <= set(es)
    assert all(set(m[k]) <= set(ps) for k in ("admcfg", "lc", "bc"))
    assert all(H in es and h in es for H, h in m["res"])
    assert all(h in es and p in ps for h, p in m["realize"])
    assert set(m["q"]) <= {"a", "b"}
    assert all(v in (0, 1) for v in m["q"].values())
    assert all(p in ps and a in {"a", "b"} and lam == "lambda" and role == "rho"
               for p, a, lam, role in m["role"])

    bad = {key: [] for key in RESIDUALS}
    for x in es:
        if x in desc and x not in adm:
            bad["R1"].append(x)
        if x in adm and [x, x] not in m["res"]:
            bad["R4"].append(x)
    for H, h in m["res"]:
        if not restricted_equal(es[H]["anch"], es[h]["anch"], es[h]["mat"]):
            bad["R2"].append([H, h])
        if h not in adm:
            bad["R3"].append([H, h])
    for h, p in m["realize"]:
        if not restricted_equal(es[h]["anch"], ps[p]["anch"], ps[p]["act"]):
            bad["R5"].append([h, p])

    kdes = [
        p for p in sorted(set(m["admcfg"]) & set(m["lc"]) & set(m["bc"]))
        if any([H, h] in m["res"] and h in desc and [h, p] in m["realize"]
               for H in es for h in es)
    ]
    active = sorted({a for p in kdes for a in ps[p]["act"]})
    bad["R6"] = sorted(set(m["q"]) - set(active))
    channels = [
        [p, a, "lambda", m["q"][a], "rho"]
        for p in kdes for a in ps[p]["act"]
        if a in m["q"] and [p, a, "lambda", "rho"] in m["role"]
    ]
    assert channels == [["p", "a", "lambda", 1, "rho"]]
    assert kdes == ["p"] and active == ["a"]
    assert m["res"] and m["realize"] and m["q"] and m["role"]
    # W=R, T(c_g)=1 from source §4.1; P_fin(C)={empty,{c_g}}.
    return {
        "residual_truth": {k: not bad[k] for k in RESIDUALS},
        "violations": bad,
        "K_des": kdes,
        "A_star": active,
        "channels": channels,
        "finite_composites": {"empty": 0, "singleton_cg": 1},
    }


def reproduce():
    cases = {}
    for target in RESIDUALS:
        result = check(example(target))
        assert result["residual_truth"][target] is False
        assert all(ok for k, ok in result["residual_truth"].items() if k != target)
        assert len(result["violations"][target]) == 1
        cases[target] = result
    return {
        "audit_id": "FAS-F2-T4.7-001",
        "source_pdf_sha256": "8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a",
        "source_section": "Proposition 4.6 and Theorem 4.7 (printed pp.10-11)",
        "tested_claim": "each residual fails with other five residuals holding",
        "claim_scope": "typed background plus the five other residual clauses, not the intact parent primitive axiom",
        "independent_external_validation": False,
        "automated_general_proof": False,
        "checked_cases": 6,
        "cases": cases,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    output = reproduce()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("6/6 residual-clause counterinterpretations VERIFIED")
    print("Output:", args.output)


if __name__ == "__main__":
    main()
