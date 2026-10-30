# M02 Input and Modes

Status: Not started | Owner: Claude | Dependencies: M01

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/02_Technical_Design.md`
- `../docs/05_Art_UI_and_Asset_Bible.md`

## Deliver

Player controller; driving/on-foot/service/placement contexts; pause flow; input test map.

## Implementation sequence

1. Create named input actions and keyboard/controller mappings.
2. Implement exclusive gameplay contexts and a mode transition service.
3. Add pause consumption, hotplug handling and controller glyph selection.
4. Record controller-only test path and inspect action firing in each mode.

## Acceptance evidence

Confirm in a menu never accelerates the car. Switching input device updates prompts. Disconnect pauses the road prototype and reconnect restores one active context.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No polished menus or advanced remapping screen yet.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
