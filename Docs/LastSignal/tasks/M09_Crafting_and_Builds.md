# M09 Crafting and Builds

Status: Not started | Owner: Claude | Dependencies: M01, M06

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/02_Technical_Design.md`
- `../docs/04_First_Three_Bases_and_Vehicles.md`

## Deliver

Recipe service; part inventory; compatibility checks; stat preview; install command.

## Implementation sequence

1. Implement ingredient validation and a single craft transaction.
2. Evaluate stock plus installed modifiers from defaults with clamps.
3. Implement install/remove with expected revision and unique part ownership.
4. Expose comparison data and refund/cancel outcomes to the UI.

## Acceptance evidence

Double confirm cannot double-charge or duplicate. Incompatible wheels are rejected. Old part returns to inventory exactly once. Save/load does not stack stat bonuses.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No physical animation or real-money purchase flow.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
