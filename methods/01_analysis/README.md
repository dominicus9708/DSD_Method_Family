# 01. DSD Analysis / DSD 분석론

Status: **established**

Role: decompose and structurally re-express **one declared target** using only the DSD layers required by the case.

Canonical existing corpus: repository root analysis records, `methodology/`, `challenges/`, and related historical analysis paths.

This directory is a registry wrapper only. Existing analysis files are intentionally not moved or retroactively reclassified.

## Current method-family boundary

Under the 22-method architecture, Analysis supplies the structural decomposition/status-separated representation of a declared target.

When the task's primary operation is one of the following, record that result under the corresponding independent method:

- cross-target structural comparison -> **DSD Comparison**;
- explicit criterion-based class assignment -> **DSD Classification**;
- source/context/interpretive-bridge reading -> **DSD Interpretation**.

Historical DSD Analysis records may contain comparison, classification, or interpretation operations together with analysis. Preserve those records as historical Analysis corpus and apply method-specific tags only when revisiting or creating new records.

Primary checks:
- candidate vs admitted/realized structure;
- undefined vs zero vs absence;
- applicability and prerequisite distinctions;
- direct/partial/encoded/non-correspondence when correspondence is part of the analysis;
- aggregate equality vs structural equality;
- first branching and boundary cases when applicable;
- for multi-step targets, the relation between an already-declared claim and intermediate requirement strength, without assuming one universal scalar resolution order;
- when multiple routes are material, AND-prerequisites, OR-alternative sufficient routes, theorem gates, bridges, attack methods, and plural minimal dependency frontiers;
- when multiple representations are material, established equivalence versus projection, contraction, coarsening, one-way sufficiency, sibling contraction, or shared latent parenthood;
- claim-strength escalation and representation information loss as separate checks when both are material.

DSD Analysis does not replace the external field's original terminology, proof rules, empirical standards, or interpretation practices.

For multi-step analyses, use [`ANALYSIS_OPERATIONAL_CONTROLLER.md`](ANALYSIS_OPERATIONAL_CONTROLLER.md) when the declared target contains material intermediate requirements, multiple sufficient routes, multiple representations, or claim-relevant reductions.

The controller analyzes an already-declared claim; it does not author domain requirements. Primary requirement specification remains DSD Specification or the competent external specification source. Dependency analysis does not decide run scheduling or resource allocation; executable omission/reuse belongs to DSD Computation, deliberate representation reduction to DSD Compression, and live lifecycle/resource orchestration to DSD Operation. When source-to-target mapping itself is the primary task, use DSD Transformation.

See [`../METHOD_BOUNDARY_MATRIX.md`](../METHOD_BOUNDARY_MATRIX.md) for the current non-duplication boundary audit.
