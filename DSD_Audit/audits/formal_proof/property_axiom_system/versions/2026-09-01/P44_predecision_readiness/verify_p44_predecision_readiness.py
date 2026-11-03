#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PA-P44 — pre-decision FPA evidence coverage, formula parity and frozen source integrity
# Author: Kwon Dominicus
# Scope: audit reproducibility, NOT formal proof of arbitrary-set theorems.
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
P27 = ROOT / "P27_independent_math_revision"
EN = P27 / "DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR = P27 / "DSD_Property_Axiom_System_KR_P27_REVISED.tex"
P42 = ROOT / "P42_consolidated_premises_countermodels_revision_spec" / "P42_20_PLUS_13_REVISION_LEDGER.json"
P41 = ROOT / "P41_dependency_chain_and_scope" / "P41_DEPENDENCY_DAG_EVIDENCE.json"
P43 = ROOT / "P43_bilingual_math_parity_closure_gates" / "P43_EN_KR_PARITY_AND_GATES.json"
EXPECTED = HERE / "P44_PREDECISION_EVIDENCE_LEDGER.json"
SECTION = re.compile(r"\\section\{([^}]+)\}")
INLINE = re.compile(r"\\\(([\s\S]*?)\\\)")
DISPLAY = re.compile(r"\\\[([\s\S]*?)\\\]")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def sections(source):
    headings = list(SECTION.finditer(source))
    return [source[v.start():headings[i+1].start() if i+1<len(headings) else len(source)]
            for i,v in enumerate(headings)]

def canonical_inline(raw):
    # A deliberately *limited* formula comparison. Does not certify text semantics.
    raw = re.sub(r"%[^\n]*", "", raw)
    raw = re.sub(r"\\text\{[^}]*\}", "", raw)
    raw = re.sub(r"\s+", "", raw)
    raw = re.sub(r"[.,;:](?=\\|$)", "", raw)
    return raw.replace(r"\quad", "").replace(r"\qquad", "")

def inline_counts(source):
    return [Counter(canonical_inline(match.group(1)) for match in INLINE.finditer(section))
            for section in sections(source)]

def delta(lhs,rhs):
    # Elementwise count excess (empty for matching multisets).
    return {key:value for key,value in (lhs-rhs).items()}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path)
    args=parser.parse_args()
    led=json.loads(EXPECTED.read_text(encoding="utf-8"))
    p42=json.loads(P42.read_text(encoding="utf-8"))
    p43=json.loads(P43.read_text(encoding="utf-8"))
    p41=json.loads(P41.read_text(encoding="utf-8"))
    en=EN.read_text(encoding="utf-8")
    kr=KR.read_text(encoding="utf-8")
    a=inline_counts(en)
    b=inline_counts(kr)
    diffs=[]
    for i,(x,y) in enumerate(zip(a,b),start=1):
        left,right=delta(x,y),delta(y,x)
        if left or right:diffs.append({"section":i,"EN_excess":left,"KR_excess":right})
    expected_diff=[
        {"section":6,"EN_excess":{},"KR_excess":{r"\Phi":1}},
        {"section":7,"EN_excess":{"5":1},"KR_excess":{}},
    ]
    reports=led["audit_reports"]
    source_sha=led["source_sha256"]
    checks={
        "frozen_EN_SHA256":digest(EN)==source_sha["EN"],
        "frozen_KR_SHA256":digest(KR)==source_sha["KR"],
        "P42_source_SHA256_same":p42["frozen_sha256"]==source_sha,
        "P43_source_SHA256_same":p43["frozen_source_sha256"]==source_sha,
        "P41_source_SHA256_same":p41["source_sha256"]==source_sha,
        "15_audit_entries_in_sequence":[r["id"] for r in reports]==[f"P{i}" for i in range(29,44)],
        "15_actual_reports_present":len(reports)==15 and all((ROOT/r["report_path"]).is_file() for r in reports),
        "P42_twenty_proof_claims":len(p42["twenty_claims"])==20,
        "P42_thirteen_final_conclusions":len(p42["main_theorem_13"])==13,
        "P41_ninety_seven_edges":p41["edges"]==97,
        "P41_no_reported_cycles":p41["cycles"]==[],
        "16_sections_each":len(a)==len(b)==p43["sections"]==16,
        "78_display_expressions_each":len(DISPLAY.findall(en))==len(DISPLAY.findall(kr))==p43["math_display"]==78,
        "222_inline_expressions_each":sum(map(sum_counters,a))==sum(map(sum_counters,b))==led["observed_bilingual"]["inline_formula_count_each"]==222,
        "only_two_expected_inline_multiset_differences":diffs==expected_diff,
        "all_other_inline_multisets_match":len(diffs)==2 and led["observed_bilingual"]["other_section_inline_multisets_match"],
        "all_three_semantics_options":{a["id"] for a in led["alternatives"]}=={"A","B1","B2"},
        "three_options_explicitly_not_selected":all("NO_SELECTION" in a["status"] for a in led["alternatives"]),
        "all_four_proof_obligations":{a["id"] for a in led["obligations"]}=={"S-01","S-02","S-03","S-04"},
        "S01_and_S03_not_collapsed":any(a["id"]=="S-03" and "S01" in a["predecision"] for a in led["obligations"]),
        "eight_review_gates":{g["id"] for g in led["gates"]}=={f"E{i}" for i in range(1,9)},
        "translation_not_formally_certified":not led["observed_bilingual"]["natural_language_full_equivalence_certified"],
        "ready_for_comparative_review_only":led["verdict"]["predecision_evidence"]=="READY_FOR_COMPARATIVE_REVIEW",
        "author_choice_still_deferred":led["verdict"]["author_choice"]=="DEFERRED",
        "full_FPA_still_OPEN":led["verdict"]["full_property_FPA"]=="OPEN",
        "external_verification_not_claimed":led["verdict"]["external_independent_verification"]=="NOT_ESTABLISHED",
    }
    out={
        "audit_id":led["audit_id"],
        "checks":checks,
        "passed":sum(checks.values()),
        "checked":len(checks),
        "observed_inline_deltas":diffs,
        "source_modified":False,
        "validity_limit":"finite/exact source checks only; not a universal proof or full translation certification",
        "predecision":"READY_FOR_COMPARATIVE_REVIEW",
        "semantics_choice":"DEFERRED",
        "full_property_FPA":"OPEN"
    }
    rendered=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
    if args.out:
        args.out.parent.mkdir(parents=True,exist_ok=True)
        args.out.write_text(rendered,encoding="utf-8")
    else:print(rendered,end="")
    if not all(checks.values()):
        raise SystemExit("P44 predecision audit regression FAILED")

def sum_counters(counter):
    return sum(counter.values())

if __name__=="__main__":
    main()
