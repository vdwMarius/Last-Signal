# M22 Release and Console Gate

Status: Not started | Owner: Human owner with Claude | Dependencies: M20

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/07_Test_Performance_and_Release.md`
- `../docs/08_Production_and_Monetisation.md`

## Deliver

PC release candidate; changelog; support instructions; console feasibility checklist.

## Implementation sequence

1. Require M21 completion or a recorded decision to ship without paid cosmetics.
2. Build and test clean install and update paths; preserve symbols, build ID and rollback artifact.
3. Audit asset provenance, content disclosures, store copy and accessible settings.
4. Scope actual consoles against approved access, devkits, SDKs and certification requirements.

## Acceptance evidence

PC candidate is reproducible and passes defined gates. Store copy states only tested features. Human owner signs off release. Console support remains unannounced until its separate gate is viable.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

Do not publish, charge customers or claim certification merely because a package builds.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
