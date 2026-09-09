# DSD Design Direct Evidence / DSD 설계론 직접 증거

Status: **Protocol v0.1 established / maturity: developing / validation in progress**

This lane records evidence that directly tests **DSD Design / DSD 설계론**. Evidence from other DSD methods or shared-core validation does not automatically count as direct Design validation.

A Design maturity audit is an **Audit meta-record** and does not increase the Design direct-pilot count.
Independent-evaluator packet preparation is also infrastructure rather than direct evidence; only an eligible frozen external submission can change the independent-validation ledger.

## Current protocol

- `methods/04_design/PROTOCOL_v0.1.md` — initial executable protocol.

## Case-ID convention

```text
DES-CH-###   constructed Design challenges
DES-APP-###  external or independently generated Design applications
DES-AUD-###  Design-specific audit / maturity records
DES-IEP-###  independent evaluator packet infrastructure
```

Case classes include `positive`, `negative_or_failure`, `boundary`, `no_gain`, `baseline_comparison`, `reproducibility`, `external_application`, and other explicitly declared classes.

## Direct evidence registry

### `DES-CH-001` — positive status-sensitive Design space

```text
ADMISSIBLE_FAMILY: {T1,T2}
PRECOMMITTED_REQUIRED_CHECKS: 11/11 PASS
TERMINAL_DESIGN_STATUS: DESIGN_ADMISSIBLE
DESIGN_PROTOCOL_CONFORMANCE: CONFORMANT
DESIGN_METHOD_GAIN_STATUS: NOT_ASSESSED
```

Preserved `DEFINED_ZERO != APPLICABLE_BUT_UNDEFINED != CHANNEL_ABSENCE` and returned the full admissible family without hidden Optimization.

### `DES-CH-002` — negative terminal-status separation

```text
Case I -> DESIGN_INFEASIBLE
Case U -> DESIGN_UNDERDETERMINED
Case B -> DESIGN_BLOCKED
PRECOMMITTED_REQUIRED_CHECKS: 20/20 PASS
```

Directly prevents non-exhaustive failure-to-find from becoming global infeasibility and confirms `DESIGN_BLOCKED + CONFORMANT` when a required predecessor is missing.

### `DES-CH-003` — first Design/Optimization boundary attempt

```text
PRECOMMITTED_REQUIRED_CHECKS: 20/21
DIRECT_EVIDENCE_RESULT: FAIL_AS_PRECOMMITTED_CHALLENGE
FAILURE_CLASS: CHALLENGE_DESIGN_DEFECT
PROTOCOL_FAILURE_INFERRED: no
```

Candidate differences existed only outside the frozen Design target resolution. The failed challenge was preserved without post-hoc repair.

### `DES-CH-004` — corrected Design/Optimization boundary

```text
Case S -> {C1,C2,C3} / DESIGN_ADMISSIBLE
Case U -> DESIGN_UNDERDETERMINED
PRECOMMITTED_REQUIRED_CHECKS: 23/23 PASS
```

The correction placed `reserve_mode = MODE_A / MODE_B / MODE_C` inside `TARGET_RESOLUTION`; downstream `resource_cost` remained Optimization-only.

### `DES-CH-005` — NO_GAIN baseline equivalence

Baseline: `B0_EXPLICIT_CONSTRAINT_MATRIX`.

```text
B0 == DSD on frozen claim-relevant result
G1-G4: NOT_ESTABLISHED
DESIGN_ADMISSIBLE / CONFORMANT / NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 25/25 PASS
```

Confirms that extra DSD bookkeeping is not method gain by itself.

### `DES-CH-006` — broader strongest-reasonable-baseline comparison

Baseline: `B1_TYPED_ADMISSIBILITY_TABLE`.

```text
Formation + General Property
15 candidates
multi-constraint failure sets
DESIGN_SPACE + UNIQUE_TARGET

Case S:
  B1  -> {A1,A2}
  DSD -> {A1,A2} / DESIGN_ADMISSIBLE

Case U:
  B1  -> NOT_UNIQUE_AT_DECLARED_RESOLUTION
  DSD -> DESIGN_UNDERDETERMINED

G1-G5: NOT_ESTABLISHED
DESIGN_METHOD_GAIN_STATUS: NO_GAIN
PRECOMMITTED_REQUIRED_CHECKS: 54/54 PASS
```

Fills the `baseline_comparison` category at constructed-evidence level. It is not a superiority result; the competent typed baseline matched DSD on all frozen measured dimensions.

### `DES-APP-001` — WCAG 2.2 external-standard application

Files:
- `DES-APP-001_precommit.md` — precommit `4847dbd`.
- `DES-APP-001_wcag22-submit-control-application.md` — result `32a7842`.

External authority: W3C `WCAG 2.2`, Recommendation 2024-12-12, limited to SC 1.4.3, 2.5.3, and 2.5.8.

```text
ADMISSIBLE_FAMILY: {W1,W2,W3}
DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 36/36 PASS
```

Kept source requirement separate from fixture assumptions, did not promote a best-practice note into a hard requirement, did not invent a post-hoc exception, and did not overclaim full WCAG conformance.

### `DES-CH-007` — deterministic retrace of DES-APP-001

Files:
- `DES-CH-007_precommit.md` — immutable artifact manifest and 44 checks frozen before retrace scoring; precommit `d6d9103`.
- `DES-CH-007_retrace-des-app-001.md` — executed retrace; result `d666a41`.

```text
RETRACE_RESULT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 44/44 PASS
REPRODUCIBILITY_LEVEL: deterministic_same_project
```

The retrace reproduced candidate verdicts, rejection bases, `{W1,W2,W3}`, the three Design ledgers, external source/version, and `WCAG_APPLICATION_BRIDGE_001` from frozen artifacts.

It does **not** establish independent reproducibility: the same project/evaluator already knew the historical result and the run was non-blinded.

### `DES-APP-002` — NIST SP 800-63B-4 AAL2 route-form application

Files:
- `DES-APP-002_precommit.md` — source, candidate grammar, 15-form fixture, scope guards, and 38 checks frozen before scoring; precommit `cadc9ae`.
- `DES-APP-002_nist-aal2-route-form-application.md` — executed result; commit `329f2b8`.

External authority: NIST SP 800-63B-4, July 2025, Authentication Assurance Level 2.

The source directly supplies the positive route-form grammar:

```text
MF out-of-band
MF OTP
MF cryptographic authentication

one of:
  look-up secret
  out-of-band device
  SF OTP
  SF cryptographic authentication
plus either:
  password
  biometric comparison
```

The frozen 15-form fixture contains those 11 permitted forms plus four source-grounded controls.

```text
N1-N11 -> admissible
N12 password only -> H1,H2 fail
N13 SF cryptographic only -> H1,H2 fail
N14 biometric alone -> H1,H2 fail; biometric is not a standalone authenticator
N15 password + biometric -> H1 fail / H2 pass

ADMISSIBLE_FAMILY:
{N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11}

DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 38/38 PASS
```

The case preserves the distinction:

```text
TWO_DISTINCT_FACTOR_STRUCTURE
!= NIST_AAL2_PERMITTED_FORM
```

It also keeps the verifier-level requirement to offer at least one phishing-resistant AAL2 option separate from individual route-form admissibility and does not fabricate replay-resistance, cryptography, protected-channel, FIPS, or full deployed-system conformance from form-level records.

This broadens external evidence from web accessibility to digital identity/authentication security and uses a source-supplied positive candidate/construction grammar. The full 15-record evaluation fixture and negative controls remain project-frozen, so independent validation is still absent.

### `DES-APP-003` — 2010 ADA ramp-run physical application

Files:
- `DES-APP-003_precommit.md` — selected ADA §405 source subset, R1-R10 fixture, scope guards, and 38 checks frozen before scoring; precommit `b78ca3a`.
- `DES-APP-003_ada-ramp-run-physical-application.md` — executed result; commit `091b969`.

External authority: U.S. Access Board, 2010 ADA Standards for Accessible Design, selected ramp requirements from §405.

Frozen source checks:

```text
§405.2 running slope 1:12 maximum
§405.3 cross slope 1:48 maximum
§405.5 clear width 36 inches minimum
§405.6 rise 30 inches maximum per run
§405.7 top and bottom landings required
```

Execution:

```text
R1 -> admissible
R2 -> admissible
R3 -> rejected H1
R4 -> rejected H2
R5 -> rejected H3
R6 -> rejected H4
R7 -> rejected H5
R8 -> rejected H1,H2,H3,H4,H5
R9 -> admissible
R10 -> rejected H0; ramp geometry remains INAPPLICABLE

ADMISSIBLE_FAMILY:
{R1,R2,R9}

DESIGN_ADMISSIBLE / CONFORMANT / NOT_ASSESSED
PRECOMMITTED_REQUIRED_CHECKS: 38/38 PASS
```

The case does not promote advisory gentler-slope recommendations into hard constraints, does not import alteration or employee-work-area exceptions after candidate inspection, and does not claim full ADA ramp compliance, structural adequacy, construction safety, or permit approval from the selected subset.

This expands external evidence into a third materially different domain: built environment / physical accessibility. The finite R1-R10 fixture is still project-constructed, so it does not resolve independent-evaluator validation.

## Independent evaluator infrastructure

### `DES-IEP-001` — blinded evaluator packet prepared

Public frozen files:

```text
DES-IEP-001_reviewer-packet.md
  commit 78b1fb45d0b2e40838517828d089942e7b55e7d8

DES-IEP-001_submission-template.md
  commit fe1eedca019b4283a21047d21fcac12dd672e328

DES-IEP-001_reference-commitment.md
  commit 8fe4ff64b3fc964746d7e8c11bd03d712c40fedd
```

Reference-key SHA-256 commitment:

```text
3f2cf7c7787578063096c98ada872f29fffb6fdef27f7893d039e04604a2b0cf
```

The plaintext reference key and nonce are withheld from the reviewer until an eligible submission is frozen.
The packet contains two held-out tasks using WCAG and NIST source rules, 12 candidate records total, three-ledger outputs, and source-scope questions.

Precommitted agreement classes:

```text
INDEPENDENT_AGREEMENT_FULL
  eligible + 24/24 semantic checks

INDEPENDENT_AGREEMENT_PARTIAL
  eligible + >=21/24 + 10/10 critical checks

INDEPENDENT_DISAGREEMENT
  eligible + <21/24 or any critical failure

CONTAMINATED_OR_INELIGIBLE
  independence gate failure
```

Current effect:

```text
INDEPENDENT_EVALUATOR_PACKET: prepared
REFERENCE_KEY_COMMITMENT: frozen
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
DESIGN_DIRECT_PILOT_INCREMENT_FROM_PACKET_PREPARATION: 0
```

This is infrastructure only. It is not counted as Design validation until a genuinely separate evaluator freezes a submission before answer-key reveal.

## Audit meta-record registry

### `DES-AUD-001` — first DSD Design maturity audit

Files:
- `DES-AUD-001_precommit.md` — maturity axes and 24 audit-discipline checks frozen before scoring; precommit `bf4c55c`.
- `DES-AUD-001_maturity-review.md` — completed audit; result `b2316d4`.

Audit ID:

```text
DSD-AUDIT-20260908-DESIGN-001
```

Final audit decision at the time it was executed:

```text
MINIMUM_PROMOTION_COMPONENTS_PRESENT: 8/8
AUDIT_EXECUTION_VERDICT: PASS
PRECOMMITTED_REQUIRED_CHECKS: 24/24 PASS
METHOD_MATURITY_CLASSIFICATION: developing
PROMOTION_TO_ESTABLISHED: INSUFFICIENT_BASIS
PRIMARY_BLOCKER: insufficient external evidence breadth
SECONDARY_BLOCKER: independent/practical evidence not established
PROTOCOL_REVISION_REQUIRED: no
SHARED_CORE_REOPEN_REQUIRED: no
DESIGN_DIRECT_PILOT_INCREMENT_FROM_AUDIT: 0
```

`DES-APP-002`, `DES-APP-003`, and `DES-IEP-001` are post-audit records and do not retroactively rewrite `DES-AUD-001`. Any new maturity decision requires a separate re-audit.

## Minimum evidence architecture

1. dedicated Design protocol — **established at v0.1**;
2. positive case — **DES-CH-001 PASS**;
3. negative/failure case — **DES-CH-002 PASS**;
4. boundary case — **DES-CH-004 PASS after DES-CH-003 failed test design was preserved**;
5. `NO_GAIN` case — **DES-CH-005 PASS**;
6. reproducibility/retrace record — **DES-CH-007 PASS at deterministic same-project level**;
7. external or independently generated applications — **DES-APP-001, DES-APP-002, and DES-APP-003 PASS across three external domains**;
8. strongest-reasonable-baseline comparison — **DES-CH-006 PASS at constructed-evidence level; result NO_GAIN**.

The minimum category architecture is fully populated, but established maturity is not inferred automatically.

## Current status

```text
DEDICATED_PROTOCOL: v0.1 established
DIRECT_CONSTRUCTED_PILOTS: 7
POSITIVE_CASES: 1
NEGATIVE_OR_FAILURE_CASES: 1
BOUNDARY_CASES_UNDER_PROTOCOL: 2 attempted
BOUNDARY_VALIDATION_PASSES: 1
BOUNDARY_TEST_DESIGN_FAILURES: 1
NO_GAIN_CASES: 1
BASELINE_COMPARISON_CASES: 1
BASELINE_COMPARISON_RESULT: NO_GAIN
REPRODUCIBILITY_CASES: 1
DEDICATED_RETRACE_PASSES: 1
REPRODUCIBILITY_LEVEL: deterministic_same_project
EXTERNAL_APPLICATIONS: 3
EXTERNAL_DOMAINS: 3
EXTERNAL_APPLICATION_PASSES: 3
INDEPENDENT_EVALUATOR_PACKET: prepared
INDEPENDENT_EVALUATOR_SUBMISSIONS: 0
INDEPENDENT_EVALUATOR_VALIDATION: not established
METHOD_MATURITY_CLASSIFICATION: developing
CURRENT_METHOD_EVIDENCE_STATUS: validation_in_progress
```

## Immediate next evidence task

The independent evaluator infrastructure is frozen but has not yet generated evidence.
External breadth now spans three materially different domains, so another same-project external application is lower priority than independent validation.

The next task is operational:

1. select a genuinely separate evaluator;
2. distribute only the frozen clean reviewer packet, submission template, and required external source material;
3. record evaluator eligibility and any contamination disclosure;
4. obtain an immutable/timestamped completed submission before answer-key reveal;
5. reveal the escrow nonce/reference key, verify the commitment hash, and score the frozen submission under a new Audit/evidence record.

Do not rewrite `DES-AUD-001`; any maturity reclassification must occur through a new revision audit after materially new evidence is frozen.
