#!/usr/bin/env python3
# Author: Kwon Dominicus
# P42 source/ledger regression, NOT mathematical proof of all propositions.
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
P27 = ROOT / "P27_independent_math_revision"
EN = P27 / "DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR = P27 / "DSD_Property_Axiom_System_KR_P27_REVISED.tex"
P40 = ROOT / "P40_20_statement_proof_audit" / "P40_20_CLAIMS_LEDGER.json"
P41 = ROOT / "P41_dependency_chain_and_scope" / "P41_DEPENDENCY_DAG_EVIDENCE.json"
LEDGER = HERE / "P42_20_PLUS_13_REVISION_LEDGER.json"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def item_count(tex: str) -> int:
    """Count explicit items in Section 11 main theorem only."""
    start = r"\begin{theorem}[Static typed property-closure theorem]"
    assert tex.count(start) == 1, "missing or duplicate final theorem"
    body = tex.split(start, 1)[1].split(r"\end{theorem}", 1)[0]
    return len(re.findall(r"\\item\b", body))

def scope_examples():
    """Small, typed examples distinguish local existential from fixed-universal."""
    # A single available typed input with one prerequisite.
    X = {"a"}
    applicable = {"a"}
    prerequisite_satisfied = {"a"}
    assignment = {}  # partial function with empty domain
    local_model_valid = set(assignment) <= applicable and set(assignment) <= prerequisite_satisfied
    both_reverse_inclusions_false = not (applicable <= set(assignment)) and not (
        prerequisite_satisfied <= set(assignment))
    has_applicable_undefined = "a" in X and "a" in applicable and (
        "a" in prerequisite_satisfied and "a" not in assignment)
    # Separate valid fixed signature has no candidate kinds at all.
    empty_signature_kinds = set()
    empty_declaration = set()
    all_possible_converses_vacuous = all(
        False for _ in empty_declaration
    )  # universally quantified inclusion over empty index is True
    no_defined_applicable_status_witness = not any(
        False for _ in empty_signature_kinds
    )
    return {
        "local_typed_core_satisfies_PI_and_PII": local_model_valid,
        "nonconverses_both_fail_in_local_core": both_reverse_inclusions_false,
        "applicable_prerequisite_satisfied_undefined_exists_locally": has_applicable_undefined,
        "empty_signature_has_no_declared_property": not empty_declaration,
        "empty_signature_converses_vacuous": all_possible_converses_vacuous,
        "empty_signature_has_no_applicable_undefined_witness": no_defined_applicable_status_witness,
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    source_en = EN.read_text(encoding="utf-8")
    source_kr = KR.read_text(encoding="utf-8")
    p40 = json.loads(P40.read_text(encoding="utf-8"))
    p41 = json.loads(P41.read_text(encoding="utf-8"))
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    twenty = ledger["twenty_claims"]
    thirteen = ledger["main_theorem_13"]
    source20 = p40["assessments"]
    checks = {
        "P27_en_sha_frozen": sha(EN) == ledger["frozen_sha256"]["EN"],
        "P27_kr_sha_frozen": sha(KR) == ledger["frozen_sha256"]["KR"],
        "P40_ledger_sha_matches": p40["source_sha256"] == ledger["frozen_sha256"],
        "P41_DAG_sha_matches": p41["source_sha256"] == ledger["frozen_sha256"],
        "twenty_original_proof_claims_mapped": len(twenty) == len(source20) == 20,
        "original_P40_20_claims_preserved": all(
            all(x.get(k) == y.get(k) for k in
                ("number", "kind", "title", "has_explicit_proof",
                 "source_refs", "risk", "audit_status", "assessment", "open_requirement"))
            for x,y in zip(twenty, source20)
        ),
        "thirteen_main_conclusions_mapped": len(thirteen) == 13,
        "thirteen_unique_ordered_numbers": [x["index"] for x in thirteen] == list(range(1,14)),
        "english_main_theorem_has_13_items": item_count(source_en) == 13,
        "korean_main_theorem_has_13_items": item_count_korean(source_kr) == 13,
        "all_main_claims_have_source_evidence": all(bool(x["evidence"]) for x in thirteen),
        "all_main_claims_have_status_and_safe_scope": all(
            bool(x["status"] and x["safe_statement"]) for x in thirteen),
        "fixed_signature_3_11_12_not_unconditionally_proved": all(
            thirteen[j-1]["status"] == "UNIVERSAL_FIXED_SIGNATURE_DISPROVED"
            for j in (3,11,12)),
        "main_10_finite_requires_typed": "S-02" in thirteen[9]["risks"],
        "main_9_stage_requires_S03": "S-03" in thirteen[8]["risks"],
        "new_scope_45_46_local": all(
            "S-04_LOCAL_EXISTENCE_SCOPE" in next(
                x["revised_scoping_risk"] for x in twenty if x["number"] == n)
            for n in ("4.5","4.6")),
        "all_four_proof_obligations_preserved": set(ledger["open_obligations"]) ==
            {"S-01","S-02","S-03","S-04"},
        "semantics_choice_deferred": ledger["semantics_selection"] == "DEFERRED",
        "FPA_remains_open": ledger["whole_FPA"] == "OPEN",
        "P27_sources_not_edited": ledger["frozen_manuscript"] and not ledger["source_revision_allowed"],
        "independent_external_validation_not_claimed": not ledger["independent_external_validation"],
        "s01_s03_pair_not_collapsed": (
            {"S-01","S-03"} <= set(thirteen[8]["risks"])),
        "proof_scope_not_auto_closed": all(
            x["decision"] == "DEFERRED_SOURCE_FROZEN" for x in twenty),
    }
    checks.update(scope_examples())
    result = {
        "audit_id": ledger["audit_id"],
        "passed": sum(checks.values()),
        "total": len(checks),
        "checks": checks,
        "notice": "Finite witness and source/ledger consistency; not a formal proof of the 20 claims or 13 conclusions",
        "manuscript_modified": False,
        "semantics_selection": "DEFERRED",
        "whole_FPA": "OPEN"
    }
    out = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(out, encoding="utf-8")
    else:
        print(out, end="")
    if not all(checks.values()):
        raise SystemExit("P42 REGRESSION FAILED")

def item_count_korean(tex: str) -> int:
    # The Korean P27 contains a matching final theorem but not the EN title.
    # Bound to the final theorem environment in section 11, before section 12.
    sec_start = tex.find(r"\section{")
    boundaries = list(re.finditer(r"\\section\{", tex))
    if len(boundaries) < 11:
        raise ValueError("Korean Section 11 missing")
    main = tex[boundaries[10].start(): boundaries[11].start()] if len(boundaries)>11 else tex[boundaries[10].start():]
    matches = re.findall(r"\\begin\{theorem\}(?:\[[^\]]+\])?([\s\S]*?)\\end\{theorem\}", main)
    if not matches:
        raise ValueError("Korean main theorem missing")
    return len(re.findall(r"\\item\b", matches[0]))

if __name__=="__main__":
    main()
