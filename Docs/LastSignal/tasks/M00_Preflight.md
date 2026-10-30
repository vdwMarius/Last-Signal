# M00 Preflight

Status: Not started | Owner: Claude | Dependencies: None

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/06_Agent_Setup_and_Workflow.md`

## Deliver

Version inventory; verified build commands; clean project; disposable automation test; first packaged executable.

## Implementation sequence

1. Inspect existing project, installed engine patch, compiler, Blender and agent tooling. Record findings without reading credentials.
2. Create or validate LastSignal C++ scaffold and Git/LFS rules; place pack under Docs/LastSignal.
3. Validate MCP with a disposable actor, or record fallback. Create minimal asset-validation and Blender cube scripts.
4. Compile, cook/package Windows and launch outside the editor. Record exact commands and failures.

## Acceptance evidence

Fresh project opens and packaged executable launches. A one-metre cube imports at correct scale. MCP operation is proven or explicitly blocked; a blocked connection does not block shell-based development.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No gameplay implementation or production asset generation.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
