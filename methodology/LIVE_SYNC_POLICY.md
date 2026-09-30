# DSD Method Family — Live Cross-Surface Synchronization Policy

Effective: **2026-09-30 KST**  
Sync epoch at adoption: `MF-SYNC-20260930-DIAG-CH005`

## Purpose

GitHub and Notion are maintained as two canonical surfaces with different roles, but their **current state, active front, latest completed evidence, next canonical step, and synchronization metadata must not intentionally drift**.

This policy applies to the DSD Method Family as a whole and to every independent method.

## Mandatory same-work-unit synchronization

Whenever a state-changing DSD Method Family action is completed, the same work unit / conversation turn must update both canonical surfaces before the action is reported as fully synchronized.

A state-changing action includes, at minimum:

- protocol creation, freeze, revision, or supersession;
- precommit, challenge, evidence, audit, reproducibility, or retrace result;
- method status or maturity change;
- active-front or next-step change;
- boundary/amendment/shared-core decision;
- evidence-scope or case-origin reclassification that changes the current registry;
- correction of claim-relevant counters, status, provenance, or current-state metadata.

Required order:

1. Preserve the immutable GitHub artifact(s) and result provenance.
2. Update the method-specific GitHub README/worklog/registry as required.
3. Update `methodology/CURRENT_SYNC_STATE.md`.
4. Update the corresponding Notion method/worklog page and the Notion current-sync page.
5. Verify that both surfaces agree on the current state and next canonical step.
6. Only then report the state as synchronized.

## Canonical roles

- **GitHub**: executable protocols, immutable/precommitted artifacts, evidence, audits, reproducibility/retrace records, repository-level canonical file state.
- **Notion**: readable canonical planning/status/roadmaps, method pages, research-note organization, cross-links, and human-facing current summaries.
- **Project chat**: working reasoning, interpretation, sequencing decisions, and temporary discussion context.
- **Published DSD papers**: foundational Formation / Property / Static Aggregation / Dynamics interfaces.

No surface silently rewrites another surface's historical record.

## Latest-record rule

When records disagree, identify the **latest claim-relevant record by explicit time/version/commit provenance** and reconcile the other current-state surfaces to it.

Historical immutable artifacts are not edited merely to make them cosmetically consistent with a later state.

A later correction record may supersede an earlier current-state summary while leaving the earlier artifact intact.

## Sync state fields

Every current synchronization checkpoint should record, where applicable:

```text
SYNC_EPOCH_ID
SYNC_DATE_KST
LATEST_CLAIM_RELEVANT_SOURCE_COMMIT
LATEST_COMPLETED_METHOD_EVENT
LATEST_METHOD_RESULT_COMMIT
ACTIVE_INTERNAL_BUILD_FRONT
NEXT_CANONICAL_STEP
GITHUB_SYNC_STATUS
NOTION_SYNC_STATUS
SYNC_PENDING_REASON
```

## Failure handling

If one canonical surface cannot be updated:

```text
SYNC_STATUS: SYNC_PENDING
SYNC_PENDING_SURFACE: GitHub | Notion
SYNC_PENDING_REASON: <explicit reason>
```

Do not state that the two surfaces are synchronized until the pending surface is updated and rechecked.

The successful write is preserved; it is not rolled back merely to hide the mismatch.

## No recursive metadata loop

Synchronization-only metadata writes made solely to record the same sync epoch do **not** trigger an infinite new synchronization cycle.

They belong to the same `SYNC_EPOCH_ID` as long as they introduce no new method claim, evidence result, protocol change, status change, or next-step change.

Any substantive change does trigger a new synchronization epoch.

## Historical and evidence discipline

Live synchronization does not weaken existing preservation rules:

- FAIL and NO_GAIN are retained.
- Shared-core support is not retroactively promoted to method-specific validation.
- Internal standardization is not external or independent validation.
- Case origin and evidence applicability remain separate axes.
- Method overlap does not by itself justify merger, absorption, deletion, or superiority claims.
