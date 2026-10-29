#!/usr/bin/env python3
# Kwon Dominicus — PA-P39 frozen manuscript dependency-structure audit
# This verifies source integrity and a finite witness, NOT arbitrary-set theorems.
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

DIR = Path(__file__).resolve().parent
P27 = DIR.parent / "P27_independent_math_revision"
EN = P27 / "DSD_Property_Axiom_System_EN_P27_REVISED.tex"
KR = P27 / "DSD_Property_Axiom_System_KR_P27_REVISED.tex"
EXPECTED = DIR / "P39_56_ITEM_DEPENDENCY_EVIDENCE.json"

TYPES = ("theorem", "proposition", "lemma", "corollary",
         "definition", "model", "countermodel", "construction",
         "example", "remark")
ENV = "|".join(TYPES)
BEGIN = re.compile(r"\\section\{([^}]+)\}|\\begin\{(" + ENV
                   + r")\}(?:\[([^\]]+)\])?")
LABEL = re.compile(r"\\label\{([^}]+)\}")
REF = re.compile(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}")

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def extract(source: str):
    sec = 0
    number = 0
    out = []
    for m in BEGIN.finditer(source):
        if m.group(1) is not None:
            sec += 1
            number = 0
            continue
        number += 1
        kind = m.group(2)
        tail = source[m.end():]
        end_token = r"\end{" + kind + "}"
        end = tail.find(end_token)
        assert end >= 0, f"unclosed {kind} section {sec}"
        body = tail[:end]
        lab = LABEL.search(body)
        following = tail[end + len(end_token):].lstrip()
        refs = list(dict.fromkeys(REF.findall(body)))
        out.append({
            "n": f"{sec}.{number}",
            "kind": kind,
            "title": m.group(3) or "",
            "label": lab.group(1) if lab else None,
            "has_explicit_immediate_proof": following.startswith(r"\begin{proof}"),
            "direct_refs": refs,
        })
    return out

def dependency_only_stage3():
    # Canonical one-input full cores; no assignment values required.
    X = {("a",)}
    applicability_a = X.copy()
    applicability_b = X.copy()
    sat_a = X.copy()
    sat_b = set()
    domain_a = set()
    domain_b = set()
    # Both PI and PII hold; the domain is empty.
    assert domain_a <= applicability_a & sat_a
    assert domain_b <= applicability_b & sat_b
    # The unique carrier bijection is identity. Stage-2 condition is true.
    stage2_bijections = [tuple(sorted(X))]
    # Stage-3 requires preservation of both applicability and Sat(d).
    stage3_bijections = [f for f in stage2_bijections
                          if applicability_a == applicability_b
                          and sat_a == sat_b]
    return len(stage2_bijections) == 1 and len(stage3_bijections) == 0

def main():
    parser = argparse.ArgumentParser(description="Reaudit frozen P27 source and P39 ledger.")
    parser.add_argument("--out", type=Path, help="Optional result JSON path; defaults to stdout.")
    args = parser.parse_args()
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    en = EN.read_text(encoding="utf-8")
    kr = KR.read_text(encoding="utf-8")
    en_items, kr_items = extract(en), extract(kr)
    checks = {
        "frozen_en_sha256": sha256(EN) == expected["sha256"]["EN"],
        "frozen_kr_sha256": sha256(KR) == expected["sha256"]["KR"],
        "en_56_items": len(en_items) == expected["numbered_total"] == 56,
        "kr_56_items": len(kr_items) == expected["numbered_total"] == 56,
        "exact_en_number_type_title_label_and_refs": all(
            {k:v for k,v in x.items()} ==
            {k:v for k,v in y.items() if k in x}
            for x,y in zip(en_items, expected["items"])
        ) and len(en_items) == len(expected["items"]),
        "kr_number_type_label_correspondence":
            [(x["n"],x["kind"],x["label"]) for x in kr_items] ==
            [(x["n"],x["kind"],x["label"]) for x in en_items],
        "en_36_labels": len(LABEL.findall(en)) == expected["global_labels"] == 36,
        "kr_36_labels": len(LABEL.findall(kr)) == expected["global_labels"] == 36,
        "en_no_dangling_refs": set(REF.findall(en)).issubset(set(LABEL.findall(en))),
        "kr_no_dangling_refs": set(REF.findall(kr)).issubset(set(LABEL.findall(kr))),
        "en_17_proof_blocks": en.count(r"\begin{proof}") == expected["proof_blocks"] == 17,
        "kr_17_proof_blocks": kr.count(r"\begin{proof}") == expected["proof_blocks"] == 17,
        "two_pi_pii_primitive_axioms": en.count(r"\begin{axiom}") == 2,
        "one_c1_closure_clause": en.count(r"\begin{closureclause}") == 1,
        "same_type_count": {kind:sum(x["kind"] == kind for x in en_items)
                              for kind in TYPES if any(x["kind"] == kind for x in en_items)}
                            == expected["counts"],
        "main_13_conclusions": len(re.findall(r"\\item\b", en.split(
            r"\begin{theorem}[Static typed property-closure theorem]", 1)[1].split(
            r"\end{theorem}", 1)[0])) == 13,
        "all_s01_s04_risks_retained": all(
            any(id_ in x.get("risk", []) for x in expected["items"])
            for id_ in ("S-01","S-02","S-03","S-04")),
        "independent_dependency_only_stage3_witness": dependency_only_stage3(),
        "fpa_open_and_semantics_undecided":
            expected["whole_fpa"] == "OPEN" and expected["semantics_choice"] == "DEFERRED",
    }
    result = {
        "audit_id": expected["audit_id"],
        "checked": len(checks),
        "passed": sum(checks.values()),
        "checks": checks,
        "frozen_sources_unchanged": checks["frozen_en_sha256"] and checks["frozen_kr_sha256"],
        "mathematical_scope": "finite witness and textual dependency inventory only",
        "whole_property_FPA": "OPEN"
    }
    result_text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(result_text, encoding="utf-8")
    else:
        print(result_text, end="")
    if not all(checks.values()):
        raise SystemExit("P39 AUDIT REGRESSION FAILED")
if __name__ == "__main__":
    main()
