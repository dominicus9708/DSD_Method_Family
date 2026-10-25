# PA-P22-20260901-STAGEVI-20261022-REGRESSION-001 — non-edit audit result

**Audit date:** 2026-10-25 KST. **Author:** Kwon Dominicus.
**Preregistered:** [P22 immutable audit plan](P22_PRIMITIVE_IDENTITY_STAGEVI_INTERFACE_PRECOMMIT.md) before executing this audit.
**Locked Property paper:** 2026.09.01, 23 pp, SHA256 `03a7e5693b73f0332e71a5eb83483e4f3539fc940d5368d5eec1523867e3d79c`.
**Revised Formation paper:** 2026.10.22, 34 pp, SHA256 `af721c4188a853880fcc896b80da494e4caa6000ab0af3131ee64cd0770fddfe`.
The revised Formation PDF is identical to the input archived as FAS F2 N1–N3; this comparison uses the fixed manuscript, **not** proof that a Zenodo new-version publication occurred.

## 1. Source-level regression of predecessor boundary

The Property paper §2.1 explicitly fixes the **Stage-VI channel-complete truncation** of one formation model and excludes post-Stage-VI term space, component-term map and finite Clause-VII aggregation from the property core. A Stage-VI channel retains identity `(p,a,lambda,v,rho)`. This is consistent with revised Formation v4.5 §2.3, Definitional Closure VI and Stage-VII boundary.

Version v4.5's audited source changes occurred at T4.7 residual six-constraint independence, P5.13 **conditional** zero-extension information loss, detailed D2 §7.3 finite material/boundary witness (57 material slots, 9 selected items, six blocked inherited slots), and §8 correction of arbitrary fixed-`J` readout language. None of the four loci changes the declared five-coordinate Stage-VI identity or turns the post-Stage-VI term map into a universal primitive property input. This is a **textual/dependency compatibility finding**, not a complete second proof of all Formation axioms.

- **T4.7:** revision concerns residual independence; no new imported property axiom.
- **P5.13:** absence versus admitted defined-zero remains distinct; zero extension can hide membership only conditionally when both types of candidate coexist. A finite P22 observation checks that possibility; no universal loss is inferred.
- **§7.3 D2:** revised material/anchor/boundary details are valid potential inherited Formation data, but the P22 finite fixture does **not** reproduce the detailed 57/9/6 D2 witness. Earlier independent FAS N2 is the correct evidence for that witness.
- **§8:** fixed arbitrary `J` agreement is not inferred from strict formation equivalence; a property readout or analytic aggregate requires its own explicit bridge and compatibility.
- **Property manuscript:** the September locked paper itself has **not** been edited or re-referenced to the October Formation version. It remains source-interface compatible, **not** proven automatically migrated.

## 2. Independent finite test execution

**[P22 standalone Python](scripts/verify_p22_stagevi_bridge_regression.py)** adds a deliberately small `FiniteStageVI` constructor to test predecessor role/assignment/channel requirements, a typed inherited-`channel` property profile, and a binding guard using a structural fixture digest plus the actual inherited channel carrier. It imports existing P17/P20 reference code; P20's original blob `9fac2c171834f126b9af12d8fedde3e0fbc59b23` is guarded by CI and not modified.

**32/32 expected observations reproduced** on both Python 3.10 and 3.12, including positive and intentionally invalid cases:
- five-coordinate zero-valued **admitted** channel versus absent channel/undefined assignment; role, admission, identity restriction, realization anchors, active material and global assignment-domain checks;
- inherited channel carrier and ordered mixed property profile; defined-zero records; unavailable-profile versus supplied empty product; exact admitted-core C1 reference roundtrip;
- changed formation value changes the inherited channel identity; a changed formation record with the **same** admitted channels also fails the test-only whole-fixture fingerprint guard; rebinding accepts the new finite formation record;
- source P20 by itself still accepts its own valid primitive even when paired externally with a different formation record: this is evidence of a **missing cross-system validator**, not a source-theorem refutation;
- repeated identical partial-function graph pairs preserve extensional values but not the raw Python list presentation; conflicting function entries are refused;
- Stage-VII postprocessing is absent from the Stage-VI input; a change of separately supplied term maps does not itself change the inherited Stage-VI test datum.

**Historical first P22 CI attempt:** [#40184657234](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40184657234) failed at `-W error` py_compile because the Windows usage example inside an ordinary Python docstring contained an invalid escape. It was preserved and the docstring changed to a raw string; this is a code-delivery failure, not a mathematical counterexample.

**Successful P22 baseline:** [#40184707507](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40184707507), both Python versions success, 32 flags true and emitted detailed JSONs equal.
**Archived exact-replay CI:** [#40184801829](https://github.com/dominicus9708/DSD_Method_Family/actions/runs/40184801829), both Python versions success, 32 flags true, and fresh **entire JSON content** equal to [committed detailed result](results/p22_stagevi_regression.json); 30-day artifacts additionally uploaded for both versions.

## 3. Mathematical and implementation boundaries

- **Critical distinction:** `FiniteStageVI` checks a purposely restricted one-expression/one-configuration finite fixture. It is NOT an implementation or proof checker of every original Formation Stage-VI descriptor, all anchor/material/incidence structures, all stages, strict formation isomorphism, or the amended D2 witness.
- The structural fixture digest is only an **audit-local binding guard**. It does not prove unique set-theoretic code of all possible Formation descriptors or a canonical normalization of arbitrary property premodels.
- P20 retains its original **string-only Stage-VI anchor**. A true formation-descriptor-aware typed implementation remains OPEN.
- The two printed Property §6 issues remain OPEN: (a) unavailable source profile quantification in F3–F5/embedding; (b) bijective-embedding shorthand in Theorem 6.8 missing S2/S3 requirements. Property Theorem 4.3 `relative to C1` source-scope issue remains OPEN.
- Independent general source proof, machine formalization of ZFC-size models, full Python malformed-input robustness, EN/KR correspondence, and external scholarly approval have NOT been established by these finite tests.
- All existing author PDF/LaTeX/Zenodo, old P17/P20/P21 scripts, previous witness results and original Formation code remain unchanged.

## 4. Next non-edit audit
[P23 prospective precommit](P23_REAL_STAGEVI_TYPED_DESCRIPTOR_REGRESSION_PRECOMMIT.md) will replace the fixture-only Stage-VI anchor by a typed source-checked finite predecessor descriptor, compare carrier maps and inherited sorts with actual formation closures and formation traces, and preserve source/Python/Zenodo separation. Unless executed with archived evidence, do not claim P23 performed.

```text
P22: COMPLETED / 32 FINITE EXPECTED OBSERVATIONS BOTH PYTHON 3.10 AND 3.12
P22 ARCHIVED FULL JSON REPLAY: PASS / GitHub Actions 40184801829
NEW FORMATION 2026-10-22: SOURCE-LEVEL STAGEVI INTERFACE COMPATIBLE
NEW FORMATION 2026-10-22: FULL DESCRIPTOR CODE VALIDATION NOT YET INTEGRATED
ORIGINAL PROPERTY PAPER REVISED: NO
PROPERTY §6 TWO PRINTED GAPS: OPEN
PROPERTY Th4.3 C1 RELATIVE SCOPE: OPEN
FORMATION v4.5 WHOLE FPA: OPEN
PROPERTY WHOLE FPA: OPEN
P23: PREREGISTERED / NOT EXECUTED
```

**Windows 11 command** from an existing local `DSD_Method_Family` checkout root:

```powershell
python DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\scripts\verify_p22_stagevi_bridge_regression.py DSD_Audit\audits\formal_proof\property_axiom_system\versions\2026-09-01\results\p22_stagevi_regression.json
```
