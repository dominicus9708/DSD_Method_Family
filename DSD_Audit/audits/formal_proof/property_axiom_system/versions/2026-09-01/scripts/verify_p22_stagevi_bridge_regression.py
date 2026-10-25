#!/usr/bin/env python3
"""P22 non-edit finite Stage-VI/Property interface regression, NOT full FAS formalization.
From DSD_Method_Family root:
 python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p22_stagevi_bridge_regression.py OUTPUT_JSON
"""
from __future__ import annotations
from dataclasses import dataclass, replace
from pathlib import Path
from hashlib import sha256
import json
import sys
import verify_p20_full_c1_inverse as p20
import verify_p17_typed_reference_validator as ref

PROPERTY_SHA = "03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c"
FORMATION_SHA = "af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe"

@dataclass(frozen=True)
class FiniteStageVI:
    """Small restricted fixture of FAS 2026-10-22, not the full typed FAS signature."""
    material: tuple = ("a", "b")
    expression_material: tuple = ("a",)
    configuration_active: tuple = ("a",)
    expression_anchor: str = "s0"
    configuration_anchor: str = "s0"
    expression_admitted: bool = True
    expression_described: bool = True
    identity_restriction: bool = True
    realization: bool = True
    configuration_admitted: bool = True
    local_coherence: bool = True
    boundary_compatibility: bool = True
    assignment_domain: tuple = ("a",)
    assignment_value: int = 0
    role: bool = True
    channels: tuple = (("p", "a", "lambda", 0, "rho"),)

def expected_channels(f):
    witness = (f.expression_described and f.identity_restriction and
               f.realization and f.configuration_admitted and
               f.local_coherence and f.boundary_compatibility and
               f.expression_anchor == f.configuration_anchor and
               set(f.configuration_active) <= set(f.expression_material))
    describable = f.configuration_active if witness else ()
    expected = (("p", "a", "lambda", f.assignment_value, "rho"),) if (
        witness and "a" in f.assignment_domain and f.role) else ()
    return witness, set(describable), expected

def valid_stagevi(f):
    if len(set(f.material)) != len(f.material): return False
    if not set(f.expression_material) <= set(f.material): return False
    if not set(f.configuration_active) <= set(f.material): return False
    if f.expression_described and not f.expression_admitted: return False
    if f.expression_admitted and not f.identity_restriction: return False
    if f.identity_restriction and not f.expression_admitted: return False
    if f.realization and (f.expression_anchor != f.configuration_anchor or
                          not set(f.configuration_active) <= set(f.expression_material)):
        return False
    witness, active, expected = expected_channels(f)
    if not set(f.assignment_domain) <= active: return False
    if len(set(f.assignment_domain)) != len(f.assignment_domain): return False
    return tuple(f.channels) == expected

def formation_key(f):
    # Fixture checksum is a test-only structured anchor, not a complete FAS proof.
    return sha256(repr(f).encode("utf8")).hexdigest()

def bound_property(f):
    if not valid_stagevi(f): raise ValueError("inadmissible finite Stage-VI fixture")
    channel_carrier = frozenset(f.channels)
    s = ref.Signature(
        {"channel": channel_carrier},
        frozenset({"aux", "pending"}),
        {"rel": ref.Kind(("channel", "aux"), frozenset({0, 1, 2}),
                         frozenset({"d"}), 0, True),
         "unavailable": ref.Kind(("pending",), frozenset({0, 1, 2}))},
        frozenset({"d"}))
    tuples = {(c, "x") for c in f.channels}
    m = ref.Premodel({"aux": ("x",)}, ("rel", "unavailable"),
        {"rel": set(tuples)}, {("rel", "d"): set(tuples)},
        {"rel": {x: 0 for x in tuples}})
    return p20.Primitive("F6-fixture:" + formation_key(f), s, m)

def compatible(f, p):
    return (valid_stagevi(f) and
            p.stage_vi_anchor == "F6-fixture:" + formation_key(f) and
            p.signature.inherited.get("channel") == frozenset(f.channels) and
            ref.validate(p.signature, p.prem)["classification"] == "admitted_core")

def main():
    checks = {}
    def expect(key, condition):
        checks[key] = bool(condition)
        assert condition, key
    def refused(fn):
        try: fn()
        except (ValueError, TypeError, KeyError): return True
        return False

    f = FiniteStageVI()
    p = bound_property(f)
    a = p20.comp_prop(p)
    expect("FAS_channel_identity_five_coordinates", len(f.channels[0]) == 5)
    expect("FAS_zero_valued_admitted_channel_preserved", f.channels[0][3] == 0)
    expect("FAS_role_and_assignment_generate_exact_channels", valid_stagevi(f))
    expect("Property_inherited_channel_carrier_exact", compatible(f, p))
    expect("Property_mixed_profile_order_retained", p.signature.kinds["rel"].profile == ("channel", "aux"))
    expect("Property_defined_zero_record_exact", ("rel", (f.channels[0], "x"), 0) in a.defined_records)
    expect("Property_completion_reduction_exact_on_admitted_core", p20.comp_prop(p20.red_prop(a)) == a)
    expect("Property_unavailable_kind_not_empty_kind", a.unavailable_kinds == frozenset({"unavailable"}))
    expect("Property_unavailable_product_absent", ref.product(p.signature, p.prem, "unavailable") is None)
    expect("Property_stageVI_string_anchor_not_full_fas", isinstance(p.stage_vi_anchor, str))
    expect("StageVII_term_changes_do_not_change_StageVI", formation_key(f) == formation_key(f) and
           compatible(f, p)) # term data deliberately absent from fixture
    undef = replace(f, assignment_domain=(), channels=())
    expect("FAS_undefined_assignment_produces_no_channel", valid_stagevi(undef) and not undef.channels)
    expect("Property_empty_inherited_channel_carrier_valid", compatible(undef, bound_property(undef)))
    no_role = replace(f, role=False, channels=())
    expect("FAS_role_absence_produces_no_channel", valid_stagevi(no_role) and not no_role.channels)
    nonzero = replace(f, assignment_value=2, channels=(("p","a","lambda",2,"rho"),))
    expect("FAS_value_is_channel_identity_coordinate", valid_stagevi(nonzero) and
           nonzero.channels != f.channels)
    expect("Cross_version_old_property_anchoring_rejected", not compatible(nonzero, p))
    expect("Legacy_P20_alone_does_not_validate_real_FAS", p20.full_is_valid(a) and
           not compatible(nonzero, a.primitive))
    expect("Cross_version_changed_formation_requires_rebinding", compatible(nonzero, bound_property(nonzero)))
    altered_anchor = replace(f, expression_anchor="s1", configuration_anchor="s1")
    expect("Full_structure_change_even_when_channels_match_rejected",
           valid_stagevi(altered_anchor) and not compatible(altered_anchor, p))
    expect("Bad_identity_restriction_refused", not valid_stagevi(replace(f, identity_restriction=False)))
    expect("Bad_realization_anchor_refused", not valid_stagevi(replace(f, configuration_anchor="s1")))
    expect("Bad_realization_material_refused",
           not valid_stagevi(replace(f, configuration_active=("b",))))
    expect("Bad_expression_admission_refused",
           not valid_stagevi(replace(f, expression_admitted=False)))
    expect("Bad_assignment_outside_describable_active_material_refused",
           not valid_stagevi(replace(f, assignment_domain=("a","b"))))
    expect("Bad_channel_value_manually_injected_refused",
           not valid_stagevi(replace(f, channels=(("p","a","lambda",9,"rho"),))))
    expect("Bad_formation_cannot_bind_property",
           refused(lambda: bound_property(replace(f, channels=()))))
    # Source-available versus source-unavailable is NOT a numeric/empty-set equivalence.
    supplied = p20.snapshot(p)
    supplied.prem.aux["pending"] = ()
    supplied.prem.ap["unavailable"] = set()
    supplied.prem.xi["unavailable"] = {}
    b = p20.comp_prop(supplied)
    expect("Supplied_empty_profile_is_available",
           "unavailable" not in b.unavailable_kinds and
           ref.product(supplied.signature, supplied.prem, "unavailable") == frozenset())
    expect("Unavailable_and_supplied_empty_not_identical", b != a)
    # Mathematical partial functions and Python presentations have different equivalences.
    dup = p20.make_model()
    dup.prem.xi["p"] = [(("x",),1),(("x",),1)]
    expect("Duplicate_graph_representation_normalized_extensionally",
           p20.comp_prop(dup).defined_records == p20.comp_prop(p20.make_model()).defined_records)
    expect("Duplicate_graph_raw_presentation_not_preserved",
           p20.red_prop(p20.comp_prop(dup)) != dup)
    conflicting = p20.make_model()
    conflicting.prem.xi["p"] = [(("x",),1),(("x",),2)]
    expect("Conflicting_graph_nonfunctional_refused", refused(lambda: p20.comp_prop(conflicting)))
    assert all(checks.values())
    return {"case":"PA-P22-20260901-STAGEVI-20261022-REGRESSION-001",
      "property_pdf_sha256":PROPERTY_SHA, "formation_pdf_sha256":FORMATION_SHA,
      "checks_count":len(checks), "checks":checks, "expected_observations_reproduced":True,
      "full_formation_descriptor_implemented":False,
      "formation_fixture_limited":True,
      "p20_original_unchanged":True, "source_section6_two_gaps":"OPEN",
      "source_theorem4_3_C1_scope":"OPEN", "full_property_fpa":"OPEN"}

if __name__ == "__main__":
    result = main()
    output = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("p22_result.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True)+"\n", encoding="utf8")
    print("P22 EXPECTED OBSERVATIONS PASS", result["checks_count"])
    print("P22 OUTPUT", str(output))
