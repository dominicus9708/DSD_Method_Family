#!/usr/bin/env python3
from __future__ import annotations
import argparse
from collections import defaultdict, deque

PROVENANCE = (
    "PRE_EXISTING_DSD",
    "GENERAL_OPERATIONAL",
    "QUANTUM_SELECTOR",
    "STANDARD_THEOREM_CONSEQUENCE",
    "REMAINS_EXTERNAL",
)

NODES = {
    # Pre-existing DSD
    "DSD_TYPED_IDENTITY_STATUS": ("PRE_EXISTING_DSD", ()),
    "DSD_APPLICABILITY_PREREQUISITES": ("PRE_EXISTING_DSD", ()),
    "DSD_RESTRICTION_EQUIVALENCE": ("PRE_EXISTING_DSD", ()),
    "DSD_AGGREGATION_INFORMATION_LOSS": ("PRE_EXISTING_DSD", ()),
    "DSD_REGULAR_EVOLUTION_LINEAGE": ("PRE_EXISTING_DSD", ()),

    # General operational structure
    "RANDOMIZED_PREPARATION_CONVEXITY": ("GENERAL_OPERATIONAL", ("DSD_TYPED_IDENTITY_STATUS",)),
    "AFFINE_PROBABILITY_READOUT": ("GENERAL_OPERATIONAL", ("RANDOMIZED_PREPARATION_CONVEXITY",)),
    "AFFINE_TRANSFORMATIONS": ("GENERAL_OPERATIONAL", ("RANDOMIZED_PREPARATION_CONVEXITY",)),
    "OPERATIONAL_CAPACITY": ("GENERAL_OPERATIONAL", ("AFFINE_PROBABILITY_READOUT",)),
    "FINITE_REAL_ORDERED_CARRIER": ("GENERAL_OPERATIONAL", ("AFFINE_PROBABILITY_READOUT",)),

    # Quantum target selectors / supplied target structure
    "COMPLEX_HILBERT_CARRIER": ("QUANTUM_SELECTOR", ("FINITE_REAL_ORDERED_CARRIER",)),
    "FULL_HILBERT_EFFECT_CARRIER": ("QUANTUM_SELECTOR", ("COMPLEX_HILBERT_CARRIER",)),
    "STANDARD_COMPLEX_TENSOR_COMPOSITION": ("QUANTUM_SELECTOR", ("COMPLEX_HILBERT_CARRIER",)),
    "LOCAL_TOMOGRAPHY_SELECTOR": ("QUANTUM_SELECTOR", ("STANDARD_COMPLEX_TENSOR_COMPOSITION",)),
    "ANCILLA_COMPATIBILITY_SELECTOR": ("QUANTUM_SELECTOR", ("STANDARD_COMPLEX_TENSOR_COMPOSITION",)),
    "SELF_ADJOINT_CANONICAL_PAIR_SELECTOR": ("QUANTUM_SELECTOR", ("COMPLEX_HILBERT_CARRIER",)),
    "WEYL_REGULARITY_IRREDUCIBILITY_SELECTOR": ("QUANTUM_SELECTOR", ("SELF_ADJOINT_CANONICAL_PAIR_SELECTOR",)),
    "QDS_SEMIGROUP_SELECTOR": ("QUANTUM_SELECTOR", ("COMPLEX_HILBERT_CARRIER",)),

    # Standard theorem consequences
    "BORN_TRACE_REPRESENTATION": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("FULL_HILBERT_EFFECT_CARRIER", "AFFINE_PROBABILITY_READOUT"),
    ),
    "COMPLETE_POSITIVITY_FROM_ANCILLA_CLOSURE": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("ANCILLA_COMPATIBILITY_SELECTOR",),
    ),
    "CPTP_DETERMINISTIC_CHANNEL": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("COMPLETE_POSITIVITY_FROM_ANCILLA_CLOSURE", "AFFINE_PROBABILITY_READOUT"),
    ),
    "INSTRUMENT_CPTNI_BRANCHES": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("CPTP_DETERMINISTIC_CHANNEL", "DSD_TYPED_IDENTITY_STATUS"),
    ),
    "UNITARY_REVERSIBLE_CHANNEL": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("CPTP_DETERMINISTIC_CHANNEL",),
    ),
    "HAMILTONIAN_GENERATOR": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("UNITARY_REVERSIBLE_CHANNEL", "DSD_REGULAR_EVOLUTION_LINEAGE"),
    ),
    "GKSL_GENERATOR": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("QDS_SEMIGROUP_SELECTOR", "CPTP_DETERMINISTIC_CHANNEL"),
    ),
    "KRAUS_STINESPRING_DILATION": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("CPTP_DETERMINISTIC_CHANNEL",),
    ),
    "NAIMARK_MEASUREMENT_DILATION": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("FULL_HILBERT_EFFECT_CARRIER",),
    ),
    "UNBOUNDED_OPERATOR_DOMAIN_DISCIPLINE": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("COMPLEX_HILBERT_CARRIER",),
    ),
    "STONE_VON_NEUMANN_EQUIVALENCE": (
        "STANDARD_THEOREM_CONSEQUENCE",
        ("WEYL_REGULARITY_IRREDUCIBILITY_SELECTOR", "UNBOUNDED_OPERATOR_DOMAIN_DISCIPLINE"),
    ),

    # Explicitly not derived / remains external at current program boundary
    "INDEPENDENT_COMPLEX_HILBERT_ORIGIN": ("REMAINS_EXTERNAL", ("COMPLEX_HILBERT_CARRIER",)),
    "NUMERICAL_HBAR_VALUE": ("REMAINS_EXTERNAL", ("WEYL_REGULARITY_IRREDUCIBILITY_SELECTOR",)),
    "UNIQUE_PHYSICAL_ENVIRONMENT": ("REMAINS_EXTERNAL", ("KRAUS_STINESPRING_DILATION",)),
    "UNIQUE_MEASUREMENT_APPARATUS": ("REMAINS_EXTERNAL", ("NAIMARK_MEASUREMENT_DILATION",)),
    "UNIQUE_MICROSCOPIC_INTERACTION": ("REMAINS_EXTERNAL", ("GKSL_GENERATOR",)),
}

TARGET_COMPONENTS = {
    "state/effect Hilbert carrier": "COMPLEX_HILBERT_CARRIER",
    "Born probability": "BORN_TRACE_REPRESENTATION",
    "composite ancilla structure": "STANDARD_COMPLEX_TENSOR_COMPOSITION",
    "complete positivity": "COMPLETE_POSITIVITY_FROM_ANCILLA_CLOSURE",
    "deterministic channel": "CPTP_DETERMINISTIC_CHANNEL",
    "instrument branches": "INSTRUMENT_CPTNI_BRANCHES",
    "reversible channel": "UNITARY_REVERSIBLE_CHANNEL",
    "Hamiltonian generator": "HAMILTONIAN_GENERATOR",
    "open-system semigroup generator": "GKSL_GENERATOR",
    "channel dilation": "KRAUS_STINESPRING_DILATION",
    "measurement dilation": "NAIMARK_MEASUREMENT_DILATION",
    "unbounded observable/domain": "UNBOUNDED_OPERATOR_DOMAIN_DISCIPLINE",
    "canonical CCR/Weyl representation": "STONE_VON_NEUMANN_EQUIVALENCE",
}

def topo_ok():
    indeg = {n:0 for n in NODES}
    children=defaultdict(list)
    missing=[]
    for n,(_,deps) in NODES.items():
        for d in deps:
            if d not in NODES:
                missing.append((n,d)); continue
            indeg[n]+=1; children[d].append(n)
    if missing:
        return False, missing, []
    q=deque([n for n,d in indeg.items() if d==0]); order=[]
    while q:
        n=q.popleft(); order.append(n)
        for c in children[n]:
            indeg[c]-=1
            if indeg[c]==0:q.append(c)
    return len(order)==len(NODES), [], order

def checks():
    out=[]
    out.append(("all nodes use declared provenance classes",
                all(cls in PROVENANCE for cls,_ in NODES.values())))
    ok, missing, order=topo_ok()
    out.append(("all dependency nodes exist", not missing))
    out.append(("dependency graph is acyclic", ok))
    out.append(("all standard target components are classified",
                all(n in NODES for n in TARGET_COMPONENTS.values())))
    out.append(("complex Hilbert carrier is not classified as independent DSD",
                NODES["COMPLEX_HILBERT_CARRIER"][0]=="QUANTUM_SELECTOR"))
    out.append(("independent complex-Hilbert origin remains external",
                NODES["INDEPENDENT_COMPLEX_HILBERT_ORIGIN"][0]=="REMAINS_EXTERNAL"))
    theorem_nodes=[n for n,(c,_) in NODES.items() if c=="STANDARD_THEOREM_CONSEQUENCE"]
    out.append(("theorem consequences are not counted as independent A/B evidence",
                all(NODES[n][0] not in ("PRE_EXISTING_DSD","GENERAL_OPERATIONAL") for n in theorem_nodes)))
    independent={n for n,(c,_) in NODES.items() if c in ("PRE_EXISTING_DSD","GENERAL_OPERATIONAL")}
    out.append(("independent evidence excludes quantum selectors",
                "COMPLEX_HILBERT_CARRIER" not in independent and "LOCAL_TOMOGRAPHY_SELECTOR" not in independent))
    out.append(("conditional standard-QM chain is represented",
                all(k in NODES for k in (
                    "BORN_TRACE_REPRESENTATION","CPTP_DETERMINISTIC_CHANNEL","UNITARY_REVERSIBLE_CHANNEL",
                    "HAMILTONIAN_GENERATOR","GKSL_GENERATOR","KRAUS_STINESPRING_DILATION",
                    "NAIMARK_MEASUREMENT_DILATION","STONE_VON_NEUMANN_EQUIVALENCE"))))
    return out

def summarize():
    counts=defaultdict(int)
    for cls,_ in NODES.values(): counts[cls]+=1
    return counts

def run(mode):
    ok=True
    if mode in ("all","ledger"):
        print("[PROVENANCE_LEDGER]")
        for label,good in checks():
            ok &= good
            print(f"{label:<78} {'PASS' if good else 'FAIL'}")
        print()
    if mode in ("all","counts"):
        print("[CLASS_COUNTS]")
        counts=summarize()
        for cls in PROVENANCE:
            print(f"{cls:<34} {counts[cls]}")
        print()
    if mode in ("all","targets"):
        print("[STANDARD_QM_TARGET_COMPONENTS]")
        for label,node in TARGET_COMPONENTS.items():
            cls=NODES[node][0]
            print(f"{label:<40} {cls}")
        print()
    if mode in ("all","boundary"):
        print("[FINAL_BOUNDARY]")
        b1=NODES["COMPLEX_HILBERT_CARRIER"][0]=="QUANTUM_SELECTOR"
        b2=NODES["INDEPENDENT_COMPLEX_HILBERT_ORIGIN"][0]=="REMAINS_EXTERNAL"
        b3=NODES["BORN_TRACE_REPRESENTATION"][0]=="STANDARD_THEOREM_CONSEQUENCE"
        for label,good in [
            ("conditional standard-QM reconstruction is represented", b3),
            ("complex Hilbert carrier remains supplied selector", b1),
            ("independent complex-Hilbert origin is not claimed", b2),
        ]:
            ok &= good
            print(f"{label:<78} {'PASS' if good else 'FAIL'}")
        print()
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode", choices=("all","ledger","counts","targets","boundary"), default="all")
    a=p.parse_args()
    return run(a.mode)

if __name__=="__main__":
    raise SystemExit(main())
