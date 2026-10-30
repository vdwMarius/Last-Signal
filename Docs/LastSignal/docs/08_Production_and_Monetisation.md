# Production scope and monetisation

## Product shape

Recommend a paid, complete single-player game with optional cosmetic DLC after a strong demo or slice proves demand. The first release should work offline once installed and must not require paid paints to enjoy customisation. Ship a useful selection of earned paint colours, decals, cabin objects and garage decorations.

The defining feature is the relationship between driving, a physical workshop and an intimate story. Spend production effort on vehicle feel, sound, visible upgrades and a few memorable places. Procedural volume does not replace authored variety. Build fewer excellent material families and reuse them deliberately.

## R1 to R5 paint idea

Treat R1-R5 per paint as an affordability goal. Do not promise those exact standalone prices before checking the actual platform product type, regional price options and transaction requirements. Steam has pricing constraints, and an in-game purchase implementation has different obligations from selling a normal DLC product [S14, S15]. Platform pricing and launch-date rules need rechecking in the partner dashboard.

A simpler initial option is a small cosmetic DLC pack with several coordinated paints/decals, where the effective per-paint cost can be low without requiring many tiny purchases. An illustrative R19-R49 pack is a concept for research, not a recommended market price or guaranteed accepted tier. Validate willingness to pay and content cost after the slice. Do not build a bespoke wallet or backend just to sell a few colours.

All premium items are strictly cosmetic: no fuel, damage, capacity, crafting-speed or checkpoint advantage. Standard colours remain earnable. Avoid paid random packs, expiring ownership, countdown pressure and charging to recover a failed run. Let users preview paints under both garage and road lighting. Keep paid looks consistent with the somber world.

## Entitlement design

Create an optional platform-entitlement adapter behind a stable interface. A paint definition references a cosmetic entitlement ID; ownership is resolved by the platform integration, not a boolean written into the ordinary save. Use developer mock ownership during production and keep store code out of the core loop.

For paid DLC, use the platform's documented ownership and install checks. For actual in-game transactions, use its required payment flow and authoritative grant confirmation [S15]. Never embed publisher secrets in a client. Handle cancellation, duplicate callbacks, pending state, offline ownership behaviour, refunds and unavailable products according to the chosen platform. Do not remove a player's build or corrupt their save if a cosmetic entitlement becomes unavailable; substitute a free appearance while preserving the chosen cosmetic ID for later restoration.

## Art sourcing and licences

Maintain a provenance register for purchased assets, generated concepts, source meshes, fonts, audio, plugins and character likenesses. Record vendor, licence/version, receipt/location, allowed redistribution, modifications and the final asset IDs. Do not redistribute source packs inside the game's mod tools or documentation unless permitted. Check current engine, marketplace, MetaHuman and store terms when choosing assets and before release; this pack is a production checklist, not a legal determination.

A sensible cost strategy is licensed background materials/foliage, original hero vehicle shapes and story props, reusable procedural kits, and targeted specialist help for rigging, animation or audio where quality stalls. Avoid committing to paid asset packs until scale, art direction and export compatibility are verified in a small test.

## Capacity and milestone control

Maintain four queues: current implementation, validated next tasks, asset backlog and deferred ideas. Limit work in progress to one runtime task plus one isolated art task. Every new feature names the existing feature or time allowance it displaces. Do not expand the campaign because procedural road generation becomes easy.

Before M15, commit only to the slice. After M15, reassess development hours, actual asset throughput, performance and player response. Before M21, decide whether cosmetics justify support and platform integration. Before M22, decide whether console ports have access, resources and a viable schedule. Gates are production decisions, not requests for the coding agent to seek permission after every reversible edit.

## Open choices that can wait

Working title and final setting; exact target consoles; release price; how much art will be purchased versus authored; full voice acting versus text/radio fragments; and final scope if the slice overruns. Current assumptions let implementation begin without these decisions. Revisit setting before final environment art, voice before narrative recording, and business model before store integration.
