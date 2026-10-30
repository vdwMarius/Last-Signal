# Implementation roadmap

Build in dependency order. Each task file contains a bounded assignment, outputs, implementation sequence, evidence and stop conditions. The owner is accountable for integration; another agent may review without changing the same files. Expect to split a task into smaller sessions when its acceptance checks cannot fit into one focused implementation.

| Task | System | Depends on | Owner |
| --- | --- | --- | --- |
| M00 | Toolchain and packaged blank project | None | Claude |
| M01 | Definitions and profile persistence | M00 | Claude |
| M02 | Input and mode switching | M01 | Claude |
| M03 | Vehicle feel test track | M02 | Claude |
| M04 | Impact and component damage | M03 | Claude |
| M05 | Fuel cargo failure and checkpoint loop | M01 M04 | Claude |
| M06 | Garage walk and interaction | M02 M05 | Claude |
| M07 | Bounded road streaming | M03 M05 | Claude |
| M08 | Drifter clinger and encounter director | M04 M07 | Claude |
| M09 | Crafting and build transactions | M01 M06 | Claude |
| M10 | Manual wheel replacement | M09 | Claude |
| M11 | Route milestones and clue journal | M05 M07 | Claude |
| M12 | Controller UI and settings | M02 M09 M11 | Claude |
| M13 | Garage decoration | M06 M09 M12 | Claude |
| M14 | First-region production art and sound | M03 M07 M10 M12 | Codex plus human review |
| M15 | Packaged vertical slice gate | M08 M10 M11 M12 M13 M14 | Claude integration |
| M16 | Runtime scenery and long-drive resilience | M15 | Claude |
| M17 | Vehicles two and three | M09 M14 M15 | Codex assets then Claude |
| M18 | Garages and regions two and three | M11 M13 M16 M17 | Codex assets then Claude |
| M19 | Finale and endless mode | M16 M18 | Claude |
| M20 | Performance accessibility and save hardening | M19 | Claude plus human testing |
| M21 | Optional cosmetic entitlement integration | M20 and business gate | Claude |
| M22 | PC release candidate and console feasibility | M20 M21 or explicit skip | Human owner plus Claude |

## The vertical slice

The slice is one polished 0-4 km leg, one walkable Mile Zero garage, the Kestrel wagon, two threats, one authored clue, one physical wheel upgrade and a small set of decorations. It includes arrival, banking, failure recovery, saving, relaunching and complete controller navigation. Use the 4 km outpost to demonstrate the loop without needing the second garage.

Use six to eight road chunks with variants and one lighting setup. A good slice can prove the experience in 15-25 minutes. It is not a miniature of every planned feature. No paid store, second car, elaborate cinematics, voiced dialogue system or full runtime PCG is required to judge it.

## Sequencing rules

Finish M03 before polishing vehicle art; finish M05 before balancing prices; finish M07 before expanding scenery; finish M10 before authoring all workshop animations. Character hands and placeholder arms suffice until the interaction is proven. M14 art can be prepared in an isolated branch after contracts stabilise, then merged with one integrator.

At every task: inspect current state, write a short local plan, implement one coherent slice, compile, run the named checks, package when required, record actual results and commit. A missing external tool is a blocker to that check, not a pass. If two repair attempts fail for the same reason, reduce to a reproducible case rather than letting an agent redesign unrelated systems.

## Work estimates

These are planning allowances for human-led development with AI assistance, not measured productivity promises. They include iteration and integration and should be recalibrated after M03 and M15.

| Gate | Cumulative effort | Meaning |
| --- | --- | --- |
| Playable greybox loop | 160-320 hours | Feel and progression work with placeholders |
| Polished vertical slice | 500-1000 hours | One presentable repeatable leg |
| Compact PC release | 3000-6500 hours | Three regions, content, QA and launch preparation |
| Console ports | Separate estimate after access | Devkits, platform work, certification and testing |

At 20 hours per week, 3000-6500 hours is approximately 150-325 working weeks before holidays and interruptions. AI can reduce scripting and repetitive setup time, but art direction, driving feel, testing and platform work remain substantial. To shorten the schedule, ship one polished region and fewer vehicles as an explicitly smaller product; do not assume generation eliminates production costs.
