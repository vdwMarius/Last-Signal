# M10 Manual Wheel Service

Status: Not started | Owner: Claude | Dependencies: M09

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/02_Technical_Design.md`
- `../docs/05_Art_UI_and_Asset_Bible.md`

## Deliver

Service state machine; jack and wheel props; snap targets; Quick Fit.

## Implementation sequence

1. Implement parked/service/raised/loosened/removed/aligned/secured/lowered presentation states.
2. Reserve the new part; keep logical build unchanged until commit.
3. Add controller focus, carry snap and cancel rollback at each stage.
4. Unlock Quick Fit after one tutorial and call the same install transaction.

## Acceptance evidence

Finish a wheel replacement using only controller. Cancel or reload at every stage preserves both inventory and a valid build. Cannot launch with an incomplete service transaction. Quick Fit produces identical stats.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No per-bolt physics, finger simulation or manual engine rebuild.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
