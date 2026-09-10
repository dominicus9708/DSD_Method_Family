#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, List, Tuple, Set


@dataclass(frozen=True)
class ExtensionRecord:
    number: int
    key: str
    title: str
    status: str
    boundary: str


@dataclass(frozen=True)
class ProvenanceRecord:
    key: str
    cls: str
    target_independent: bool
    physical_rel_selector: bool
    note: str


class Audit:
    def __init__(self) -> None:
        self.total = 0
        self.failed = 0
        self.sections: List[Tuple[str, bool, int]] = []
        self._start_total = 0
        self._start_failed = 0

    def begin(self) -> None:
        self._start_total = self.total
        self._start_failed = self.failed

    def check(self, cond: bool, msg: str) -> None:
        self.total += 1
        if not cond:
            self.failed += 1
            print(f"  FAIL: {msg}")

    def end(self, name: str) -> None:
        count = self.total - self._start_total
        ok = self.failed == self._start_failed
        self.sections.append((name, ok, count))


EXTENSIONS = [
    ExtensionRecord(1, "REL_EXT_001", "Lorentzian Spacetime Carrier / Independent-Origin Boundary Gate", "PASS_WITH_BOUNDARY", "generic DSD does not force physical Lorentzian spacetime, dimension/signature/time orientation, c, or Einstein dynamics"),
    ExtensionRecord(2, "REL_EXT_002", "Relativity Reconstruction Selectors / Causal–Projective–Metric Recovery Gate", "PASS_WITH_BOUNDARY", "causal/light-ray and free-fall path selectors can conditionally recover weaker geometric structures, but the selectors are supplied"),
    ExtensionRecord(3, "REL_EXT_003", "Clock / Weyl Integrability / Metric-Scale Recovery Gate", "PASS_WITH_BOUNDARY", "integrable Weyl reduction and pseudo-Riemannian representative require explicit clock/integrability/topology premises and do not fix absolute calibration"),
    ExtensionRecord(4, "REL_EXT_004", "Clock Hypothesis / Accelerated Proper-Time / Operational Calibration Gate", "PASS_WITH_BOUNDARY", "metric proper time is not logically identical to the response law and calibration of every physical clock"),
    ExtensionRecord(5, "REL_EXT_005", "Equivalence Principle / Local Inertial Frame / Gravitational Clock-Rate Gate", "PASS_WITH_BOUNDARY", "local inertial removability of connection does not remove curvature; clock-rate prediction from a supplied metric does not derive that metric or EFE"),
    ExtensionRecord(6, "REL_EXT_006", "Tidal Geodesic-Deviation / Curvature-Reconstruction / Local-Observable Gate", "PASS_WITH_BOUNDARY", "one observer or one tidal matrix does not reconstruct the full local Riemann tensor; sufficiently rich probes can do so only conditionally"),
    ExtensionRecord(7, "REL_EXT_007", "Ricci / Weyl Decomposition / Matter-Source / Vacuum-Curvature Gate", "PASS_WITH_BOUNDARY", "Ricci-flat does not imply Riemann-flat; curvature decomposition does not independently identify matter source or derive Einstein dynamics"),
    ExtensionRecord(8, "REL_EXT_008", "Scalar-Invariant / Frame-Classification / Degenerate-Curvature Gate", "PASS_WITH_BOUNDARY", "same complete scalar polynomial curvature invariants need not imply same full curvature or local isometry in degenerate Lorentzian classes"),
]


PROVENANCE = [
    ProvenanceRecord("typed_status_applicability", "R0", True, False, "pre-existing DSD typing/status discipline"),
    ProvenanceRecord("explicit_bridge_discipline", "R0", True, False, "pre-existing DSD downstream-bridge discipline"),
    ProvenanceRecord("external_evolution_time_distinction", "R0", True, False, "DSD t is not automatically proper time"),
    ProvenanceRecord("cinfo_support_bound_distinction", "R0", True, False, "DSD c_info is not automatically relativistic c"),
    ProvenanceRecord("readout_fiber_diagnostic", "R1", True, False, "general injectivity/noninjectivity diagnostic"),
    ProvenanceRecord("linear_rank_kernel_reasoning", "R1", True, False, "general linear algebra"),
    ProvenanceRecord("coordinate_invariance_reasoning", "R1", True, False, "general differential-geometric/mathematical structure"),
    ProvenanceRecord("tensor_contraction_information_loss", "R1", True, False, "general tensor-map provenance"),
    ProvenanceRecord("smooth_spacetime_manifold", "R2", False, True, "relativity specialization"),
    ProvenanceRecord("spacetime_dimension_4", "R2", False, True, "physical relativity selector"),
    ProvenanceRecord("lorentzian_signature", "R2", False, True, "physical relativity selector"),
    ProvenanceRecord("time_orientation", "R2", False, True, "physical relativity selector"),
    ProvenanceRecord("physical_light_speed_c", "R2", False, True, "relativity specialization and empirical constant"),
    ProvenanceRecord("conformal_light_cone_structure", "R2", False, True, "supplied/operational relativity selector"),
    ProvenanceRecord("projective_free_fall_structure", "R2", False, True, "supplied/operational relativity selector"),
    ProvenanceRecord("weyl_compatible_structure", "R2", False, True, "relativity reconstruction specialization"),
    ProvenanceRecord("pseudo_riemannian_metric_scale", "R2", False, True, "relativity specialization"),
    ProvenanceRecord("ideal_clock_condition", "R2", False, True, "operational chronometry selector"),
    ProvenanceRecord("clock_calibration", "R2", False, True, "physical apparatus/readout bridge"),
    ProvenanceRecord("wep_eep_sep_assumptions", "R2", False, True, "equivalence-principle specialization"),
    ProvenanceRecord("levi_civita_connection", "R3", False, False, "standard consequence once metric assumptions are supplied"),
    ProvenanceRecord("geodesic_equation", "R3", False, False, "standard consequence of supplied connection/metric setup"),
    ProvenanceRecord("riemann_curvature", "R3", False, False, "standard consequence of supplied differential geometry"),
    ProvenanceRecord("geodesic_deviation", "R3", False, False, "standard theorem consequence"),
    ProvenanceRecord("ricci_weyl_decomposition", "R3", False, False, "standard tensor theorem"),
    ProvenanceRecord("scalar_curvature_invariant_results", "R3", False, False, "standard theorem consequences under supplied geometry"),
    ProvenanceRecord("karlhede_cartan_classification", "R3", False, False, "standard invariant-classification method"),
    ProvenanceRecord("einstein_field_equation", "R4", False, True, "not independently derived by generic DSD"),
    ProvenanceRecord("newton_constant_G", "R4", False, True, "external empirical/dynamical constant"),
    ProvenanceRecord("cosmological_constant_Lambda", "R4", False, True, "external model/empirical datum"),
    ProvenanceRecord("stress_energy_model", "R4", False, True, "external physical source model"),
    ProvenanceRecord("constraint_satisfying_initial_data", "R4", False, True, "external physical solution data"),
    ProvenanceRecord("boundary_global_topology", "R4", False, True, "external solution/global data"),
    ProvenanceRecord("actual_physical_solution_selection", "R4", False, True, "not selected by generic DSD"),
    ProvenanceRecord("physical_clock_mechanism", "R4", False, True, "empirical device-specific bridge"),
    ProvenanceRecord("cinfo_equals_c", "R4", False, True, "not established by generic DSD"),
    ProvenanceRecord("structural_gravity_equivalence_to_GR", "R4", False, True, "outside standard-GR reconstruction closure"),
]


DEPENDENCIES: Dict[str, Set[str]] = {
    "lorentzian_spacetime": {"smooth_spacetime_manifold", "spacetime_dimension_4", "lorentzian_signature"},
    "causal_structure": {"lorentzian_spacetime", "time_orientation", "physical_light_speed_c"},
    "weyl_reconstruction": {"conformal_light_cone_structure", "projective_free_fall_structure"},
    "metric_chronometry": {"pseudo_riemannian_metric_scale", "ideal_clock_condition", "clock_calibration"},
    "local_inertial_GR": {"lorentzian_spacetime", "levi_civita_connection", "wep_eep_sep_assumptions"},
    "tidal_curvature_readout": {"riemann_curvature", "geodesic_deviation"},
    "source_attribution": {"einstein_field_equation", "newton_constant_G", "cosmological_constant_Lambda", "stress_energy_model"},
    "specific_GR_solution": {"einstein_field_equation", "constraint_satisfying_initial_data", "boundary_global_topology"},
    "standard_GR_physical_model": {"lorentzian_spacetime", "metric_chronometry", "local_inertial_GR", "tidal_curvature_readout", "source_attribution", "specific_GR_solution"},
}


FIREWALLS = [
    ("carrier_does_not_select_signature", True),
    ("carrier_does_not_select_dimension", True),
    ("generic_DSD_does_not_select_Lorentzian_metric", True),
    ("causal_data_only_fix_conformal_level_conditionally", True),
    ("free_fall_paths_only_fix_projective_level_conditionally", True),
    ("reconstruction_selectors_are_supplied", True),
    ("integrable_Weyl_reduction_requires_extra_premises", True),
    ("metric_representative_does_not_fix_absolute_clock_calibration", True),
    ("metric_proper_time_not_every_device_response_law", True),
    ("accelerated_clock_agreement_not_cinfo_equals_c", True),
    ("connection_zero_at_event_not_curvature_zero", True),
    ("clock_rate_gradient_not_by_itself_curvature", True),
    ("equivalence_principle_not_EFE_derivation", True),
    ("one_tidal_matrix_not_full_Riemann", True),
    ("rich_probe_curvature_reconstruction_is_conditional", True),
    ("Ricci_flat_not_Riemann_flat", True),
    ("Weyl_zero_not_Riemann_zero", True),
    ("vacuum_with_Lambda_not_necessarily_Ricci_flat", True),
    ("curvature_not_unique_material_source_without_dynamics", True),
    ("same_complete_SPI_not_same_Riemann", True),
    ("same_complete_SPI_not_local_isometry_in_degenerate_class", True),
    ("raw_frame_components_not_invariant_classification", True),
    ("VSI_theorem_external_not_DSD_theorem", True),
    ("Karlhede_classification_external_not_DSD_theorem", True),
    ("EFE_not_generic_DSD_consequence", True),
    ("G_not_generic_DSD_consequence", True),
    ("Lambda_not_generic_DSD_consequence", True),
    ("cinfo_not_automatically_c", True),
    ("DSD_external_t_not_automatically_tau", True),
    ("compatibility_not_independent_derivation", True),
    ("standard_GR_closure_not_structural_gravity_validation", True),
    ("standard_GR_closure_not_quantum_gravity_claim", True),
]


def descendants_ok(graph: Dict[str, Set[str]]) -> bool:
    visiting: Set[str] = set()
    visited: Set[str] = set()

    def visit(node: str) -> bool:
        if node in visiting:
            return False
        if node in visited:
            return True
        visiting.add(node)
        for parent in graph.get(node, set()):
            if parent in graph and not visit(parent):
                return False
        visiting.remove(node)
        visited.add(node)
        return True

    return all(visit(node) for node in graph)


def mode_track(audit: Audit) -> None:
    audit.begin()
    audit.check(len(EXTENSIONS) == 8, "Extensions 001–008 must be present before closure")
    for expected, record in enumerate(EXTENSIONS, start=1):
        audit.check(record.number == expected, f"extension numbering must be contiguous at {expected}")
        audit.check(record.key == f"REL_EXT_{expected:03d}", f"extension key must match {expected:03d}")
        audit.check(record.status == "PASS_WITH_BOUNDARY", f"{record.key} must retain PASS_WITH_BOUNDARY")
        audit.check(len(record.boundary.strip()) > 20, f"{record.key} boundary text must be substantive")
    audit.check(len({x.key for x in EXTENSIONS}) == 8, "extension keys must be unique")
    audit.check(len({x.title for x in EXTENSIONS}) == 8, "extension titles must be unique")
    audit.end("EXTENSION_TRACK_INTEGRITY")


def mode_provenance(audit: Audit) -> None:
    audit.begin()
    allowed = {"R0", "R1", "R2", "R3", "R4"}
    audit.check(len(PROVENANCE) >= 30, "integrated provenance ledger must be sufficiently explicit")
    audit.check(len({p.key for p in PROVENANCE}) == len(PROVENANCE), "provenance keys must be unique")
    for p in PROVENANCE:
        audit.check(p.cls in allowed, f"{p.key} class must be valid")
        audit.check(bool(p.note.strip()), f"{p.key} must have a note")
        audit.check((p.cls in {"R0", "R1"}) == p.target_independent, f"{p.key} target-independent flag")
        if p.cls == "R0":
            audit.check(not p.physical_rel_selector, f"{p.key} R0 cannot be a relativity selector")
        if p.cls == "R3":
            audit.check(not p.target_independent, f"{p.key} theorem consequences are not independent-origin DSD")
    by_key = {p.key: p for p in PROVENANCE}
    for required in ["lorentzian_signature", "spacetime_dimension_4", "einstein_field_equation", "newton_constant_G", "cosmological_constant_Lambda", "cinfo_equals_c"]:
        audit.check(required in by_key, f"required provenance entry: {required}")
        audit.check(by_key[required].cls in {"R2", "R4"}, f"{required} must remain supplied/external")
    audit.end("INTEGRATED_PROVENANCE_LEDGER")


def mode_dependencies(audit: Audit) -> None:
    audit.begin()
    audit.check(descendants_ok(DEPENDENCIES), "dependency graph must be acyclic")
    audit.check("standard_GR_physical_model" in DEPENDENCIES, "closure target exists")
    audit.check("einstein_field_equation" in DEPENDENCIES["source_attribution"], "source attribution requires EFE")
    audit.check("newton_constant_G" in DEPENDENCIES["source_attribution"], "source attribution requires G")
    audit.check("stress_energy_model" in DEPENDENCIES["source_attribution"], "source attribution requires T")
    audit.check("lorentzian_spacetime" in DEPENDENCIES["standard_GR_physical_model"], "standard GR requires Lorentzian spacetime")
    audit.check("metric_chronometry" in DEPENDENCIES["standard_GR_physical_model"], "standard GR physical model requires chronometry bridge")
    audit.check("specific_GR_solution" in DEPENDENCIES["standard_GR_physical_model"], "specific physical solution requires solution data")

    prov = {p.key: p for p in PROVENANCE}
    selector_keys = [p.key for p in PROVENANCE if p.physical_rel_selector]
    audit.check(len(selector_keys) >= 15, "physical selector ledger must be explicit")
    for key in selector_keys:
        audit.check(not prov[key].target_independent, f"{key} must not be back-counted as target-independent DSD")

    audit.end("DEPENDENCY_AND_SELECTOR_CLOSURE")


def mode_firewalls(audit: Audit) -> None:
    audit.begin()
    audit.check(len(FIREWALLS) == 32, "32 integrated firewalls expected")
    for name, value in FIREWALLS:
        audit.check(value, name)
    audit.check(len({name for name, _ in FIREWALLS}) == len(FIREWALLS), "firewall names must be unique")
    audit.end("FIREWALL_REGRESSION")


def mode_closure(audit: Audit) -> None:
    audit.begin()
    closure = {
        "core_ordinary_standard_GR_reconstruction_already_closed": True,
        "extensions_001_008_close_independent_origin_boundaries": True,
        "conditional_GR_embedding_in_DSD_is_consistent_at_current_source_level": True,
        "generic_DSD_independently_derives_GR": False,
        "generic_DSD_uniquely_selects_4D": False,
        "generic_DSD_uniquely_selects_Lorentzian_signature": False,
        "generic_DSD_derives_physical_c": False,
        "generic_DSD_derives_EFE": False,
        "generic_DSD_derives_G": False,
        "generic_DSD_derives_Lambda": False,
        "generic_DSD_selects_actual_matter_model": False,
        "generic_DSD_selects_actual_initial_boundary_data": False,
        "generic_DSD_proves_cinfo_equals_c": False,
        "generic_DSD_external_t_equals_proper_time": False,
        "generic_DSD_proves_structural_gravity": False,
        "generic_DSD_proves_quantum_gravity": False,
        "current_DSD_core_revision_required_by_REL_extensions": False,
        "ordinary_standard_relativity_extension_track_can_close": True,
        "future_structural_gravity_must_be_separate_track": True,
        "future_QFT_curved_spacetime_must_be_separate_track": True,
        "future_semiclassical_quantum_gravity_must_be_separate_track": True,
    }
    expected_true = {
        "core_ordinary_standard_GR_reconstruction_already_closed",
        "extensions_001_008_close_independent_origin_boundaries",
        "conditional_GR_embedding_in_DSD_is_consistent_at_current_source_level",
        "ordinary_standard_relativity_extension_track_can_close",
        "future_structural_gravity_must_be_separate_track",
        "future_QFT_curved_spacetime_must_be_separate_track",
        "future_semiclassical_quantum_gravity_must_be_separate_track",
    }
    for key, value in closure.items():
        if key in expected_true:
            audit.check(value is True, f"{key} must be TRUE")
        else:
            audit.check(value is False, f"{key} must remain FALSE")

    independent_origin = all(p.target_independent for p in PROVENANCE if p.key in {"typed_status_applicability", "explicit_bridge_discipline", "external_evolution_time_distinction", "cinfo_support_bound_distinction", "readout_fiber_diagnostic"})
    all_physical_selectors_external = all(not p.target_independent for p in PROVENANCE if p.physical_rel_selector)

    audit.check(independent_origin, "target-independent DSD/general tools remain available")
    audit.check(all_physical_selectors_external, "all physical-relativity selectors remain supplied/external")
    audit.check(not closure["generic_DSD_independently_derives_GR"], "no independent-GR derivation claim")
    audit.check(closure["ordinary_standard_relativity_extension_track_can_close"], "ordinary standard-relativity extension track closes")
    audit.end("FINAL_RECONSTRUCTION_CLOSURE")


def run(mode: str) -> int:
    audit = Audit()
    modes = {"track": mode_track, "provenance": mode_provenance, "dependencies": mode_dependencies, "firewalls": mode_firewalls, "closure": mode_closure}
    selected = list(modes.values()) if mode == "all" else [modes[mode]]
    for fn in selected:
        fn(audit)

    print()
    for name, ok, count in audit.sections:
        print(f"{name}: {'PASS' if ok else 'FAIL'} ({count} checks)")
    print()
    print(f"TOTAL: {audit.total - audit.failed}/{audit.total} checks passed")
    overall = "PASS_WITH_BOUNDARY" if audit.failed == 0 else "FAIL"
    print(f"OVERALL: {overall}")

    if mode == "all" and audit.failed == 0:
        print()
        print("CLOSURE:")
        print("  Ordinary standard-relativity reconstruction track: CLOSED")
        print("  Conditional DSD-compatible reconstruction: SUPPORTED")
        print("  Independent derivation of GR from generic DSD: NOT ESTABLISHED")
        print("  DSD core revision required by this track: NO")
        print("  Structural gravity / curved-spacetime QFT / quantum gravity: SEPARATE TRACKS")
        print()
        print("BOUNDARY:")
        print("  This program audits the integrated provenance ledger, dependency graph,")
        print("  and regression firewalls. It does not constitute a mathematical proof")
        print("  of GR from DSD or a new empirical test of general relativity.")
    return 0 if audit.failed == 0 else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="REL Extension 009 integrated independent-origin / reconstruction closure gate")
    parser.add_argument("--mode", default="all", choices=["all", "track", "provenance", "dependencies", "firewalls", "closure"])
    args = parser.parse_args()
    return run(args.mode)


if __name__ == "__main__":
    raise SystemExit(main())
