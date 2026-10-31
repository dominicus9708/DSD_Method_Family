#!/usr/bin/env python3
# Kwon Dominicus — PA-P41 dependency DAG audit; not a formal proof.
import argparse, hashlib, json, re
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
P27=ROOT/"P27_independent_math_revision"
EN=P27/"DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR=P27/"DSD_Property_Axiom_System_KR_P27_REVISED.tex"
P39=ROOT/"P39_global_56_item_dependency"/"P39_56_ITEM_DEPENDENCY_EVIDENCE.json"
P40=ROOT/"P40_20_statement_proof_audit"/"P40_20_CLAIMS_LEDGER.json"
GRAPH=HERE/"P41_DEPENDENCY_DAG_EVIDENCE.json"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def labels_refs(s):
    return set(re.findall(r"\\label\{([^}]+)\}",s)),set(re.findall(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}",s))
def order(v):
    return 0 if v in {"PI","PII","C1"} else int(v.split(".")[0])*100+int(v.split(".")[1])
def cycles(graph):
    seen={};found=[]
    def visit(n,stack):
        if seen.get(n)==2:return
        if seen.get(n)==1:found.append(stack+[n]);return
        seen[n]=1
        for d in graph.get(n,[]):visit(d,stack+[n])
        seen[n]=2
    for n in graph:visit(n,[])
    return found
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",type=Path)
    args=p.parse_args()
    a=json.loads(GRAPH.read_text(encoding="utf-8"))
    b=json.loads(P39.read_text(encoding="utf-8"))
    c=json.loads(P40.read_text(encoding="utf-8"))
    graph=a["manual_dependency_graph"]
    edges=[(n,d) for n,children in graph.items() for d in children]
    ids={x["n"] for x in b["items"]}|{"PI","PII","C1"}
    el,er=labels_refs(EN.read_text(encoding="utf-8"))
    kl,kr=labels_refs(KR.read_text(encoding="utf-8"))
    checks={
      "en_frozen_sha256":sha(EN)==a["source_sha256"]["EN"],
      "kr_frozen_sha256":sha(KR)==a["source_sha256"]["KR"],
      "p39_sha_same":b["sha256"]==a["source_sha256"],
      "p40_sha_same":c["source_sha256"]==a["source_sha256"],
      "56_source_items":b["numbered_total"]==a["numbered_source_items"]==56,
      "20_proof_nodes":len(graph)==c["claims"]==a["proof_claims"]==20,
      "same_claim_ids":set(graph)=={x["number"] for x in c["assessments"]},
      "97_edges":len(edges)==a["edges"]==97,
      "edges_valid":all(n in ids and d in ids for n,d in edges),
      "edges_ordered_to_earlier":all(order(d)<order(n) for n,d in edges),
      "no_manual_cycles":cycles(graph)==a["cycles"]==[],
      "no_missing_nodes":a["missing_nodes"]==[],
      "no_forward_dependency":a["nonprior_dependency_edges"]==[],
      "en_refs_exist":er.issubset(el),
      "kr_refs_exist":kr.issubset(kl),
      "both_36_labels":len(el)==len(kl)==36,
      "final_thm_precursors":set(["4.3","7.5","8.4","9.2"]).issubset(graph["11.1"]),
      "completion_before_stage5":set(["3.7","C1"]).issubset(graph["7.2"]) and "7.2" in graph["8.8"],
      "corollary_stage4_needs_iso":set(["7.2","6.8"]).issubset(graph["7.3"]),
      "typed_countermodels_no_C1":all("C1" not in graph[n] and "3.7" not in graph[n] for n in ("4.3","4.4")),
      "finite_realization_needs_typed":set(["2.5","2.6","3.7"]).issubset(graph["8.4"]),
      "all_s01_s04_retained":set(a["open_scope_conditions"])=={"S-01","S-02","S-03","S-04"},
      "A_B_choice_deferred":c["semantics_selection"]=="DEFERRED",
      "FPA_open_manuscript_frozen":a["FPA"]=="OPEN" and a["manuscript_modified"] is False
    }
    result={"audit_id":a["audit_id"],"checked":len(checks),"passed":sum(checks.values()),"checks":checks,"scope":"mapped dependency DAG and original source hash; NOT a complete mathematical formal proof","manuscript_edited":False,"FPA":"OPEN"}
    out=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(out,encoding="utf-8")
    else:print(out,end="")
    if not all(checks.values()):raise SystemExit("P41 FAILED")
if __name__=="__main__":main()
