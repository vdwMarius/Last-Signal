# Data use and production values

balance_seed.json contains untested balance proposals. It is not a drop-in Unreal plugin or finished gameplay schema. M01 imports or translates it into project definitions and validates every referenced ID.

One cargo slot holds ten units of a common material; each spare part uses one slot. Scrap, clues and blueprints consume no cargo slots. Garage inventory is unbounded in version 1. A full-cargo pickup must show a readable refusal or offer a swap at a safe location; never silently destroy items.

The stock build always includes compatible wheels and core modules. Generate immutable stock definitions from each vehicle in M01; these have no purchase cost. Add soft asset paths only after real assets exist. The tutorial grants one Kestrel retread wheel and tools. CP00 unlocks Kestrel T1 recipes; CP12 and CP30 unlock their vehicle's T1 recipes; CP24 unlocks the three common specialisations.

Free part rewards: CP08 one Kestrel retread wheel; CP18 one Mule suspension kit; CP24 one Mule utility module; CP36 one Warden reinforced wheel. These use unique grant IDs and do not duplicate on revisit. A purchased copy does not prevent earning a separate free physical part. The three specialisations are compatible alternative parts, not extra slots.

Guarantee at least one visible fuel pickup before a marginal-range leg and tutorial materials for the first demonstration. Nominal fuel range excludes boost and idle. Tune guaranteed pickup placement so skillful stock play can reach the next checkpoint; never require random loot to avoid a softlock.

Asset manifest is the initial production inventory, not every shipping variant. Planned means no mesh or concept has yet been generated. Estimate actual effort after scale blockouts and expand only after the slice passes.
