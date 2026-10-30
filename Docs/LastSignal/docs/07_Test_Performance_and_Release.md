# Testing performance and release gates

## Candidate hardware targets

Aim for 60 fps during driving on a midrange PC profile, with scalable visual settings. A candidate development baseline is a Ryzen 5 3600-class CPU, RTX 3060 12 GB-class GPU, 16 GB RAM and SSD at 1080p output. This is an unvalidated target, not a published minimum specification. Establish the actual minimum from packaged-build testing. Your RTX 5080 development PC is useful for authoring, but it cannot stand in for slower customer hardware.

Use Lumen and Nanite selectively, with TSR or another validated upscaler where appropriate. Epic's Lumen guide ties scalability to specific frame budgets and internal resolution; enabling every highest-quality setting does not guarantee high fidelity at 60 fps [S04]. A 1440p/4K output label does not mean native rendering at that resolution. Keep transparent options for resolution scale, upscaling and frame generation if added; measure latency without relying on generated frames.

Initial project budgets: GPU work below 14 ms in the representative stress route, game thread below 8 ms and render thread below 10 ms, leaving room within a 16.67 ms frame. CPU and GPU work overlap; do not add these numbers together as a single frame budget. Allocate a starting 4 ms GPU to GI/reflections and profile the remainder by pass. Adjust quality or content if a measured bottleneck disagrees with the plan.

## Runtime limits to test

- Starting maximum: 24 active road enemies, four attached clingers, eight short-lived ragdolls and twelve significant dynamic debris pieces. Reduce expensive states first when pressure rises; logical encounter difficulty must remain consistent.
- Start with 8 live road chunks including the current one; variations in chunk size or sightline may require changes. No growth in resident actor count across repeated streaming cycles.
- Candidate memory goals: below 10 GB process working set and 8 GB VRAM on the baseline profile, while retaining safety margins. Track texture residency, shader/PSO compilation hitches and audio memory separately.
- Measure a warm 10-minute route and a fresh cold-cache route in packaged builds. Report median, p95 and p99 frame times and every hitch over 50 ms. Provisional driving gate: median at or below 16.67 ms, p95 below 20 ms, p99 below 33 ms, and no recurring streaming hitch over 50 ms. These allow occasional misses and are not a claim of locked 60 fps.
- Run a 60-minute soak and accelerated route-index tests. After garbage collection, no sustained upward memory trend greater than 5% from the steady baseline; investigate the source rather than hiding it by restarting maps.

## What to automate

Unit-level checks: stat evaluation order and clamps; negative-price rejection; recipe deductions; ownership invariants; duplicate checkpoint commits; schema migration; missing content fallback; seed/hash stability; and route progress excluding reverse/circle farming.

Functional checks: one complete run; failure and restart; controller-only wheel change; cancellation at every service stage; garage placement exclusion; a clinger attaching/detaching across chunk cleanup; save/load after checkpoint arrival; and resume after an ordinary quit. Test repeated confirm, rapid menu opening, device disconnect and missing assets.

Seed validation: at least 1000 generated layouts across each biome, checking connector compatibility, clear width, branch connectivity, pickup reachability and guaranteed critical rewards. Automated geometry checks do not prove fair encounters; review representative footage and test the hardest combinations manually.

Save fault injection: interrupt each write stage, corrupt one slot, remove a cosmetic definition, migrate an old profile, simulate disk-full and replay a reward transaction. Expected result: newest valid profile or clear fallback, no duplicated grants and no loss of prior banked inventory.

## Manual playtest script

Give testers a controller and no explanation beyond the first in-game tutorial. Observe whether they can launch, dodge, recognise fuel danger, remove a clinger, bank salvage, identify an affordable upgrade, replace a wheel and relaunch. Record confusion, unnecessary menu actions, time spent servicing and whether they choose another attempt. Do not prompt the desired answer.

Track locally, with no remote telemetry service required: run start/end, reason for failure, distance, earned/spent resources, part choices, service duration, checkpoint arrival and frame-time samples. If remote analytics is later added, specify consent/data minimisation and platform requirements before collecting player data.

## Accessibility and presentation

Verify text at couch distance; test UI scale at 720p and ultrawide. Every key audio cue has a visual equivalent. Provide subtitle backgrounds, speaker labels, reduced flashing, separate music/effects/dialogue volume, toggle holds, reduced shake and camera bob, readable night contrast and gore reduction. Include an assist mode with more forgiving fuel and damage, and record the chosen mode for local scores without blocking the story.

## Release checklist

Build from a fresh clone with LFS assets resolved; validate clean cook and all maps, dynamic asset references and shader precaches. Test clean install, update over an older build, save migration, offline launch, controller hotplug, suspend/resume where applicable, language expansion, display changes and absent/corrupt optional DLC. Keep crash logs and symbols organised by build ID.

PC completion does not establish console readiness. Platform access, devkit testing, required SDKs, entitlement handling, storage rules, user switching, suspend/resume, certification and release scheduling need a separate platform-specific plan. Decide actual consoles before advertising support. No public documentation or AI connection substitutes for approved platform access.

## Risk register

| Risk | Early evidence | Response |
| --- | --- | --- |
| Driving is not fun | Players quit after one run | Stop expansion; tune M03 and encounters |
| Manual repairs become chores | Service time dominates play | Improve Quick Fit and reduce required rituals |
| AI assets lack consistency | Wheelbase/materials drift | Lock references and technical manifests |
| Streaming stutters | Repeated p99 spikes | Prebake variants, shorten views, preload earlier |
| Scope overwhelms one developer | Tasks expand without gates | Reduce cars/regions before dropping quality |
| Experimental MCP breaks | Missing tools or changed schema | Use scripts and pin engine patch |
| Story feels manipulative | Twist invalidates player evidence | Keep objective clues and earned resolution |
| Economy forces grind | Several empty-value runs | Increase guarantees, reduce cost, remove debt |
| Saves lose progress | Interrupted-write failures | Fix transaction and A/B recovery before content |
