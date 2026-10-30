# M03 Vehicle Feel

Status: Not started | Owner: Claude | Dependencies: M02

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/02_Technical_Design.md`

## Deliver

Kestrel placeholder rig; Chaos setup; test circuit; chase camera; exposed tuning data.

## Implementation sequence

1. Validate rig scale, wheel axes, collision and contact points.
2. Implement throttle, brake/reverse, steering, handbrake and a controlled boost prototype.
3. Tune camera, steering speed curve, bounded assists and recovery behaviour.
4. Test slalom, brake, curb, ramp, reverse and rollover reset at 30/60/120 fps.

## Acceptance evidence

Drive five minutes without physics explosion or lost input. A gentle lane correction stays controllable near the intended top speed. Record handling observations and frame-rate differences.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No expensive final vehicle art, weapons or fuel economy.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
