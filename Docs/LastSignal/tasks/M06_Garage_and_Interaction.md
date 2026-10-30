# M06 Garage and Interaction

Status: Not started | Owner: Claude | Dependencies: M02, M05

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/04_First_Three_Bases_and_Vehicles.md`

## Deliver

Mile Zero blockout; garage character; interaction interface; bay parking and station zones.

## Implementation sequence

1. Block out G01 at specified scale with service and exit exclusion volumes.
2. Implement focus trace, prompt and interaction validation.
3. Add car/character possession transitions and one reachable bench.
4. Provide workshop-menu access to essential actions and a safe spawn fallback.

## Acceptance evidence

Controller user can leave vehicle, reach bench, inspect route and return to driving. No spawn inside a car or wall. Interaction selects one valid target with a readable reason when blocked.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No on-foot combat, jumping puzzles or final interiors.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
