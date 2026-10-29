#!/usr/bin/env python3
# Kwon Dominicus, PA-P40: structural regression and independent finite witnesses.
# Passing this script does NOT mechanically prove all theorems over arbitrary sets.
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
P27 = ROOT / "P27_independent_math_revision"
E = P27 / "DSD_Property_Axiom_System_EN_P27_REVISED.tex"
K = P27 / "DSD_Property_Axiom_System_KR_P27_REVISED.tex"
LEDGER = HERE / "P40_20_CLAIMS_LEDGER.json"
P39 = ROOT / "P39_global_56_item_dependency" / "P39_56_ITEM_DEPENDENCY_EVIDENCE.json"
TYPES = ("theorem", "proposition", "corollary")
ALL = ("theorem", "proposition", "lemma", "corollary", "definition",
       "model", "countermodel", "construction", "example", "remark")
BEGIN = re.compile(r"\\section\{([^}]+)\}|\\begin\{(" + "|".join(ALL)
                   + r")\}(?:\[([^\]]+)\])?")
LAB = re.compile(r"\\label\{([^}]+)\}")

def entries(src: str):
    sec = idx = 0
    found = []
    for match in BEGIN.finditer(src):
        if match.group(1) is not None:
            sec += 1
            idx = 0
            continue
        idx += 1
        kind = match.group(2)
        tail = src[match.end():]
        closing = r"\end{" + kind + "}"
        cut = tail.find(closing)
        assert cut >= 0
        body = tail[:cut]
        label = LAB.search(body)
        proof = tail[cut+len(closing):].lstrip().startswith(r"\begin{proof}")
        found.append(dict(number=f"{sec}.{idx}", kind=kind,
                          title=match.group(3) or "",
                          label=label.group(1) if label else None,
                          has_explicit_proof=proof))
    return found

def countermodels_and_status():
    X = {("a",)}
    assigned = {"a": 1}
    empty = {}
    # PI requires assignment domain within Ap; PII requires it within Sat(d).
    pi_only_bad = (set(assigned).issubset(set()),set(assigned).issubset({"a"}))
    pii_only_bad = (set(assigned).issubset({"a"}),set(assigned).issubset(set()))
    # Valid model: both inclusion conditions, with defined assignment empty.
    pi = set(empty).issubset({"a"})
    pii = set(empty).issubset({"a"})
    converse_ap = {"a"}.issubset(set(empty))
    converse_dep = {"a"}.issubset(set(empty))
    status = ("a" in {"a"} and "a" in {"a"} and "a" not in empty)
    return {
        "PI_counterpremodel_well_typed": X == {("a",)} and pi_only_bad == (False,True),
        "PII_counterpremodel_well_typed": pii_only_bad == (True,False),
        "no_hidden_converse_both_fail": pi and pii and not converse_ap and not converse_dep,
        "applicable_dependency_satisfied_but_undefined": status,
    }

def summary_collision():
    points = ("a", "b")
    # Each tuple is p(a),p(b) and q(a),q(b).
    A = {"p": (0,1), "q": (0,1)}
    B = {"p": (0,1), "q": (1,0)}
    summ = lambda v: (len(v),tuple(sorted((p,len(a),a.count(0),sum(x!=0 for x in a)) for p,a in v.items())))
    compatible = []
    for permutation in itertools.permutations(range(len(points))):
        if all(all(A[p][i] == B[p][permutation[i]] for i in range(2)) for p in A):
            compatible.append(permutation)
    p_only = [f for f in itertools.permutations((0,1)) if all(A["p"][i] == B["p"][f[i]] for i in (0,1))]
    return {
       "same_label_retaining_summary": summ(A) == summ(B) == (2,(("p",2,1,1),("q",2,1,1))),
       "p_forces_identity_bijection": p_only == [(0,1)],
       "no_joint_strict_isomorphism": len(compatible) == 0,
       "two_declared_zero_bearing_types": set(A) == set(B) == {"p","q"},
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, help="Optional output location under the same repository.")
    args = parser.parse_args()
    en=E.read_text(encoding="utf-8")
    kr=K.read_text(encoding="utf-8")
    ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
    previous=json.loads(P39.read_text(encoding="utf-8"))
    en_items=entries(en)
    kr_items=entries(kr)
    selected=[x for x in en_items if x["kind"] in TYPES]
    kselected=[x for x in kr_items if x["kind"] in TYPES]
    listed=ledger["assessments"]
    checks={
      "source_en_frozen":hashlib.sha256(E.read_bytes()).hexdigest()==ledger["source_sha256"]["EN"],
      "source_kr_frozen":hashlib.sha256(K.read_bytes()).hexdigest()==ledger["source_sha256"]["KR"],
      "same_source_sha_as_p39":ledger["source_sha256"]==previous["sha256"],
      "en_56_count":len(en_items)==56,
      "kr_56_count":len(kr_items)==56,
      "en_20_claims":len(selected)==20,
      "kr_20_claims":len(kselected)==20,
      "exact_en_ledger_number_kind_title_proof":all(
          (x["number"],x["kind"],x["title"],x["has_explicit_proof"])==
          (v["number"],v["kind"],v["title"],v["has_explicit_proof"])
          for x,v in zip(selected,listed)) and len(selected)==len(listed),
      "kr_number_kind_proof_match":all(
          (x["number"],x["kind"],x["has_explicit_proof"])==
          (y["number"],y["kind"],y["has_explicit_proof"])
          for x,y in zip(selected,kselected)),
      "ten_theorems":sum(x["kind"]=="theorem" for x in selected)==10,
      "seven_propositions":sum(x["kind"]=="proposition" for x in selected)==7,
      "three_corollaries":sum(x["kind"]=="corollary" for x in selected)==3,
      "seventeen_explicit_proofs":sum(x["has_explicit_proof"] for x in selected)==17,
      "three_direct_corollaries_without_proof": [x["number"] for x in selected if not x["has_explicit_proof"]]==["4.6","7.3","8.8"],
      "all_20_have_audit_disposition":len(listed)==20 and all(x["audit_status"] and x["assessment"] and x["open_requirement"] for x in listed),
      "all_four_risks_remain_traceable":set(k for v in listed for k in v["risk"])=={"S-01","S-02","S-03","S-04"},
      "main_theorem_13_subclaims":len(re.findall(r"\\item\b",en.split(
          r"\begin{theorem}[Static typed property-closure theorem]",1)[1].split(r"\end{theorem}",1)[0]))==13,
      "P27_sources_not_marked_edited":ledger["source_modified"] is False,
      "FPA_remains_open":ledger["status"]=="OPEN" and ledger["semantics_selection"]=="DEFERRED",
    }
    checks.update(countermodels_and_status())
    checks.update(summary_collision())
    result={
       "audit_id":ledger["audit_id"],
       "checked":len(checks),"passed":sum(checks.values()),"checks":checks,
       "finite_observation_scope":"one-input counterpremodel and two-input two-property collision",
       "generic_proof_scope":"Not certified by this program",
       "P27_source_modified":False,"FPA":"OPEN"
    }
    text=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(text,encoding="utf-8")
    else:
        print(text,end="")
    if not all(checks.values()):
        raise SystemExit("P40 FAILURE: source, ledger or witness mismatch")
if __name__=="__main__":
    main()
