#!/usr/bin/env python3
"""P37 independent bounded typed-premodel / full-core audit; not a ZFC proof."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path

STATES = ("unavailable", "empty", "singleton")

def signature_classes():
    for hs in (0, 1):
        for aux in (False, True):
            yield (hs, aux, None, False, False, False)
            profiles = (("h",), ("u",), ("h", "u"), ("h", "h")) if aux else (("h",), ("h", "h"))
            for prof in profiles:
                for dep in (False, True):
                    for val in (False, True):
                        for zero in ((False, True) if val else (False,)):
                            yield (hs, aux, prof, dep, val, zero)

def supplied_states(sig):
    return STATES if sig[1] else ("no-aux-sort",)

def typed_inputs(sig, state):
    hsize, _, prof, _, _, _ = sig
    if prof is None:
        return None
    sizes = {"h": hsize, "u": {
        "unavailable": None, "empty": 0, "singleton": 1,
        "no-aux-sort": None}[state]}
    if any(sizes[x] is None for x in prof):
        return None
    return tuple(itertools.product(
        *(tuple(range(sizes[x])) for x in prof)))

def subset_choices(values):
    return [tuple(v for i, v in enumerate(values) if (mask >> i) & 1)
            for mask in range(2 ** len(values))]

def premodels(sig):
    _, _, prof, has_dep, value_present, _ = sig
    for state in supplied_states(sig):
        X = typed_inputs(sig, state)
        for declared in ((False, True) if prof is not None else (False,)):
            if not declared or X is None:
                yield (state, declared, None, None, None, True, True)
                continue
            ap_choices = subset_choices(X)
            sat_choices = subset_choices(X) if has_dep else ((),)
            for ap, sat in itertools.product(ap_choices, sat_choices):
                assignments = [()]
                if value_present:
                    assignments += [((x, 0),) for x in X]
                for xi in assignments:
                    dom = tuple(k for k, _ in xi)
                    PI = set(dom).issubset(ap)
                    PII = set(dom).issubset(sat) if has_dep else True
                    yield (state, declared, ap, sat, xi, PI, PII)

def stage_relation(sig, a, b):
    s1 = a[0] == b[0]
    s2 = s1 and a[1] == b[1]
    s3 = s2 and (not a[1] or typed_inputs(sig, a[0]) is None or
                 (a[2] == b[2] and a[3] == b[3]))
    s4 = s3 and (not a[1] or typed_inputs(sig, a[0]) is None or a[4] == b[4])
    return s1, s2, s3, s4

def summary(sig, model):
    _, _, prof, _, _, zero = sig
    state, declared, ap, sat, xi, pi, pii = model
    if not declared:
        return (0, ())
    if not zero or typed_inputs(sig, state) is None:
        return None
    return (1, (("p", len(xi), len(xi), 0),))

def criteria(sig):
    hs, aux, prof, has_dep, value, zero = sig
    realizable = prof is not None and ("h" not in prof or hs > 0)
    return {
        "mutual_independence": bool(realizable and value and has_dep),
        "branch2": prof is not None,
        "branch3": bool(realizable),
        "branch4": bool(realizable and value),
        "summary_collision": bool(aux or (realizable and zero)),
    }

def observations(sig):
    pre = list(premodels(sig))
    cores = [x for x in pre if x[5] and x[6]]
    pi_fails = any(not x[5] and x[6] for x in pre)
    pii_fails = any(x[5] and not x[6] for x in pre)
    seen = dict(mutual_independence=pi_fails and pii_fails,
                branch2=False, branch3=False,
                branch4=False, summary_collision=False)
    for a, b in itertools.product(cores, repeat=2):
        s1, s2, s3, s4 = stage_relation(sig, a, b)
        seen["branch2"] |= s1 and not s2
        seen["branch3"] |= s2 and not s3
        seen["branch4"] |= s3 and not s4
        sa, sb = summary(sig, a), summary(sig, b)
        seen["summary_collision"] |= sa is not None and sa == sb and not s4
    return seen, len(pre), len(cores)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out")
    args = parser.parse_args()
    classes = checks = npre = ncore = 0
    examples = {}
    for sig in signature_classes():
        classes += 1
        expected = criteria(sig)
        actual, np, nc = observations(sig)
        npre += np
        ncore += nc
        for k in expected:
            checks += 1
            assert expected[k] == actual[k], (
                f"{sig}: {k} expected={expected[k]} actual={actual[k]}")
            if actual[k] and k not in examples:
                examples[k] = dict(
                    h_size=sig[0], aux_sort=sig[1], profile=sig[2],
                    has_dependency=sig[3], has_value=sig[4], zero_bearing=sig[5])
    result = {
        "audit_id": "PA-P37-20261029-S02-S04-FIXED-SIGNATURE",
        "assumption": "Canonical restricted active property coordinates A; one candidate p max, inherited carrier h size 0/1, optional auxiliary u of size missing/empty/singleton, values absent or singleton, zero-bearing optional, one or no prerequisite",
        "checked_signature_classes": classes,
        "checks": checks,
        "typed_premodels_enumerated": npre,
        "admissible_primitive_cores_enumerated": ncore,
        "criteria": {
            "mutual_independence": "exists realizable nonempty typed input and nonempty value carrier with at least one prerequisite",
            "branch2": "at least one candidate property kind",
            "branch3": "at least one candidate property kind with realizable nonempty typed input",
            "branch4": "at least one candidate kind with realizable nonempty input and nonempty value carrier",
            "summary_collision": "available optional auxiliary sort OR an available zero-bearing candidate kind with realizable nonempty input",
        },
        "example_signatures": examples,
        "universal_proof_status": "GENERAL_ZFC_ARGUMENT_IN_SEPARATE_REPORT_NOT_ESTABLISHED_BY_FINITE_CHECKS",
        "S01_semantics_selected": False,
        "P27_manuscript_modified": False,
        "whole_FPA": "OPEN",
    }
    data = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(data, encoding="utf-8")
    else:
        print(data, end="")

if __name__ == "__main__":
    main()
