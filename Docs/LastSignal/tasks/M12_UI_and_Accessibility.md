# M12 UI and Accessibility

Status: Not started | Owner: Claude | Dependencies: M02, M09, M11

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/05_Art_UI_and_Asset_Bible.md`
- `../docs/07_Test_Performance_and_Release.md`

## Deliver

Common UI screens; driving HUD; settings; part comparison; focus and glyph tests.

## Implementation sequence

1. Implement shared component states and safe-area scaling.
2. Wire HUD and screens to read-only data/events rather than direct save edits.
3. Add remapping, contrast, subtitles, camera comfort and hold alternatives.
4. Test modal focus restoration, device switch, locked/error/loading states.

## Acceptance evidence

Complete run to upgrade to relaunch without a mouse. At 720p and 4K no essential labels clip. Large text fits. Closing a modal restores focus. Pause input never leaks into driving.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No baked screenshot UI or storefront integration.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
