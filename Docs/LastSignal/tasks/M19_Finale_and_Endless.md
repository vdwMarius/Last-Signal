# M19 Finale and Endless

Status: Not started | Owner: Claude | Dependencies: M16, M18

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/09_Narrative_Bible_SPOILERS.md`

## Deliver

Final relay scene; complete story journal; post-story state; endless rules.

## Implementation sequence

1. Implement finale arrival, recording restoration and transcript/skip path.
2. Resolve campaign state and one cosmetic epilogue choice.
3. Unlock endless from the completed profile with bounded threat scaling.
4. Store local scores with seed, rule version and assists; keep story rewards out.

## Acceptance evidence

Skipping dialogue still commits ending correctly. Rewatching does not duplicate rewards. Endless runs reuse builds without changing campaign history. Difficulty caps do not overflow counters or actor budgets.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No online leaderboard, multiplayer or alternative unfinished endings.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
