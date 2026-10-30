# M20 Hardening and Optimisation

Status: Not started | Owner: Claude plus human testing | Dependencies: M19

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/07_Test_Performance_and_Release.md`

## Deliver

Measured quality presets; save migration suite; accessibility fixes; release blocker report.

## Implementation sequence

1. Profile representative and worst-case routes on candidate baseline hardware.
2. Fix CPU/GPU/streaming bottlenecks based on captures, not guesses.
3. Run save fault injection, controller, display, offline and long-run scenarios.
4. Reduce or defer content that fails budgets; retest affected paths.

## Acceptance evidence

Document actual hardware, build and frame-time results. No critical save/ownership failure. Minimum specification remains provisional until measured. Publish unresolved lower-severity defects with reproduction steps.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No feature expansion during hardening.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
