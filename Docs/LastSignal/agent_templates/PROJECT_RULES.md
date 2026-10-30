# Shared project rules

- Version-lock UE, Blender and exporters per milestone; record upgrades as decisions.
- C++ owns core transactions and rules; Blueprint owns assembly/presentation; Python is editor tooling.
- Read only the current task and its references. Scope file ownership before changing anything.
- Use stable IDs and soft asset references. Never save transient actor pointers as identity.
- Inventory and checkpoint grants are atomic and idempotent. Preserve compatible saves or implement migration.
- Critical hazards, clues and rewards are governed by explicit rules, never unconstrained random scatter.
- All essential interactions and UI work with controller. Menu input must not leak to gameplay.
- Never edit binary Unreal assets as text. Serialise all mutations against a running editor.
- Keep credentials and proprietary platform SDKs out of version control.
- Compile affected code and run named checks. Package at milestone gates. Record blocked checks honestly.
- Do not add purchases, online services, engine plugins or scope-expanding gameplay without a concrete task.
- Keep asset provenance, export manifests and current handoff with the project. Do not replace approved references silently.
