# M15 Vertical Slice Gate

Status: Not started | Owner: Claude integration; human playtest | Dependencies: M08, M10, M11, M12, M13, M14

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/03_Implementation_Roadmap.md`
- `../docs/07_Test_Performance_and_Release.md`

## Deliver

Tagged packaged slice; tester observations; defect list; scope decision.

## Implementation sequence

1. Package from a clean checkout with resolved LFS assets.
2. Run full 0-4 km loop, failure recovery, service, decoration and restart.
3. Observe five external testers using only tutorial guidance.
4. Record actual task hours, performance and dominant friction; prioritise fixes.

## Acceptance evidence

No progression-blocking defect or lost save in the tested loop. At least four of five testers choose another run. Every tester can service and relaunch. If not, iterate within slice scope.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

Do not begin full content production automatically when the gate fails.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
