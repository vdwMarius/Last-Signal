# Technical design and contracts

## Runtime shape

Use a C++ core with Blueprint children for assembly and tuning. Keep transactional inventory, persistence, procedural scheduling and rule calculations in testable C++; use Blueprint for presentation, interactions and art hooks. Python is an editor/asset-pipeline tool, not packaged gameplay [S05]. Start with one runtime module `LastSignal` and one optional editor module `LastSignalEditor`; do not build a framework of many plugins before the slice.

Use separate garage maps and one streamed road runtime. Loading a destination garage is an intentional safe transition. World Partition can help an authored region when justified, but is not the generator for an endless road. The first implementation uses a bounded chunk manager with authored connectors, reusable actors and data-driven content.

## Responsibilities and stable boundaries

| Owner | Responsibility | Must not own |
| --- | --- | --- |
| ULSProfileSubsystem | Profile, banked inventory, unlock ledger, save commits | Live physics |
| ULSRunSubsystem | Run lifecycle, seed, unbanked cargo, checkpoint and failure resolution | UI widgets |
| ALSRouteDirector | Chunk readiness, safe corridors, encounter schedule | Economy mutation |
| ALSVehiclePawn | Driving, component damage, sockets, presentation events | Permanent unlocks |
| ULSVehicleBuildComponent | Installed part IDs and evaluated stats | Crafting wallet |
| ULSWorkshopService | Craft/install/remove validation and atomic changes | Input polling |
| ALSGarageCharacter | Walk, carry visual and interaction trace | Inventory authority |
| ULSUIRouter | Common UI screens and focus restoration | Save-file writes |

Names are proposed project types, not existing engine APIs. Confirm engine APIs against the installed headers before implementing. Gameplay Ability System and Mass are unnecessary for the first bounded enemy counts; add them only after profiling or requirements justify the migration.

## Data definitions

Definitions are Primary Data Assets with stable string-like IDs and soft asset references. Instances store IDs and state, not transient UObject pointers. Blueprint display names can change without changing save identity. Keep definitions versioned and validate references during cook.

- VehicleDefinition: ID, chassis asset, compatible part tags, base mass, fuel/range tuning, socket map, steering/torque profiles and default build.
- PartDefinition: ID, slot category, compatibility tags, recipe, stat modifiers, visual asset, unlock condition and preview text.
- PartInstance: unique instance ID, definition ID, condition and cosmetic overrides. An instance exists either in inventory or exactly one installed slot.
- RoadChunkDefinition: ID, length, entry/exit transforms, lane widths, speed band, biome tags, clear zones, optional sockets and collision/visual assets.
- EncounterDefinition: stable ID, tags, cost, warning distance, spawn bounds, cooldown and mutually exclusive hazards.
- CheckpointDefinition: ID, route distance, arrival map or outpost, reward IDs and mandatory clue IDs.
- DecorationInstance: unique ID, definition ID, base ID, local transform, surface ID and colour selection.
- ClueDefinition: ID, exact text/audio, prerequisite, guaranteed placement, journal order and spoiler tier.

Start with the included JSON for tuning and CSV for art planning. They are seed specifications, not files Unreal automatically imports into these structures; M01 builds and validates the import or equivalent Data Assets.

## Events and commands

Use commands for mutations and events after success. `TryInstallPart(vehicleId, slotId, partInstanceId, expectedRevision)` returns success or a structured failure; UI never edits arrays directly. Publish `BuildChanged`, `CargoChanged`, `CheckpointCommitted`, `ClueRecorded`, `RunEnded` and `InteractionStateChanged` with IDs and compact payloads. Bind listeners once and remove bindings on teardown.

Run states: AtRefuge, Preparing, Driving, Arriving, Failed, Resolving, Suspended. Only one state transition owns reward settlement. A checkpoint commit uses a unique transaction ID, banks cargo, grants once-only rewards, advances the checkpoint and writes the durable profile before presenting success. Retrying that transaction must not grant twice.

## Distance and procedural road

Maintain three different measures: `RunDistanceM` for forward progression in the current attempt; `CampaignFrontierM` for the furthest committed story checkpoint; and `LifetimeOdometerM` for statistics. Reverse movement and circles do not increase route progress. Route position comes from ordered chunk index and monotonic spline progress, rather than accumulated absolute wheel travel. Branches rejoin one logical checkpoint distance and cannot skip required milestones.

Begin with 250 m nominal chunks, five ahead and two behind the current chunk. Treat these as starting values; actual chunk length and visibility determine the active count. At 110 km/h, five forward chunks give about 41 seconds of look-ahead. Schedule data preparation first, then asset loading, collision readiness, gameplay placement and decorative PCG work. All lane collision and mandatory gameplay must be ready before entry.

The generation seed is a stable hash of campaign seed, route segment ID, chunk index and generator version. Keep separate random streams for layout, encounter and decoration. Log resolved chunk/encounter IDs, so a failing seed can be replayed even after cosmetic changes. Deterministic layout does not imply cross-platform deterministic Chaos physics.

PCG dresses the corridor with vegetation, rocks, poles and ruins; reserved volumes protect lanes, sightlines, garage doors, rewards and required story scenes. Prefer pre-generated scenery variants in the slice. Introduce runtime PCG only after M07 is stable, with generation/cleanup radii and work budgets measured in a packaged build [S03]. Critical route selection is owned by game code, not a free-form PCG graph.

Keep one fixed global weather/time profile per run initially. Change weather at checkpoint transitions. This avoids spending the art budget on every lighting condition before the route works. Stop repetition with a recent-chunk exclusion list, biome grammar, direction changes within connectors and authored landmarks. Seed validation checks every branch for sufficient clearance and reachable exits.

## Long-distance coordinates and streaming recovery

Use an int64 logical route index/distance alongside local transforms. Validate an origin-rebase implementation at a controlled streaming boundary, transforming the active road, vehicle, physics state, attachments and VFX together; do not assume large-world coordinates alone solve an unbounded journey. Test after a simulated 1,000 km. Save logical route coordinates, not only a huge world-space vector.

If a required chunk is not ready, extend a preloaded safe straight segment and defer the next encounter. A checkpoint loading transition is the last fallback. Never expose missing collision, hide a hard stop inside fog, or teleport the car without a visible transition. Chunk pooling must reset timers, attachment lists, collision, delegates, audio and loot state.

## Vehicles and damage

Prototype with Chaos Vehicles [S06] and a known-good four-wheel rig. Keep wheel bones and visible interchangeable wheel meshes aligned through a tested import convention. Wheel upgrades may modify grip and visual tread without changing rolling radius in version 1; reconfigure runtime wheel parameters only through verified APIs. Rebuild the parked vehicle physics state when needed.

Apply assists through bounded, delta-time-aware control. Test identical scenarios at 30, 60 and 120 fps; do not assume presentation tick timing equals physics timing. Use query-only sensors for clinger sockets, one target resolution window per collision and simple convex collision for dynamic parts. Cosmetic break-off panels are pooled and capped; damage swaps/decals replace soft-body crumpling.

Vehicle modules: engine, body, wheels and fuel. Losing engine/body integrity ends the run; a damaged wheel degrades handling but does not become unrecoverably random. Fuel exhaustion permits a brief coast, then a clear recovery action. Upgrades modify baseline stats through one evaluator: additive values first, multiplicative values second, then clamps. Recompute from defaults to avoid stacking a bonus again after loading.

## Transactional workshop

Keep a logical service transaction separate from carried visual props. Validate vehicle parked, service mode, compatible slot, ownership, recipe or inventory state, and current revision before changing anything. Reserve the incoming part; never deduct both at craft time and again at installation. During a wheel animation the old part is visually detached, but logical replacement commits only on successful completion. Cancellation returns visuals and reservations to their original state.

Save only settled workshop state. If interrupted mid-animation, reload the last committed build with both inventories intact. Repeated confirm inputs are debounced by transaction ID. Quick Fit calls the same service command and bypasses only presentation.

## Persistence and migration

Profile schema: schemaVersion, contentVersion, profileId, revision, banked resources, owned parts, vehicle builds, checkpoints, once-only reward ledger, clues, per-base decoration layouts and settings. Run snapshot: seed/version, route location, vehicle state, cargo, consumed pickups and resolved encounter IDs. Keep purchase entitlement data separate from editable gameplay saves.

Implement A/B save slots with generation numbers and integrity checks. Write the inactive slot, read-validate it, then select the newest valid generation at load. Preserve the older valid slot; a checksum detects corruption but is not an anti-cheat system. Test interrupted writes, disk-full errors, migration of the previous schema and missing/retired asset IDs. Unknown cosmetic IDs fall back; unknown core part IDs restore a compatible stock item with a logged migration.

## Input and UI

Enhanced Input supplies mutually exclusive driving, on-foot, service and placement contexts [S09]. Common UI supplies layered screens, controller navigation and glyph routing [S10]. Pause/menu input consumes gameplay actions. Centralise device switching so mouse jitter does not flicker controller prompts. A controller disconnect pauses single-player driving and shows reconnect guidance.

## Content folders

Use `Source/LastSignal/{Core,Vehicle,Route,Workshop,Garage,Narrative,UI}`, `Content/LastSignal/{Core,Vehicles,World,Garages,Characters,UI,Audio,Data}`, `Scripts/{Unreal,Blender}`, `Tests/`, and `Docs/LastSignal/`. Put external assets under `Content/External/<Vendor>` and preserve licence information. Runtime code must not import editor-only modules. Use soft references and explicit cook rules for dynamically selected assets.
