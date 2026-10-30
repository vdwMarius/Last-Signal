# M13 Garage Decoration

Status: Not started | Owner: Claude | Dependencies: M06, M09, M12

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/05_Art_UI_and_Asset_Bible.md`

## Deliver

Placement mode; category definitions; per-base layouts; undo/reset.

## Implementation sequence

1. Create six placeholder decorations and valid surface categories.
2. Implement preview, grid/free placement, rotation and collision validation.
3. Apply vehicle, door, stairs and station exclusion volumes.
4. Save local transforms per garage and restore to validated fallback positions.

## Acceptance evidence

Controller can place, move, undo and remove each item. Cannot block the only exit or service position. Reset returns items without duplicate ownership. Layout survives reload.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No structural building, wiring simulation or buffs from furniture.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
