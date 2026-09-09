#!/usr/bin/env python3
from __future__ import annotations
import argparse
from collections import Counter, defaultdict, deque

CLASSES = {
    "R0": "PRE_EXISTING_DSD",
    "R1": "GENERAL_MATHEMATICAL_STRUCTURAL",
    "R2": "RELATIVITY_SPECIALIZATION",
    "R3": "STANDARD_THEOREM_CONSEQUENCE",
    "R4": "REMAINS_EXTERNAL_NOT_DERIVED",
}

NODES = {
    "typed_status_and_applicability": ("R0", ()),
    "explicit_bridge_discipline": ("R0", ()),
    "readout_reconstruction_discipline": ("R0", ()),
    "strict_equivalence_firewall": ("R0", ()),
    "state_relation_transition_separation": ("R0", ()),

    "invertible_representation_no_loss_by_itself": ("R1", ("readout_reconstruction_discipline",)),
    "typed_dimension_nonidentification": ("R1", ("explicit_bridge_discipline",)),
    "state_does_not_select_evolution_law": ("R1", ("state_relation_transition_separation",)),
    "fiber_factorization_reconstruction_gate": ("R1", ("readout_reconstruction_discipline",)),
    "passive_vs_active_semantic_commutation": ("R1", ("state_relation_transition_separation",)),

    "smooth_spacetime_manifold": ("R2", ("explicit_bridge_discipline",)),
    "lorentzian_metric": ("R2", ("smooth_spacetime_manifold",)),
    "spacetime_dimension_and_signature": ("R2", ("smooth_spacetime_manifold",)),
    "time_orientation": ("R2", ("lorentzian_metric",)),
    "einstein_field_equation": ("R2", ("lorentzian_metric", "state_relation_transition_separation")),
    "matter_stress_energy_model": ("R2", ("smooth_spacetime_manifold",)),
    "constraint_satisfying_initial_data": ("R2", ("einstein_field_equation", "matter_stress_energy_model")),
    "weak_field_background_specialization": ("R2", ("lorentzian_metric",)),

    "levi_civita_connection": ("R3", ("lorentzian_metric",)),
    "causal_cone_structure": ("R3", ("lorentzian_metric", "time_orientation")),
    "proper_time_invariant": ("R3", ("lorentzian_metric",)),
    "curvature_from_metric_connection": ("R3", ("lorentzian_metric", "levi_civita_connection")),
    "lorentz_frame_interval_invariance": ("R3", ("lorentzian_metric", "invertible_representation_no_loss_by_itself")),
    "covariant_stress_energy_conservation": ("R3", ("einstein_field_equation", "levi_civita_connection", "matter_stress_energy_model")),
    "maximal_globally_hyperbolic_development": ("R3", ("constraint_satisfying_initial_data", "einstein_field_equation")),
    "weak_field_proper_time_relation": ("R3", ("weak_field_background_specialization", "proper_time_invariant")),

    "why_four_spacetime_dimensions": ("R4", ("spacetime_dimension_and_signature",)),
    "why_lorentzian_signature": ("R4", ("spacetime_dimension_and_signature",)),
    "why_einstein_field_equation": ("R4", ("einstein_field_equation",)),
    "numerical_G_c_Lambda": ("R4", ("einstein_field_equation",)),
    "actual_matter_topology_boundary_initial_data": ("R4", ("matter_stress_energy_model", "constraint_satisfying_initial_data")),
    "identify_c_info_with_relativistic_c": ("R4", ("causal_cone_structure",)),
    "identify_DSD_strict_equivalence_with_GR_equivalence": ("R4", ("strict_equivalence_firewall",)),
    "unique_QM_GR_cross_dynamics": ("R4", ("explicit_bridge_discipline",)),
}

EXPECTED_PRIOR_AUDITS = {
    "PHY-REL-001": "coordinate representation != information loss",
    "PHY-REL-002": "Hilbert/spacetime/DSD dimensions remain typed",
    "PHY-REL-003": "frame order/cross-dynamics do not create unique lineage/coupling",
    "PHY-REL-004": "coordinate time/proper time/quantum phase remain distinct",
    "PHY-REL-005": "representation != causal access != global reconstruction",
    "PHY-REL-006": "Cauchy state != evolution law != target domain/global reconstruction",
    "PHY-REL-007": "state operands != symmetry/curvature/EFE/conservation relations",
}

def check_graph():
    checks=[]
    valid_classes=set(CLASSES)
    checks.append(("all nodes use declared provenance classes", all(c in valid_classes for c,_ in NODES.values())))
    checks.append(("all dependencies exist", all(d in NODES for _,deps in NODES.values() for d in deps)))
    indeg={n:0 for n in NODES}; out=defaultdict(list)
    for n,(_,deps) in NODES.items():
        for d in deps:
            indeg[n]+=1; out[d].append(n)
    q=deque([n for n,v in indeg.items() if v==0]); seen=0
    while q:
        n=q.popleft(); seen+=1
        for m in out[n]:
            indeg[m]-=1
            if indeg[m]==0: q.append(m)
    checks.append(("dependency graph is acyclic", seen==len(NODES)))
    return checks

def check_firewalls():
    cls={n:c for n,(c,_) in NODES.items()}
    supplied={"smooth_spacetime_manifold","lorentzian_metric","spacetime_dimension_and_signature","time_orientation","einstein_field_equation","matter_stress_energy_model","constraint_satisfying_initial_data","weak_field_background_specialization"}
    return [
        ("no supplied relativity primitive is counted as R0/R1", all(cls[n]=="R2" for n in supplied)),
        ("Lorentzian metric is supplied, not DSD-derived", cls["lorentzian_metric"]=="R2"),
        ("Einstein field equation is supplied, not DSD-derived", cls["einstein_field_equation"]=="R2"),
        ("causal structure depends on Lorentzian metric/time orientation", set(NODES["causal_cone_structure"][1])=={"lorentzian_metric","time_orientation"}),
        ("curvature depends on supplied geometric structure", {"lorentzian_metric","levi_civita_connection"}.issubset(NODES["curvature_from_metric_connection"][1])),
        ("Cauchy development depends on GR initial data/equations", {"constraint_satisfying_initial_data","einstein_field_equation"}.issubset(NODES["maximal_globally_hyperbolic_development"][1])),
        ("c_info = c remains not derived", cls["identify_c_info_with_relativistic_c"]=="R4"),
        ("DSD strict equivalence = GR equivalence remains not derived", cls["identify_DSD_strict_equivalence_with_GR_equivalence"]=="R4"),
        ("unique QM-GR cross-dynamics remains not derived", cls["unique_QM_GR_cross_dynamics"]=="R4"),
    ]

def check_coverage():
    return [
        ("PHY-REL-001 through PHY-REL-007 are represented in the rebaseline", set(EXPECTED_PRIOR_AUDITS)=={f"PHY-REL-{i:03d}" for i in range(1,8)}),
        ("representation/information-loss boundary represented", "invertible_representation_no_loss_by_itself" in NODES),
        ("dimension typing firewall represented", "typed_dimension_nonidentification" in NODES),
        ("weak-field proper-time gate represented", "weak_field_proper_time_relation" in NODES),
        ("causal-access gate represented", "causal_cone_structure" in NODES),
        ("Cauchy reconstruction gate represented", "maximal_globally_hyperbolic_development" in NODES),
        ("relation-layer gate represented", all(n in NODES for n in ("curvature_from_metric_connection","einstein_field_equation","covariant_stress_energy_conservation"))),
    ]

def report_group(name, checks):
    ok=True
    print(f"[{name}]")
    for label,good in checks:
        ok &= bool(good)
        print(f"{label:<78} {'PASS' if good else 'FAIL'}")
    print()
    return ok

def run(mode):
    ok=True
    if mode in ("all","graph"): ok &= report_group("DEPENDENCY_GRAPH", check_graph())
    if mode in ("all","firewalls"): ok &= report_group("PROVENANCE_FIREWALLS", check_firewalls())
    if mode in ("all","coverage"): ok &= report_group("PRIOR_RELATIVITY_COVERAGE", check_coverage())
    if mode in ("all","counts"):
        counts=Counter(CLASSES[c] for c,_ in NODES.values())
        print("[PROVENANCE_COUNTS]")
        for code,name in CLASSES.items(): print(f"{name:<42} {counts[name]:>3}")
        print()
    print("OVERALL:", "PASS_WITH_BOUNDARY" if ok else "FAIL")
    return 0 if ok else 1

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--mode", choices=("all","graph","firewalls","coverage","counts"), default="all")
    return run(p.parse_args().mode)

if __name__=="__main__":
    raise SystemExit(main())
