# Sources assumptions and decision log

## Evidence status

Technical sources were checked on 29 October 2026. Documentation is version-sensitive. Recheck the installed engine patch, plugin tool schemas and store dashboard before execution. The sources establish tool capabilities and constraints; the game's mechanics, budgets, prices, content and estimates are original proposals requiring validation.

S01. Epic Games, Unreal Engine 5.8 release announcement. Confirms the release and distinguishes Experimental features.
https://www.unrealengine.com/news/unreal-engine-5-8-is-now-available

S02. Epic Games, Unreal MCP in Unreal Editor, 5.8. Connection setup, local endpoint, toolsets and Experimental status.
https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor?application_version=5.8

S03. Epic Games, Using PCG Generation Modes. Runtime generation and cleanup are available; the game's bounded road scheduler remains a separate design.
https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine

S04. Epic Games, Lumen Performance Guide. Quality, resolution and frame-budget tradeoffs.
https://dev.epicgames.com/documentation/unreal-engine/lumen-performance-guide-for-unreal-engine?lang=en-US

S05. Epic Games, Scripting the Unreal Editor Using Python. Editor automation rather than packaged gameplay.
https://dev.epicgames.com/documentation/en-us/unreal-engine/scripting-the-unreal-editor-using-python

S06. Epic Games, Chaos Vehicles. Vehicle simulation starting point.
https://dev.epicgames.com/documentation/unreal-engine/chaos-vehicles

S07. Epic Games, Nanite Virtualized Geometry. Supported content and practical performance constraints; consult the installed version for feature maturity.
https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine

S08. Epic Games, MetaHuman Assembly. Gameplay-oriented assembly and optimisation options.
https://dev.epicgames.com/documentation/metahuman/assembly?lang=en-US

S09. Epic Games, Enhanced Input. Contextual actions and remapping.
https://dev.epicgames.com/documentation/en-us/unreal-engine/enhanced-input-in-unreal-engine

S10. Epic Games, Common UI. Layered UI, controller focus and glyph support.
https://dev.epicgames.com/documentation/en-us/unreal-engine/common-ui-plugin-for-advanced-user-interfaces-in-unreal-engine

S11. Blender Foundation, Command Line Arguments, versioned 3.6 reference. Establishes the background/Python workflow; validate flags and API against the pinned installed Blender release. The latest manual endpoint could not be retrieved in this research session.
https://docs.blender.org/manual/en/3.6/advanced/command_line/arguments.html

S12. Anthropic, Claude Code MCP documentation. Client connection and tool discovery; follow the official site navigation for current installation instructions.
https://code.claude.com/docs/en/mcp

S13. Anthropic, How Claude remembers your project. Project instruction files and scoped context.
https://code.claude.com/docs/en/memory

S14. Valve, Steamworks Pricing. Product pricing and regional/minimum constraints; exact product prices require partner validation.
https://partner.steamgames.com/doc/store/pricing

S15. Valve, Microtransactions. In-game purchase requirements, distinct from a normal DLC product.
https://partner.steamgames.com/doc/features/microtransactions

## Decision log

| ID | Decision | Reason | Revisit |
| --- | --- | --- | --- |
| D01 | PC first, consoles later | Establish performance and fund platform work | After slice |
| D02 | Single-player offline core | Keep scope and save ownership simple | Separate sequel/expansion |
| D03 | Chase driving and first-person garages | Strong car readability and tactile service | M03/M10 feedback |
| D04 | Three cars and three garages | Finite content budget | M15 scope review |
| D05 | Authored chunks with procedural dressing | Fair driving and reliable narrative | M16 profiling |
| D06 | Physical service plus Quick Fit | Preserve ritual without forced repetition | M15 playtests |
| D07 | Cosmetics only, store deferred | Protect progression and production time | M21 business gate |
| D08 | Stable part IDs and transaction ledger | Protect saves and rewards | Schema changes |
| D09 | Optimised hero humans, simpler horde | Spend character cost where visible | Character profiling |
| D10 | Authored ending, optional eerie details | Give the search a coherent resolution | Before recording |

## Remaining validation

No UE build, Blender export, MCP connection, gameplay benchmark or console test was performed in this planning session. All commands in the setup guide are labelled templates. The balance seeds, technical type names, dimensions, asset counts and estimates are specifications to implement and test. The PDF and pack structure were checked as documents; this does not certify the planned game systems.
