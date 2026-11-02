#!/usr/bin/env python3
# P43 EN/KR structural and displayed-formula parity audit
# Author: Kwon Dominicus
# This is NOT a machine proof of full translated natural-language semantics.
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HERE = Path(__file__).resolve().parent
P27 = ROOT / "P27_independent_math_revision"
EN = P27 / "DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR = P27 / "DSD_Property_Axiom_System_KR_P27_REVISED.tex"
LEDGER = HERE / "P43_EN_KR_PARITY_AND_GATES.json"
P42 = ROOT / "P42_consolidated_premises_countermodels_revision_spec" / "P42_20_PLUS_13_REVISION_LEDGER.json"

SEC = re.compile(r"\\section\{([^}]*)\}")
ENV = "definition|theorem|proposition|lemma|corollary|model|countermodel|construction|example|remark"
BEGIN = re.compile(r"\\section\{[^}]*\}|\\begin\{(" + ENV + r")\}(?:\[([^\]]+)\])?")
DISP = re.compile(r"\\\[([\s\S]*?)\\\]")
REF = re.compile(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}")
LABEL = re.compile(r"\\label\{([^}]+)\}")
TEXT = re.compile(r"\\text\{([^}]*)\}")
END_PUNCT = re.compile(r"[.,;:](?=(?:\\\\|\\end\{|$))")

def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def canonical_formula(formula: str) -> str:
    # Only the formula skeleton is compared. Prose inside LaTeX \text{...}
    # can affect meaning and is explicitly NOT certified by this comparator.
    formula = re.sub(r"%[^\n]*", "", formula)
    def localized(m):
        t = m.group(1)
        return m.group(0) if re.fullmatch(r"\([EF]\d+\)", t) else ""
    formula = TEXT.sub(localized, formula)
    formula = re.sub(r"\s+", "", formula)
    formula = END_PUNCT.sub("", formula)
    return formula.replace(r"\quad", "").replace(r"\qquad", "")

def sections(source: str):
    matches = list(SEC.finditer(source))
    return [(m.group(1), source[m.start():matches[i+1].start() if i+1<len(matches) else len(source)])
            for i,m in enumerate(matches)]

def environments(source: str):
    sec = 0
    idx = 0
    items = []
    for match in BEGIN.finditer(source):
        if match.group(0).startswith(r"\section"):
            sec += 1
            idx = 0
            continue
        idx += 1
        kind = match.group(1)
        tail = source[match.end():]
        close = tail.find(r"\end{" + kind + "}")
        if close < 0: raise ValueError("Unclosed " + kind)
        lab = LABEL.search(tail[:close])
        items.append((f"{sec}.{idx}",kind,lab.group(1) if lab else None))
    return items

def main13(source: str):
    pos = source.index(r"\label{thm:main}")
    end = source.index(r"\end{theorem}", pos)
    return len(re.findall(r"\\item\b", source[pos:end]))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, help="Optional replay result under P43")
    args = parser.parse_args()
    en = EN.read_text(encoding="utf-8")
    kr = KR.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    p42 = json.loads(P42.read_text(encoding="utf-8"))
    en_sections = sections(en)
    kr_sections = sections(kr)
    en_env = environments(en)
    kr_env = environments(kr)
    sec_results=[]
    for (e_title,e_text),(k_title,k_text) in zip(en_sections,kr_sections):
        en_equations=[canonical_formula(m.group(1)) for m in DISP.finditer(e_text)]
        kr_equations=[canonical_formula(m.group(1)) for m in DISP.finditer(k_text)]
        sec_results.append({
            "english":e_title,"korean":k_title,
            "EN_display":len(en_equations),"KR_display":len(kr_equations),
            "normalized_order_match":en_equations==kr_equations,
        })
    en_labs = LABEL.findall(en)
    kr_labs = LABEL.findall(kr)
    en_refs = REF.findall(en)
    kr_refs = REF.findall(kr)
    macros = re.compile(r"\\newcommand\{\\([^}]+)\}")
    axiom = re.compile(r"\\begin\{axiom\}")
    closure = re.compile(r"\\begin\{closureclause\}")
    assertions={
      "frozen_EN_SHA256":sha(EN)==ledger["frozen_source_sha256"]["EN"],
      "frozen_KR_SHA256":sha(KR)==ledger["frozen_source_sha256"]["KR"],
      "P42_source_SHA256_same":p42["frozen_sha256"]==ledger["frozen_source_sha256"],
      "16_sections_both":len(en_sections)==len(kr_sections)==ledger["sections"]==16,
      "30_subsections_EN":en.count(r"\subsection{")==ledger["subsections"]==30,
      "30_subsections_KR":kr.count(r"\subsection{")==ledger["subsections"]==30,
      "56_numbered_items_EN":len(en_env)==ledger["numbered_items"]==56,
      "56_numbered_items_KR":len(kr_env)==ledger["numbered_items"]==56,
      "numbered_sequence_type_and_label_same":en_env==kr_env,
      "manifest_all_56_match":all(
          (z[0],z[1],z[2])==(v["number"],v["kind"],v["label"])
          for z,v in zip(en_env,ledger["parallel_numbered"])
      ) and len(ledger["parallel_numbered"])==56,
      "36_labels_both":len(en_labs)==len(kr_labs)==ledger["labels"]==36,
      "label_sequence_equal":en_labs==kr_labs,
      "all_explicit_refs_resolved":set(en_refs)<=set(en_labs) and set(kr_refs)<=set(kr_labs),
      "31_reference_uses_both":len(en_refs)==len(kr_refs)==ledger["inline_reference_uses"]==31,
      "reference_multisets_match":Counter(en_refs)==Counter(kr_refs),
      "17_proof_environments_both":en.count(r"\begin{proof}")==kr.count(r"\begin{proof}")==ledger["proof_environments"]==17,
      "two_axioms_both":len(axiom.findall(en))==len(axiom.findall(kr))==ledger["axioms"]==2,
      "one_C1_both":len(closure.findall(en))==len(closure.findall(kr))==ledger["definitional_closure_clauses"]==1,
      "17_common_macros_order_equal":macros.findall(en)==macros.findall(kr)==ledger["macros"],
      "13_EN_main_items":main13(en)==ledger["main_theorem_count"]["EN"]==13,
      "13_KR_main_items":main13(kr)==ledger["main_theorem_count"]["KR"]==13,
      "per_section_math_counts_frozen":all(
           x["EN_display"]==v["EN_display"] and x["KR_display"]==v["KR_display"]
           for x,v in zip(sec_results,ledger["section_comparison"])
      ) and len(sec_results)==len(ledger["section_comparison"])==16,
      "per_section_math_order_equal":all(x["normalized_order_match"] for x in sec_results),
      "78_display_equations_each":sum(z["EN_display"] for z in sec_results)==sum(z["KR_display"] for z in sec_results)==ledger["math_display"]==78,
      "eight_high_risk_spots":len(ledger["bilingual_high_risk_statement_parity"])==8,
      "seven_gate_rows":len(ledger["closure_gates"])==7,
      "all_four_scoping_obligations_still_open":set(p42["open_obligations"])=={"S-01","S-02","S-03","S-04"},
      "semantics_deferred":ledger["semantics_decision"]=="DEFERRED",
      "FPA_OPEN":ledger["final_status"]=="FULL_FPA_OPEN",
      "no_source_edits":ledger["source_modified"] is False,
    }
    result={
       "audit_id":ledger["audit_id"],
       "checked":len(assertions),"passed":sum(assertions.values()),
       "checks":assertions,"compared_sections":16,
       "parallel_numbered_items":56,"display_math_count_each":78,
       "scope":"Formula skeleton and structural comparison; not proof of all bilingual natural-language semantics",
       "source_modified":False,"A_B_selection":"DEFERRED","full_FPA":"OPEN"
    }
    out=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(out,encoding="utf-8")
    else:
        print(out,end="")
    if not all(assertions.values()):
        raise SystemExit("P43 SOURCE/PARITY REGRESSION FAILURE")
if __name__=="__main__":
    main()
