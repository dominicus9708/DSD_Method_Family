# SPEC-CH-005 Precommit — Reproducibility / Independent Retrace Challenge

Status: **precommitted before retrace scoring**  
Date: 2026-09-06  
Method: **DSD Specification / DSD 명세론**  
Protocol: **DSD Specification Protocol v0.1**

## 1. Purpose

Test whether a frozen specification packet can be retraced to the same Specification-specific requirement atomization and final verdicts under a fixed protocol, without changing the scoring rule after seeing the retrace output.

This challenge distinguishes two ideas:

```text
reproducibility / retraceability
  same locked packet + same protocol -> same operational classification

independent evaluator validation
  a genuinely separate reviewer/model/team reproduces the result
```

The present challenge can test the first and a limited procedural form of the second, but **does not claim a genuinely independent evaluator** because the retrace is performed in the same project session by the same assistant/model family.

## 2. Locked source packet

Benchmark: `RetraceSpecToy-v5`  
Requirement packet: `RT-SPEC-005-v1`

```text
FORMATION_LAYER: used
PROPERTY_CORE: used
STATIC_AGGREGATION_LAYER: inactive unless explicitly required by a case
DYNAMICS_LAYER: inactive unless explicitly required by a case
REALIZED_AXIS_SPECIALIZATION: inactive unless explicitly required by a case
EXTERNAL_DOMAIN: none
```

Carrier vocabulary:

```text
C_src
C_dst
B_sd : C_src -> C_dst
```

Property-status vocabulary includes `defined_zero` and `applicable_but_undefined` as distinct statuses.

## 3. Frozen cases

### R1 — Minimal usable bridged case

```text
ACTIVE context
source carrier: C_src
target carrier: C_dst
cross-carrier transfer: required
bridge: explicit B_sd : C_src -> C_dst
status distinction: defined_zero != applicable_but_undefined
violation rule: supplied
optional Static/Dynamics/axis: not required
```

### R2 — Same-context contradiction

```text
ACTIVE -> gate_state = OPEN
ACTIVE -> gate_state = CLOSED
OPEN and CLOSED are mutually exclusive
```

### R3 — Activation scope omitted

```text
source distinguishes NORMAL and EMERGENCY
requirement: gate_state = OPEN
activation condition: omitted
```

### R4 — Irrelevant Dynamics injection

```text
locked claim uses only status + explicit bridge
no time/order/transition/lineage requirement
DYNAMICS_LAYER: nevertheless required
```

### R5 — Operationally complete non-DSD baseline

```text
baseline already contains requirement IDs, source/version links, typed carriers,
activation, status distinctions, explicit bridge, dependencies, violation rule,
unresolved rule, and retraceable trace links
DSD re-expression changes only terminology/order
```

### R6 — Traceability gain without source-fact invention

```text
all required facts already exist in the source
source location and dependency references are scattered
DSD atomization links existing requirement -> source reference -> dependency explicitly
no new fact is added
```

### R7 — Same-carrier case with no bridge obligation

```text
q(s) remains on C_src
no cross-carrier transfer claim
no bridge supplied
optional Static/Dynamics/axis inactive
```

### R8 — Required bridge omitted

```text
claim requires C_src -> C_dst transfer
no explicit or canonical bridge supplied
```

## 4. Required retrace record

For each case, the retrace must record:

```text
CASE_ID:
TARGET_CARRIER_OR_RELATION:
ACTIVATION_STATUS:
STATUS_DISTINCTIONS_REQUIRED:
DEPENDENCY_CLASS:
BRIDGE_OBLIGATION:
OPTIONAL_LAYER_STATUS:
SOURCE_FACT_INVENTION: yes / no
FINAL_SPEC_STATUS:
DIAGNOSTIC_FAMILY:
MANUAL_JUDGMENT_NOTE:
```

## 5. Locked final-status families

```text
usable
contradictory
underspecified
overconstrained
no_gain
```

Allowed diagnostic families for this packet:

```text
NONE
C1_MUTUALLY_EXCLUSIVE_STATE_REQUIREMENTS
U1_ACTIVATION_SCOPE_UNRESOLVED
O1_OPTIONAL_DYNAMICS_INJECTION
NG1_OPERATIONALLY_EQUIVALENT_BASELINE
G1_TRACEABILITY_GAIN
B1_REQUIRED_BRIDGE_OMITTED
```

## 6. Reference-key commitment

The reference classification was fixed before retrace scoring and committed only as a SHA-256 digest here.

```text
REFERENCE_KEY_SHA256:
42dcc5398d60e26c1d7954cc794a7887fb4b03d28ca5c5aaea532564390cb945
```

The plaintext key must be revealed only in the result record, where its hash is checked against this precommit.

## 7. Two retrace orders

To test order sensitivity procedurally, run the packet in two orders:

```text
TRACE_A_ORDER:
R1 R2 R3 R4 R5 R6 R7 R8

TRACE_B_ORDER:
R6 R2 R8 R1 R7 R3 R5 R4
```

The two traces must use the same protocol and source packet.

## 8. Precommitted scoring

Primary checks:

```text
SOURCE_PACKET_UNCHANGED: yes required
PROTOCOL_VERSION_UNCHANGED: yes required
REFERENCE_KEY_HASH_MATCH: yes required
TRACE_A_FINAL_STATUS_MATCHES: 8/8 required
TRACE_B_FINAL_STATUS_MATCHES: 8/8 required
TRACE_A_B_FINAL_STATUS_AGREEMENT: 8/8 required
TRACE_A_B_DIAGNOSTIC_AGREEMENT: 8/8 required
SOURCE_FACT_INVENTION: 0 required
POST_REVEAL_RULE_CHANGE: no required
```

Secondary atomization check:

```text
For each case, the two traces must agree on whether:
- activation is resolved or unresolved;
- a bridge obligation exists;
- an optional layer is relevant or injected;
- the source is operationally complete for the locked task.
```

## 9. Outcome rule

```text
if all primary checks pass
and secondary operational-boundary classifications agree:
  SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_PASS_WITH_LIMITATIONS
else:
  SPECIFICATION_RETRACE_REPRODUCIBILITY_PILOT_FAIL_OR_PARTIAL
```

## 10. Independence limitation fixed in advance

Even on a perfect score, the strongest allowed claim is:

```text
procedural_retrace_reproducibility: supported on locked constructed packet
order_invariance: supported on locked two-order retrace
independent_evaluator_validation: not established
external_real_world_validation: not established
```

The result must not relabel this same-session retrace as external or blind independent validation.
