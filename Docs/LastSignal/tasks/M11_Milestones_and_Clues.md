# M11 Milestones and Clues

Status: Not started | Owner: Claude | Dependencies: M05, M07

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/04_First_Three_Bases_and_Vehicles.md`
- `../docs/09_Narrative_Bible_SPOILERS.md`

## Deliver

Checkpoint data; route board; journal; guaranteed clue/reward placement.

## Implementation sequence

1. Implement forward checkpoint reach requirements and permanent launch unlocks.
2. Add once-only rewards and mandatory clue injection outside random loot rolls.
3. Implement journal records with facts separated from commentary.
4. Add map travel between secured refuges and a blocked state for unbanked cargo.

## Acceptance evidence

CP04 unlocks once and survives restart. A missing random encounter cannot hide the clue. Repeated arrivals cannot duplicate a vehicle. Travel cannot bank cargo outside a safe checkpoint.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

Only CP00 and CP04 need final presentation for the slice.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
