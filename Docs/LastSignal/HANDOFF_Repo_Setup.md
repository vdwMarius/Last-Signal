# Handoff: repository setup → M00 on the Windows dev PC

Date: 30 October 2026 | From: cloud Claude session (Linux, no Unreal) | To: Claude Code on the Windows dev PC

## Where things stand

- Repo: https://github.com/vdwMarius/Last-Signal (branch `main`).
- The repo contains the full design pack (`Docs/LastSignal/`), root agent files (`CLAUDE.md`, `AGENTS.md`, `PROJECT_STATE.md`), Git + LFS rules and a **text-only, never-compiled** UE C++ scaffold.
- No `.uasset`/`.umap` files exist yet. No test map, no packaged build, no MCP connection.
- Current task: **M00 Preflight** (`Docs/LastSignal/tasks/M00_Preflight.md`). Nothing in M00 has been done or verified.

## What was created (all untested)

| File | Purpose |
| --- | --- |
| `LastSignal.uproject` | EngineAssociation `5.8`; enables ChaosVehiclesPlugin, EnhancedInput, PythonScriptPlugin and EditorScriptingUtilities (editor-only) |
| `Source/LastSignal.Target.cs`, `Source/LastSignalEditor.Target.cs` | Game and editor targets, `BuildSettingsVersion.Latest` |
| `Source/LastSignal/LastSignal.Build.cs` | Module deps: Core, CoreUObject, Engine, InputCore, EnhancedInput, ChaosVehicles |
| `Source/LastSignal/LastSignal.{h,cpp}` | Primary game module + `LogLastSignal` category |
| `Source/LastSignal/Tests/LastSignalSmokeTest.cpp` | Disposable automation test `LastSignal.Preflight.Smoke` |
| `Config/Default{Engine,Game,Input}.ini` | Minimal config; DX12; Enhanced Input as default input classes; no default map yet |
| `Scripts/Blender/build_test_cube.py` | Exports a 1 m cube FBX to `Saved/BlenderTest/` for the scale test |
| `.gitattributes` / `.gitignore` | LFS for uasset/umap/blend/textures/audio/video; ignores Binaries, Intermediate, Saved, DDC, IDE files, `.mcp.json`, credentials |

Known risks to check first: the installed engine may report a version string other than `5.8` (re-associate the `.uproject`); plugin or module names may differ in the installed 5.8 patch; the automation flag combination in the smoke test may need adjusting.

## Dev PC (as reported by the owner, not verified)

- Windows PC with GitHub Desktop, UE 5.8, Blender and VS Code.
- The owner mentioned a command-line compiler ("mlc"). Confirm that Visual Studio 2022 (or Build Tools) with the MSVC C++ game-development workload is installed; VS Code alone does not provide it.
- Suggested clone path: `C:\Dev\LastSignal` (short, to avoid Windows path-length problems).
- Git workflow: owner commits/pushes via GitHub Desktop; Git LFS should be initialised on clone. The UE built-in Git revision-control plugin is not enabled and is not required.

## What the new session should do

1. Read `CLAUDE.md`, `PROJECT_STATE.md`, `Docs/LastSignal/agent_templates/PROJECT_RULES.md`, this handoff, `Docs/LastSignal/tasks/M00_Preflight.md` and `Docs/LastSignal/docs/06_Agent_Setup_and_Workflow.md`.
2. Inspect the actual environment: engine install path and patch, MSVC/Windows SDK, Blender path/version, git + git-lfs, and whether the repo was cloned with LFS.
3. Execute M00 only:
   - Generate project files and compile `LastSignalEditor Win64 Development`; fix scaffold errors minimally.
   - Open the editor, create a test map (e.g. `/Game/LastSignal/Maps/L_M00_Test`), set it as the editor/game default.
   - Run `LastSignal.Preflight.Smoke` from the command line.
   - Enable and test the Unreal MCP server (list actors, create/save/delete a disposable cube), or record it as blocked and use the shell fallback.
   - Run `Scripts/Blender/build_test_cube.py`, import the FBX and confirm 100 × 100 × 100 UU.
   - Package Win64 Development with RunUAT and launch the exe outside the editor.
4. Fill `Docs/LastSignal/BUILD_COMMANDS.md` with the real paths, commands and exit codes; update `PROJECT_STATE.md`; mark blocked checks as blocked, not passed.
5. Commit the result (check the diff; confirm new `.uasset`/`.umap` files are stored as LFS objects) and stop at the M00 boundary.
