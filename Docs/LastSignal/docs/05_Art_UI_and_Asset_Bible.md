# Art UI and asset bible

## Visual language

Believable materials and grounded proportions carry the fidelity; bold silhouettes and restrained exaggeration carry the arcade readability. The world is damaged by weather, repair and abandonment, not uniformly covered in noise. Keep 60% of each important surface relatively quiet, with grime concentrated at seams, runoff paths, wheel arches and handling points.

Palette: charcoal #181B1D, cold slate #53616A, bone #E5DFD1, rust #965640, work amber #D8A247, faded olive #666C54, danger red #D75B50. Red marks immediate danger, amber marks actionable service states, bone carries text, and a muted blue-green #7DB7AE marks confirmed success. Do not use colour as the only state indicator.

Exterior light is soft overcast, late dusk or thin mist; the first slice uses overcast dusk only. Garages contrast cool ambient light with warm practical lamps. Avoid crushed black driving lanes, excessive bloom, constant wetness, neon RGB gear, screen-wide grunge overlays and comic-outline zombies. Lights, glass and rubber must remain distinct from painted metal under every quality preset.

## Asset families and modularity

Build three reusable environment families: service masonry and corrugated metal; depot brick and red oxide steel; caretaker timber and concrete. Common props share metal, rubber, cloth and painted wood master materials. Use trim sheets and tiling surfaces for large areas, decals for local storytelling, and unique textures only where the camera benefits.

Kit grid is 0.5 m with major 2 m and 4 m wall pieces. Floor modules are 4 x 4 m; connectors must align without visible light or collision seams. Vehicle geometry has separate doors/panels only where animation or damage needs them. Wheel origins sit at hub centres; attachment sockets use stable names such as Wheel_FL, Wheel_FR, Wheel_RL, Wheel_RR, Ram_Front, Utility_Rear and Ornament_Dash. Publish transforms in a manifest and never silently move them after an animation is authored.

## Starting production budgets

| Asset | Starting budget | Validation |
| --- | --- | --- |
| Hero vehicle | 80k-150k conventional LOD0 triangles | Profile close workshop and moving road views |
| Vehicle materials | 6-8 slots including glass | Prefer shared atlases and masks |
| Vehicle textures | 2K sets; selected 4K body if justified | Check actual residency and blur at distance |
| Common prop | 1K or shared trim; simple collision | Judge silhouette at intended distance |
| Hero prop | 2K where close inspection needs it | Compare with cheaper variant |
| Road zombie | 15k-35k LOD0 with cheaper distant LODs | Budget animation and shadows, not only triangles |
| Architecture | Nanite candidate for static opaque detail | Inspect material cost, fallback and collision |

These are project starting budgets, not engine limits or guaranteed optimal counts. Test Nanite on appropriate content; do not remove collision, material, animation or memory budgets because geometry streams efficiently [S07]. Keep the proven conventional vehicle rig until a measured Nanite skeletal experiment wins on the target hardware.

## Image generation brief contract

Every request names asset ID, role, camera, dimensions, stock/upgrade state, palette, material hierarchy, approved references and excluded features. Generate a small set of concepts, select one, then derive supporting views. Maintain a reference index so later tasks reuse the selected design rather than inventing another car or room.

Image outputs can serve as mood boards, paint explorations, decals after cleanup and reference sheets. They are not reliable orthographic measurements, mesh topology, UVs, seamless PBR sets or a consistent multi-view reconstruction by default. Generated UI screenshots are layout references; generate actual text, icons and widgets in vector/code/UMG. Do not make a functional menu by placing a generated screenshot behind invisible buttons.

Reusable request: Create a reference image for [ASSET_ID] in Last Signal. Follow the approved [REFERENCE_IDS], exact design brief and palette. Show [VIEW], [STOCK_OR_UPGRADE_STATE], and the complete silhouette without cropping. Keep surfaces physically plausible and readable; use restrained rust and wear. No labels, logos, invented text, extra wheels, impossible joints or unrelated objects. This is a visual reference, not a production mesh.

## Blender to Unreal pipeline

1. Freeze the approved reference and dimensions. Build a scale blockout and export it before detailing.
2. Choose one tested axis/unit preset: Blender scene units in metres, applied transforms, export mapped to Unreal +X forward/+Z up. Validate with a 1 m cube and wheel axle test; do not assume a vehicle rig follows a static-mesh export preset.
3. Build clean topology, UVs and material IDs. Separate movable or replaceable components. Generate simple collision independently of visual detail.
4. Create the skeleton/skin where required, check normals and weighted transforms, then bake or author textures with a consistent channel convention. Document packed textures explicitly, for example ORM = occlusion/roughness/metallic.
5. Export with a pinned preset; import through a repeatable Unreal script. Reimport must preserve approved materials and references.
6. Inspect scale, pivots, wheel motion, collisions, LOD behaviour, lighting and damage states in the target map. Produce an asset report with measured issues.

Claude and Codex can both write Blender Python. Assign Codex the asset pipeline and visual review to reduce ownership conflicts, not because Claude is technically unable to do it. Use batch scripts for repeatable geometry and exports [S11]. Complex hero vehicles, clothing and faces still benefit from skilled manual art work or licensed base assets.

## Characters and animation

Eli Vale, the playable lead, is an ordinary adult mechanic in a worn canvas jacket, layered shirt, practical trousers and work boots. Use arms/hands and a shadow/body representation first; a full cinematic head is unnecessary for driving and first-person service. Mara Vale, an adult emergency logistics coordinator, has a repaired blue coat and recognisable scarf; her identity comes through decisions and objects before her face appears.

Use MetaHuman Creator for hero human baselines if chosen. Assemble gameplay characters through the UE Optimized pipeline and verify LOD, hair and material costs [S08]. Start with hair cards or a measured economical hair setup; reserve cinematic settings for tightly controlled shots. Create original clothed characters; likeness and voice assets require permission from the relevant people.

Animation minimum: on-foot walk/idle, carrying a wheel, focus/reach, jack action, fastener action, wheel lift/seat, vehicle entry/exit transition, three enemy locomotion families, attach/hold/scrape-off, hit reactions. Use snap-assisted interactions and short transitions first. Avoid full-body first-person collision and complex finger simulation before the loop is fun. Do not use full MetaHumans for the road horde.

## HUD layout and typography

At 1920 x 1080 reference resolution: keep essential information inside a 5% safe area. Bottom left: 260 x 120 vehicle condition cluster with body, wheel and fuel icons. Bottom right: 220 x 150 speed/boost display, with speed the largest number. Top centre: compact next-refuge name and remaining distance; no permanent paragraph of quest text. Clinger warnings appear on the affected screen side and include an icon plus direction, with optional sound/haptics.

Use a clean licensed sans-serif for body text and one restrained condensed face for labels. Prototype at 20-24 px body, 28-36 px section headers and 48-64 px speed readout, then scale for 720p, 1080p, 1440p, 4K and living-room distance. Offer UI scale and subtitle size. Texture wear belongs on frame edges; never distress essential text. Keep text as localisable strings and allow at least 35% expansion.

| Screen | Composition | Controller behaviour |
| --- | --- | --- |
| Driving HUD | Corner status, quiet centre, directional threats | No cursor; pause always available |
| Workbench | Categories left, 3D preview centre, stats/cost right | D-pad list, shoulder categories, confirm/back |
| Part comparison | Current and proposed with explicit tradeoffs | Focus change previews, confirm commits |
| Route board | Secured route, next refuge, optional detours | Focus nodes; reachable and locked use labels |
| Decoration | World preview with compact action strip | Stick move, bumpers rotate, confirm/place, back/cancel |
| Journal | Clue list left, readable evidence right | Next/previous; audio replay and transcript |
| Cosmetics | Paint groups and live vehicle preview | Preview free; purchase opens platform flow |

All components need normal, focused, pressed, disabled, loading, error and selected states. Disabled actions explain why. Destructive choices require a separate confirm; ordinary navigation does not. Restoring a closed modal returns focus to its initiating control. Never require a mouse drag for inventory, decoration or wheel fitting.

## Default controller map

| Action | Driving | On foot or workshop |
| --- | --- | --- |
| Left stick | Steering | Move |
| Right stick | Limited camera orbit | Look |
| RT / LT | Accelerate / brake then reverse | Placement fine controls when explicitly shown |
| South face button | Handbrake | Interact or confirm |
| West face button | Boost | Context action or rotate mode |
| East face button | Cancel in UI | Back or cancel carry |
| North face button | Look back | Inspect |
| LB / RB | Optional quick look left/right | Tabs or placement rotation |
| D-pad | Lights and accessible shortcuts | Navigate or nudge |
| Menu / View | Pause / route summary | Pause / journal |

Button names resolve to the connected device's glyphs. Remapping is supported; a keyboard preset remains available. Add hold-to-toggle alternatives, deadzone/sensitivity settings, separate camera inversion, reduced shake/head bob/motion blur, subtitles, contrast options and no-mash service controls.

## Audio identity

Layer engine load, RPM, tyre surface and loose body rattle; upgrades should change a recognisable sound without increasing perceived loudness unfairly. Impacts need onset, body resonance and debris tails, with voice limits. Warm garage room tone, distant wind and intermittent radio noise create contrast. Music is sparse, original/licensed and avoids constant action scoring. The story uses radio repetition sparingly; mandatory cues have subtitles and visual alternatives.

## Reusable UI prompt

Design [SCREEN_ID] for Last Signal using the listed layout, palette and state model. Produce a 1920 x 1080 reference and a component/state inventory. Keep essential text clean and editable, edges subtly worn, centre visibility high, and controller focus unmistakable. Show current and proposed stats with units, costs, locked reasons and back navigation. Do not add premium currency, neon cyberpunk styling, fake tiny text or mouse-only controls. Implement approved widgets in UMG/Common UI with data bindings; the image is only the reference.
