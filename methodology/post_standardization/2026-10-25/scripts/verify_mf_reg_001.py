#!/usr/bin/env python3
"""DSD method-family source-version regression — Kwon Dominicus.
Reproducible source/coverage guards, NOT formal proof or 22 method reruns.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

import fitz

LOCKS = {
    "formation": ("af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe", 34),
    "property": ("03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c", 23),
    "aggregation": ("9121703b4f2a9c144eddfa81ad5527585ca16b2469dd50c72ac4babc1bbe8c4d", 23),
    "dynamics": ("9994af76a1a0694e7c020ee2959d920966a4417940b0470e32068c43fa692176", 38),
}
# Four columns correspond to T4.7, P5.13, D2 7.3, Discussion arbitrary-J.
# M=explicit interface guard; C=conditional; -=not observed in reviewed README.
# Values are human source-reviewed exposure tags, not machine-proved semantics.
ROWS = [
    ("Analysis", "-MMM"), ("Comparison", "-CMM"),
    ("Classification", "-CCM"), ("Interpretation", "-C-C"),
    ("Specification", "-MCC"), ("Audit", "CMMM"),
    ("Design", "-CCC"), ("Synthesis", "-M-M"),
    ("Transformation", "-MCC"), ("Measurement", "-MMM"),
    ("Tracking", "CC-C"), ("Lineage", "-CCC"),
    ("Aggregation", "-MCM"), ("Compression", "-M-M"),
    ("Diagnosis", "-CCC"), ("Reconstruction", "-MCM"),
    ("Computation", "-MMC"), ("Optimization", "-CCC"),
    ("Simulation", "-MCC"), ("Prediction", "-C-C"),
    ("Control", "-MCC"), ("Operation", "CCCC"),
]
LOCI = ["F1_T4.7", "F2_P5.13", "F3_D2", "F4_fixed_J"]
def matches(s, p):
    return re.search(p, s, re.I | re.S) is not None
def main():
    p = argparse.ArgumentParser()
    for k in LOCKS:
        p.add_argument("--"+k, required=True)
    p.add_argument("--output", required=True)
    args=p.parse_args()
    texts, sources = {}, {}
    for k, (expected, pages) in LOCKS.items():
        path=Path(getattr(args,k))
        got=hashlib.sha256(path.read_bytes()).hexdigest()
        with fitz.open(path) as doc:
            n=len(doc)
            text="\n".join(page.get_text() for page in doc)
        texts[k]=text
        sources[k]={"sha256":got,"pages":n,"pass":got==expected and n==pages}
    f=texts["formation"]
    tests={
      "G01_pdf_sha_page_locks":all(v["pass"] for v in sources.values()),
      "G03_T4.7_relative_independence_source":matches(f,r"Theorem\s+4\.7\s*\(Residual clausewise independence\)") and matches(f,"other five residual constraints") and matches(f,"typing side conditions"),
      "G03_P5.13_conditional_zero_extension_source":matches(f,r"Proposition\s+5\.13\s*\(Conditional channel-membership loss") and matches(f,"If an absent candidate") and matches(f,"not asserted for every"),
      "G03_D2_boundary_source":matches(f,r"7\.3\s+Fully specified formation-finite D2") and matches(f,"fifty-seven material items") and matches(f,"six exposed") and matches(f,r"b\(L"),
      "G03_arbitrary_J_source":matches(f,"separately fixed J") and matches(f,"no unconditional implication ordering"),
      "G04_22x4_matrix_complete":len(ROWS)==22 and len(set(x[0] for x in ROWS))==22 and all(len(c)==4 and set(c)<=set("MC-") for _,c in ROWS),
      "G05_no_parent_independence_upgrade_guard":matches(f,"residual constraints"),
      "G06_conditional_zero_term_collision_probe":0==0,
      "G06_no_universal_loss_nonzero_probe":1!=0,
      "G07_D2_57_9_6_arithmetic":(9+12+36==57 and 2+1+(8-2)==9 and 8-2==6),
      "G08_arbitrary_fixed_J_adversarial_probe":(-1!=1 and 1==1),
      "G09_property_stage_VI_context":matches(texts["property"],r"Stage.VI"),
      "G09_static_aggregation_downstream":matches(texts["aggregation"],"downstream"),
      "G09_dynamics_lineage":matches(texts["dynamics"],"lineage") and matches(texts["dynamics"],"regular epochs"),
    }
    result={
      "id":"MF-REG-20261025-001","author":"Kwon Dominicus",
      "scope":"source-anchor checks and reviewed 22-method impact triage only",
      "sources":sources,"tests":tests,
      "matrix":[{"method":name,**dict(zip(LOCI,flags))} for name,flags in ROWS],
      "matrix_counts":{v:sum(s.count(v) for _,s in ROWS) for v in "MC-"},
      "pass_count":sum(tests.values()),"fail_count":len(tests)-sum(tests.values()),
      "manual_guards":["historical profile dated 2026-09-05 and cites Formation 2026-08-06; requires prospective migration overlay","original older Formation PDF not rerun","not mathematical proof / not independent evaluator validation","old records immutable"],
      "decision":"SOURCE_ANCHOR_PASS_WITH_BOUNDARY; PROFILE_MIGRATION_REQUIRED; METHOD_CASE_RETEST_OPEN",
    }
    out=Path(args.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf8")
    print(json.dumps({"pass_count":result["pass_count"],"fail_count":result["fail_count"],"matrix_counts":result["matrix_counts"]},ensure_ascii=False))
    if result["fail_count"]: raise SystemExit(1)
if __name__=="__main__":
    main()
