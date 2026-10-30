# M07 Road Streaming

Status: Not started | Owner: Claude | Dependencies: M03, M05

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/02_Technical_Design.md`
- `../docs/07_Test_Performance_and_Release.md`

## Deliver

Chunk definitions; connector validator; bounded chunk manager; deterministic layout log.

## Implementation sequence

1. Create at least six greybox straight/bend/choke/junction chunks.
2. Implement monotonic route distance and seeded selection with separate random streams.
3. Preload and validate gameplay collision before admitting the car; recycle behind.
4. Add safe straight fallback, branch rejoin and debug view of chunk states.

## Acceptance evidence

Drive 30 minutes without gaps, missing collision or increasing live chunk count. Same seed/version produces the same chunk IDs. Reversing or circling cannot advance the campaign frontier.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No runtime decorative PCG or huge continuous terrain.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
