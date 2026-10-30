# Claude and Codex setup and workflow

## Division of work

Claude Code owns runtime implementation, build integration, gameplay data, save migrations and tests. Codex owns concept briefs, Blender generation scripts, asset manifests, UI visual references and independent review. The human owner approves driving feel, silhouettes, story, licences and release decisions. This division reduces conflicting edits; it is not a benchmark claim that one model is inherently better at either task.

Use one active Unreal editor controller at a time. Independent branches may contain code or Blender source work, but two agents must not concurrently mutate the same map, Blueprint, material or running editor. Assign the actual file write scope in each task. A handoff is a committed artifact with evidence, not only a chat summary.

## Local preflight

1. Install the chosen UE 5.8 patch through Epic and the matching supported C++ build toolchain from its versioned documentation. Record exact versions; do not install compiler versions from an old tutorial blindly.
2. Create a C++ project named LastSignal. Start from a minimal template or a verified vehicle template; the template is scaffolding, not the final architecture. Create a dedicated test map and confirm the editor opens without missing modules.
3. Pin a stable Blender release and export preset. Install Claude Code using its current official instructions [S12]. Authenticate through the normal account flow. Install the chosen local Codex client separately; its editor access must be verified rather than assumed from this chat.
4. Initialise Git and Git LFS. Track `.uasset`, `.umap`, `.blend`, source textures and large audio with LFS; ignore DerivedDataCache, Intermediate, Saved, generated IDE files and local credentials. Verify LFS files are actual files after a fresh clone.
5. Copy this pack into `Docs/LastSignal/`. Copy `agent_templates/CLAUDE.md`, `AGENTS.md` and `PROJECT_STATE.md` into the project root. Copy the BUILD_COMMANDS.md template to `Docs/LastSignal/BUILD_COMMANDS.md`. Keep one shared project-rules file to avoid contradictory instruction copies.
6. Compile and package an empty Windows build. Launch it outside the editor and record commands, versions and logs in the M00 handoff before adding systems.

## Connect Claude Code to UE 5.8

Epic documents an Experimental built-in Unreal MCP server [S02]. Check that the installed patch actually exposes these settings and tools.

1. In Edit > Plugins, enable Unreal MCP and All Toolsets, then restart.
2. In Editor Preferences > General > Model Context Protocol, enable Auto Start Server, or use the editor console command `ModelContextProtocol.StartServer`.
3. In the editor console, run `ModelContextProtocol.GenerateClientConfig ClaudeCode` to generate the project configuration. For Codex, inspect its existing config before generating the corresponding client configuration.
4. Start Claude Code in the project root after the editor is running. Use `/mcp` to inspect connection status. The documented default endpoint is `http://127.0.0.1:8000/mcp`.
5. Discover the available tool schemas. First list actors, then create a disposable cube in the test map, save/reopen and delete it. Verify each result before automating production assets. Send editor mutations serially.

The server is local and lacks a default authentication layer; do not expose it through a public port or a VPN listener. This setup is a documented starting point, not a claim of connection in this session. If the tools differ, record the mismatch and use the fallback below rather than inventing tool names.

## Reliable fallback and command templates

Use local file edits, Unreal Build Tool/Automation Tool and editor scripts when MCP is absent or insufficient. Enable Python Editor Script Plugin and Editor Scripting Utilities for editor automation. Keep gameplay in C++/Blueprint. Editor scripts must be rerunnable: resolve by stable path, validate existing assets, create only missing items and report changes. Binary `.uasset` and `.umap` files must be edited through supported editor operations, never as raw text.

The following are Windows PowerShell templates, not tested commands on your machine. M00 replaces the example paths with actual verified paths and records exit codes. Close the editor for reflected C++ layout changes and full clean validation; Live Coding is an iteration aid, not release evidence.

```powershell
$UE_ROOT = 'C:\Program Files\Epic Games\UE_5.8'
$PROJECT_FILE = 'D:\Projects\LastSignal\LastSignal.uproject'
& "$UE_ROOT\Engine\Build\BatchFiles\Build.bat" LastSignalEditor Win64 Development $PROJECT_FILE -WaitMutex
& "$UE_ROOT\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" $PROJECT_FILE -run=pythonscript -script="D:\Projects\LastSignal\Scripts\Unreal\validate_assets.py" -unattended
& "$UE_ROOT\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun "-project=$PROJECT_FILE" -noP4 -platform=Win64 -clientconfig=Development -build -cook -stage -pak -archive -archivedirectory="D:\Builds\LastSignal"
```

`validate_assets.py` is a script to implement during M00/M01, not a supplied working Unreal integration. Tool availability and commandlet flags must be confirmed against the installed patch. Interactive editor operations cannot all run inside a commandlet.

For Blender, start with a batch script test using a disposable cube [S11]:

```powershell
& 'C:\Path\To\blender.exe' --background --python-exit-code 1 --python 'D:\Projects\LastSignal\Scripts\Blender\build_test_cube.py'
```

Use a fresh process for reproducible asset builds; save `.blend` source and export logs. Do not overwrite a manually refined production asset without version control and an explicit asset task. An optional Blender MCP bridge is not required for this pipeline.

## Small context workflow

Keep root instructions short. Store exact build commands, contracts and decisions in referenced files; Claude project memory supports repository instruction files [S13]. Give each session the task ID, current handoff, relevant source paths and a concrete reproduction or acceptance scenario.

Ask for one system or one coherent increment. First inspect existing code, then name the files to change. Require compiled implementation, a minimal test map or reproducible test, and recorded results. When the work is accepted, commit and update `PROJECT_STATE.md` before moving on. Read only changed interfaces and the next task at the next session.

Limit expensive visual loops: approve silhouette, then scale/import, then surface detail, then final render. Do not repeatedly generate polished images while pivots and wheel locations are unresolved. Batch similar props with one material family. Cache approved references and asset manifests. Avoid pasting large logs; include the first causal error and its context, then keep full logs on disk.

## Task prompt template

Read CLAUDE.md, the current PROJECT_STATE.md, task [ID] and only its listed references. Inspect the implementation and dependencies. State the smallest coherent change and file scope, then implement it. Reuse current interfaces; do not rewrite unrelated systems. Compile and run the task's checks. Report exact commands and observed results, changed files, limitations and remaining work. Update the handoff. Stop at this task boundary; do not start the next system or add speculative features.

## Asset handoff template

Build asset [ID] from the approved brief and reference set using the pinned Blender pipeline. First validate a scale blockout in Unreal; then detail. Deliver editable source, export, textures, collision, sockets, material assignments, preview and measured validation. Do not modify gameplay code. If the concept conflicts with dimensions or rig constraints, preserve the contract and flag the visual adjustment.

## Review prompt template

Review task [ID] against its acceptance criteria and the diff. Prioritise save corruption, duplicate rewards, input conflicts, bad asset references, streaming failures and unbounded costs. Reproduce suspicious behaviour before asserting it. Return concrete findings with file paths and severity; make no changes during this review. List untested areas separately from failures.

## Definition of done

Code or assets exist in the repository; the owner can reproduce the result; the named checks have evidence; no unrelated edits slipped in; data and save contracts remain compatible or have a migration; and the handoff states exactly what works. A screenshot of an editor viewport alone does not prove a packaged game feature works.
