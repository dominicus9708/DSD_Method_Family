#!/usr/bin/env python3
"""Adversarial mutations of immutable MF-REG-002 fixture; never overwrites it.
Author: Kwon Dominicus. Runs existing frozen source-locked checker as child processes.
"""
import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

MUTATIONS = (
    ("NC1_false_zero_collision", "Z0", "collision_with_membership_difference", False),
    ("NC2_false_J_coincidence", "J0", "j_composite_coincidence", True),
    ("NC3_false_first_branch", "B1", "first_justified_branch", 3),
    ("NC4_corrupt_formation_hash", "__SOURCE__", "formation_sha256", "0" * 64),
)

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--verifier", required=True)
    a.add_argument("--fixtures", required=True)
    for k in ("formation", "property", "aggregation", "dynamics"):
        a.add_argument("--"+k, required=True)
    a.add_argument("--output", required=True)
    opts = a.parse_args()
    immutable = Path(opts.fixtures).read_bytes()
    p = json.loads(immutable)
    runs = []
    for name, case, field, wrong in MUTATIONS:
        q = copy.deepcopy(p)
        if case == "__SOURCE__":
            q["source_locks"]["formation"]["sha256"] = wrong
        else:
            next(v for v in q["cases"] if v["id"] == case)["expected"][field] = wrong
        with tempfile.TemporaryDirectory(prefix="mf_reg_002_nc_") as d:
            f, out = Path(d)/"tampered.json", Path(d)/"out.json"
            f.write_text(json.dumps(q), encoding="utf-8")
            cmd = [sys.executable,"-W","error",opts.verifier,"--fixtures",str(f)]
            for k in ("formation","property","aggregation","dynamics"):
                cmd.extend(["--"+k,getattr(opts,k)])
            cmd.extend(["--output",str(out)])
            cp = subprocess.run(cmd,capture_output=True,text=True,timeout=45,check=False)
            observed = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
        rejected = cp.returncode == 1 and observed.get("verdict") == "FAIL_WITH_EVIDENCE"
        runs.append({"negative_control":name,"mutated_case":case,"mutated_field":field,"rejected":rejected,
                     "process_returncode":cp.returncode,"verdict":observed.get("verdict"),
                     "original_fixture_preserved":Path(opts.fixtures).read_bytes()==immutable})
    report = {"audit_id":"MF-REG-20261025-002-NC","source_fixture_sha256":hashlib.sha256(immutable).hexdigest(),
              "negative_controls":runs,"rejected_count":sum(x["rejected"] for x in runs),
              "total":len(runs),"verdict":"4_OF_4_DETECTED" if all(x["rejected"] for x in runs) else "DETECTION_FAILURE"}
    o=Path(opts.output);o.parent.mkdir(parents=True,exist_ok=True)
    o.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"verdict":report["verdict"],"rejected":report["rejected_count"]}))
    if report["rejected_count"] != len(runs):raise SystemExit(1)

if __name__ == "__main__":main()
