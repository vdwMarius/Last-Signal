# M01 Data and Save

Status: Not started | Owner: Claude | Dependencies: M00

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/02_Technical_Design.md`

## Deliver

Definition types; initial data import; profile subsystem; A/B save storage; schema fixture; ID validator.

## Implementation sequence

1. Implement stable definition IDs, soft references and resource/part instance types.
2. Translate balance_seed.json into validated definitions; reject duplicate IDs and invalid slot tags.
3. Implement profile revisions, A/B save validation and migration entry points.
4. Add transactional reward ledger and fixtures for fresh, old and damaged profiles.

## Acceptance evidence

A newly owned part survives restart. Corrupt newest slot falls back. Replaying a grant creates exactly one item. Missing cosmetic IDs do not prevent loading.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No UI store, cloud save or online services.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
