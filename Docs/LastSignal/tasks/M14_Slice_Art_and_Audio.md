# M14 Slice Art and Audio

Status: Not started | Owner: Codex assets; Claude integration | Dependencies: M03, M07, M10, M12

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/04_First_Three_Bases_and_Vehicles.md`
- `../docs/05_Art_UI_and_Asset_Bible.md`

## Deliver

Approved G01/V01 assets; one road kit; two enemy looks; UI theme; basic audio mix.

## Implementation sequence

1. Approve stock silhouette and workshop blockout before detailed modelling.
2. Build modular sources, materials and exports with asset IDs and provenance.
3. Import and validate rig, sockets, collision and reimport behaviour.
4. Light one representative road and workshop; profile materials and sound voices.

## Acceptance evidence

Packaged slice contains no missing textures. Tyres and hand targets align. Clean text remains readable against final art. Capture a driving video and wheel-change video, and record performance.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No cars two/three, final hero face or broad weather system.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
