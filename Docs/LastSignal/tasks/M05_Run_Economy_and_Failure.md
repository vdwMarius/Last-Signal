# M05 Run Economy and Failure

Status: Not started | Owner: Claude | Dependencies: M01, M04

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/02_Technical_Design.md`

## Deliver

Run lifecycle; fuel/cargo; checkpoint settlement; failure recovery; suspend snapshot.

## Implementation sequence

1. Implement AtRefuge to Driving to Resolving transitions.
2. Add fuel consumption, pickup ownership and unbanked resource accounting.
3. Make bank/failure outcomes atomic and idempotent; guarantee free service/departure.
4. Persist a resumable run and consumed pickup IDs; restore at a safe pose.

## Acceptance evidence

A 4 km test run banks once. Failure keeps floor(0.30 x unbanked scrap) and no unbanked common materials. Quest clues survive. Reloading cannot respawn collected fuel for duplication.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No tuned grind or visual results screen beyond functional text.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
