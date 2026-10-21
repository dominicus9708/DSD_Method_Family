#!/usr/bin/env python3
"""F2 Corollaries 6.6 and 6.7: bounded, source-typed finite checks.

This verifies finite, deliberately degenerate full Formation models. It does not
prove arbitrary-category axioms, replace the written mathematical proof, or
certify the source manuscript externally.

Run from DSD_Method_Family repository root:
  python DSD_Audit/audits/formal_proof/formation_axiom_system/scripts/verify_c66_c67.py
Pass an optional output JSON path as the first CLI argument.
"""
import itertools
import json
import sys
from dataclasses import dataclass
from pathlib import Path

SOURCE_SHA256 = '8856fc426941c0facc8dcf63e35e9a4630ebd0b05e5e25e4165c1e260d26b93a'


@dataclass(frozen=True)
class Model:
    name: str
    material: frozenset
    base: str = 'B_fixed'
    scalar_field: str = 'Q_fixed'
    material_signature: tuple = ()
    expressions: frozenset = frozenset()
    configurations: frozenset = frozenset()
    quantity_kinds: frozenset = frozenset()
    roles: frozenset = frozenset()
    admitted_channels: frozenset = frozenset()
    term_space: frozenset = frozenset({0})


def full_formation_model(m):
    """Check the source's vacuous primitive/closure conditions.

    All expression/configuration/quantity/role sorts and relations are empty.
    The material-record signature is empty, and W={0} is a zero Q-vector space.
    IV yields no describable configuration, V has no assignment maps, VI
    yields no channels, VII assigns the empty family the zero composite.
    """
    assert m.base == 'B_fixed' and m.scalar_field == 'Q_fixed'
    assert m.material_signature == ()
    assert m.expressions == m.configurations == frozenset()
    assert m.quantity_kinds == m.roles == frozenset()
    assert m.admitted_channels == frozenset()
    assert m.term_space == frozenset({0})
    assert sum((), 0) == 0
    return True


@dataclass(frozen=True)
class Map:
    source: Model
    target: Model
    material_pairs: tuple

    def __post_init__(self):
        material_mapping = dict(self.material_pairs)
        assert set(material_mapping) == set(self.source.material)
        assert set(material_mapping.values()) <= set(self.target.material)
        assert len(self.material_pairs) == len(material_mapping)
        assert full_formation_model(self.source)
        assert full_formation_model(self.target)
        # The remaining components are unique maps on empty sorts or {0};
        # F1-F6 thus hold by their explicit empty-source interpretation.

    def of(self, x):
        return dict(self.material_pairs)[x]

    def embedding(self):
        # All R1-R5 and witness reflections are vacuous; material injectivity
        # is the only nonvacuous embedding condition in this fixture family.
        return len(set(dict(self.material_pairs).values())) == len(self.material_pairs)

    def literal_inclusion(self):
        return self.embedding() and all(self.of(x) == x for x in self.source.material)


def forward_maps(a, b):
    domain = tuple(sorted(a.material))
    codomain = tuple(sorted(b.material))
    for y in itertools.product(codomain, repeat=len(domain)):
        yield Map(a, b, tuple(zip(domain, y)))


def identity(a):
    return Map(a, a, tuple((x, x) for x in sorted(a.material)))


def compose(second, first):
    assert first.target == second.source, 'typed composition required'
    return Map(first.source, second.target,
               tuple((x, second.of(first.of(x))) for x in sorted(first.source.material)))


def leq_formation(a, b):
    """A is a genuinely included submodel of B, not merely embeddable."""
    if not a.material <= b.material:
        return False
    return Map(a, b, tuple((x, x) for x in sorted(a.material))).literal_inclusion()


def main():
    models = [Model('A', frozenset({'a'})),
              Model('B', frozenset({'a', 'b'})),
              Model('C', frozenset({'a', 'b', 'c'})),
              Model('D', frozenset({'a', 'b', 'c', 'd'}))]
    A, B, C, D = models
    tested = {'left_right_identity': 0, 'associativity': 0,
              'embedding_composition': 0, 'submodel_reflexivity': 0,
              'submodel_transitivity': 0}

    maps_ab = list(forward_maps(A, B))
    maps_bc = list(forward_maps(B, C))
    maps_cd = list(forward_maps(C, D))
    assert len(maps_ab) == 2 and len(maps_bc) == 9 and len(maps_cd) == 64

    for x in models:
        for y in models:
            for f in forward_maps(x, y):
                assert compose(identity(y), f) == f
                assert compose(f, identity(x)) == f
                tested['left_right_identity'] += 1

    for f in maps_ab:
        for g in maps_bc:
            for h in maps_cd:
                assert compose(h, compose(g, f)) == compose(compose(h, g), f)
                tested['associativity'] += 1
                if f.embedding() and g.embedding() and h.embedding():
                    assert compose(h, compose(g, f)).embedding()
                    tested['embedding_composition'] += 1

    for x in models:
        assert leq_formation(x, x)
        tested['submodel_reflexivity'] += 1
    for x in models:
        for y in models:
            for z in models:
                if leq_formation(x, y) and leq_formation(y, z):
                    assert leq_formation(x, z)
                    tested['submodel_transitivity'] += 1

    # An embedding need not be a literal inclusion submodel.
    X = Model('X', frozenset({'u'}))
    Y = Model('Y', frozenset({'v'}))
    non_inclusion_embedding = Map(X, Y, (('u', 'v'),))
    assert non_inclusion_embedding.embedding()
    assert not non_inclusion_embedding.literal_inclusion()
    assert not leq_formation(X, Y)
    assert not leq_formation(Y, X)

    # Forward maps may fail the additional injectivity requirement.
    noninjective = Map(B, A, (('a', 'a'), ('b', 'a')))
    assert not noninjective.embedding()

    result = {
        'case_id': 'FAS-F2-SEC6.2-C6.6-C6.7-001',
        'source_sha256': SOURCE_SHA256,
        'source_fixed_base_and_field': True,
        'finite_witness_scope': 'empty expression/configuration/quantity/role types; zero term space; set-sized material carriers; mathematical proof is separate',
        'four_full_models_valid_under_vacuous_axioms': True,
        'source_model_material_sizes': [len(x.material) for x in models],
        'tests': tested,
        'large_category_associativity_is_proved_by_mathematical_argument_not_tests': True,
        'wide_subcategory_inclusion_illustrated': True,
        'genuine_inclusion_preorder_checked': True,
        'distinct_isomorphic_models_not_literal_submodels': True,
        'not_every_forward_map_is_an_embedding': True,
        'antisymmetry_not_claimed_or_tested_as_a_corollary_obligation': True,
        'all_checks_passed': True,
        'independent_external_verification': False,
    }
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        Path(__file__).resolve().parent.parent / 'results' / 'c66_c67_category_preorder.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    print('C6.6/C6.7 finite checks: PASS')
    for k, v in tested.items():
        print(f'{k}: {v}')
    print('OUTPUT:', output)


if __name__ == '__main__':
    main()
