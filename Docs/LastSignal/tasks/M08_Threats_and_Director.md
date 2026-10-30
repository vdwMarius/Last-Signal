# M08 Threats and Director

Status: Not started | Owner: Claude | Dependencies: M04, M07

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/01_Game_Design.md`
- `../docs/02_Technical_Design.md`

## Deliver

Drifter and clinger state machines; socket occupancy; bounded encounter director.

## Implementation sequence

1. Add pooled Drifter behaviour and visible roadside spawn zones.
2. Implement clinger approach, attach, local drag/damage and scrape removal.
3. Reserve one feasible corridor; add warning and cooldown constraints.
4. Implement cleanup across chunks and a recovery period after intense encounters.

## Acceptance evidence

At most four clingers attach, one per occupied socket. Side scrape removes only the intended side. Enemies cannot appear inside reserved stopping corridors. Chunk recycle leaves no attached orphan actor.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No Brute, gunplay or large horde framework.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
