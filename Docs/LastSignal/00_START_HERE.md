# Last Signal production pack

Version 1.0 | 29 October 2026 | Working title subject to name clearance

Build an original, single-player vehicle survival game: make one more desperate drive, bring home salvage, physically improve a battered car, and follow a missing partner's trail through increasingly unsettling safe houses. The target is responsive arcade driving with believable materials, weight and damage. This pack defines the game and the implementation contracts; it is not a finished Unreal project or a claim that the supplied designs have been playtested.

## Decisions used to make this pack actionable

- Windows PC first; controller support from the first prototype; console ports after PC performance and funding gates. No mobile, multiplayer or VR in version 1.
- Third-person chase camera while driving; first-person exploration inside safe garages and small fenced forecourts. No on-foot combat or freely explorable open world.
- A compact campaign through three garages and three mechanically distinct vehicles, followed by an endless mode. A 4-6 hour first-playthrough target is a hypothesis, not a content promise.
- Fictional Greywater evacuation corridor: misty inland grassland, industrial outskirts and a reservoir upland. Local details can later be adapted to a South African setting without changing the systems.
- Premium base game; optional cosmetic packs after the core game is complete. The requested R1-R5 paints remain a pricing idea to validate, not a storefront commitment.
- Unreal Engine 5.8.x, with the exact installed patch and toolchain recorded in M00. Avoid engine upgrades in the middle of a milestone.

## Read and use in this order

1. Read `docs/01_Game_Design.md` for the player experience and scope.
2. Follow `docs/06_Agent_Setup_and_Workflow.md` on the development PC.
3. Copy the agent instruction templates from `agent_templates/` to the Unreal repository root. Fill in verified local paths during M00.
4. Work through `tasks/M00_*.md` onward, in the order in `docs/03_Implementation_Roadmap.md`.
5. Give Claude only the current task, referenced documents and relevant code. Give Codex the relevant asset brief and style bible. Do not paste this whole pack into every session.
6. Tag the playable vertical slice at M15. Decide whether the driving is worth expanding before producing the remaining art.

## Deliverables and authority

The PDF is a human-readable edition of this pack's overview and ten design documents. The ZIP adds individually scoped task cards, prompts, editable design sources, balance seeds, asset inventory and handoff templates. Markdown and JSON are the editable sources. Gameplay values in `data/balance_seed.json` are the tuning source of truth; the design documents explain their purpose. Update both when changing a rule.

Every generated asset still needs a provenance entry, import check and in-engine review. Image generation produces concepts, not automatically rigged vehicle meshes, clean UI layouts or production-ready MetaHumans. Neither Claude nor Codex has been connected to your local tools in this session.

## Start with this prompt

Read CLAUDE.md, Docs/LastSignal/00_START_HERE.md, Docs/LastSignal/tasks/M00_Preflight.md and Docs/LastSignal/docs/06_Agent_Setup_and_Workflow.md. Execute M00 only. Inspect installed versions and the existing project before choosing commands. Create or validate the project scaffold, report tool availability, package the empty PC project if tooling permits, and update the handoff. Do not implement the game systems yet. Distinguish tested steps from blocked steps.
