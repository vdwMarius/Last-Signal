# Game design

## Player promise

Your car is your weapon, your workshop project and the last familiar object in a collapsing world. Short, dangerous drives fund visible improvements. Each secured refuge gives you a more personal home and another piece of your wife's journey. The excitement comes from recovering control under pressure; the sadness comes from what remains after the engine stops.

The inspirations describe functions: Zombie Highway supplies evasive driving and attached threats; Earn to Die supplies earned vehicle growth; Pacific Drive supplies attachment to a physical car; Dying Light supplies weathered atmosphere. Create original silhouettes, fiction, encounters, interface, audio and branding.

## Design pillars

- Driving must feel good before art: readable hazards, responsive steering, weight without simulator friction, and recoverable mistakes.
- Upgrades change both handling and appearance. More armour trades agility and efficiency for impact protection; no vehicle makes the previous one obsolete.
- Garages provide calm, ownership and brief tactile work. Service is optional ritual after the tutorial, never a compulsory chore between every run.
- The road tells a controlled story inside a replayable structure. Mandatory clues and rewards never depend on lucky procedural rolls.
- Darkness sets the mood without concealing required information. Silhouette, sound and lighting must make hazards readable at speed.

## Core and long-term loops

At a refuge, choose a destination and vehicle, review fuel and installed parts, then leave. Drive for roughly 6-10 minutes including hazards and deliberate slowdowns; collect salvage, fuel and evidence while choosing safer or richer branches. Reach a safe checkpoint to bank everything and refill, or fail and return with a small salvage recovery. Back at a garage, craft or find an upgrade, fit it, decorate one corner and inspect a new clue. Repeat until the next major refuge is secured.

The campaign has fixed regional milestones at route km 0, 12 and 30, with a finale at km 48. Intermediate checkpoints divide long distances into achievable legs. These are logical route distances, not a promise to store 48 km of unique terrain. Replayed legs have new encounter variants but retain the same authored landmark sequence. A player cannot unlock story progress by repeatedly driving around a loop.

## Modes and failure rules

Campaign: reaching a forward checkpoint permanently unlocks it as a launch location. Outposts bank salvage, refill fuel and allow recovery, but full upgrades and decoration happen in garages. A map travel option between already secured refuges avoids forcing players to replay earlier roads for routine workshop access. Travelling home safely is a menu transition; unbanked cargo must first be banked at a safe location.

Endless: unlocked by completing the campaign, uses the same vehicle builds with a growing distance score and bounded difficulty. No critical story unlocks or exclusive power rewards depend on endless play. Record seed, rules version, assists and distance with each result; no online leaderboard in version 1.

Failure: banked inventory and ownership are safe; keep floor(30% of unbanked scrap), lose unbanked common crafting materials, and retain collected story evidence and first-time blueprint unlocks. Return to the selected secured refuge with the car recovered and serviceable. Basic repairs and a standard departure tank are free. Do not charge a repair debt that prevents another attempt. Explain recovery as assistance from an off-screen relay network, not resurrection.

Quitting is separate from failure. Normal exit creates a resumable run snapshot. Story evidence is journalled immediately. A corrupt or incompatible run snapshot falls back to the last committed checkpoint with an explanation and no banked-item loss.

## Driving and impact combat

Use continuous steering, acceleration, braking and reverse. Keep roads broadly three lanes wide, with shoulders and occasional junctions; do not lock the car to discrete lanes. Add adjustable steering assist, traction aid, restrained anti-roll support and automatic transmission. Start with a high chase camera and limited player orbit; cockpit driving is deferred.

The default combat tools are steering, impact, boost and scraping attached zombies against marked obstacles. No manual gun aiming, weapons inventory or ammunition economy in the first release. Optional late development roof devices must pass a separate scope gate.

Zombies enter from verges or visible road spaces. A clinger can attach at a named vehicle socket, increase handling drag, and damage that local component. A side scrape dislodges clingers on that side; an intentional scrape causes a small, predictable body cost. At most four attached threats exist on one car. Do not make each attached zombie a fully simulated ragdoll.

An enemy or obstacle hit resolves once per impact window: relative speed, impact angle, vehicle mass class, ram rating and target type determine the outcome. Avoid real-world lethal speed thresholds. Low-speed bumps do little; clean frontal hits reward committed driving; hitting an immovable barrier is costly. Hit audio, suspension compression, a brief camera response and directional feedback sell the impact. Offer reduced gore and reduced camera motion.

## Threat catalogue and encounter rhythm

| Threat | Readable warning | Player answer | Initial scope |
| --- | --- | --- | --- |
| Drifter | Upright silhouette and slow crossing | Steer or ram | Slice |
| Clinger | Flank sprint and side warning | Scrape that side or avoid attachment | Slice |
| Brute | Broad stance, distinctive heavy sound | Avoid or use a strong ram at a cost | Region 2 |
| Wreck choke | Reflective markers, visible gap | Brake and pick a lane | Slice |
| Fuel detour | Lit can symbol before junction | Trade time and exposure for range | Slice |
| Flooded rut | Water reflection and road warning | Slow down or use suitable tyres | Region 3 |

Alternate 20-45 seconds of active pressure with 15-30 seconds of recovery, adjusted by playtests. A director can lower spawn density after repeated failures but cannot fabricate an obstacle in the player's stopping distance. Reserve at least one feasible vehicle-width corridor. No unavoidable damage introduced by generation.

## Economy and upgrades

Use one spendable currency, Scrap, plus three non-premium materials: Rubber, Alloy and Electronics. Blueprints unlock recipes and are permanent. Found complete parts are persistent unique inventory instances only after banking; quest-granted parts are granted transactionally at checkpoints. There is no energy timer, paid fuel or purchasable stat advantage.

Seed costs are 120 scrap for a first useful part, roughly 250-700 for mid-tier parts and 900-1500 for specialisations. Target a meaningful choice every 1-2 early runs and 2-3 later runs. The first tutorial provides materials for one wheel replacement. Measure actual earnings before balancing a grind around these numbers.

Each vehicle has engine, fuel, suspension, ram, utility and four wheel slots. Cosmetic paint, decals, mirrors, roof trim and cabin ornaments use separate non-stat slots. Weight changes only come from gameplay parts. Four individual tyres use one compatible wheel family per car; mixed tyres are allowed only when radius matches. UI warns about mixed grip, while mismatched radii block departure.

Crafting creates an item; installation changes the vehicle. Replaced parts return to inventory. Sell or salvage parts only with an explicit confirmation, and never destroy the only compatible wheel needed to leave. Unlocks do not auto-equip parts or reset a favourite build.

## Workshop and home customisation

Walk to the bench, vehicle, wardrobe, radio or route board. The same functions are reachable through an accessible workshop menu. Repair and upgrade interactions share one focus target and one confirm action, with clear invalid-state text.

Wheel sequence: park in the bay; engage service mode; raise the axle with the jack; loosen an abstracted fastener group; remove the old wheel; carry and align the new wheel to a snap target; tighten; lower. No per-bolt physics or precision hand IK is required for the slice. Cancel returns safely to the last valid state. After doing it once, Quick Fit performs the same validated transaction without the animation. Both methods have identical stats and costs.

Home decoration uses a placement mode with snap rotation, grid/free positioning, wall/floor categories and undo. Start with 20 approved objects across benches, storage, seating, rugs, lights and personal keepsakes. Block exits, vehicle clearance and required station exclusion volumes from placement. Decorations carry no performance buffs; unlocked stations provide functionality. Save each base layout independently and offer Reset Layout without deleting owned items.

## Narrative interaction

Mandatory clues sit on the route board, checkpoint arrival scene or another guaranteed position. Optional personal objects add context. The journal records exact observations separately from the protagonist's interpretation. Garages have short, optional environmental stories; no mandatory ten-minute dialogue scene interrupts a driving session.

The full spoiler treatment is in document 09. The ending is authored and resolves the wife's fate; procedural ambiguity must not substitute for a coherent conclusion.

## Scope boundaries and success gates

Ship three cars, three garages, three region kits, three enemy behaviours and one complete story. Exclude multiplayer, survival hunger/thirst, open-world foot travel, structural base construction, dynamic vehicle crumple simulation, fully simulated loose cargo and live-service seasons.

Prototype gate: five independent testers understand steering and identify why they failed. Slice gate: at least four of five voluntarily choose another run, and all can replace a wheel and launch using only a controller. These are small-sample development signals, not market forecasts. Cut features before compromising feel, stability or readability.
