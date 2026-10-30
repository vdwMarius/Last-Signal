# M21 Optional Cosmetics

Status: Not started | Owner: Claude | Dependencies: M20

## Read first

Read the root agent instructions and latest project handoff, then only the relevant code plus:

- `../docs/08_Production_and_Monetisation.md`
- `../docs/02_Technical_Design.md`

## Deliver

Either explicit defer record, or tested cosmetic entitlement adapter and approved product data.

## Implementation sequence

1. Confirm commercial choice, platform access, product type and accepted prices.
2. Keep mock entitlements for tests; implement platform ownership adapter if authorised for release scope.
3. Separate preview, purchase request and confirmed ownership; preserve offline core.
4. Test cancellation, duplicate callbacks, unavailable cosmetic, refund and restore paths.

## Acceptance evidence

No stats differ between paid and free appearances. No client secrets. Failed purchase cannot consume scrap or damage saves. Store backend assumptions are validated in the platform test environment.

Record the build/test command, observed result, relevant screenshot/video/log path and any untested condition. A blocked test is not a pass. Add focused automation where state integrity or repeatability matters; use manual playtests for feel and visuals.

## Boundaries

No premium currency, paid progression or guessed standalone R1-R5 price support.

Declare actual file ownership before editing. Keep unrelated files unchanged. Do not open a second writer against the same Unreal editor or binary asset. If a dependency is missing, complete the smallest necessary dependency fix and record it; do not silently redesign the feature.

## Handoff

Update PROJECT_STATE.md with completed work, exact changed files, tested results, known issues and next task. Commit the coherent change after checking the diff. Mark this card complete only when acceptance evidence exists; stop at the task boundary.
