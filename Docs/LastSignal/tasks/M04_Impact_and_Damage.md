# M04 Impact and Damage

Status: Not started | Owner: Claude | Dependencies: M03

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/02_Technical_Design.md`

## Deliver

Damage evaluator; engine/body/wheel conditions; collision cooldown; pooled impact presentation.

## Implementation sequence

1. Create component health and one bounded impact-resolution path.
2. Use relative impact conditions to distinguish glancing, frontal and static barrier hits.
3. Add visual damage placeholders, sound hooks and reduced-shake option.
4. Reset wreck state completely on respawn.

## Acceptance evidence

One collision window cannot apply damage every render frame. Glancing and direct collisions differ predictably. Damaged wheel handling is recoverable. Repeated resets do not retain old effects.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No soft-body destruction or fully simulated scrap.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
