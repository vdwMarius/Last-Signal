# M16 PCG and Long Drives

Status: Not started | Owner: Claude | Dependencies: M15

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/02_Technical_Design.md`
- `../docs/07_Test_Performance_and_Release.md`

## Deliver

Budgeted decorative generation; origin strategy; seed validator; long-drive report.

## Implementation sequence

1. Add PCG only outside gameplay reservations and compare against prebaked variants.
2. Profile generation scheduling, instancing and cleanup in packaged builds.
3. Implement tested local-coordinate rebasing at safe streaming boundaries.
4. Run seeded geometry validation, 60-minute soak and accelerated 1000 km coordinates.

## Acceptance evidence

No accumulating actors, lost attachments, visual jumps or collision discontinuities after rebase. Seed tests preserve guaranteed corridors. Runtime PCG is retained only if it meets the measured budget.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No experimental worldbuilding feature required for core progression.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
